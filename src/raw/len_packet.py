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
        if value:
            self.l2_packets.append(value)

    def segmentation_packets(self, data: bytes) -> types.GeneratorType :
        self.__add_packet(data)
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
            self.data_send = b''.join([self.data_send, packet])
