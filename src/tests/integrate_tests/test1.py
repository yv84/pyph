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

    @unittest.skip('-')
    def testEchoServer(self):
        self.port1 = '9999'
        conn = {'ip': '127.0.0.1', 'port': self.port1}
        N = 3
        os.system('fuser -k '+conn['port']+'/tcp')
        def start_server():
            os.system('python3 tests/integrate_tests/tcp_echo.py --server --port 9999 > /dev/null')
        def start_client():
            os.system('python3 tests/integrate_tests/tcp_echo.py --client --port 9999 > /dev/null')
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
        N = 1
        for d, k in zip([c for c in conn], [conn[c] for c in conn]):
            os.system('fuser -k '+conn[d]['port']+'/tcp')
        os.system('fuser -k '+'5000'+'/tcp') # web
        def start_server():
            os.system('python3 tests/integrate_tests/tcp_echo.py --server --port 9999 > /dev/null')
        def start_proxy():
            os.system('python3 run.py')
        def start_client():
            os.system('python3 tests/integrate_tests/tcp_echo.py --client --port 8888 > /dev/null')
        processes = [Process(target=start_server, args=()),]
        #processes.append(Process(target=start_proxy, args=()))
        #from src.l2.xor import Xor
        import __init__
        processes.append(Process(target=__init__.main, args=()),)
        from tests.integrate_tests import ws_client
        processes.append(Process(target=ws_client.main, args=()),) # test_web_socket
        for i in range(N):
            processes.append(Process(target=start_client, args=()))
        processes[0].start()
        processes[1].start()
        time.sleep(1)
        for p in processes[2:]:
            p.start()
            time.sleep(0.1)
        time.sleep(25)

        processes.reverse()
        for p in processes:
            p.terminate()
            p.join()




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
