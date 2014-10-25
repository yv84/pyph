# /usr/bin/python3

# python3 -m unittest -v l2.test.test
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import sys
import os
import time
import io
import re
from itertools import tee
import asyncio
from asyncio.queues import Queue, QueueEmpty


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

    @patch('proxy.manager.Manager')  
    @patch('importlib.import_module')
    def test_packet1(self, imp, manager):
        from proxy.packet_buffer import Packet

        packet = Packet(manager, None)
        from l2 import packet_pipe
        packet.client = packet_pipe.Connect('client', packet)
        packet.server = packet_pipe.Connect('server', packet)

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


class TestSocketConnection2(unittest.TestCase):

    @patch('proxy.manager.Manager')  
    @patch('importlib.import_module')
    def test_packet_packet_handlers(self, imp, manager):
        
        from proxy.packet_buffer import Packet

        packet = Packet(manager, None)
        from l2 import packet_pipe
        packet.client = packet_pipe.Connect('client', packet)
        packet.server = packet_pipe.Connect('server', packet)

        class SideEffect1():
            def __init__(self, test):
                self.test = test
                self.client_value = []
                self.server_value = []

            def side_effect_client(self, arg):
                arg, value = tee(arg)
                value = list(value)
                if value:
                    self.test.assertEqual(list(value), self.client_value)
                return arg

            def side_effect_server(self, arg):
                arg, value = tee(arg)
                value = list(value)
                if value:
                    self.test.assertEqual(list(value), self.server_value)
                return arg

            def side_effect(self, arg):
                return arg

        side_effect1 = SideEffect1(self)
        packet.client.pipe.pck_get_data = MagicMock(
            side_effect=side_effect1.side_effect_client)
        packet.client.pipe.pck_manager = MagicMock(
            side_effect=side_effect1.side_effect)
        packet.server.pipe.pck_get_data = MagicMock(
            side_effect=side_effect1.side_effect_server)
        packet.server.pipe.pck_manager = MagicMock(
            side_effect=side_effect1.side_effect)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.loop = asyncio.get_event_loop()
        couroutine = packet.packet_handlers()
        result = self.loop.run_until_complete(couroutine)
        self.assertRaises(QueueEmpty, packet.client.q.get_nowait)
        self.assertRaises(QueueEmpty, packet.server.q.get_nowait)
        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'')
        self.assertEqual(packet.client.pipe.pck_get_data.call_count, 0)
        self.assertEqual(packet.server.pipe.pck_get_data.call_count, 0)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        packet.update_data('client', b'\x19\x00.\x01\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\x01\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(packet.client._data, b'\x19\x00.\x01\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\x01\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(packet.server._data, b'')
        self.loop = asyncio.get_event_loop()
        couroutine = packet.packet_handlers()
        result = self.loop.run_until_complete(couroutine)
        self.assertEqual(packet.client.pipe.pck_get_data.call_count, 1)
        self.assertEqual(packet.server.pipe.pck_get_data.call_count, 0)
        self.assertRaises(QueueEmpty, packet.client.q.get_nowait)
        self.assertEqual(packet.server.q.get_nowait(), b'\x19\x00.\x01\xa9\x90\x0f\x8b\x19\x82\xdf\xa0\x01\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00')
        self.assertRaises(QueueEmpty, packet.client.q.get_nowait)
        self.assertRaises(QueueEmpty, packet.server.q.get_nowait)
        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        side_effect1.client_value = []
        side_effect1.server_value = [b'+s\x001\x001\x00a\x00\x00\x006r\x1d\x000\x88\x00\x006r\x1d\x00\xf2g+\x10\x08\x00\x00\x00\x01\x00\x00\x00\xe0>\x9e ']
        packet.update_data('client', b')\x00\x82an\xd4\xcd~\xa1`\xa8\x8f\x1c+\xf8\x89\xb8\x1f>\xae\xa1\x1cw\xe87e\xca\xc6EL\xed\x81\xb0&\x8f\x1f\x10{\\@\xbf')
        self.assertEqual(packet.client._data, b')\x00\x82an\xd4\xcd~\xa1`\xa8\x8f\x1c+\xf8\x89\xb8\x1f>\xae\xa1\x1cw\xe87e\xca\xc6EL\xed\x81\xb0&\x8f\x1f\x10{\\@\xbf')
        self.loop = asyncio.get_event_loop()
        couroutine = packet.packet_handlers()
        result = self.loop.run_until_complete(couroutine)
        self.assertEqual(packet.client.pipe.pck_get_data.call_count, 2)
        self.assertEqual(packet.server.pipe.pck_get_data.call_count, 1)
        self.assertRaises(QueueEmpty, packet.client.q.get_nowait)
        self.assertEqual(packet.server.q.get_nowait(), b')\x00\x82an\xd4\xcd~\xa1`\xa8\x8f\x1c+\xf8\x89\xb8\x1f>\xae\xa1\x1cw\xe87e\xca\xc6EL\xed\x81\xb0&\x8f\x1f\x10{\\@\xbf')
        self.assertRaises(QueueEmpty, packet.client.q.get_nowait)
        self.assertRaises(QueueEmpty, packet.server.q.get_nowait)
        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        side_effect1.client_value = [b"\t\x02\x00\x00\x00\x07\x00\x00'\x00t\x00e\x00s\x00t\x00d\x00s\x00a\x00A\x00a\x00s\x00d\x00f\x00\x00\x00\xb4y\x00\x00T\x001\x001\x00a\x00\x00\x006r\x1d\x00\x00\x00'\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\n\x00'\x00\x01\x00\x00\x00\x16\x9e\xfe\xff\xd3\xc9\x03\x00\x10\xf2\xd8\xff\xb5\xa6y\xc7)\x0eh@\xf8\xa0g\xb3\xeaSD@Q\x03\x00\x00\xa40\x00\x00\x00\x00\x00\x00\x07\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\xa9\x01\x00\x00\xcd\x01\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb5\xa6^\xc7)\x0eh@\xf8\xa0g\xb3\xeaSc@\x00\x00'\x00\n\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00t\x002\x003\x004\x005\x006\x007'8\x009\x000\x001\x002\x003\x004\x005'6\x00\x00\x00\xd3\xa8\x01\x00s\x001\x001\x00a'\x00\x006r\x1d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x01\x00\x00\x00\xf6\xbb\xfe\xff\xdb\xc8\x03\x00\x0e\xf2\xff\xff\x1f\x85\xebQ\xb8\x99X@\x9a\x99\x99\x99\x99\x99M@\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa9\x01\x00\x00\xcd&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80X@\x00'\x00\x00\x00\x80M@\x00\x00\x00\x00\n\x00\x00\x00\x00'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"]
        side_effect1.server_value = []
        packet.update_data('server', b'v\x02\xa02=\xb6\xaf*\xf5U\xba\x9dz{\xbf\xd3\x91\x06\xdbK \xab\xc1C\xfd]\xd4\xf3\x01\x00\xd2\xbe\xeb|\xb3#,\xa7\n\xf1.\x8e\x125\x97\x96\x06j:\xad\x04\x94\xadTP\xd2\r\xadBe\xf6\xf7V:\n\x9d4\xa4\xab 9\xbbn\xce!\x06\x94\x954X\x7fv!N\x92\xd0\xcaH\x87\xd5\xc5\x1d;\x9cD\xef\xf7n\xaf\x7f\x88\xa3\xdd\xec\xd9*\xa6\xc1\x03\x01\xa0\xccY\xfeW\xc7\xc8CZ\xd8\x00\xa0Oh\xfb\xfa[7\x06\x918\xa8\xa7,5\xb7h\xc8\'\x00\x93\x923_n\xf9P\xc0\xcfD]\xdf\x00\xa0Oh\xfb\xfa[7\x06\x918\xa8\xa7,5\xb7h\xc8\'\x00\x93\x923_n\xf9P\xc0\xcfD]\xdf\x00\xa0Oh\xfb\xfa[7\x00\x97>\xae\xa1*3\xb1n\xce!\x06<<\x9d\xf1\r\x9b2\xa2\xad&?\xbdb\xc2-\n\x99\x989Ud\xf3Z\xca\xc5NW\xd5\n\xaaEb\xf1\xf0Q=\x0c\x9b2\xa2\xad&?\xbdb\xc2-\n\x99\x989Ud\xf3Z\xca\xc5NW\xd5\n\xaaEb\xf1\xf0Q=\x0c\x9b2\xa2\xad&?\xbd\xd7\xd1G\xa7\x1d\x12\xdb\xf7>\t\xc7\xe4\x01\xd9\xa3a\xbe\x1e\xf1\xd6ON\xef\x83\xb3$\x8d\x1d\x12\x99\x80\x02\xdd}\x92\xb5&S\xf2\xac\x9d9\x904;\x85\x9c(\xf7`\x8f\x90\x03;\x9a\xc6\xf7Q\xf8ZU\xed\xf4B\x9d\x08\xe7\xf6ed\xc5z\xe3u\xdc?0\x8a\x93 \xff>\xd1\xf6eR\x81\xf0\xc1V\xffo`\xeb\xf2p\xaf\x0e\xe1\xc6UT\xf5\x99\xa85\x9c\x0c\x03\x89\x90\x12\xcd\x9b\xe81]\x87\xee\x81\xb0)r\x1d\xedy\xe5\x8c\x02\x1aK4\xe7|D\xb1\x19\x17\'\xfa\xb5>\'\xa5z\xda5\x12\x81\x80!M|\xeaC\xd3\xdcWN\xcc\x13\xb3\\{\xe8\xe9H$\x15\x82+\xbb\xb4?&\xa4{\xdb4\x13\x80\x81 L}\xeaC\xd3\xdcWN\xcc\x13\xb3\\{\xe8\xe9H$\x15\x82+\xbb\xb4?&\xa4{\xdb4\x13\x80\x81 L}\xeaC\xd3\xdcWN\xcc\x13\xb5Z}\xee\xefN"\x13\x84-\xbd\xb2\x90\x88\n\xd5\xb8Vq\xe2\xe3B.\x1f\x88!\xb1\xbe5,\xaeq\xd1>\x19\x8a\x8b*Fw\xe0I\xd9\xd6]D\xc6\x19\xb9Vq\xe2\xe3B.\x1f\x88!\xb1\xbe5,\xaeq\xd1>\x19\x8a\x8b*Fw\xe0I\xd9\xd6]D\xc6\x19\xb9Vq\xe2\xe3B.\x1f\x88!\xb1\xbe5\xacv\xe9I\xa6\x81\x12\x132\x13b\xf5\\\xcc\xc3B[\xd9\x06\xa6In\xfd\xfc]1\x00\x97>\xae\xa1*')
        self.assertEqual(packet.server._data, b'v\x02\xa02=\xb6\xaf*\xf5U\xba\x9dz{\xbf\xd3\x91\x06\xdbK \xab\xc1C\xfd]\xd4\xf3\x01\x00\xd2\xbe\xeb|\xb3#,\xa7\n\xf1.\x8e\x125\x97\x96\x06j:\xad\x04\x94\xadTP\xd2\r\xadBe\xf6\xf7V:\n\x9d4\xa4\xab 9\xbbn\xce!\x06\x94\x954X\x7fv!N\x92\xd0\xcaH\x87\xd5\xc5\x1d;\x9cD\xef\xf7n\xaf\x7f\x88\xa3\xdd\xec\xd9*\xa6\xc1\x03\x01\xa0\xccY\xfeW\xc7\xc8CZ\xd8\x00\xa0Oh\xfb\xfa[7\x06\x918\xa8\xa7,5\xb7h\xc8\'\x00\x93\x923_n\xf9P\xc0\xcfD]\xdf\x00\xa0Oh\xfb\xfa[7\x06\x918\xa8\xa7,5\xb7h\xc8\'\x00\x93\x923_n\xf9P\xc0\xcfD]\xdf\x00\xa0Oh\xfb\xfa[7\x00\x97>\xae\xa1*3\xb1n\xce!\x06<<\x9d\xf1\r\x9b2\xa2\xad&?\xbdb\xc2-\n\x99\x989Ud\xf3Z\xca\xc5NW\xd5\n\xaaEb\xf1\xf0Q=\x0c\x9b2\xa2\xad&?\xbdb\xc2-\n\x99\x989Ud\xf3Z\xca\xc5NW\xd5\n\xaaEb\xf1\xf0Q=\x0c\x9b2\xa2\xad&?\xbd\xd7\xd1G\xa7\x1d\x12\xdb\xf7>\t\xc7\xe4\x01\xd9\xa3a\xbe\x1e\xf1\xd6ON\xef\x83\xb3$\x8d\x1d\x12\x99\x80\x02\xdd}\x92\xb5&S\xf2\xac\x9d9\x904;\x85\x9c(\xf7`\x8f\x90\x03;\x9a\xc6\xf7Q\xf8ZU\xed\xf4B\x9d\x08\xe7\xf6ed\xc5z\xe3u\xdc?0\x8a\x93 \xff>\xd1\xf6eR\x81\xf0\xc1V\xffo`\xeb\xf2p\xaf\x0e\xe1\xc6UT\xf5\x99\xa85\x9c\x0c\x03\x89\x90\x12\xcd\x9b\xe81]\x87\xee\x81\xb0)r\x1d\xedy\xe5\x8c\x02\x1aK4\xe7|D\xb1\x19\x17\'\xfa\xb5>\'\xa5z\xda5\x12\x81\x80!M|\xeaC\xd3\xdcWN\xcc\x13\xb3\\{\xe8\xe9H$\x15\x82+\xbb\xb4?&\xa4{\xdb4\x13\x80\x81 L}\xeaC\xd3\xdcWN\xcc\x13\xb3\\{\xe8\xe9H$\x15\x82+\xbb\xb4?&\xa4{\xdb4\x13\x80\x81 L}\xeaC\xd3\xdcWN\xcc\x13\xb5Z}\xee\xefN"\x13\x84-\xbd\xb2\x90\x88\n\xd5\xb8Vq\xe2\xe3B.\x1f\x88!\xb1\xbe5,\xaeq\xd1>\x19\x8a\x8b*Fw\xe0I\xd9\xd6]D\xc6\x19\xb9Vq\xe2\xe3B.\x1f\x88!\xb1\xbe5,\xaeq\xd1>\x19\x8a\x8b*Fw\xe0I\xd9\xd6]D\xc6\x19\xb9Vq\xe2\xe3B.\x1f\x88!\xb1\xbe5\xacv\xe9I\xa6\x81\x12\x132\x13b\xf5\\\xcc\xc3B[\xd9\x06\xa6In\xfd\xfc]1\x00\x97>\xae\xa1*')
        self.loop = asyncio.get_event_loop()
        couroutine = packet.packet_handlers()
        result = self.loop.run_until_complete(couroutine)
        self.assertEqual(packet.client.pipe.pck_get_data.call_count, 3)
        self.assertEqual(packet.server.pipe.pck_get_data.call_count, 2)
        self.assertEqual(packet.client.q.get_nowait(), b'v\x02\xa02=\xb6\xaf*\xf5U\xba\x9dz{\xbf\xd3\x91\x06\xdbK \xab\xc1C\xfd]\xd4\xf3\x01\x00\xd2\xbe\xeb|\xb3#,\xa7\n\xf1.\x8e\x125\x97\x96\x06j:\xad\x04\x94\xadTP\xd2\r\xadBe\xf6\xf7V:\n\x9d4\xa4\xab 9\xbbn\xce!\x06\x94\x954X\x7fv!N\x92\xd0\xcaH\x87\xd5\xc5\x1d;\x9cD\xef\xf7n\xaf\x7f\x88\xa3\xdd\xec\xd9*\xa6\xc1\x03\x01\xa0\xccY\xfeW\xc7\xc8CZ\xd8\x00\xa0Oh\xfb\xfa[7\x06\x918\xa8\xa7,5\xb7h\xc8\'\x00\x93\x923_n\xf9P\xc0\xcfD]\xdf\x00\xa0Oh\xfb\xfa[7\x06\x918\xa8\xa7,5\xb7h\xc8\'\x00\x93\x923_n\xf9P\xc0\xcfD]\xdf\x00\xa0Oh\xfb\xfa[7\x00\x97>\xae\xa1*3\xb1n\xce!\x06<<\x9d\xf1\r\x9b2\xa2\xad&?\xbdb\xc2-\n\x99\x989Ud\xf3Z\xca\xc5NW\xd5\n\xaaEb\xf1\xf0Q=\x0c\x9b2\xa2\xad&?\xbdb\xc2-\n\x99\x989Ud\xf3Z\xca\xc5NW\xd5\n\xaaEb\xf1\xf0Q=\x0c\x9b2\xa2\xad&?\xbd\xd7\xd1G\xa7\x1d\x12\xdb\xf7>\t\xc7\xe4\x01\xd9\xa3a\xbe\x1e\xf1\xd6ON\xef\x83\xb3$\x8d\x1d\x12\x99\x80\x02\xdd}\x92\xb5&S\xf2\xac\x9d9\x904;\x85\x9c(\xf7`\x8f\x90\x03;\x9a\xc6\xf7Q\xf8ZU\xed\xf4B\x9d\x08\xe7\xf6ed\xc5z\xe3u\xdc?0\x8a\x93 \xff>\xd1\xf6eR\x81\xf0\xc1V\xffo`\xeb\xf2p\xaf\x0e\xe1\xc6UT\xf5\x99\xa85\x9c\x0c\x03\x89\x90\x12\xcd\x9b\xe81]\x87\xee\x81\xb0)r\x1d\xedy\xe5\x8c\x02\x1aK4\xe7|D\xb1\x19\x17\'\xfa\xb5>\'\xa5z\xda5\x12\x81\x80!M|\xeaC\xd3\xdcWN\xcc\x13\xb3\\{\xe8\xe9H$\x15\x82+\xbb\xb4?&\xa4{\xdb4\x13\x80\x81 L}\xeaC\xd3\xdcWN\xcc\x13\xb3\\{\xe8\xe9H$\x15\x82+\xbb\xb4?&\xa4{\xdb4\x13\x80\x81 L}\xeaC\xd3\xdcWN\xcc\x13\xb5Z}\xee\xefN"\x13\x84-\xbd\xb2\x90\x88\n\xd5\xb8Vq\xe2\xe3B.\x1f\x88!\xb1\xbe5,\xaeq\xd1>\x19\x8a\x8b*Fw\xe0I\xd9\xd6]D\xc6\x19\xb9Vq\xe2\xe3B.\x1f\x88!\xb1\xbe5,\xaeq\xd1>\x19\x8a\x8b*Fw\xe0I\xd9\xd6]D\xc6\x19\xb9Vq\xe2\xe3B.\x1f\x88!\xb1\xbe5\xacv\xe9I\xa6\x81\x12\x132\x13b\xf5\\\xcc\xc3B[\xd9\x06\xa6In\xfd\xfc]1\x00\x97>\xae\xa1*')
        self.assertRaises(QueueEmpty, packet.server.q.get_nowait)
        self.assertRaises(QueueEmpty, packet.client.q.get_nowait)
        self.assertRaises(QueueEmpty, packet.server.q.get_nowait)
        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        side_effect1.client_value = [b's\x00\x01']
        side_effect1.server_value = [b'\x12\x00\x00\x00\x00\x00\x00\x00\x8c\r\x00\x00\x00\x00\x00\x00\x00\x00\x00']
        packet.update_data('client', b'\x15\x00\xbb+$\xaf\xb64\xebK(\x02\x91\x901]l\xfbR\xc2\xcd')
        packet.update_data('server', b'\x05\x00\xdaJD')
        self.assertEqual(packet.client._data, b'\x15\x00\xbb+$\xaf\xb64\xebK(\x02\x91\x901]l\xfbR\xc2\xcd')
        self.assertEqual(packet.server._data, b'\x05\x00\xdaJD')
        self.loop = asyncio.get_event_loop()
        couroutine = packet.packet_handlers()
        result = self.loop.run_until_complete(couroutine)
        self.assertEqual(packet.client.pipe.pck_get_data.call_count, 4)
        self.assertEqual(packet.server.pipe.pck_get_data.call_count, 3)
        self.assertEqual(packet.client.q.get_nowait(), b'\x05\x00\xdaJD')
        self.assertEqual(packet.server.q.get_nowait(), b'\x15\x00\xbb+$\xaf\xb64\xebK(\x02\x91\x901]l\xfbR\xc2\xcd')
        self.assertRaises(QueueEmpty, packet.client.q.get_nowait)
        self.assertRaises(QueueEmpty, packet.server.q.get_nowait)
        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        side_effect1.client_value = [b"\x0bt\x00e\x00s\x00tFd\x00s\x00a\x00f\x00a\x00s\x00d\x00fF\x00\x00\xb4y\x00\x00\x00\x006r\x1d\x00\x00\x00\x00F\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\n\x00\x00F\x01\x00\x00\x00\x16\x9e\xfe\xff\xd3\xc9\x03\x00\x10\xf2\xff\xb9\xb5\xa6y\xc7)\x0eh@\xf8\xa0g\xb3\xeaSc\x06Q\x03\x00\x00\xa40\x00\x00\x00\x00\x00\x00\x07\x00\x00F\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x15\x00\x00F\x1b\x00\x00\x00)\x00\x00\x00\x14\x00\x00\x00'\x00\x00F\xcb\x03\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00F"]
        side_effect1.server_value = [b'\xd0\x01\x00', b'\xd0!\x00']
        packet.update_data('client', b"".join([b'\x05\x00y\xe8\xe7', b'\x05\x00y\xc8\xc7']))
        packet.update_data('server', b'\xeb\x00\xa2FI\xa7\xbeO\x90D=s\xe0\x923>\x0f\xfeW\xa6\xa9QH\xaeq\xb7\xce\xe4w\xc2\x1avG\xd0y\xdf\xa24-\xafp\xd0\xa9\x83\x10\x11\xb0\xdd\xec{\xd2BM\xc6\xdfW\x88(Qz\xe9\xe8I3\x9c\xf5\xa3\xe0&\xae\xb7%\x08W\xd1N{\x03e \x1f\xe0\ta\xce"\x88\xe0l\xaf\x96\xed}|\xdd\x15\x14\x83*\xba\xb5>\'\xa2}\xdd\xa4\x8e\x1d\x1c\xbd\xd1\xe0w\xdeXW\xdc\xc5R\x8d-Te\xf6\xf7V\x13"\xb5\x1c\x98\x97\x1c\x05\xa0\x7f\xdf\xa6G\xd7\xd6w\x1b*\xbd\x14\x8e\x81\n\x13\x91N\xee\x97\xbd./\x8e\xe2\xd3D\xed}r\xf9\xe0b\xbd\x1ddN\xdd\xdc}\x11 \xb7\x1e\x8e\x81\n\x13\x91N\xee\x97\xbd./\x8e\xe2\xd3D\xed}r\xf9\xe0b\xbd\x1ddN\xdd\xdc}\x11 \xb7\x1e\x8e\x81\n\x13\x91N\xee\x97\xbd./\x8e\xe2\xd3D\xed}r\xf9\xe0b\xbd\x1dd')
        self.assertEqual(packet.client._data, b'\x05\x00y\xe8\xe7\x05\x00y\xc8\xc7')
        self.assertEqual(packet.server._data, b'\xeb\x00\xa2FI\xa7\xbeO\x90D=s\xe0\x923>\x0f\xfeW\xa6\xa9QH\xaeq\xb7\xce\xe4w\xc2\x1avG\xd0y\xdf\xa24-\xafp\xd0\xa9\x83\x10\x11\xb0\xdd\xec{\xd2BM\xc6\xdfW\x88(Qz\xe9\xe8I3\x9c\xf5\xa3\xe0&\xae\xb7%\x08W\xd1N{\x03e \x1f\xe0\ta\xce"\x88\xe0l\xaf\x96\xed}|\xdd\x15\x14\x83*\xba\xb5>\'\xa2}\xdd\xa4\x8e\x1d\x1c\xbd\xd1\xe0w\xdeXW\xdc\xc5R\x8d-Te\xf6\xf7V\x13"\xb5\x1c\x98\x97\x1c\x05\xa0\x7f\xdf\xa6G\xd7\xd6w\x1b*\xbd\x14\x8e\x81\n\x13\x91N\xee\x97\xbd./\x8e\xe2\xd3D\xed}r\xf9\xe0b\xbd\x1ddN\xdd\xdc}\x11 \xb7\x1e\x8e\x81\n\x13\x91N\xee\x97\xbd./\x8e\xe2\xd3D\xed}r\xf9\xe0b\xbd\x1ddN\xdd\xdc}\x11 \xb7\x1e\x8e\x81\n\x13\x91N\xee\x97\xbd./\x8e\xe2\xd3D\xed}r\xf9\xe0b\xbd\x1dd')
        self.loop = asyncio.get_event_loop()
        couroutine = packet.packet_handlers()
        result = self.loop.run_until_complete(couroutine)
        self.assertEqual(packet.client.pipe.pck_get_data.call_count, 5)
        self.assertEqual(packet.server.pipe.pck_get_data.call_count, 4)
        self.assertEqual(packet.client.q.get_nowait(), b'\xeb\x00\xa2FI\xa7\xbeO\x90D=s\xe0\x923>\x0f\xfeW\xa6\xa9QH\xaeq\xb7\xce\xe4w\xc2\x1avG\xd0y\xdf\xa24-\xafp\xd0\xa9\x83\x10\x11\xb0\xdd\xec{\xd2BM\xc6\xdfW\x88(Qz\xe9\xe8I3\x9c\xf5\xa3\xe0&\xae\xb7%\x08W\xd1N{\x03e \x1f\xe0\ta\xce"\x88\xe0l\xaf\x96\xed}|\xdd\x15\x14\x83*\xba\xb5>\'\xa2}\xdd\xa4\x8e\x1d\x1c\xbd\xd1\xe0w\xdeXW\xdc\xc5R\x8d-Te\xf6\xf7V\x13"\xb5\x1c\x98\x97\x1c\x05\xa0\x7f\xdf\xa6G\xd7\xd6w\x1b*\xbd\x14\x8e\x81\n\x13\x91N\xee\x97\xbd./\x8e\xe2\xd3D\xed}r\xf9\xe0b\xbd\x1ddN\xdd\xdc}\x11 \xb7\x1e\x8e\x81\n\x13\x91N\xee\x97\xbd./\x8e\xe2\xd3D\xed}r\xf9\xe0b\xbd\x1ddN\xdd\xdc}\x11 \xb7\x1e\x8e\x81\n\x13\x91N\xee\x97\xbd./\x8e\xe2\xd3D\xed}r\xf9\xe0b\xbd\x1dd')
        self.assertEqual(packet.server.q.get_nowait(), b'\x05\x00y\xe8\xe7\x05\x00y\xc8\xc7')
        self.assertRaises(QueueEmpty, packet.client.q.get_nowait)
        self.assertRaises(QueueEmpty, packet.server.q.get_nowait)
        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        side_effect1.client_value = [b'\xfe"\x00\t\x00\x00\x00\x01@\x00\x00g\x00l\x00u\x00d\x00i\x00o\x00\x00@\x02\x00\x00\x00d\x00i\x00o\x00n\x00\x00\x00\x03@\x00\x00g\x00i\x00r\x00a\x00n\x00\x00\x00\x04@\x00\x00o\x00r\x00e\x00n\x00\x00\x00\x05\x00\x00@a\x00d\x00e\x00n\x00\x00\x00\x06\x00\x00\x00i@n\x00n\x00a\x00d\x00r\x00i\x00l\x00e@\x00\x00\x07\x00\x00\x00g\x00o\x00d\x00a\x00r@d\x00\x00\x00\x08\x00\x00\x00r\x00u\x00n\x00e@\x00\x00\t\x00\x00\x00s\x00h\x00u\x00t\x00t@g\x00a\x00r\x00t\x00\x00\x00']
        side_effect1.server_value = [b'\x11\x00\x00\x00\x00\x00\x00\x00\x03\x04\x00\x00\x00\x00\x00\x00\x00\xc9\xbc\xf2\xa7fZ\x0b\x9b2\xa5\xbd\x89\xed\x7f\xe4\xd7kI\xe2\x9f\xefv\xeb\xcd\xa7\xfa\xf4\xbf\x0cd\xa3\xb4\xa4\xce\xdc\xc6\x08>n\xe9A\xca\xd3\xfe\x88\x13\x87\xb8\x06,\x96\xf0\x9b\x1e\x8e\xbf\xc2\x9b\x98\xc8c\x16\xcf\xd0\xbe\x18\x00\x00\xc0\xa8d\x06\xc4\xa8d\x01S\xdb\x08\x01S\xdb\x05\x11Z\x96\x02\x19']
        packet.update_data('client', b"k\x00\xb8('\xac\xb57\xe8HCo\xfc\xfd\\0\x01\x96?f\xd5\xac\x12\xf6s\xd8KQg\xdb\xf3r<O1\xca\x8c\xe5c\x0e\xa7\xec)\xa6\xcf:$D\x11%8\x0c\xcd\x9aE\xcf.\xe0\x01h1\xe3\xbcXzj{\xed\xce\xd3:#\xe2\xcc{\x91\x99\x00ifA\x19`NY\xd2\xcb\x89\xfe:4\xd8\xe3\x86&\x19\xf3l\xc4\x07\xd3]U\x8d\xc4fw")
        packet.update_data('server', b'\xa5\x00W\xe5\xeahq\xf3,\x8d\xe5\xce];\x9a\x9a\xabI\xe0\x14\x1b\xf9\xe0\r\xd2r\x1a3\xa0\xa1\x00\x089\xc7n\x91\x9e{b\xe0?\x9c\xf4\xdfL*\x8b\x8e\xbfZ\xf3\x02\r\xe8\xf1s\xac\x08`K\xd8\xb6\x17\t8\xcac\x9d\x92\x19\x00\x87X\xf8\x90\xdaI,\x8d\x84\xb5L\xe5uz\xf7\xeel\xb3z\x12W\xc4\xab\n\x076\xc5l\x8e\x81cz\x94K\x8e\xe6\xcd^X\xf9\x95\xa4T\xfd\x02\r\xe2\xfb\x18\xc7\x15}2\xa1\xa0\x01eT\xc3j\x88\x87y`\x8cS\x96\xfe\xd5FN\xef\x83\xb2V\xff\x07\x08\xf6\xef\x19\xc6\x12z6\xa5\xc5dzK\xa8\x01\x91\x9e')
        self.assertEqual(packet.client._data, b"k\x00\xb8('\xac\xb57\xe8HCo\xfc\xfd\\0\x01\x96?f\xd5\xac\x12\xf6s\xd8KQg\xdb\xf3r<O1\xca\x8c\xe5c\x0e\xa7\xec)\xa6\xcf:$D\x11%8\x0c\xcd\x9aE\xcf.\xe0\x01h1\xe3\xbcXzj{\xed\xce\xd3:#\xe2\xcc{\x91\x99\x00ifA\x19`NY\xd2\xcb\x89\xfe:4\xd8\xe3\x86&\x19\xf3l\xc4\x07\xd3]U\x8d\xc4fw")
        self.assertEqual(packet.server._data, b'\xa5\x00W\xe5\xeahq\xf3,\x8d\xe5\xce];\x9a\x9a\xabI\xe0\x14\x1b\xf9\xe0\r\xd2r\x1a3\xa0\xa1\x00\x089\xc7n\x91\x9e{b\xe0?\x9c\xf4\xdfL*\x8b\x8e\xbfZ\xf3\x02\r\xe8\xf1s\xac\x08`K\xd8\xb6\x17\t8\xcac\x9d\x92\x19\x00\x87X\xf8\x90\xdaI,\x8d\x84\xb5L\xe5uz\xf7\xeel\xb3z\x12W\xc4\xab\n\x076\xc5l\x8e\x81cz\x94K\x8e\xe6\xcd^X\xf9\x95\xa4T\xfd\x02\r\xe2\xfb\x18\xc7\x15}2\xa1\xa0\x01eT\xc3j\x88\x87y`\x8cS\x96\xfe\xd5FN\xef\x83\xb2V\xff\x07\x08\xf6\xef\x19\xc6\x12z6\xa5\xc5dzK\xa8\x01\x91\x9e')
        self.loop = asyncio.get_event_loop()
        couroutine = packet.packet_handlers()
        result = self.loop.run_until_complete(couroutine)
        self.assertEqual(packet.client.pipe.pck_get_data.call_count, 6)
        self.assertEqual(packet.server.pipe.pck_get_data.call_count, 5)
        self.assertEqual(packet.client.q.get_nowait(), b'\xa5\x00W\xe5\xeahq\xf3,\x8d\xe5\xce];\x9a\x9a\xabI\xe0\x14\x1b\xf9\xe0\r\xd2r\x1a3\xa0\xa1\x00\x089\xc7n\x91\x9e{b\xe0?\x9c\xf4\xdfL*\x8b\x8e\xbfZ\xf3\x02\r\xe8\xf1s\xac\x08`K\xd8\xb6\x17\t8\xcac\x9d\x92\x19\x00\x87X\xf8\x90\xdaI,\x8d\x84\xb5L\xe5uz\xf7\xeel\xb3z\x12W\xc4\xab\n\x076\xc5l\x8e\x81cz\x94K\x8e\xe6\xcd^X\xf9\x95\xa4T\xfd\x02\r\xe2\xfb\x18\xc7\x15}2\xa1\xa0\x01eT\xc3j\x88\x87y`\x8cS\x96\xfe\xd5FN\xef\x83\xb2V\xff\x07\x08\xf6\xef\x19\xc6\x12z6\xa5\xc5dzK\xa8\x01\x91\x9e')
        self.assertEqual(packet.server.q.get_nowait(), b"k\x00\xb8('\xac\xb57\xe8HCo\xfc\xfd\\0\x01\x96?f\xd5\xac\x12\xf6s\xd8KQg\xdb\xf3r<O1\xca\x8c\xe5c\x0e\xa7\xec)\xa6\xcf:$D\x11%8\x0c\xcd\x9aE\xcf.\xe0\x01h1\xe3\xbcXzj{\xed\xce\xd3:#\xe2\xcc{\x91\x99\x00ifA\x19`NY\xd2\xcb\x89\xfe:4\xd8\xe3\x86&\x19\xf3l\xc4\x07\xd3]U\x8d\xc4fw")
        self.assertRaises(QueueEmpty, packet.client.q.get_nowait)
        self.assertRaises(QueueEmpty, packet.server.q.get_nowait)
        self.assertEqual(packet.client._data, b'')
        self.assertEqual(packet.server._data, b'')
        # #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == '__main__':
    unittest.main(warnings='ignore')
