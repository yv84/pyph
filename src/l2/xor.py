import struct
import types

class Xor():
    def __init__(self, xor_type):
        self.key = b''
        self.xor_type = xor_type
        if xor_type == 'code':
            self.xor_func = self.__code_packet
        elif xor_type == 'decode':
            self.xor_func = self.__decode_packet
        else:
            raise Exception("xor_type can be code/decode, not: " + xor_type)

    def init_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def xor(self, generator):
        # print("xor", 'self.key', self, self.xor_type, "key=", self.key, generator)
        for packet in generator:
            # print('self.key', self, self.xor_type, "key=", self.key, packet)
            if self.key:
                yield self.xor_func(packet, self.key)
                self.key = self.__set_key(packet, self.key)
            elif self.key == b'':
                yield packet
                self.key = self.__set_new_key(packet, self.key)
                print('new key ->', self, self.key)

    #get xor key
    @staticmethod
    def __set_new_key(pck, key):
        #packet without length header / pck[0]
        if key == b'' and len(pck) > 12 and pck[0:1] == b'\x19':      # prishel packet inicializacii key
            key = pck[4:12] + b'\xC8\x27\x93\x01\xA1\x6C\x31\x97'     # key v packete + const (4 = len(2) + type(2))
        return key

    # get_new_key(old.key, len(packet))
    @staticmethod
    def __set_key(pck, key):
        key=struct.pack('<q',(struct.unpack('<q',key[:8])[0])) + struct.pack('<q',(struct.unpack('<q',key[8:])[0] + len(pck)))
        return key

    @staticmethod
    def __decode_packet(pck, key):
        pck_new_list = []
        for i in range(len(pck)):
            pck_new_list.append(0)  #- list
        k=len(pck)
        k = k - 1
        keyLen = len(key)
        while k > 0 :
            pck_new_list[k] = pck[k] ^ key[(lambda : k if k < keyLen else (k % (keyLen)))()] ^ pck[k-1]
            k = k -1
        if len(pck) > 0 : pck_new_list[0] = pck[0] ^ key[0]
        #list  - > byte massiv
        pck_decode = struct.pack('B' * len(pck_new_list), *pck_new_list)     # - dekodirovaniu' packet
        return pck_decode

    @staticmethod
    def __code_packet(pck_decode, key):
        pck_new_list = []
        for i in range(len(pck_decode)):
            pck_new_list.append(0)  #- list
        keyLen = len(key)
        if len(pck_decode) > 0 : pck_new_list[0] = pck_decode[0] ^ key[0]
        k = 1
        while k < (len(pck_decode) ) :
            pck_new_list[k] = pck_decode[k] ^ key[(lambda : k if k < keyLen else (k % (keyLen)))()] ^ pck_new_list[k-1]
            k = k + 1
        pck_code = struct.pack('B' * len(pck_new_list), *pck_new_list)           # - kodirovaniu' packet
        return pck_code


class XorInOut():
    def __init__(self, packet_buffer):
        self.packet_buffer = packet_buffer
        self.xor_in = Xor('decode')
        self.xor_out = Xor('code')

    def pck_in(self, gen: types.GeneratorType) -> types.GeneratorType:
        yield from self.xor_in.xor(gen)

    def pck_out(self, gen: types.GeneratorType) -> types.GeneratorType:
        yield from self.xor_out.xor(gen)

    def init_xor(self, gen):
        yield from self.packet_buffer.client.xor.xor_in.xor(gen)
        yield from self.packet_buffer.client.xor.xor_out.xor(gen)
        yield from self.packet_buffer.server.xor.xor_in.xor(gen)
        yield from self.packet_buffer.server.xor.xor_out.xor(gen)
