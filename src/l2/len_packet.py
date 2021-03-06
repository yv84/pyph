import struct
import types


class LenPackets():
    def __init__(self):
        self.data_rcv = b''

    def pck_in(self, data: types.GeneratorType) -> types.GeneratorType:
        """
        get packet from length header
        """
        self.data_rcv = b''.join([self.data_rcv, b''.join(data)])
        # esli razmer packeta dostatochen dlya dekodirovaniya
        while (len(self.data_rcv) > 2) and (len(self.data_rcv) >= \
              (struct.unpack('<H',self.data_rcv[:2])[0])):
            # get packet header
            head = struct.unpack('<H',self.data_rcv[:2])[0]
            pck = self.data_rcv[:head]
            # remove packet from buffer
            self.data_rcv = self.data_rcv[head:]
            # remove header from packet
            yield pck[2:]

    def pck_out(self, value: types.GeneratorType) -> types.GeneratorType:
        """
        add length header to packet
        """
        for packet in value:
            head = struct.pack('<H',len(packet)+2)
            yield b''.join([head, packet])
