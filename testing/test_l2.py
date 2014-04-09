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


def get_exec_path():
        try:
            sFile = os.path.abspath(sys.modules['__main__'].__file__)
        except:
            sFile = sys.executable
        return os.path.dirname(sFile)

if __name__ == '__main__':
    print(get_exec_path())
    unittest.main()