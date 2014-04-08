#===============================================================================
# Vladimir Yudintsev 2012
#===============================================================================

#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import socket
import _thread as thread
import gs_packet
import time

class Pck():
 def __init__(self, Rules):
   self.F = {}
   self.l2_d = {} # slovar' dannix
   self.Pck_invoke_s = {}
   self.Pck_invoke_c = {}
   self.Pck_invoke = {'S': self.Pck_invoke_s, 'C': self.Pck_invoke_c} # slovar' classov strukturi packetov
   Rules['dest'] = 'C'
   self.F['C'] = gs_packet.packet_c(self,Rules) #создаем объект обработчика клиентских пакетов
   Rules['dest'] = 'S'
   self.F['S'] = gs_packet.packet_s(self,Rules) #создаем объект обработчика серверных пакетов
   # помещаем ссылки на объекты в словарь

class Forwarder():
 def __init__(self, Dest, Rules):
  self.Dest = {'ip_local':'','ip_remote':'','port_local':0,'port_remote':0,'socks5':False}
  if isinstance(Dest.get('ip_local'), str): self.Dest['ip_local'] = Dest.get('ip_local')     # на нем сидит наш слушатель форвардер
  if isinstance(Dest.get('ip_remote'), str): self.Dest['ip_remote'] = Dest.get('ip_remote')  # форвардер принимает любые соединения и отправляет на ip_remote
  if isinstance(Dest.get('port_local'), int): self.Dest['port_local'] = Dest.get('port_local') # на нем сидит наш слушатель форвардер
  if isinstance(Dest.get('port_remote'), int): self.Dest['port_remote'] = Dest.get('port_remote') # форвардер принимает любые соединения и отправляет на port_remote
  if isinstance(Dest.get('socks5'), bool): self.Dest['socks5'] = Dest.get('socks5') 
  self.Rules = {'xor':'native','server':'native','chronicles':'native'} # значения по умолчанию
  if isinstance(Rules.get('xor'), str): self.Rules['xor'] = Rules.get('xor')  # шифрование
  if isinstance(Rules.get('server'), str): self.Rules['server'] = Rules.get('server')  # сервер
  if isinstance(Rules.get('chronicles'), str): self.Rules['chronicles'] = Rules.get('chronicles') # True если нужно socks5 соединение
  self.Dest['dest'] = ''
  self.mutex = thread.allocate_lock() 
  self.F = {}                                     # помещаем ссылки на объекты в словарь
  self.C = {}                             # словарь коннектов
 def server(self):
  try:
   dock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   dock_socket.bind((self.Dest['ip_local'], self.Dest['port_local']))    # слушатель ip_local/port_local
   dock_socket.listen(1)
   while True:
    print('start')
    self.client_socket = dock_socket.accept()[0]
    self.mutex.acquire()
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
    self.server_socket.connect((self.Dest['ip_remote'], self.Dest['port_remote']))      # коннект к удаленному хосту ip_remote/port_remote
    self.C[self.server_socket] = self.client_socket
    self.C[self.client_socket] = self.server_socket          # запоминаю адреса сокетов
    print('self.C = ', self.C)
    self.F[self.C[self.client_socket]] = self.F[self.client_socket] = self.packet = Pck(self.Rules)
    print('self.F = ', self.F)
    self.forward_thr()
    self.mutex.release()
  finally:
    print('finally', self.C)
    print('finally', self.F)
    time.sleep(4)
    thread.start_new_thread(self.server, ())
    #ne ochischayutsya C i F pri except
    #if self.F.get(source): self.F.pop(source)
    #self.C.pop(source): self.C.pop(source)
 def forward_thr(self):
  if self.Dest['socks5']:
   thread.start_new_thread(self.socks5, (self.client_socket))
  else:
   thread.start_new_thread(self.get_packet,  (self.client_socket, 'C'))
   thread.start_new_thread(self.send_packet, (self.C[self.client_socket], 'C'))
   thread.start_new_thread(self.get_packet,  (self.C[self.client_socket], 'S'))
   thread.start_new_thread(self.send_packet, (self.client_socket, 'S'))
 def send_packet(self, destination, d):  
  string = b''                                    
  while self.C.get(destination):            # для входа в цикл while
    time.sleep(0.05)
    # Обработчик
    #self.F[d].check_inject()                # проверяем есть ли пакеты на отправку через инжект
    try:
     if self.F[destination].F[d].data_rec:                  # проверяем есть ли пакеты на отправку через форвардинг
       with self.mutex: self.F[destination].F[d].rec_pck()                    # обработка пакета
       string = self.F[destination].F[d].data_send           # подготовка к посылке
       self.F[destination].F[d].data_send = b''
     # Посылка
     if string:                              # если буфер посылки не пуст, посылаем
       #print(d,': dest - ', destination)
       #print('%s: %s'% (d,string))
       with self.mutex: destination.sendall(string)
       string = b''
    except: print(d,': socket zakrit i dannie ne mogut bit dostavleni')
 def get_packet(self, source, d):                                 
  def close_connect():
    with self.mutex: 
      print(d,': shutdown C:- ', self.C)
      try:
       if source:
        source.shutdown(socket.SHUT_RD)
      except: print(source,' shutdown_RD false')
      try:
       if self.C.get(source):
        self.C.get(source).shutdown(socket.SHUT_WR)
      except: print(self.C.get(source),' shutdown_WR false')
      try:      
       self.F.pop(source)
       print(d,': shutdown F:- ', self.F) 
      except: print(source,' self.F.pop(source) not found')
      try:
       print(d, ': ', self.C.pop(self.C.get(source)), ' / ', self.C.pop(source))
       self.C.pop(source)   #self.C.pop(self.C.get(source)) and 
      except: pass
  while True:                                 # для входа в цикл while
   # Получение
   #print(d,': srs - ', source)
   try:
     string = source.recv(4096)                 # приходит пакет
     if string:                                 # если содержит данные, добавляем во входящий буфер
       with self.mutex: self.F[source].F[d].data_rec += string
       string = b''
     else: 
       close_connect()                      # пустой пакет, закрываем соединение
       break
   except: 
     close_connect()
     break
  
 # не готово, черновик
 def socks5(self, source):
  SOCKS5_Authentication_to_the_PS = False       # False соединение не установлено
  SOCKS5_Authentication_through_PS = False
  while not(SOCKS5_Authentication_to_the_PS):
   print('ожидание запроса на авторизацию по socks5')
   string = source.recv(1024)                 # приходит пакет
   if (SOCKS5_Authentication_to_the_PS == False) and (string == b'\x05\x01\x00'): # от клиента запрос на аутентификацию по сокс5
    SOCKS5_Authentication_to_the_PS = True  
    source.sendall(b'\x05\x00')# посылаем в сторону клиента  b'\x05\x00'
    print('self.SOCKS5_Authentication_to_the_PS')
  while not(SOCKS5_Authentication_through_PS):
   string = source.recv(1024)                 # приходит пакет
   if (SOCKS5_Authentication_through_PS == False) and (string == b'\x05\x01\x00\x01\xd5;,2\x1ea'): # от клиента запрос на аутентификацию по сокс5
    SOCKS5_Authentication_through_PS = True  
    source.sendall(b'\x05\x00\x00\x01\x7f\x00\x00\x01\x00\x00')# посылаем в сторону клиента  b'\x05\x00\x00\x01\x7f\x00\x00\x01\x00\x00'
    print('self.SOCKS5_Authentication_through_PS')
  thread.start_new_thread(self.get_packet,  (self.server_socket, 'S'))
  thread.start_new_thread(self.send_packet, (self.client_socket, 'S'))
  thread.start_new_thread(self.send_packet, (self.server_socket, 'C'))
  self.get_packet(self.client_socket, 'C') #после установки socks5 соединения - коннект
  
 # SOCKS5 нужен в сторону сервера also
  
