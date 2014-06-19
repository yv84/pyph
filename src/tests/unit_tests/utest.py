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
from subprocess import Popen
from multiprocessing import Process, Manager, JoinableQueue


class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip("!")
    def testSimple(self):
        self.assertTrue(True)


    @unittest.skip("import Message -> ImportError: No module named 'repr_to_bytes'") # from proxy.repr_to_bytes import repr_to_bytes
    def testMessageClass(self):
        from testing.msg_log import Message
        from testing.game_log import log
        _log, _side_log = Message.game_log_from_import(log())
        # with open(os.path.dirname(__file__) + '/game_log_15122012', 'r') as f:
        message_client = Message('client', log=_log, side_log=_side_log)
        message_server = Message('server', log=_log, side_log=_side_log)
        self.assertTrue(b''.join(message_client(b'')) == b''.join(_log[0:2]))
        self.assertTrue(b''.join(message_server(_log[0+7])) == _log[1+7])
        self.assertTrue(b''.join(message_client(_log[1+7])) == _log[2+7])
        self.assertTrue(b''.join(message_server(_log[2+7])) == b''.join(_log[3+7:4+1+7]))
        self.assertTrue(b''.join(message_client(b''.join(_log[3+7:4+1+7]))) == b''.join(_log[5+7:6+1+7]))

    @unittest.skip("import Message -> ImportError: No module named 'repr_to_bytes'")
    def test_repr_to_bytes(self):
        from testing.msg_log import Message
        f = os.path.dirname(__file__) + '/game_log_15122012'
        pattern = {'c': b'C-', 's': b'S-', 'start': 6, 'end': -2}
        log = Message.get_log_from_file(f, pattern)
        print(log)





def get_exec_path():
        try:
            sFile = os.path.abspath(sys.modules['__main__'].__file__)
        except:
            sFile = sys.executable
        return os.path.dirname(sFile)


if __name__ == '__main__':
    print(get_exec_path())
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner().run(suite)
    #unittest.main()
