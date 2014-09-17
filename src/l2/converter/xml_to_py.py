from lxml import etree


class XmlToPy():
    def __init__(self):
        pass

    def convert(self, xml_string):
        py_out = b''
        root = etree.XML(xml_string)
        root.getchildren()
        pck_struct = root.getchildren()[0]
        py_string = """
class {name}(UTF):
    @staticmethod
    def dtype(act, data):
        dtype = [('pck_type', 'i1')]
        return dtype

pck["{type}"] = c_Logout""".format(**pck_struct.attrib)

        return py_string
