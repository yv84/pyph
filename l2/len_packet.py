#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import struct


class LenL2PacketRcv():
    def __init__(self, name=''):
        self.name = name
        self.data_rcv = b''
        self.l2_packets = []

    def add_packet(self, value):
        """
        get packet from length header
        """
        self.data_rcv = b''.join([self.data_rcv, value])
        # esli razmer packeta dostatochen dlya dekodirovaniya
        while (len(self.data_rcv) > 2) and (len(self.data_rcv) >= (struct.unpack('<H',self.data_rcv[:2])[0])):
            # print('''struct.unpack('<H',self.data_rcv[:2])[0]) = ''',struct.unpack('<H',self.data_rcv[:2])[0])
            # get packet header
            head = struct.unpack('<H',self.data_rcv[:2])[0]
            pck = self.data_rcv[:head]
            # remove packet from buffer
            self.data_rcv = self.data_rcv[head:]
            # remove header from packet
            pck = pck[2:]
            self.l2_packets.append(pck)

    def get_packets(self):
        return self.l2_packets
    
    def pop_packets(self):
        while self.l2_packets:
            yield self.l2_packets.pop(0)


class LenL2PacketSend():
    def __init__(self, name=''):
        self.name = name
        self.data_send = b''

    def pop_packet(self):
        data_send = self.data_send
        self.data_send = b''
        return data_send

    def add_packet(self, value):
        """
        add length header to packet
        """
        head = struct.pack('<H',len(value)+2)
        self.data_send = b''.join([self.data_send, head, value])