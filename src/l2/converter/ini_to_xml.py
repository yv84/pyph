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
            (?P<name>[a-z0-9]+)
            \)
        """)

    def convert(self, line_in):
        xml_out = b''

        d = self.regex_header.match(line_in).groupdict() #
        opt_code, header, body = d['opt_code'], d['header'], d['body']
        primitives = self.regex_body.findall(body) # list(type, name)

        root = etree.Element('root', nsmap={'la2': 'la2'})
        tree = etree.ElementTree(root)
        packet = etree.SubElement(root, '{la2}pck_struct',
            name=b''.join([self.side[0:1], b'_', header.lower()]),
            side=self.side,
            type=opt_code)
        for primitive in primitives:
            etree.SubElement(packet, '{la2}primitive',
                name=primitive[1],
                type=primitive[0])
        xml_out = etree.tostring(tree, encoding='ASCII', xml_declaration=True,
            pretty_print=True)

        return xml_out
