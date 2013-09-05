#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
На стороне сервера: открывает сокет на указанном порту, ожидает поступления 
сообщения от клиента и отправляет его обратно; эта версия использует 
стандартный модуль socketserver; модуль socketserver предоставляет классы 
TCPServer, ThreadingTCPServer, ForkingTCPServer, их варианты для протокола 
UDP и многое другое, передает каждый запрос клиента на соединение методу 
handle нового экземпляра указанного объекта обработчика; кроме того, 
модуль socketserver поддерживает доменные сокеты Unix, но только 
в Unix­подобных системах; смотрите руководство по стандартной 
библиотеке Python.
"""
import socketserver, time  # получить серверы сокетов, объекты ­обработчики


def MyClientHandler(m_f):
    class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
      
        def setup(self):
            self.m_func = m_f
            print(m_f)
              
        def handle(self):                      # для каждого клиента
            print(self.client_address, self.m_func.now())  # показать адрес этого клиента
            #time.sleep(1)                      # имитировать блокирующие действия
            while True:                        # self.request  сокет клиента
                try:
                    data = self.request.recv(1024) # чтение, запись в сокет клиента
                    #Rules.match(data)
                    reply = ''
                    if not data: break
                    if data == b'hello world':
                        reply +=  ";".join(["%s=%s" % (k, v) for i in self.m_func.process for k, v in self.m_func.process[i].F.items()])
                        reply += 'Echo=>%s at %s' % (data, self.m_func.now())
                    if data == b'inj-00':
                        self.m_func.currentConn.F['C'].inject_tpl((0,),)
                        reply += 'conn close: %s'%self.m_func.currentConn
                        #for i in self.m_func.process: # dict of port listeners
                            #for k, v in self.m_func.process[i].F.items(): #dict of forwarders in port 
                                #print('quit')
                                #v.F['C'].inject_pck(b'\x00')
                                #v.F['C'].inject_tpl((0,),)
                                #break
                                #break
                    if data == b'get_connect':
                        self.m_func.get_connect()
                        reply += '=>%s at %s' % (self.m_func.conn, self.m_func.now())
                    if data == b'set_connect':
                        if not self.m_func.conn : 
                            self.request.send(b'net soedineniu')
                        else:
                            self.request.send(b'vvedite nomer soedineniya, 0-'+str(len(self.m_func.conn)-1).encode('latin-1')+b':')
                            data = self.request.recv(1024)
                            if not data: break
                            if data.isdigit():
                                data = int(data)
                                if data >= 0 and data < len(self.m_func.conn):
                                    self.m_func.currentConn = self.m_func.conn[data]
                                    reply += 'select %s' % self.m_func.currentConn
                                    print(reply)
                    if reply: self.request.send(reply.encode())
                except: break
            self.request.close()
            
    return ThreadedTCPRequestHandler



class management():
    def __init__(self, process, host ='', port = 3006):
        
        self.myHost = host              # компьютер­сервер, '' означает локальный хост
        self.myPort = port              # использовать незарезервированный номер порта
        self.m_f = m_func(process)
    def server(self):    
        # создать сервер с поддержкой многопоточной модели выполнения, 
        # слушать/обслуживать клиентов непрерывно
        myaddr = (self.myHost, self.myPort)
        print("init management ", self.m_f)
        self.server = socketserver.ThreadingTCPServer(myaddr, MyClientHandler(self.m_f))
        self.server.serve_forever()

   
class m_func():
    def now(self):
        return time.ctime(time.time())
    def __init__(self, process):
        self.process = process
        self.conn = [] 
        self.currentConn = None

    def get_connect(self):
        self.conn = []
        def match_conn(conn, j):
            for i in self.conn:
                if i == j: 
                    return False
            return True
        for i in self.process: # dict of port listeners
            for j, k in self.process[i].F.items(): #dict of forwarders in port
                if match_conn(self.conn, k): self.conn.append(k)