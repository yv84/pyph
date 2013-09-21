#-------------------------------------------------------------------------------
# Name:        
# Purpose:
#
# Author:      
#
# Created:     26.12.2012
# Copyright:   
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import io
import os.path
import sys



class print_to_file():
    
    """zapis' preobrazovaniu' v fail """
    def XML_to_class(path=''):
        std = sys.stdout
        py_file = os.path.join(path, 'rpgClubEmpire', 'class_la2_gracia_final.py')
        xml_file = os.path.join(path, 'rpgClubEmpire', 'class_la2_gracia_final.xml')
        with open(py_file, 'w') as sys.stdout:
            print('import struct')
        sys.stdout = std
        with open(xml_file, 'r') as xml_file:
            with open(py_file, 'a') as sys.stdout:
                tree_ = etree.parse(xml_file)
                root_ = tree_.getroot()
                for child in root_:
                    if type(child) == etree._Element: 
                          Obj2 = construct_pck_class(child)
                          Obj2.parse_XML()
                          Obj2.print_pck_class_from_XML()
                          Obj2.packet_for_dtype_parse_from_XML_packet()
                          Obj2.packet_for_dtype_parse_from_XML_list()
        sys.stdout = std
        cl = ""
        with open(py_file, 'r') as file_r:
            for line in file_r:
                cl+= line
        #count_Unknown = 0
        #count_0 = 0
        #for line in s.split('\n'):
        # print(line.replace('U', 'B'))
        with open(py_file, 'a') as sys.stdout:
            print("class Pck_invoke_dict():")
            print(" def __init__(self):")
            print("   self.Pck_invoke_s = {}")
            print("   self.Pck_invoke_c = {}")
            print(" def get_Pck_invoke_c(self):")
            for chunk in cl.split('class '):
                  chunk = chunk[:chunk.find('(')]
                  if chunk[0] == 'c': print("   self.Pck_invoke_s[%s().invoke] = %s()" %  (chunk, chunk) )
            print("   return self.Pck_invoke_s")
            print(" def get_Pck_invoke_s(self):")
            for chunk in cl.split('class '):
                  chunk = chunk[:chunk.find('(')]
                  if chunk[0] == 's': print("   self.Pck_invoke_c[%s().invoke] = %s()" %  (chunk, chunk) )
            print("   return self.Pck_invoke_c")
        sys.stdout = std
        print('succesfull create %s from %s' %(py_file,xml_file))


class construct_pck_class():
       
    """sozdanie strukturi classov dlya zapisi v fail,
     na osnove xml faila 
    """
    def __init__(self, tree):
        self.tree_ = tree
    def parse_XML(self):
        """poluchenie dereva xml iz faila xml
        """
        #self.root = self.tree_.getroot()
        self.root = self.tree_
        self.pck_attr = self.root.attrib
        #print(self.root.tag, self.pck_attr["pck_name"], self.pck_attr["pck_type"])
        #print(len(self.root))
        """zdes' testovie zapisi ???
        """
        self.Dict= {}
        self.Dict["root"] = []
        for child in self.root:
            #print(child)
            self.Dict["root"].append( ((child.tag).split(".")[1], (child.tag).split(".")[0]) )
        #print("#############----------------##################")
        a = True
        L_parent = self.root
        while a:
            #print("ok")
            a= False
            L_child = []
            for child in L_parent:
                if len(child) > 0:
                    #print(len(child))
                    a = True
                    for child2 in child:
                        #print(child, child2, "+")
                        L_child.append(child2)
        L_parent = L_child
    
    def print_pck_class_from_XML(self):
          """poisk odinakovix elementov v root
          """
          count = 0
          match = False
          for i in self.root:
              x = i.tag[i.tag.find(".")+1:]
              match = False
              for j in self.root:
                  y = j.tag[i.tag.find(".")+1:]
                  if i!=j and x == y:
                      j.tag = j.tag + '_'+ str(count + 1)
                      count += 1
                      match = True
              count = 0
              if match == True:
                  i.tag = i.tag + '_' + str(count)
          #print(self.pck_attr)
          """sozdanie strukturi classa -zagolovok, __init__
          """
          print("#--------------------------------------------------------------------------#%s" % self.pck_attr["pck_type"])
          if self.pck_attr["pck_name"][-1:] != '\n': print("class %s():" % self.pck_attr["pck_name"])
          else: print("class %s():" % self.pck_attr["pck_name"][:-1])
          print("  def __init__(self):")
          if len(self.pck_attr["pck_type"]) == 2 :print("    self.lst, self.pck, self.invoke= [], b'', b'\\x%s'" %self.pck_attr["pck_type"])
          if len(self.pck_attr["pck_type"]) == 4 :print("    self.lst, self.pck, self.invoke= [], b'', b'\\x%s\\x%s\\x00'" %(self.pck_attr["pck_type"][:2],self.pck_attr["pck_type"][2:4]))
          """ def dtype()
          """
          print("  def dtype(self, act, data):")
          if len(self.root) > 0:
              for child in self.root:
                  if (child.tag)[:2] == 'S.' or child.tag.find('Value') > 0:
                      print('    if   act == 1:')
                      print("      self.It = self.parse_packet()")
                      print("      self.pck= data")
                      print('    elif act == 2:')
                      print("      self.It = self.parse_list()")
                      print("      self.lst= data")
                      break
          print("    dtype = [('pck_type', 'i1')")
          skip = 0
          zapyataya = ','
          for child in self.root:
              y = ((child.tag).split(".")[1], (child.tag).split(".")[0])
              if child.attrib.get('skip'): skip, name_skip = int(child.attrib.get('skip'))+1, y[0][:y[0].find('Value')]
              if   y[1] == 'S' : print("              %s ('%s', '|%s'+str(self.It.__next__()) )" % (zapyataya, y[0],y[1]))
              elif y[1] == 'S-': print("              %s ('%s', '|%s')" % (zapyataya, y[0],'S'+y[0]))
              else             : print("              %s ('%s', '%s')" % (zapyataya, y[0],y[1]))
              zapyataya = ','
              if skip > 0:
                  skip -= 1
                  if skip == 0:
                      print("                  ]+ list(self.f_%s()) +[" % name_skip)
                      zapyataya = ''
          print("                  ]")
          print("    return dtype")
        
          """ poisk odinakovix elementov nije root
          """
          #print("#############----------------##################")
          a = True
          L_parent = self.root
          while a:
               a= False
               L_child = []
               for child in L_parent:
                   count = 0
                   match = False
                   for i in child:
                       x = i.tag[i.tag.find(".")+1:]
                       match = False
                       for j in child:
                           y = j.tag[i.tag.find(".")+1:]
                           if i!=j and x == y:
                               j.tag = j.tag + '_'+ str(count + 1)
                               count += 1
                               match = True
                       count = 0
                       if match == True:
                           i.tag = i.tag + '_' + str(count)
                   """sozdanie podfunkcii dtype, ierarhiya vlojennix elementov
                   """
                   if len(child) > 0:
                        #print(len(child))
                        print('  def f_%s(self):' %child.tag[child.tag.find('.')+1:child.tag.find('Value')])
                        print('    for i in range(self.It.__next__()):')
                        print("      dtype = ('%s_' + str(i) , [" % child.tag[child.tag.find('.')+1:child.tag.find('Value')])
                        a = True
                        zapyataya = ''
                        for child2 in child:
                            y = ((child2.tag).split(".")[1], (child2.tag).split(".")[0])
                            if child2.attrib.get('skip'): skip, name_skip = int(child2.attrib.get('skip'))+1, y[0][:y[0].find('Value')]
                            if   y[1] == 'S' : print("              %s ('%s', '|%s'+str(self.It.__next__()) )" % (zapyataya, y[0],y[1]))
                            elif y[1] == 'S-': print("              %s ('%s', '|%s')" % (zapyataya, y[0],'S'+y[0]))
                            else             : print("              %s ('%s', '%s')" % (zapyataya, y[0],y[1]))
                            zapyataya = ','
                            L_child.append(child2)
                            if skip > 0:
                                skip -= 1
                                if skip == 0:
                                    print("                  ]+ list(self.f_%s()) +[" % name_skip)
                                    zapyataya = ''
                        print("                  ])")
                        print('      yield dtype ')
               L_parent = L_child
    
    
    def packet_for_dtype_parse_from_XML_packet(self):
        """preobrazovanie XML v python classi
        """
        const_packet_error = 100
        skip = 0
        self.nested = 0
        self.s = "   " #s*nested
        self.space = lambda n : ("   "*(n+1))
        self.It = 0   # iterator
        loop= {}
        loop[self.nested] = 0
        etr={}
        etr[self.nested] = self.root
        num_etr = {}
        num_etr[self.nested] = 0
        self.text = []
        self.flag_print ={}
        self.flag_print[self.nested] = False
        def queue_print():
            """ pechat' ocheredi
            """
            if self.text:
                for line in self.text:
                    print(line)
            self.text = []
        def struct_unpack_count(y):
            """ poluchenie kol-va loop iz dannix packeta
            """
            queue_print()
            if self.It != 0 : print("%si += %i" %(self.space(self.nested),self.It))
            print("%sp = self.pck[i:i+%s]" %(self.space(self.nested),y[1]))
            self.It = 0
            count = lambda s : print("%scount = struct.unpack('%s', p)[0]" %(self.space(self.nested), s) )
            err = lambda : print("%sif count > %i: raise PacketError" %(self.space(self.nested), const_packet_error) )
            if   y[1] == '1':   #i1
                count('b')
                err()
                i = 1
            elif y[1] == '2':   #i2
                count('h')
                err()
                i = 2
            elif y[1] == '4':   #i4
                count('i')
                err()
                i = 4
            elif y[1] == '8':   #i8
                count('q')
                err()
                i = 8
            #self.It += i
            return
     
        def len_element(y, name):
            """ poluchae dlinnu elementa dlya polucheniya mestopolojeniya v razbore packeta
            """
            if y == 'S':
                queue_print()
                self.flag_print[self.nested] = True
                if self.It != 0: print("%si += %i" % (self.space(self.nested),self.It))
                print("%ss_len = f_s_len(self.pck[i:])" %self.space(self.nested))
                print("%syield s_len" %self.space(self.nested))
                self.text.append("%si += s_len" %self.space(self.nested))
                i = 0
                self.It = 0
            elif y == 'S-':
                i = int(name)
            else:
                i = int(y[1:])
            self.It += i
            #print(self.It)
            return
          
        def parse():
            """ razbiraem packet na vixode yield dlya dtype 
            porveryaem est' li elementi loop i String
            """
            x = False
            if len(self.root) > 0:
                for child in self.root:
                    if (child.tag)[:2] == 'S.' or child.tag.find('Value') > 0:
                        print("  def parse_packet(self):")
                        self.text.append("   f_s_len = (lambda data: (data[::2].find(b'\\x00')+1)*2)")
                        x = True
                        break
            return x
       
        def yield_loop():
            """ sozdanie cikla for dlya vlojennix struktur
            """
            if skip == 0:
                if self.flag_print[self.nested] == True: queue_print()
                self.flag_print[self.nested] = False
                print("%syield count" %self.space(self.nested))
                if self.It != 0: self.text.append("%si += %i" %(self.space(self.nested),self.It))
                # stepen' vlojeniya(nested) otvechaet za kol-vo probelov
                self.text.append("%sfor _ in range(count):" %self.space(self.nested))
                self.nested += 1
                self.flag_print[self.nested] = False
                #for i in range(self.nested):
                      #self.flag_print[i] = True
                self.It = 0
                #print('self.nested = ', self.nested)
                #print("%si += %i" %(self.nested*self.s,self.It))
                #func(Idparent)
       
        """ glavniu' cikl
        """
        if parse():
            print("%si = 1" %self.space(self.nested))
            #for child in etr[self.nested]:
            while True:
                try:
                    #print(self.nested, num_etr[self.nested])
                    #print(self.nested)
                    child = etr[self.nested][num_etr[self.nested]]
                    #print(child)
                except (IndexError):
                    if self.nested == 0: break
                    else: pass
                num_etr[self.nested] += 1
                #print(child.tag)
                if child.attrib.get('skip'): skip = int(child.attrib.get('skip'))+1
                if child.attrib.get('loop'):
                    num_etr[self.nested+1] = 0
                    loop[self.nested+1] = int(child.attrib.get('loop'))+1
                if len(child) > 0: etr[self.nested+1] = child
                if len(child) > 0 and skip > 0:
                     #print("%si += %i" %(self.nested*self.s,self.It))
                     struct_unpack_count(child.tag[:child.tag.find('.')])
                len_element(child.tag[:child.tag.find('.')], child.tag[child.tag.find('.')+1:])
                if skip > 0:
                     skip -= 1
                     yield_loop()
                #print(self.nested)
                #print(child)
                #print(loop)
                if loop[self.nested] >= 0 and skip == 0:
                     loop[self.nested] -= 1
                     if loop[self.nested] == 0: 
                         if self.It != 0: self.text.append("%si += %i" % (self.space(self.nested),self.It))
                         self.It = 0
                         #print(self.flag_print, self.nested)
                         if self.flag_print[self.nested] == True: queue_print()
                         self.flag_print[self.nested] = False
                         self.nested -= 1
    
    def packet_for_dtype_parse_from_XML_list(self):
        """preobrazovanie XML v python classi
        """
        const_tuple_error = 100
        skip = 0
        self.nested = 0
        self.s = "   " #s*nested
        self.space = lambda n : ("   "*(n+1))
        self.It = 0   # iterator
        loop= {}
        loop[self.nested] = 0
        etr={}
        etr[self.nested] = self.root
        num_etr = {}
        num_etr[self.nested] = 0
        self.text = []
        self.flag_print ={}
        self.flag_print[self.nested] = False
        yield_straight_flag = True
        def queue_print():
            """ pechat' ocheredi
            """
            if self.text:
                for line in self.text:
                    print(line)
            self.text = []
        def struct_unpack_count(y):
            """ poluchenie kol-va loop iz dannix packeta
            """
            queue_print()
            if self.It != 0 : print("%si += %i" %(self.space(self.nested),self.It))
            self.It = 0
            print("%scount = self.lst[i]"%self.space(self.nested))
            print("%sif count > %i: raise PacketError" %(self.space(self.nested), const_tuple_error))
            return
    
        def len_element(y, name):
            """ poluchae dlinnu elementa dlya polucheniya mestopolojeniya v razbore packeta
            """
            if y == 'S':
                queue_print()
                self.flag_print[self.nested] = True
                if self.It != 0: print("%si += %i" % (self.space(self.nested),self.It))
                print("%ss_len = len(self.lst[i])" %self.space(self.nested))
                print("%syield s_len" %self.space(self.nested))
                i = 1
                self.It = 0
            else:
                i = 1
            self.It += i
            #print(self.It)
            return
          
        def parse():
            """ razbiraem packet na vixode yield dlya dtype 
            porveryaem est' li elementi loop i String
            """
            x = False
            if len(self.root) > 0:
                for child in self.root:
                    if (child.tag)[:2] == 'S.' or child.tag.find('Value') > 0:
                        print("  def parse_list(self):")
                        x = True
                        break
            return x
      
        def parse_loop():
            """ razbiraem packet na vixode yield dlya dtype 
            porveryaem est' li elementi loop - 
            """
            x = False
            if len(self.root) > 0:
                for child in self.root:
                    if child.tag.find('Value') > 0:
                        x = True
                        break
            return x
    
        def yield_straight():
            """esli vstrechaem tupple, razbiraem
            """
            self.text.append("%spointer_list_in = self.lst" %self.space(self.nested))
            self.text.append("%sself.lst = []" %self.space(self.nested))
            self.text.append("%sdef it(lst_in, lst_out):" %self.space(self.nested))
            self.text.append("%s  for i in lst_in:" %self.space(self.nested))
            self.text.append("%s    if isinstance(i ,tuple):" %self.space(self.nested))
            self.text.append("%s      it(i, lst_out)" %self.space(self.nested))
            self.text.append("%s    else: lst_out.append(i)" %self.space(self.nested))
            self.text.append("%sit(pointer_list_in, self.lst)" %self.space(self.nested))
            yield_straight_flag = False
    
        def yield_loop():
            """ sozdanie cikla for dlya vlojennix struktur
            """
            if skip == 0:
                if self.flag_print[self.nested] == True: queue_print()
                self.flag_print[self.nested] = False
                if yield_straight_flag:  yield_straight()
                print("%syield count" %self.space(self.nested))
                if self.It != 0: self.text.append("%si += %i" %(self.space(self.nested),self.It))
                # stepen' vlojeniya(nested) otvechaet za kol-vo probelov
                self.text.append("%sfor _ in range(count):" %self.space(self.nested))
                self.nested += 1
                self.flag_print[self.nested] = False
                #for i in range(self.nested):
                    #self.flag_print[i] = True
                self.It = 0
                #print('self.nested = ', self.nested)
                #print("%si += %i" %(self.nested*self.s,self.It))
                #func(Idparent)
       
        """ glavniu' cikl
        """
        if parse():
            print("%si = 1" %self.space(self.nested))
            #for child in etr[self.nested]:
            while True:
                try:
                    #print(self.nested, num_etr[self.nested])
                    #print(self.nested)
                    child = etr[self.nested][num_etr[self.nested]]
                    #print(child)
                except (IndexError):
                    if self.nested == 0: break
                    else: pass
                num_etr[self.nested] += 1
                #print(child.tag)
                if child.attrib.get('skip'): skip = int(child.attrib.get('skip'))+1
                if child.attrib.get('loop'):
                    num_etr[self.nested+1] = 0
                    loop[self.nested+1] = int(child.attrib.get('loop'))+1
                if len(child) > 0: etr[self.nested+1] = child
                if len(child) > 0 and skip > 0:
                    #print("%si += %i" %(self.nested*self.s,self.It))
                    struct_unpack_count(child.tag[:child.tag.find('.')])
                len_element(child.tag[:child.tag.find('.')], child.tag[child.tag.find('.')+1:])
                if skip > 0:
                    skip -= 1
                    yield_loop()
                #print(self.nested)
                #print(child)
                #print(loop)
                if loop[self.nested] >= 0 and skip == 0:
                    loop[self.nested] -= 1
                    if loop[self.nested] == 0: 
                        if self.It != 0: self.text.append("%si += %i" % (self.space(self.nested),self.It))
                        self.It = 0
                        #print(self.flag_print, self.nested)
                        if self.flag_print[self.nested] == True: queue_print()
                        self.flag_print[self.nested] = False
                        self.nested -= 1
    

class run():
    def __init__(self, path=''):
        print_to_file.XML_to_class(path)
    
if __name__ == "__main__":
    run()
