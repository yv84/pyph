from lxml import etree


class XmlToPy():
    def __init__(self):
        pass

    def convert(self, xml_string):
        py_out = b''
        root = etree.XML(xml_string)
        root.getchildren()
        pck_struct = root.getchildren()[0]
        dtype = [('pck_type', 'i1'),]
        for primitive in pck_struct.iterchildren():
            dtype.append((primitive.attrib['name'],
                primitive.attrib['type']))

        py_string = """
class {name}(UTF):
    @staticmethod
    def dtype(act, data):
        dtype = {dtype}
        return dtype

pck["{type}"] = {name}""" \
            .format(dtype=dtype, **pck_struct.attrib) \
            .replace("'S')", "'|S'+self.unicode_string(data))")

        return py_string
