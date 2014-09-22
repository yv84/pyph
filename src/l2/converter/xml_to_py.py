import binascii


from lxml import etree
from jinja2 import Template


class XmlToPy():
    def __init__(self):
        pass

    def convert(self, xml_string):
        py_out = b''
        root = etree.XML(xml_string)
        pck_struct = root.getchildren()[0]
        dtype = [('pck_type', 'i1'),]
        for primitive in pck_struct.iterchildren():
            dtype.append((primitive.attrib['name'],
                primitive.attrib['type']))

        py_string = Template("""
class {{name}}(UTF):
    @classmethod
    def dtype(cls, data):{% if complexity == "complex" %}
        pos = GetPosition(data){% endif %}
        {% if complexity == "simple" %}dtype = [{% for n, t in dtype %}(\'{{n}}\', \'{{t}}\'){% if not loop.last %}, {% endif %}{% endfor %}]{% elif complexity == "complex" %}dtype = [{% for n, t in dtype %}(\'{{n}}\', pos.next(\'{{t}}\')){% if not loop.last %}, {% endif %}{% endfor %}]{% endif %}
        return dtype

pck_{{side}}[{{b_type}}] = {{name}}""") \
        .render(
            dtype=dtype,
            b_type=binascii.unhexlify(pck_struct.attrib["type"]),
            **pck_struct.attrib)
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
        j = i
        while True:
            i = j
            j = cls.unicode_string(i, data)
            yield str(j-i+1)

class GetPosition():

    def __init__(self, data):
        self.data = data
        self.i = 0

    def next(self, np_type):
        if np_type.startswith('i'):
            self.i += int(np_type[1:2])
            return np_type
        elif np_type == '|S':
            j = self.unicode_string(self.i)
            i = self.i
            self.i = j
            return np_type+str(j-i+1)
        elif np_type.startswith('loop'):
            self.i += int(np_type[6:7])
            return np_type[5:7]
        else:
            raise Exception("Unknown np_type")

    def unicode_string(self, i):
        while self.data and self.data[i:i+2] != b"\\x00\\x00":
            i += 2
        return (i+1)

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
