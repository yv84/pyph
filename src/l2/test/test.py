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
import asyncio
from asyncio.queues import Queue, QueueEmpty


PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))



def async_test(f):
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)
    return wrapper


class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSimple(self):
        self.assertTrue(True)

    @patch('proxy.manager.Manager')  
    @patch('importlib.import_module')
    def test_packet1(self, imp, manager):
        from proxy.packet_buffer import Packet

        packet = Packet(manager, None)
        from l2 import packet_pipe
        packet.client = packet_pipe.Connect('client', packet)
        packet.server = packet_pipe.Connect('server', packet)
        # packet.packet_pipe = import_module('l2.packet_pipe')

        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'')


    @patch('proxy.manager.Manager')  
    @patch('importlib.import_module')
    def test_packet_update1(self, imp, manager):
        from proxy.packet_buffer import Packet

        packet = Packet(manager, None)
        from l2 import packet_pipe
        packet.client = packet_pipe.Connect('client', packet)
        packet.server = packet_pipe.Connect('server', packet)

        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'')
        packet.update_data('server', b"123")
        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'123')       
        packet.update_data('server', b"456")
        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'123456') 
        packet.update_data('client', b"123")
        self.assertEqual(packet.client._data, b'123')
        self.assertEqual(packet.server._data, b'123456')       
        packet.update_data('client', b"456")
        self.assertEqual(packet.client._data, b'123456')
        self.assertEqual(packet.server._data, b'123456')



class TestSocketConnection1(unittest.TestCase):

    @patch('proxy.manager.Manager')  
    @patch('importlib.import_module')
    def test_packet_packet_handlers(self, imp, manager):
        
        from proxy.packet_buffer import Packet

        packet = Packet(manager, None)
        from l2 import packet_pipe
        packet.client = packet_pipe.Connect('client', packet)
        packet.server = packet_pipe.Connect('server', packet)
        
        self.loop = asyncio.get_event_loop()
        couroutine = packet.packet_handlers()
        result = self.loop.run_until_complete(couroutine)
        self.assertRaises(QueueEmpty, packet.client.q.get_nowait)
        self.assertRaises(QueueEmpty, packet.server.q.get_nowait)

        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'')
        packet.update_data('server', b"123")
        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'123')       
        packet.update_data('server', b"456")
        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'123456') 
        packet.update_data('client', b"123")
        self.assertEqual(packet.client._data, b'123')
        self.assertEqual(packet.server._data, b'123456')       
        packet.update_data('client', b"456")
        self.assertEqual(packet.client._data, b'123456')
        self.assertEqual(packet.server._data, b'123456')

        self.loop = asyncio.get_event_loop()
        couroutine = packet.packet_handlers()
        result = self.loop.run_until_complete(couroutine)
        self.assertEqual(packet.client.q.get_nowait(), b'123456')
        self.assertEqual(packet.server.q.get_nowait(), b'123456')
        self.assertRaises(QueueEmpty, packet.client.q.get_nowait)
        self.assertRaises(QueueEmpty, packet.server.q.get_nowait)




if __name__ == '__main__':
    unittest.main(warnings='ignore')
