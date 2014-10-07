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
 
    def test_xor_init(self):
        from l2.xor import Xor
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



if __name__ == '__main__':
    unittest.main()
