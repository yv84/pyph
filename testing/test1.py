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

    def testSimple(self):
        self.assertTrue(True)


    def testEchoServer(self):
        self.port1 = '9999'
        conn = {'ip': '127.0.0.1', 'port': self.port1}
        N = 10
        os.system('fuser -k '+conn['port']+'/tcp')
        def start_server():
            os.system('python3 testing/tcp_echo.py --server > /dev/null')
        def start_client():
            os.system('python3 testing/tcp_echo.py --client > /dev/null')
        processes = [Process(target=start_server, args=()),]
        for i in range(N):
            processes.append(Process(target=start_client, args=()))
        processes[0].start()
        time.sleep(0.1)
        for p in processes[1:]:
            p.start()
            time.sleep(0.1)

        processes.reverse()
        for p in processes:
            p.terminate()
            p.join()



    def testProxyServer(self):
        self.port1 = '9999'
        self.port2 = '8888'
        conn = {
            'client': {'ip': '127.0.0.1', 'port': self.port1}, # client -> proxy
            'server': {'ip': '127.0.0.1', 'port': self.port2}, # proxy -> server
            }
        N = 10
        for d, k in zip([c for c in conn], [conn[c] for c in conn]):
            os.system('fuser -k '+conn[d]['port']+'/tcp')
        def start_server():
            os.system('python3 testing/tcp_echo.py --server > /dev/null')
        def start_proxy():
            os.system('python3 proxy.py > /dev/null')
        def start_client():
            os.system('python3 testing/tcp_echo.py --client --port 8888 > /dev/null')
        processes = [Process(target=start_server, args=()),]
        processes.append(Process(target=start_proxy, args=()))
        for i in range(N):
            processes.append(Process(target=start_client, args=()))
        processes[0].start()
        time.sleep(0.1)
        for p in processes[1:]:
            p.start()
            time.sleep(0.1)
        
        processes.reverse()
        for p in processes:
            p.terminate()
            p.join()



    def testMessageClass(self):
        from testing.msg_log import Message
        from testing.game_log import log
        _log = []
        _side_log = {'client': [], 'server': []}
        i = 0
        while log:
            if log and log[0].get('C'):
                _side_log['client'].append(i)
                _log.append(log.pop(0)['C'])
            elif log and log[0].get('S'):
                _side_log['server'].append(i)
                _log.append(log.pop(0)['S'])
            else:
                raise Exception("S/C key wrong")
            i += 1
        # with open(os.path.dirname(__file__) + '/game_log_15122012', 'r') as f:
        message_client = Message('client', log=_log, side_log=_side_log)
        message_server = Message('server', log=_log, side_log=_side_log)
        self.assertTrue(b''.join(message_client(b'')) == _log[0])
        self.assertTrue(b''.join(message_server(_log[0])) == _log[1])
        self.assertTrue(b''.join(message_client(_log[1])) == _log[2])
        self.assertTrue(b''.join(message_server(_log[2])) == b''.join(_log[3:4+1]))
        self.assertTrue(b''.join(message_client(b''.join(_log[3:4+1]))) == b''.join(_log[5:6+1]))



def get_exec_path():
        try:
            sFile = os.path.abspath(sys.modules['__main__'].__file__)
        except:
            sFile = sys.executable
        return os.path.dirname(sFile)

if __name__ == '__main__':
    print(get_exec_path())
    unittest.main()