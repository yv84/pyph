import numpy
import binascii

from .packets.PacketsGraciaFinal import Pck_invoke_dict


class gs_l2_packet():
    def __init__(self):
        gameapi = Pck_invoke_dict()
        self.gameapi ={}
        self.gameapi['c'] = gameapi.get_Pck_invoke_c() # Pck_invoke_c
        self.gameapi['s'] = gameapi.get_Pck_invoke_s() # Pck_invoke_s

    def unpack(self, pck, side):
        """na vxode packet - na vixode numpy array
        """
        def get_packet_head():
            if   self.gameapi[side].get(pck[:1]): return 1
            elif self.gameapi[side].get(pck[:3]): return 3
            else: return 0
        l = get_packet_head()
        if l:
            dtype = self.gameapi[side][pck[:l]].dtype(1,pck)  # 1 - unpack
            #print(dtype)
            pck_np_array = numpy.zeros(1,dtype)
            if len(pck) == pck_np_array.dtype.itemsize : 
                pck_np_array[:] = pck
            else:
                print("Error length packet")
                raise Exception('PacketError')
            return pck_np_array
        else: 
            print("Unknown Packet")

    def pack(self, tpl, side):
        """na vxode list - na vixode packet
        """
        def get_packet_head():
            if self.gameapi[side].get(chr(tpl[0]).encode('latin-1')):
                return chr(tpl[0]).encode('latin-1')
            elif self.gameapi[side].get((chr(l[0])+chr(l[1])+chr(l[2])).encode('latin-1')):
                return (chr(l[0])+chr(l[1])+chr(l[2])).encode('latin-1')
            else: return 0
        tpl = tpl[0]
        l = get_packet_head()
        if l:
            dtype = self.gameapi[side][l].dtype(2, tpl) #при приеме функции list* # 2 -pack
            pck_byte_array = numpy.zeros(1,dtype)
            try: pck_byte_array[:] = tpl
            except: 
                print('inject error(pack)')
                return b''
            return pck_byte_array.tostring()
        else: 
            print("inject error(head)")
            return b''