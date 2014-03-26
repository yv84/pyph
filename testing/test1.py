# /usr/bin/python3

# python3 -m unittest -v testing.test1
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import sys
import os
import time
import io
from subprocess import Popen
from multiprocessing import Process, Manager, JoinableQueue


class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSimple(self):
        self.assertTrue(True)

    class DummyFile(object):
        def open(self, x): pass
        def write(self, x): pass
        def flush(self): pass

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




if __name__ == '__main__':
    unittest.main()