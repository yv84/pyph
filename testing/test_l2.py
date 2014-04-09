# /usr/bin/python3

# python3 -m unittest -v testing.test1
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import sys
import os
import time
import io
import re


class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSimple(self):
        self.assertTrue(True)

    def test_len_packet(self):
        from src.l2.len_packet import LenL2PacketRcv, LenL2PacketSend
        rcv = LenL2PacketRcv('test')
        send = LenL2PacketSend('test')
        self.assertTrue(rcv.name == 'test')
        self.assertTrue(send.name == 'test')

        self.assertTrue(list(rcv.segmentation_packets(b'\x0b\x00123456789')) == [b'123456789'])
        self.assertTrue(list(rcv.segmentation_packets(
            b'\x0b\x00123456789\x05\x00123')) == [b'123456789', b'123'])

        send.add_packets([b'123456789', b'123'])
        self.assertTrue(send.pop_packet() == b'\x0b\x00123456789\x05\x00123')

    def test_xor_init(self):
        from src.l2.xor import Xor
        xor = Xor('decode')
        pck = [b'.\x01\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\x01\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00',]
        key_xor = b"\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\xc8'\x93\x01\xa1l1\x97"
        self.assertTrue(list(xor.xor(pck)) == pck)
        self.assertTrue(xor.key == key_xor)
        self.assertTrue(list(xor.xor([b'123456789101112'])) == \
            [b'\x98\x93\x0e\x8c\x18\x81\xde\xaf\xc9/\x92\x00\xa1l2'])
        self.assertFalse(xor.key == key_xor)
        self.assertTrue(xor.key == b"\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\xd7'\x93\x01\xa1l1\x97")

        xor = Xor('code')
        self.assertTrue(list(xor.xor(pck)) == pck)
        self.assertTrue(xor.key == key_xor)
        self.assertTrue(list(xor.xor([b'\x98\x93\x0e\x8c\x18\x81\xde\xaf\xc9/\x92\x00\xa1l2'])) == \
            [b'123456789101112'])
        self.assertFalse(xor.key == key_xor)
        self.assertTrue(xor.key == b"\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\xd7'\x93\x01\xa1l1\x97")



def get_exec_path():
        try:
            sFile = os.path.abspath(sys.modules['__main__'].__file__)
        except:
            sFile = sys.executable
        return os.path.dirname(sFile)

if __name__ == '__main__':
    print(get_exec_path())
    unittest.main()