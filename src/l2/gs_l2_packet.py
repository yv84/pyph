import numpy
import binascii

from .packets.PacketsGraciaFinal import Pck_invoke_dict
from .converter.xml_to_py import XmlToPy



class PacketError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class gs_l2_packet():
    def __init__(self):
        gameapi = Pck_invoke_dict()
        self.gameapi ={}
        self.gameapi['c'] = gameapi.get_Pck_invoke_c() # Pck_invoke_c
        self.gameapi['s'] = gameapi.get_Pck_invoke_s() # Pck_invoke_s
        xml_to_py = XmlToPy()
        import os
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        self.pck = xml_to_py.execute(xml_to_py.convert_file(BASE_DIR+'/l2/packets/PacketsGraciaFinal.xml'))


    def xunpack(self, pck_data, side):
        try:
            dtype = self.pck.dtype(side, pck_data)
            pck_np_array = numpy.zeros(1, dtype)
            pck_np_array[:] = pck_data
            return pck_np_array
        except:
            raise PacketError('unpack error: cant get dtype')

    def unpack(self, pck, side):
        """na vxode packet - na vixode numpy array
        """
        def get_packet_head():
            if   self.gameapi[side].get(pck[:1]): return 1
            elif self.gameapi[side].get(pck[:3]): return 3
            else: return 0
        l = get_packet_head()
        if l:
            try:
                dtype = self.gameapi[side][pck[:l]].dtype(1,pck)  # 1 - unpack
            except:
                raise PacketError('unpack error: cant get dtype')
            pck_np_array = numpy.zeros(1,dtype)
            if len(pck) == pck_np_array.dtype.itemsize : 
                pck_np_array[:] = pck
            else:
                raise PacketError('unpack error: wrong dtype')
            return pck_np_array
        else: 
            raise PacketError("unpack error: unknown packet header")

    def pack(self, tpl, side):
        """na vxode list - na vixode packet
        """
        def flat(tpl):
            lst = []
            for i in tpl:
                if isinstance(i, tuple) or isinstance(i, list):
                    lst.extend(flat(i))
                else:
                    lst.append(i)
            return lst

        def get_packet_head(tpl):
            if self.gameapi[side].get(chr(tpl[0]).encode('latin-1')):
                return chr(tpl[0]).encode('latin-1')
            elif self.gameapi[side].get((chr(tpl[0])+chr(tpl[1])+chr(tpl[2])).encode('latin-1')):
                return (chr(tpl[0])+chr(tpl[1])+chr(tpl[2])).encode('latin-1')
            else: return 0

        def islst(lst, l):
            if l:
                dtype = self.gameapi[side][l].dtype(2, tpl) #при приеме функции list* # 2 -pack
                pck_byte_array = numpy.zeros(1,dtype)
                #d = numpy.array(data, dtype=dt)
                try: 
                    pck_byte_array[:] = tpl
                except: 
                    raise PacketError('pack error: wrong dtype')
                    return b''
                return pck_byte_array.tostring()
            else: 
                raise PacketError("pack error: unknown packet header")

        if isinstance(tpl, numpy.ndarray):
            return tpl.tostring()
        elif isinstance(i, tuple) or isinstance(i, list):   
            return islst(flat(tpl), get_packet_head(tpl))
        else:
            raise PacketError('wrong type of agrument')


