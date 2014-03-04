#===============================================================================
# Vladimir Yudintsev 2012
#===============================================================================
#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import struct

from imp import reload
import binascii
import gs_f_pck_factory
import cProfile


class packet():
    
    def __init__(self, parent, Rules):
        self.data_rec = b''
        self.data_send  = b''
        self.key_in = b''
        self.key_out = b''
        self.pck = b''
        self.pck_decode = b''
        self.pck_code = b''
        self.pck_inject = []
        self.parent=parent
        self.event = ''
        self.Pck_invoke = parent.Pck_invoke
        self.pck_f = gs_f_pck_factory.f_pck_factory(Rules,0)(self.parent)
       #print(dir(self.pck))
       
    def load(self):
        self.pck_f = gs_f_pck_factory.f_pck_factory(Rules,1)(self.parent)
        #print('reload rules')
        
    # xD
    def t_pck(self, b_str):
        return ' '.join(["%02X" %  x for x in b_str])
    
    def rec_pck_direct_send(self):
    #===========================================================================
    #  propuskaem trafik bez videleniya
    #===========================================================================
        #print('direct_send_s = ', self.t_pck(self.data_rec))
        self.data_send +=self.data_rec
        self.data_rec = b''
        
    def rec_pck_set_new_key(self):
    #============================================================================
    # inicializaciya key (4 - in(c/s) / out(c/s) )
    #============================================================================
        if (self.key_in == b'') and (len(self.data_rec) > 2):           
            #print('set_key')
            self.key_in = self.pck_f.set_new_key(self.data_rec, self.key_in)     #togda videlyaem key bez decodirovaniya
            self.parent.F['C'].key_in  = self.key_in
            self.key_out               = self.key_in
            self.parent.F['C'].key_out = self.key_in
            #print('self.key_in = ', self.key_in)
            
    #==============================================================================
    # inject: pck(bez razmera), key_out, flag(0/1)(ustanavlivaet pravilo, obrabotki do ili pered modifikacieu' packeta)
    #==============================================================================
    def inject_tpl(self, *inject_t):
        """ inject data from tuple
        """
        if inject_t:
            for pk in inject_t:
                self.pck_inject.append(self.pck_f.pack(pk, self.Pck_invoke, self.side))
                
    def inject_pck(self, *inject_p):
        """ inject data from packet
        """
        if inject_p:
            for pk in inject_p:
                self.pck_inject.append(pk)
                
    def rec_pck_get_decode_packet(self):
        """videlyaem zagolovok dlinni packeta, deshifruem po XOR
        """
        while (len(self.data_rec) > 2) and (len(self.data_rec) >= (struct.unpack('<H',self.data_rec[:2])[0])): #esli razmer packeta dostatochen dlya dekodirovaniya
            #print('''struct.unpack('<H',self.data_rec[:2])[0]) = ''',struct.unpack('<H',self.data_rec[:2])[0])
            self.pck = self.data_rec[:(struct.unpack('<H',self.data_rec[:2])[0])]                          #videlyaem packet s kotorim budem rabotat'
            self.data_rec = self.data_rec[(struct.unpack('<H',self.data_rec[:2])[0]):]                     #srezaem prishedshie dannie na razmer packeta
            self.pck = self.pck[2:]                                                                        #srezaem po shapke s razmerom packeta
            #==========================================================================
            # decodiruem packet
            #==========================================================================
            self.pck_decode = self.pck_f.Decode(self.pck, self.key_in)           #decodiruem packet
            self.key_in = self.pck_f.set_key(self.pck, self.key_in)           #poluchasem noviu' key_in
            yield self.pck_decode
            
    def rec_pck_alteration_decode_packet(self):
        """ get data from packet and/or change it
        """
        for pk in self.rec_pck_get_decode_packet():
            self.pck_decode = pk
            if self.pck_decode: yield self.pck_decode
            
    def rec_pck_code(self, pck_decode):
        """shifruem po XOR, dobavlyaem zagolovok packeta
        """
        #==========================================================================
        # codiruem packet
        #==========================================================================
        self.pck = self.pck_f.Code(pck_decode, self.key_out)             #codiruem packet
        #print('Code.pck = ', self.pck)
        self.key_out = self.pck_f.set_key(self.pck, self.key_out)
        #print('self.key_out = ', self.key_out)                        #poluchasem noviu' key_out
        self.pck = struct.pack('<H',len(self.pck)+2) + self.pck        # dobavlyaem razmer packeta v packet
        self.data_send += self.pck
        #print('''self.pck = ''',self.pck)
        
    def rec_pck_recode_packet(self):
        """ razbiraem i sobiraem packet
        """
        for self.pck_decode in self.rec_pck_alteration_decode_packet():
            if self.pck_decode: self.rec_pck_code(self.pck_decode)
    def inject_pck_code_packet(self):
        """ get queue from data to inject and set head len(pck)
        """
        while self.pck_inject: self.rec_pck_code(self.pck_inject.pop())


#===============================================================================
# server(in) -> client(out)
#===============================================================================
class packet_s(packet):
    
    def __init__(self, parent, Rules):
        self.side = 'S'
        packet.__init__(self, parent, Rules)
        self.Pck_invoke[self.side] = self.pck_f.init_Pck_invoke_dict_s()
        print(self.Pck_invoke[self.side])
        
    def rec_pck_alteration_decode_packet(self):
        for pk in self.rec_pck_get_decode_packet():
            self.pck_decode = pk
            #==========================================================================
            # server - preobrazuem
            #==========================================================================
            #print('1',self.pck_decode)
            #self.pck_decode = self.pck_f.ChangePck_in(self.pck_decode) # otkucheno - net primeneniya
            #print('2',self.pck_decode)
            try:
                #cProfile.run('self.pck_f.act_s(self.pck_decode, self.Pck_invoke)')
                self.pck_f.act_s(self.pck_decode, self.Pck_invoke)
            except:
                print("err unpack: ", self.side, "-", binascii.b2a_hex(self.pck_decode))#[:4])
            ###print('S- ', self.pck_decode)
            #self.pck_decode = self.pck_f.ChangePck_out(self.pck_decode) # otkucheno - net primeneniya
            #print('Modified.server = ', self.t_pck(self.pck_decode))
            if self.pck_decode: yield self.pck_decode
        #  self.pck_decode = pk
        #  if self.pck_decode: yield self.pck_decode
        
    def rec_pck(self):
        #print('decode ',len(self.data_rec))
        if (len(self.data_rec) > 2) and (len(self.key_in) != 0):                     #esli packet imeet razmer
            self.rec_pck_recode_packet()
            self.inject_pck_code_packet()
        if (len(self.key_in) != 0):
            self.inject_pck_code_packet()
        if (len(self.key_in) == 0):
            self.rec_pck_set_new_key()
            self.rec_pck_direct_send()
        return
     
    #===============================================================================
    # client(in) -> server(out) 
    #===============================================================================
class packet_c(packet):
    def __init__(self, parent, Rules):
        self.side = 'C'
        packet.__init__(self, parent, Rules)
        self.Pck_invoke[self.side] = self.pck_f.init_Pck_invoke_dict_c()
        print(self.Pck_invoke[self.side])
        
    def rec_pck_alteration_decode_packet(self):
        for pk in self.rec_pck_get_decode_packet():
            self.pck_decode = pk
            #==========================================================================
            # client - preobrazuem
            #==========================================================================
            #print('1',self.pck_decode)
            #self.pck_decode = self.pck_f.ChangePck_in(self.pck_decode) # otkucheno - net primeneniya
            #print('2',self.pck_decode)
            #print('self.ChangePck_in: ', self.pck_decode)
            try:
                self.pck_f.act_c(self.pck_decode, self.Pck_invoke)
            except:
                print("err unpack: ", self.side, "-", binascii.b2a_hex(self.pck_decode))#[:4])
            ###print('C- ', self.pck_decode)
            #print('self.pck_f.act_c: ', self.pck_f.act_c)
            #self.pck_decode = self.pck_f.ChangePck_out(self.pck_decode) # otkucheno - net primeneniya
            #print('Modified.client = ', self.pck_decode)
            #print('Modified.client = ', self.t_pck(self.pck_decode))
            if self.pck_decode: yield self.pck_decode
            
    def rec_pck(self):
        #print('pck_client_get: ',self.data_rec)
        if (len(self.data_rec) > 2) and (len(self.key_in) != 0):                     #esli packet imeet razmer
            self.rec_pck_recode_packet()
            self.inject_pck_code_packet()
        if (len(self.key_in) != 0):
            self.inject_pck_code_packet()
        if (len(self.key_in) == 0):
            self.rec_pck_direct_send()
        return
  
class comm():
    
    def __init__(self, parent):
        self.parent=parent
        
    def load(self):
        self.parent.F['C'].pck_f = gs_f_pck_factory.f_pck_factory(Rules,1)(self)
        self.parent.F['S'].pck_f = gs_f_pck_factory.f_pck_factory(Rules,1)(self)
        #print('reload rules')
        
    def inject_server(self, pck):
        self.parent.F['C'].inject_pck(pck)
        
    def inject_client(self, pck):
        self.parent.F['S'].inject_pck(pck)

