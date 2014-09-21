from lxml import etree
import binascii


class XmlToPy():
    def __init__(self):
        pass

    def convert(self, xml_string):
        py_out = b''
        root = etree.XML(xml_string)
        root.getchildren()
        pck_struct = root.getchildren()[0]
        dtype = [('pck_type', 'i1'),]
        i = 1
        for primitive in pck_struct.iterchildren():
            dtype.append((primitive.attrib['name'],
                primitive.attrib['type']))

        py_string = """
class {name}(UTF):
    @classmethod
    def dtype(cls, data):
        dtype = {dtype}
        return dtype

pck_{side}[{b_type}] = {name}""" \
            .format(
                dtype=dtype,
                b_type=binascii.unhexlify(pck_struct.attrib["type"]),
                **pck_struct.attrib)
        if py_string.find("'S')") != -1:
              py_string = py_string.replace("def dtype(cls, data):",
"""def dtype(cls, data):
        gen = cls.var_value(1, data)""")
              py_string = py_string.replace("'S')", "'|S'+gen.__next__())")
        return py_string

    @property
    def py_header(self):
        return """import struct

class UTF():
    @staticmethod
    def unicode_string(i, data):
        while data and data[i:i+2] != b"\\x00\\x00":
            i += 2
        return (i+1)

    @classmethod
    def var_value(cls, i, data):
        j = 0
        while True:
            i += int(j)
            j = cls.unicode_string(i, data)
            yield str(j-i+1)

pck_client = {}
pck_server = {}
"""

    @property
    def py_footer (self):
        return """

class Pck():
    def __init__(self):
        Pck.client = pck_client
        Pck.server = pck_server

    def dtype(self, side, data):
        if side.lower() in ("c", "client", b"c", b"client"):
            if data[0:1] != b'\\xd0':
                return self.client[data[0:1]].dtype(data)
            else:
                return self.client[data[0:2]].dtype(data)
        elif side.lower() in ("s", "server", b"s", b"server"):
            if data[0:1] != b'\\xfe':
                return self.server[data[0:1]].dtype(data)
            else:
                return self.server[data[0:2]].dtype(data)
        else:
           raise Exception("Invalid side")

pck = Pck()
"""
