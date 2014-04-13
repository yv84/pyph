#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import struct
import types


class LenL2PacketRcv():
    def __init__(self, name=''):
        self.name = name
        self.data_rcv = b''
        self.l2_packets = []

    def __add_packet(self, value: bytes) -> None:
        """
        get packet from length header
        """
        self.data_rcv = b''.join([self.data_rcv, value])
        # esli razmer packeta dostatochen dlya dekodirovaniya
        # if (len(self.data_rcv) > 2):
        while (len(self.data_rcv) > 2) and (len(self.data_rcv) >= (2+struct.unpack('<H',self.data_rcv[:2])[0])):
            # get packet header
            head = struct.unpack('<H',self.data_rcv[:2])[0]
            pck = self.data_rcv[:head+2]
            # remove packet from buffer
            self.data_rcv = self.data_rcv[head+2:]
            # remove header from packet
            pck = pck[2:]
            self.l2_packets.append(pck)
    
    def segmentation_packets(self, to_s_data: bytes) -> types.GeneratorType :
        self.__add_packet(to_s_data)
        while self.l2_packets:
            yield self.l2_packets.pop(0)


class LenL2PacketSend():
    def __init__(self, name=''):
        self.name = name
        self.data_send = b''

    def pop_packet(self) -> bytes :
        data_send = self.data_send
        self.data_send = b''
        return data_send

    def add_packets(self, value: types.GeneratorType) -> None :
        """
        add length header to packet
        """
        for packet in value:
            head = struct.pack('<H',len(packet))
            self.data_send = b''.join([self.data_send, head, packet])