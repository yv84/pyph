import binascii
import sys
import types


from lxml import etree
from jinja2 import Template


class XmlToPy():
    def __init__(self):
        self.py_string = Template("""
class {{pck_name}}():
    @classmethod
    def dtype(cls, data):{% if complexity == "complex" %}
        pos = GetPosition(data){% endif %}
        {% if complexity == "simple" %}dtype = {{dtype}}{% elif complexity == "complex" %}dtype = pos.get_dtype({{dtype}}){% endif %}
        return dtype

pck_{{side}}[{{b_type}}] = {{pck_name}}""")

    def get_children(self, parent):
        dtype = []
        for primitive in parent.iterchildren():
            if primitive.tag.endswith('loop'):
                dtype.append((primitive.attrib['name'], 'value',
                    primitive.attrib['type']))
                if int(primitive.attrib['skip']) != 0:
                    dtype.extend(self.get_children(primitive[0]))
                    dtype.append((primitive.attrib['name'], 'loop',
                        self.get_children(primitive[1])))
                else:
                    dtype.append((primitive.attrib['name'], 'loop',
                        self.get_children(primitive)))
            else:
                dtype.append((primitive.attrib['name'],
                    primitive.attrib['type']))
        return dtype

    def convert(self, xml_string):
        root = etree.XML(xml_string)
        pck_struct = root.getchildren()[0]
        dtype = [(pck_struct.attrib['name'], pck_struct.attrib['type']),]
        dtype.extend(self.get_children(pck_struct))

        py_string = self.py_string.render(
            dtype=dtype,
            b_type=binascii.unhexlify(pck_struct.attrib["opt_code"]),
            **pck_struct.attrib)
        return py_string


    @property
    def py_header(self):
        return """
from .converter_runtime_util import GetPosition, Pck
pck_client = {}
pck_server = {}
pck = Pck(pck_client, pck_server)
"""

    def execute(self, py_string):
        if isinstance(py_string, str):
            code = ''.join([self.py_header, py_string])
        elif hasattr(py_string, '__iter__'):
            code = ''.join([self.py_header, ''.join(py_string)])

        code = compile(code, '<string>', 'exec')
        selfModule = types.ModuleType(__name__)
        context = selfModule.__dict__
        exec(code, context)
        return context['pck']