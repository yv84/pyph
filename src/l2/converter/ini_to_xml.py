import re

from lxml import etree


class IniToXml():
    def __init__(self):
        self.side = b'client'
        self.regex_header = re.compile(b"""(?xi)
            ^[\s\t\r\n]*
            (?P<opt_code>[0-9a-f]{2,4})
            =
            (?P<header>[a-z][a-z0-9]*)
            :
            (?P<body>.*)
        """)
        self.regex_body = re.compile(b"""(?xi)
            (?P<type>[a-z0-9])
            \(
            (?P<name>[a-z0-9:.]+)
            \)
        """)
        self.regex_body_loop = re.compile(b"""(?xi) # :Loop.01.0001
            ^
            (?P<name>[a-z0-9:]+?)
            :Loop.
            (?P<skip>\d{2}).
            (?P<loop>\d{4})
            $
        """)
        self.ctypes_to_numpy = {
            b'b': b'i1',
            b'c': b'i1',
            b'B': b'u1',
            b'h': b'i2',
            b'H': b'u2',
            b'z': b'i4',
            b'd': b'i4',
            b'i': b'i4',
            b'l': b'i4',
            b'I': b'u4',
            b'L': b'u4',
            b'o': b'i4',
            b'd': b'i4',
            b'q': b'i8',
            b'Q': b'u8',
            b'f': b'f8',
            b's': b'S', # UTF-16-LE string
            b'-': b'S', # byte string
        }

    # header - replace cames style - > underscore
    @staticmethod
    def camel(s):
        if s == b':':
            return b'U'
        return s  #.lower()

    def element_append_loop(self, cursor, element_loop, primitive):
        el = element_loop.groupdict()
        skip = int(el['skip'])-1
        loop = int(el['loop'])
        element = etree.SubElement(cursor, '{la2}loop',
            name=self.camel(el['name']),
            type=self.ctypes_to_numpy[primitive[0]],
            skip=str(skip).encode('utf-8'),
            loop=str(loop).encode('utf-8'),
        )
        return element, loop

    def element_append_primitive(self, cursor, primitive):
        return etree.SubElement(cursor, '{la2}primitive',
            name=self.camel(primitive[1]),
            type=self.ctypes_to_numpy[primitive[0]])


    def convert(self, line_in):
        xml_out = b''

        d = self.regex_header.match(line_in).groupdict() #
        opt_code, header, body = d['opt_code'], d['header'], d['body']
        primitives = self.regex_body.findall(body) # list(type, name)

        root = etree.Element('root', nsmap={'la2': 'la2'})
        tree = etree.ElementTree(root)
        packet = etree.SubElement(root, '{la2}pck_struct',
            name=b''.join([self.side[0:1], b'_', self.camel(header)]),
            side=self.side,
            type=opt_code)
        cursor = packet
        loop = 0
        skip = 0

        for primitive in primitives:
            element_loop = self.regex_body_loop.match(primitive[1])
            #print(primitive, loop, cursor.tag)

            if element_loop:
                chield, loop = self.element_append_loop(
                                  cursor, element_loop, primitive)
                cursor = chield
                loop += 1
            else:
                chield = self.element_append_primitive(cursor, primitive)

            if loop:
                loop -= 1
                if not loop:
                    cursor = cursor.getparent()

        xml_out = etree.tostring(tree, encoding='ASCII', xml_declaration=True,
            pretty_print=True)

        return xml_out
