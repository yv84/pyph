import binascii


from lxml import etree
from jinja2 import Template


class XmlToPy():
    def __init__(self):
        self.py_string = Template("""
class {{pck_name}}(UTF):
    @classmethod
    def dtype(cls, data):{% if complexity == "complex" %}
        pos = GetPosition(data){% endif %}
        {% if complexity == "simple" %}dtype = {{dtype}}{% elif complexity == "complex" %}dtype = pos.get_dtype({{dtype}}){% endif %}
        return dtype

pck_{{side}}[{{b_type}}] = {{pck_name}}""")

    def get_children(self, parent):
        dtype = []
        for primitive in parent.iterchildren():
            dtype.append((primitive.attrib['name'],
                primitive.attrib['type']))
            if primitive.tag.endswith('loop'):
                dtype.append((primitive.attrib['name']+":loop",
                    self.get_children(primitive)))
        return dtype

    def convert(self, xml_string):
        root = etree.XML(xml_string)
        pck_struct = root.getchildren()[0]
        dtype = [(pck_struct.attrib['name'], pck_struct.attrib['type']),]
        #import pdb; pdb.set_trace()
        dtype.extend(self.get_children(pck_struct))

        py_string = self.py_string.render(
            dtype=dtype,
            b_type=binascii.unhexlify(pck_struct.attrib["opt_code"]),
            **pck_struct.attrib)
        return py_string


    @property
    def py_header(self):
        return """import struct

class UTF():
    pass

class GetPosition():

    def __init__(self, data):
        self.data = data
        self.i = 0
        self.c_type = {"i1": b"b", "i2": b"h", "i4": b"i", "i8": b"q",}
        self.c_type_len = {"i1": 1, "i2": 2, "i4": 4, "i8": 8,}

    def get_dtype(self, np_type):
        dtype = []
        for primitive in np_type:
            if isinstance(primitive[1], str) and primitive[1].startswith('i'):
                self.i += int(primitive[1][1:2])
                dtype.append((primitive[0], primitive[1]))
            elif isinstance(primitive[1], str) and primitive[1] == '|S':
                j = self.unicode_string(self.i)
                i = self.i
                self.i = j
                dtype.append((primitive[0], primitive[1]+str(j-i)))
            elif isinstance(primitive[1], list):
                loop_value = self.get_loop_value(self.i, dtype[-1][1])
                # import pdb; pdb.set_trace()
                for i in range(1, loop_value+1):
                    dtype.append((primitive[0][:-5]+str(i), self.get_dtype(primitive[1])))
            else:
                raise Exception("Unknown np_type")
        return dtype

    def unicode_string(self, i):
        i += 4
        l = len(self.data)
        while self.data[i-3:i-1] != b"\\x00\\x00":
            if i > l:
                raise Exception("Error parsing np_type: get string value")
            i += 2
        return i

    def get_loop_value(self, i, t):
        if i > len(self.data):
            raise Exception("Error parsing np_type: get loop value")
        count = struct.unpack(self.c_type[t], self.data[i-self.c_type_len[t]:i])[0]
        if count > 50:
            raise Exception("Error parsing np_type: to many loops")
        return count if count < 50 else 50


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
