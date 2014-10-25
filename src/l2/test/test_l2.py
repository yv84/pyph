# /usr/bin/python3

# python3 -m unittest l2.test.test_l2
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import sys
import os
import time
import io
import re


PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))




class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSimple(self):
        self.assertTrue(True)

    def test_len_packet1(self):
        from l2.len_packet import LenPackets
        rcv = LenPackets()
        pck_in = [b'\x06\x00test',]
        pck_unpacked = [b'test',]
        self.assertEqual(
            list(rcv.pck_in(pck_in)),
            pck_unpacked,
        )
        self.assertEqual(
            pck_in,
            list(rcv.pck_out(pck_unpacked)),
        )

    def test_len_packet2(self):
        from l2.len_packet import LenPackets
        rcv = LenPackets()
        pck_in = [b'\x0b\x00123456789',]
        pck_unpacked = [b'123456789',]
        self.assertEqual(
            list(rcv.pck_in(pck_in)),
            pck_unpacked,
        )
        self.assertEqual(
            pck_in,
            list(rcv.pck_out(pck_unpacked)),
        )

    def test_len_packet3(self):
        from l2.len_packet import LenPackets
        rcv = LenPackets()
        pck_in = [b'\x0b\x00123456789\x05\x00123',]
        pck_unpacked = [b'123456789', b'123',]
        pck_out = [b'\x0b\x00123456789', b'\x05\x00123',]
        self.assertEqual(
            list(rcv.pck_in(pck_in)),
            pck_unpacked,
        )
        self.assertEqual(
            pck_out,
            list(rcv.pck_out(pck_unpacked)),
        )       	
 

    def test_len_packet4(self):
        from l2.len_packet import LenPackets
        rcv = LenPackets()
        pck_in = [b'\x19\x00.\x01\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\x01\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00',]
        pck_unpacked = [b'.\x01\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\x01\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00',]
        pck_out = [b'\x19\x00.\x01\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\x01\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00',]
        self.assertEqual(
            list(rcv.pck_in(pck_in)),
            pck_unpacked,
        )
        self.assertEqual(
            pck_out,
            list(rcv.pck_out(pck_unpacked)),
        )           
 


class TestCase2(unittest.TestCase):

    def test_xor_set1(self):
        from l2.xor import XorInOut

        class PacketBuffer():
            class Side():
                xor = XorInOut(None)
            client = Side()
            server = Side()
        
        packet_buffer = PacketBuffer()
        xor_c = XorInOut(packet_buffer.client)
        xor_s = XorInOut(packet_buffer.server)
        xor_c.xor_in.packet_buffer = \
            xor_c.xor_out.packet_buffer = \
            xor_s.xor_in.packet_buffer = \
            xor_s.xor_out.packet_buffer = packet_buffer

        old_key = b''
        xor_c.xor_in.key = \
            xor_c.xor_out.key = \
            xor_s.xor_in.key = \
            xor_s.xor_out.key = old_key

        pck_packed = b'\x19\x00.\x01\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\x01\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00'
        pck_unpacked = b'\x19\x00.\x01\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\x01\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00'
        key_new =  b"\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\xc8'\x93\x01\xa1l1\x97"
        
        pck_out = list(xor_c.pck_in([pck_packed,]))

        self.assertEqual(
            xor_c.xor_in.key,
            key_new,
        )
        self.assertEqual(
            xor_s.xor_in.key,
            old_key,
        )
        self.assertEqual(
            xor_c.xor_out.key,
            old_key,
        )
        self.assertEqual(
            xor_s.xor_out.key,
            old_key,
        )
        self.assertEqual(
            pck_out,
            [pck_unpacked,],
        )


    def test_xor_set2(self):
        from l2.xor import XorInOut

        class PacketBuffer():
            class Side():
                xor = XorInOut(None)
            client = Side()
            server = Side()
        
        packet_buffer = PacketBuffer()
        xor_c = XorInOut(packet_buffer.client)
        xor_s = XorInOut(packet_buffer.server)
        xor_c.xor_in.packet_buffer = \
            xor_c.xor_out.packet_buffer = \
            xor_s.xor_in.packet_buffer = \
            xor_s.xor_out.packet_buffer = packet_buffer

        old_key = b"\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\xc8'\x93\x01\xa1l1\x97"
        xor_c.xor_in.key = \
            xor_c.xor_out.key = \
            xor_s.xor_in.key = \
            xor_s.xor_out.key = old_key

        pck_packed = b'\x82an\xd4\xcd~\xa1`\xa8\x8f\x1c+\xf8\x89\xb8\x1f>\xae\xa1\x1cw\xe87e\xca\xc6EL\xed\x81\xb0&\x8f\x1f\x10{\\@\xbf'
        pck_unpacked = b'+s\x001\x001\x00a\x00\x00\x006r\x1d\x000\x88\x00\x006r\x1d\x00\xf2g+\x10\x08\x00\x00\x00\x01\x00\x00\x00\xe0>\x9e '
        key_new =  b"\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\xef'\x93\x01\xa1l1\x97"

        pck_out = list(xor_c.pck_in([pck_packed,]))

        self.assertEqual(
            xor_c.xor_in.key,
            key_new,
        )
        self.assertEqual(
            xor_s.xor_in.key,
            old_key,
        )
        self.assertEqual(
            xor_c.xor_out.key,
            old_key,
        )
        self.assertEqual(
            xor_s.xor_out.key,
            old_key,
        )
        self.assertEqual(
            pck_out,
            [pck_unpacked,],
        )

        pck_out = list(xor_c.pck_out(pck_out))

        self.assertEqual(
            xor_c.xor_in.key,
            key_new,
        )
        self.assertEqual(
            xor_s.xor_in.key,
            old_key,
        )
        self.assertEqual(
            xor_c.xor_out.key,
            key_new,
        )
        self.assertEqual(
            xor_s.xor_out.key,
            old_key,
        )
        self.assertEqual(
            pck_out,
            [pck_packed,],
        )



    def test_xor_set3(self):
        from l2.xor import XorInOut

        class PacketBuffer():
            class Side():
                xor = XorInOut(None)
            client = Side()
            server = Side()
        
        packet_buffer = PacketBuffer()
        xor_c = XorInOut(packet_buffer.client)
        xor_s = XorInOut(packet_buffer.server)
        xor_c.xor_in.packet_buffer = \
            xor_c.xor_out.packet_buffer = \
            xor_s.xor_in.packet_buffer = \
            xor_s.xor_out.packet_buffer = packet_buffer

        old_key = b"\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\xc8'\x93\x01\xa1l1\x97"
        xor_c.xor_in.key = \
            xor_c.xor_out.key = \
            xor_s.xor_in.key = \
            xor_s.xor_out.key = old_key

        pck_packed = b'\xa02=\xb6\xaf*\xf5U\xba\x9dz{\xbf\xd3\x91\x06\xdbK \xab\xc1C\xfd]\xd4\xf3\x01\x00\xd2\xbe\xeb|\xb3#,\xa7\n\xf1.\x8e\x125\x97\x96\x06j:\xad\x04\x94\xadTP\xd2\r\xadBe\xf6\xf7V:\n\x9d4\xa4\xab 9\xbbn\xce!\x06\x94\x954X\x7fv!N\x92\xd0\xcaH\x87\xd5\xc5\x1d;\x9cD\xef\xf7n\xaf\x7f\x88\xa3\xdd\xec\xd9*\xa6\xc1\x03\x01\xa0\xccY\xfeW\xc7\xc8CZ\xd8\x00\xa0Oh\xfb\xfa[7\x06\x918\xa8\xa7,5\xb7h\xc8\'\x00\x93\x923_n\xf9P\xc0\xcfD]\xdf\x00\xa0Oh\xfb\xfa[7\x06\x918\xa8\xa7,5\xb7h\xc8\'\x00\x93\x923_n\xf9P\xc0\xcfD]\xdf\x00\xa0Oh\xfb\xfa[7\x00\x97>\xae\xa1*3\xb1n\xce!\x06<<\x9d\xf1\r\x9b2\xa2\xad&?\xbdb\xc2-\n\x99\x989Ud\xf3Z\xca\xc5NW\xd5\n\xaaEb\xf1\xf0Q=\x0c\x9b2\xa2\xad&?\xbdb\xc2-\n\x99\x989Ud\xf3Z\xca\xc5NW\xd5\n\xaaEb\xf1\xf0Q=\x0c\x9b2\xa2\xad&?\xbd\xd7\xd1G\xa7\x1d\x12\xdb\xf7>\t\xc7\xe4\x01\xd9\xa3a\xbe\x1e\xf1\xd6ON\xef\x83\xb3$\x8d\x1d\x12\x99\x80\x02\xdd}\x92\xb5&S\xf2\xac\x9d9\x904;\x85\x9c(\xf7`\x8f\x90\x03;\x9a\xc6\xf7Q\xf8ZU\xed\xf4B\x9d\x08\xe7\xf6ed\xc5z\xe3u\xdc?0\x8a\x93 \xff>\xd1\xf6eR\x81\xf0\xc1V\xffo`\xeb\xf2p\xaf\x0e\xe1\xc6UT\xf5\x99\xa85\x9c\x0c\x03\x89\x90\x12\xcd\x9b\xe81]\x87\xee\x81\xb0)r\x1d\xedy\xe5\x8c\x02\x1aK4\xe7|D\xb1\x19\x17\'\xfa\xb5>\'\xa5z\xda5\x12\x81\x80!M|\xeaC\xd3\xdcWN\xcc\x13\xb3\\{\xe8\xe9H$\x15\x82+\xbb\xb4?&\xa4{\xdb4\x13\x80\x81 L}\xeaC\xd3\xdcWN\xcc\x13\xb3\\{\xe8\xe9H$\x15\x82+\xbb\xb4?&\xa4{\xdb4\x13\x80\x81 L}\xeaC\xd3\xdcWN\xcc\x13\xb5Z}\xee\xefN"\x13\x84-\xbd\xb2\x90\x88\n\xd5\xb8Vq\xe2\xe3B.\x1f\x88!\xb1\xbe5,\xaeq\xd1>\x19\x8a\x8b*Fw\xe0I\xd9\xd6]D\xc6\x19\xb9Vq\xe2\xe3B.\x1f\x88!\xb1\xbe5,\xaeq\xd1>\x19\x8a\x8b*Fw\xe0I\xd9\xd6]D\xc6\x19\xb9Vq\xe2\xe3B.\x1f\x88!\xb1\xbe5\xacv\xe9I\xa6\x81\x12\x132\x13b\xf5\\\xcc\xc3B[\xd9\x06\xa6In\xfd\xfc]1\x00\x97>\xae\xa1*'
        pck_unpacked = b"\t\x02\x00\x00\x00\x07\x00\x00'\x00t\x00e\x00s\x00t\x00d\x00s\x00a\x00A\x00a\x00s\x00d\x00f\x00\x00\x00\xb4y\x00\x00T\x001\x001\x00a\x00\x00\x006r\x1d\x00\x00\x00'\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\n\x00'\x00\x01\x00\x00\x00\x16\x9e\xfe\xff\xd3\xc9\x03\x00\x10\xf2\xd8\xff\xb5\xa6y\xc7)\x0eh@\xf8\xa0g\xb3\xeaSD@Q\x03\x00\x00\xa40\x00\x00\x00\x00\x00\x00\x07\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\xa9\x01\x00\x00\xcd\x01\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb5\xa6^\xc7)\x0eh@\xf8\xa0g\xb3\xeaSc@\x00\x00'\x00\n\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00t\x002\x003\x004\x005\x006\x007'8\x009\x000\x001\x002\x003\x004\x005'6\x00\x00\x00\xd3\xa8\x01\x00s\x001\x001\x00a'\x00\x006r\x1d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x01\x00\x00\x00\xf6\xbb\xfe\xff\xdb\xc8\x03\x00\x0e\xf2\xff\xff\x1f\x85\xebQ\xb8\x99X@\x9a\x99\x99\x99\x99\x99M@\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa9\x01\x00\x00\xcd&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80X@\x00'\x00\x00\x00\x80M@\x00\x00\x00\x00\n\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        key_new =  b'\xa9\x90\x0f\x8b\x19\x82\xdf\xa0<*\x93\x01\xa1l1\x97'

        pck_out = list(xor_s.pck_in([pck_packed,]))

        self.assertEqual(
            xor_c.xor_in.key,
            old_key,
        )
        self.assertEqual(
            xor_s.xor_in.key,
            key_new,
        )
        self.assertEqual(
            xor_c.xor_out.key,
            old_key,
        )
        self.assertEqual(
            xor_s.xor_out.key,
            old_key,
        )
        self.assertEqual(
            pck_out,
            [pck_unpacked,],
        )

        pck_out = list(xor_s.pck_out(pck_out))

        self.assertEqual(
            xor_c.xor_in.key,
            old_key,
        )
        self.assertEqual(
            xor_s.xor_in.key,
            key_new,
        )
        self.assertEqual(
            xor_c.xor_out.key,
            old_key,
        )
        self.assertEqual(
            xor_s.xor_out.key,
            key_new,
        )
        self.assertEqual(
            pck_out,
            [pck_packed,],
        )



    def test_xor_set4(self):
        from l2.xor import XorInOut

        class PacketBuffer():
            class Side():
                xor = XorInOut(None)
            client = Side()
            server = Side()
        
        packet_buffer = PacketBuffer()
        xor_c = XorInOut(packet_buffer.client)
        xor_s = XorInOut(packet_buffer.server)
        xor_c.xor_in.packet_buffer = \
            xor_c.xor_out.packet_buffer = \
            xor_s.xor_in.packet_buffer = \
            xor_s.xor_out.packet_buffer = packet_buffer

        old_key = b"\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\xef'\x93\x01\xa1l1\x97" 
        xor_c.xor_in.key = \
            xor_c.xor_out.key = \
            xor_s.xor_in.key = \
            xor_s.xor_out.key = old_key

        pck_packed = b'\xbb+$\xaf\xb64\xebK(\x02\x91\x901]l\xfbR\xc2\xcd' 
        pck_unpacked =b'\x12\x00\x00\x00\x00\x00\x00\x00\x8c\r\x00\x00\x00\x00\x00\x00\x00\x00\x00' 
        key_new = b'\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\x02(\x93\x01\xa1l1\x97'  

        pck_out = list(xor_c.pck_in([pck_packed,]))

        self.assertEqual(
            xor_c.xor_in.key,
            key_new,
        )
        self.assertEqual(
            xor_s.xor_in.key,
            old_key,
        )
        self.assertEqual(
            xor_c.xor_out.key,
            old_key,
        )
        self.assertEqual(
            xor_s.xor_out.key,
            old_key,
        )
        self.assertEqual(
            pck_out,
            [pck_unpacked,],
        )

        pck_out = list(xor_c.pck_out(pck_out))

        self.assertEqual(
            xor_c.xor_in.key,
            key_new,
        )
        self.assertEqual(
            xor_s.xor_in.key,
            old_key,
        )
        self.assertEqual(
            xor_c.xor_out.key,
            key_new,
        )
        self.assertEqual(
            xor_s.xor_out.key,
            old_key,
        )
        self.assertEqual(
            pck_out,
            [pck_packed,],
        )


    def test_xor_set5(self):
        from l2.xor import XorInOut

        class PacketBuffer():
            class Side():
                xor = XorInOut(None)
            client = Side()
            server = Side()
        
        packet_buffer = PacketBuffer()
        xor_c = XorInOut(packet_buffer.client)
        xor_s = XorInOut(packet_buffer.server)
        xor_c.xor_in.packet_buffer = \
            xor_c.xor_out.packet_buffer = \
            xor_s.xor_in.packet_buffer = \
            xor_s.xor_out.packet_buffer = packet_buffer

        old_key = b'\xa9\x90\x0f\x8b\x19\x82\xdf\xa0(+\x93\x01\xa1l1\x97'
        xor_c.xor_in.key = \
            xor_c.xor_out.key = \
            xor_s.xor_in.key = \
            xor_s.xor_out.key = old_key

        pck_packed = b'W\xe5\xeahq\xf3,\x8d\xe5\xce];\x9a\x9a\xabI\xe0\x14\x1b\xf9\xe0\r\xd2r\x1a3\xa0\xa1\x00\x089\xc7n\x91\x9e{b\xe0?\x9c\xf4\xdfL*\x8b\x8e\xbfZ\xf3\x02\r\xe8\xf1s\xac\x08`K\xd8\xb6\x17\t8\xcac\x9d\x92\x19\x00\x87X\xf8\x90\xdaI,\x8d\x84\xb5L\xe5uz\xf7\xeel\xb3z\x12W\xc4\xab\n\x076\xc5l\x8e\x81cz\x94K\x8e\xe6\xcd^X\xf9\x95\xa4T\xfd\x02\r\xe2\xfb\x18\xc7\x15}2\xa1\xa0\x01eT\xc3j\x88\x87y`\x8cS\x96\xfe\xd5FN\xef\x83\xb2V\xff\x07\x08\xf6\xef\x19\xc6\x12z6\xa5\xc5dzK\xa8\x01\x91\x9e'  
        pck_unpacked = b'\xfe"\x00\t\x00\x00\x00\x01@\x00\x00g\x00l\x00u\x00d\x00i\x00o\x00\x00@\x02\x00\x00\x00d\x00i\x00o\x00n\x00\x00\x00\x03@\x00\x00g\x00i\x00r\x00a\x00n\x00\x00\x00\x04@\x00\x00o\x00r\x00e\x00n\x00\x00\x00\x05\x00\x00@a\x00d\x00e\x00n\x00\x00\x00\x06\x00\x00\x00i@n\x00n\x00a\x00d\x00r\x00i\x00l\x00e@\x00\x00\x07\x00\x00\x00g\x00o\x00d\x00a\x00r@d\x00\x00\x00\x08\x00\x00\x00r\x00u\x00n\x00e@\x00\x00\t\x00\x00\x00s\x00h\x00u\x00t\x00t@g\x00a\x00r\x00t\x00\x00\x00'
        key_new = b'\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\xcb+\x93\x01\xa1l1\x97'

        pck_out = list(xor_s.pck_in([pck_packed,]))

        self.assertEqual(
            xor_c.xor_in.key,
            old_key,
        )
        self.assertEqual(
            xor_s.xor_in.key,
            key_new,
        )
        self.assertEqual(
            xor_c.xor_out.key,
            old_key,
        )
        self.assertEqual(
            xor_s.xor_out.key,
            old_key,
        )
        self.assertEqual(
            pck_out,
            [pck_unpacked,],
        )

        pck_out = list(xor_s.pck_out(pck_out))

        self.assertEqual(
            xor_c.xor_in.key,
            old_key,
        )
        self.assertEqual(
            xor_s.xor_in.key,
            key_new,
        )
        self.assertEqual(
            xor_c.xor_out.key,
            old_key,
        )
        self.assertEqual(
            xor_s.xor_out.key,
            key_new,
        )
        self.assertEqual(
            pck_out,
            [pck_packed,],
        )



    def test_xor_set6(self):
        from l2.xor import XorInOut

        class PacketBuffer():
            class Side():
                xor = XorInOut(None)
            client = Side()
            server = Side()
        
        packet_buffer = PacketBuffer()
        xor_c = XorInOut(packet_buffer.client)
        xor_s = XorInOut(packet_buffer.server)
        xor_c.xor_in.packet_buffer = \
            xor_c.xor_out.packet_buffer = \
            xor_s.xor_in.packet_buffer = \
            xor_s.xor_out.packet_buffer = packet_buffer

        old_key = b'\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\x02(\x93\x01\xa1l1\x97'
        xor_c.xor_in.key = \
            xor_c.xor_out.key = \
            xor_s.xor_in.key = \
            xor_s.xor_out.key = old_key

        pck_packed = b'y\xe8\xe7'
        pck_unpacked = b'\xd0\x01\x00'
        key_new = b'\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\x05(\x93\x01\xa1l1\x97'

        pck_out = list(xor_c.pck_in([pck_packed,]))

        self.assertEqual(
            xor_c.xor_in.key,
            key_new,
        )
        self.assertEqual(
            xor_s.xor_in.key,
            old_key,
        )
        self.assertEqual(
            xor_c.xor_out.key,
            old_key,
        )
        self.assertEqual(
            xor_s.xor_out.key,
            old_key,
        )
        self.assertEqual(
            pck_out,
            [pck_unpacked,],
        )

        pck_out = list(xor_c.pck_out(pck_out))

        self.assertEqual(
            xor_c.xor_in.key,
            key_new,
        )
        self.assertEqual(
            xor_s.xor_in.key,
            old_key,
        )
        self.assertEqual(
            xor_c.xor_out.key,
            key_new,
        )
        self.assertEqual(
            xor_s.xor_out.key,
            old_key,
        )
        self.assertEqual(
            pck_out,
            [pck_packed,],
        )







class TestCase3(unittest.TestCase):
    def test_converter(self):
        from l2.gs_l2_packet import GSL2Packet
        pck = b'+s\x001\x001\x00a\x00\x00\x006r\x1d\x000\x88\x00\x006r\x1d\x00\xf2g+\x10\x08\x00\x00\x00\x01\x00\x00\x00\xe0>\x9e '
        side = 'client'
        l = [(43, b's\x001\x001\x00a', 1929782, 34864, 1929782, 271280114, 8)]
        gameapi = GSL2Packet()
        unpack = gameapi.unpack(pck, side)
        self.assertEqual(
           unpack.tolist(),
            l,
        )

    def test_converter2(self):
        from l2.gs_l2_packet import GSL2Packet
        self.maxDiff = None
        pck = b'\x11\x00\x00\x08\x00\x04\x00\xae%t@\xd1\x18\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00i\x07\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\x07\x00\x00\x00\xff\xff\xff\xff\xfe\xff\x00\x00\x00\x00\x00i\x07\x00\x00\x00\x00\x00\x00\x00\xf1\xd8\xff\xff\x04\x00.\x8bq@9\x00\x00\x00\x01\x00\x00\x00\xfc\x05\x00\x00\x00i\x07\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\x07\x00\x00\x00\xff\xff\xff\xff\xfe\xff\x00\x00\x00\x00\x00i\x07\x00\x00\x00\x00\x00\x00\x00\xf1\xd8\xff\xff\x04\x00r\x10o@\xd11\x00\x00\x02\x00\x00\x00\n\x00\x00\x00\x00i\x07\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\x07\x00\x00\x00\xff\xff\xff\xff\xfe\xff\x00\x00\x00\x00\x00i\x07\x00\x00\x00\x00\x00\x00\x00\xf1\xd8\xff\xff\x04\x00\x9e\x0ft@\x9a)\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x00i\x07\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\x07\x00\x00\x00\xff\xff\xff\xff\xfe\xff\x00\x00\x00\x00\x00i\x07\x00\x00\x00\x00\x00\x00\x00\xf1\xd8\xff\xff\x04\x00\x1d\x19p@\xd4\x15\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00i\x07\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\x07\x00\x00\x00\xff\xff\xff\xff\xfe\xff\x00\x00\x00\x00\x00i\x07\x00\x00\x00\x00\x00\x00\x00\xf1\xd8\xff\xff\x01\x00\x9c\xd2q@\xcd\x01\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00i\x07\x00\x01\x00\x00\x00\x01\x00\x00\x08\x00\x00\x00\x00\x00i\x07\x00\x00\x00\xff\xff\xff\xff\xfe\xff\x00\x00\x00\x00\x00i\x07\x00\x00\x00\x00\x00\x00\x00\xf1\xd8\xff\xff\x01\x00\x1b\x7fp@\xa9\x01\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00i\x07\x00\x01\x00\x00\x00\x01\x00\x00\x04\x00\x00\x00\x00\x00i\x07\x00\x00\x00\xff\xff\xff\xff\xfe\xff\x00\x00\x00\x00\x00i\x07\x00\x00\x00\x00\x00\x00\x00\xf1\xd8\xff\xff\x00\x00\x9e\xe5p@\x06\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00i\x07\x00\x00\x00\x00\x00\x01\x00\x80\x00\x00\x00\x00\x00\x00i\x07\x00\x00\x00\xff\xff\xff\xff\xfe\xff\x00\x00\x00\x00\x00i\x07\x00\x00\x00\x00\x00\x00\x00\xf1\xd8\xff\xff'
        side = 'server'
        l = [(17, 0, 8, (4, 1081353646, 6353, 0, 2085773557891074, 5, 0, 0, 0, 0, 26880, 7, -1, -2, 0, 0, 26880, 7, 0, 0, 0, -9999), (4, 1081183022, 57, 1, 2085773557892604, 4, 0, 0, 0, 0, 26880, 7, -1, -2, 0, 0, 26880, 7, 0, 0, 0, -9999), (4, 1081020530, 12753, 2, 2085773557891082, 5, 0, 0, 0, 0, 26880, 7, -1, -2, 0, 0, 26880, 7, 0, 0, 0, -9999), (4, 1081347998, 10650, 3, 2085773557891077, 5, 0, 0, 0, 0, 26880, 7, -1, -2, 0, 0, 26880, 7, 0, 0, 0, -9999), (4, 1081088285, 5588, 4, 2085773557891073, 5, 0, 0, 0, 0, 26880, 7, -1, -2, 0, 0, 26880, 7, 0, 0, 0, -9999), (1, 1081201308, 461, -1, 2085773557891073, 1, 0, 1, 2048, 0, 26880, 7, -1, -2, 0, 0, 26880, 7, 0, 0, 0, -9999), (1, 1081114395, 425, -1, 2085773557891073, 1, 0, 1, 1024, 0, 26880, 7, -1, -2, 0, 0, 26880, 7, 0, 0, 0, -9999), (0, 1081140638, 6, -1, 2085773557891073, 0, 0, 1, 128, 0, 26880, 7, -1, -2, 0, 0, 26880, 7, 0, 0, 0, -9999))]
        gameapi = GSL2Packet()
        unpack = gameapi.unpack(pck, side)
        self.assertEqual(
            unpack.tolist(),
            l,
        )
    def test_converter3(self):
        from l2.gs_l2_packet import GSL2Packet
        self.maxDiff = None
        pck = b'2\x16\x9e\xfe\xff\xd3\xc9\x03\xec\x10\xf2\xff\xff\x00\x00\x00\x00n\xd5\xd0It\x00e\xecs\x00t\x00d\x00s\x00a\x00f\x00a\x00s\xecd\x00f\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\n\xec\x00\x00\x07\x00\x00\x00\xa40\x00\x00\x00\x00\x00\x00\x16\xec\x00\x00\x15\x00\x00\x00\x1b\x00\x00\x00)\x00\x00\x00\x14\xec\x00\x00\'\x00\x00\x00\xc0\x00\x00\x00\xc0\x00\x00\x00\x9a\xec\x00\x00\x9a\x00\x00\x00Q\x03\x00\x00Z\x14\x00\x00$\xe4\x01\x00(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x9e\x8cw@\x00\x00\x00\x00\x00\x00\x00\x00\x1b\xfaw@\x9c\xbbv@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\xa9\x01\x00\x00\xcd\x01\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00~\x01\x00\x007\xec\x00\x00"\x00\x00\x00\'\x00\x00\x00(\x00\x00\x00\t\xec\x00\x00M\x01\x00\x00~\x01\x00\x00:\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00x\x00\x00\x00N\x00\x00\x002\xec\x00\x002\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00)\\\x8f\xc2\xf5(\xf0?4\xc3\x87\xddw\x0c\xf6?\x00\x00\x00\x00\x00\x00\x1a@\x00\xec\x00\x00\x00\x806@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\n\x00\xec\x00\x00\x00\x00\x00`\x00\x00\x00`\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\xff\xff\xff\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00N\xf9\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xff\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x01\x00\x00\x00 N\x00\x00\x00\x00\x00\x00\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        side = 'server'
        l = [(50, -90602, -335296045, -3568, 0, 1238422894, b't\x00e\xecs\x00t\x00d\x00s\x00a\x00f\x00a\x00s\xecd\x00f', 0, 1, 60426, 7, 12452, 60438, 21, 27, 41, 60436, 39, 192, 192, 60570, 154, 849, 5210, 123940, 40, 0, 0, 60416, 0, 0, 0, 60416, 1081576606, 0, 0, 1081604635, 1081523100, 0, 0, 60416, 0, 0, 0, 60416, 0, 0, 0, 60416, 0, 0, 0, 60416, 0, 0, 0, 60416, 0, 0, 6, 60416, 0, 425, 461, 60416, 0, 0, 0, 60416, 0, 0, 0, 60416, 0, 0, 0, 60416, 0, 0, 0, 60416, 0, 0, 0, 60416, 0, 0, 0, 60416, 0, 0, 0, 60416, 0, 0, 0, 60416, 0, 0, 0, 60416, 0, 0, 0, 60416, 0, 3, 382, 60471, 34, 39, 40, 60425, 333, 382, 58, 60416, 0, 120, 78, 60466, 50, 0, 0, 60416, -4310085664768.0, -3.62209960601457e+142, 5.301767334e-315, 1.28203029047762e-309, 1077313536, 0, 0, b'\x00\xec', 0, 0, -335544320, 0, 0, 0, 0, 0, 60416, 0, 0, 0, 0, 0, 236, 0, 0, 0, 655440, 236, 6291456, 0, 24576, 0, 0, 0, 236, 0, 0, 0, -20, -65536, 65791, 0, 1308622848, 60665, 0, 0, 0, -512, 255, -5120, 0, 0, 0, 0, -335544320, 16777216, 536870912, 78, -335544320, 0)]
        gameapi = GSL2Packet()
        unpack = gameapi.unpack(pck, side)
        self.assertEqual(
            unpack.tolist(),
            l,
        )



if __name__ == '__main__':
    unittest.main()
