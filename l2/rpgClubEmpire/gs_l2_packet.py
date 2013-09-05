
import numpy
from . import class_la2_gracia_final
import binascii


class gs_l2_packet():
    def init_Pck_invoke_dict_c(self):
        """pomeschaem classi s dtype packetov v dict"""
        return class_la2_gracia_final.Pck_invoke_dict().get_Pck_invoke_c()
    def init_Pck_invoke_dict_s(self):
        """pomeschaem classi s dtype packetov v dict"""
        return class_la2_gracia_final.Pck_invoke_dict().get_Pck_invoke_s()
    def unpack(self, pck, Pck_invoke, side):
        """na vxode packet - na vixode numpy array
        """
        def get_packet_head():
            if   Pck_invoke[side].get(pck[:1]): return 1
            elif Pck_invoke[side].get(pck[:3]): return 3
            else: return 0
        l = get_packet_head()
        if l:
            dtype = Pck_invoke[side][pck[:l]].dtype(1,pck)
            pck_np_array = numpy.zeros(1,dtype)
            if len(pck) == pck_np_array.dtype.itemsize : pck_np_array[:] = pck
            else: raise PacketError
            return pck_np_array
        else: print("Unknown Packet")
    
    def pack(self, tpl, Pck_invoke, side):
        """na vxode list - na vixode packet
        """
        def get_packet_head():
            if   Pck_invoke[side].get(chr(tpl[0]).encode('latin-1')): return chr(tpl[0]).encode('latin-1')
            elif Pck_invoke[side].get((chr(l[0])+chr(l[1])+chr(l[2])).encode('latin-1')): return (chr(l[0])+chr(l[1])+chr(l[2])).encode('latin-1')
            else: return 0
        l = get_packet_head()
        if l:
            dtype = Pck_invoke[side][l].dtype(2, tpl) #при приеме функции list*
            pck_byte_array = numpy.zeros(1,dtype)
            try: pck_byte_array[:] = tpl
            except: 
                print('inject error(pack)')
                return b''
            return pck_byte_array.tostring()
        else: 
            print("inject error(head)")
            return b''
       