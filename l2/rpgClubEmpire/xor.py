#! /usr/local/bin/python3
# -*- coding: utf-8 -*-



import struct
class xor():
 #poluchenie klyucha pri inicializacii
 def set_new_key(self, pck, key):
  if key == b'' and pck[2] == 46:                                           #prishel packet inicializacii key
   key = pck[4:12] + b'\xC8\x27\x93\x01\xA1\x6C\x31\x97'                       #key v packete + const
  return key
 #vichislenie novogo klyuchas po staromu key i len(packet)
 def set_key(self, pck, key):
  key=struct.pack('<q',(struct.unpack('<q',key[:8])[0])) + struct.pack('<q',(struct.unpack('<q',key[8:])[0] + len(pck)))
  return key
 def Decode(self, pck, key):
  pck_new_list = []
  for i in range(len(pck)):
   pck_new_list.append(0)  #- list
  k=len(pck)
  k = k - 1
  keyLen = len(key)
  while k > 0 :
   pck_new_list[k] = pck[k] ^ key[(lambda : k if k < keyLen else (k % (keyLen)))()] ^ pck[k-1]
   k = k -1
  if len(pck) > 0 : pck_new_list[0] = pck[0] ^ key[0]
  #list  - > byte massiv
  pck_decode = struct.pack('B' * len(pck_new_list), *pck_new_list)           # - dekodirovaniu' packet
  return pck_decode
 def Code(self, pck_decode, key):
  pck_new_list = []
  for i in range(len(pck_decode)):
   pck_new_list.append(0)  #- list
  keyLen = len(key)
  if len(pck_decode) > 0 : pck_new_list[0] = pck_decode[0] ^ key[0]
  k = 1
  while k < (len(pck_decode) ) :
   pck_new_list[k] = pck_decode[k] ^ key[(lambda : k if k < keyLen else (k % (keyLen)))()] ^ pck_new_list[k-1]
   k = k + 1
  pck_code = struct.pack('B' * len(pck_new_list), *pck_new_list)           # - kodirovaniu' packet
  return pck_code