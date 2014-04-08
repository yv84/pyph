#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

#import pck_conversion.pck_reader as pck_reader
#import pck_conversion.pck_reader as pck_writer

class mod_pck_c():
 def pck_conv():
  pass
 def ChangePck_in(self, pck_decode):
  # select target
  # shifrovaniu' action 01 ( 01=AttackRequest:d(ObjectID)d(OrigX)d(OrigY)d(OrigZ)c(AttackID) )
 # if (len(pck_decode) == 18 ) and (pck_decode[:1] == b'\x1f'):    
 #  print('1F->01')
 #  pck_decode =  b'\x01' + pck_decode[1:]
 #  print('ChangePck_mod_pck_c = %s' % (pck_decode))
  return pck_decode

 def ChangePck_out(self, pck_decode):
 # select target
 # shifrovaniu' action 01 ( 01=AttackRequest:d(objectID)d(OrigX)d(OrigY)d(OrigZ)c(AttackID) )
 # if (len(pck_decode) == 18 ) and (pck_decode[:1] == b'\x1f'):    
 #  print('1F->01')
 #  pck_decode =  b'\x01' + pck_decode[1:]
 #  print('ChangePck_mod_pck_c = %s' % (pck_decode))
  return pck_decode