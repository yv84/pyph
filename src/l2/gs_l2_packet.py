import numpy
import binascii

from .converter.xml_to_py import XmlToPy



class PacketError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class GSL2Packet():
    def __init__(self):
        xml_to_py = XmlToPy()
        import os
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        self.pck = xml_to_py.execute(xml_to_py.convert_file(
            BASE_DIR+'/l2/converter/xml/PacketsGraciaFinal.xml'
        ))

    def unpack(self, pck_data, side):
        try:
            dtype = self.pck.dtype(side, pck_data)
            pck_np_array = numpy.zeros(1, dtype)
            pck_np_array[:] = pck_data
            return pck_np_array
        except:
            raise PacketError('unpack error: cant get dtype')
