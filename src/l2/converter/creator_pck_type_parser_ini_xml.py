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

from lxml import etree
import io
#import numpy


class parser_struct_l2ph():
 def __init__(self):
   self.pck_skip = 0
 def parser_struct_l2ph(self,str_):
  c_to_np={'b':'i1','c':'i1','h':'i2', 'z':'i4', 'd':'i4','f':'f8','q':'i8','s':'S','i':'i4','l':'i4','o':'i4', '-':'S-', 'B':'u1', 'H':'u2', 'I':'u4', 'Q':'u8', 'L':'u4'}
  bad_simvol__ = lambda line : 'U' if line == ':' else line
  bad_simvol_ = lambda line : line if line.find('Loop')>0 or line.find('For')>0 else line.replace('.','')
  bad_simvol = lambda line : (bad_simvol__(bad_simvol_(line))).replace('?', 'U').replace('+','').replace('-','').replace('/','').replace('*','').replace('-','').replace(' ','').replace(' ','').replace('$','').replace('=','').replace(',','').replace('&','').replace(';','').replace('(','')
  while(str_.find(')')>0):
   if str_[0] in ('z', 'b','c','h','d','f','q','s','i','l','o','-','B', 'H', 'I', 'Q', 'L'):     
    str_, y = str_[str_.find(')')+1:], (bad_simvol(str_[str_.find('(')+1:str_.find(')')]), c_to_np.get(str_[0])) if str_[0] != 's' else (bad_simvol(str_[str_.find('(')+1:str_.find(')')]), c_to_np.get(str_[0]) )
    yield y
   else: raise
 def construct(self,s, way):
  if s.find(':') > 0: (pck_type, pck_name, pck_reader) = (s[:s.find('=')], way+'_'+s[s.find('=')+1:s.find(':')], list(self.parser_struct_l2ph(s[s.find(':')+1:])))
  else: pck_type, pck_name, pck_reader = s[:s.find('=')], way+'_'+s[s.find('=')+1:-1], []
  self.root = etree.Element("pck_struct", pck_type = pck_type, pck_name = pck_name)
  skip, now_nested, future_nested= 0,0,0
  etr={}
  loop = {}
  loop[now_nested] = 0
  etr[now_nested] = self.root
  if pck_reader:
    for y in pck_reader:
      if skip > 0 :
        skip -= 1
      a = True
      while a == True:
       a = False
       if loop[now_nested] > 0 and skip > 0:
        loop[now_nested] -= 1
       if loop[future_nested] > 0 and skip == 0:
        now_nested = future_nested
        etr[now_nested] = etree_child
        loop[now_nested] -= 1
        if loop[now_nested] == 0:
          now_nested -= 1
          future_nested = now_nested
          a = True
      if y[0].find(":") > 0:
         if y[0].find(":Loop") > 0:
           child = y[1] + '.' + y[0][:y[0].find(":")]
           chunk = y[0][y[0].find('.')+1:]
           future_nested = 1+now_nested
           skip, loop[future_nested] = int(chunk[:chunk.find('.')]), int(chunk[chunk.find('.')+1:])+1
           etree_child = etree.SubElement(etr[now_nested], child+'Value', loop = str(loop[future_nested]-1), skip=str(skip-1))
         elif y[0].find(":For") > 0:
           child = y[1] + '.' + y[0][:y[0].find(":")]
           #print('child: ', child)
           #print('y[0]: ', y[0])
           chunk = y[0][y[0].find('.')+1:]
           #print('chunk: ',chunk)
           future_nested = 1+now_nested
           skip, loop[future_nested] = 1, int(chunk)+1
           etree_child = etree.SubElement(etr[now_nested], child+'Value', loop = str(loop[future_nested]-1), skip=str(skip-1))             
         else:
           child = y[1] + '.' + y[0][:y[0].find(":")]
           etree.SubElement(etr[now_nested], child)
      else:
        child = y[1] + '.' + y[0]
        etree.SubElement(etr[now_nested], child)


#zapis' preobrazovaniu' v fail
class print_to_file():
 def ini_to_XML():
   import sys
   std = sys.stdout
   way = ""
   with open(name_ini_file+'.xml', 'w') as sys.stdout:
     print('<?xml version="1.0" encoding="UTF-8"?>')
     print("<xml>")
   with open(name_ini_file+'.ini', 'r') as file_r:
     for line in file_r:
      with open(name_ini_file+'.xml', 'a') as sys.stdout:
        if line.replace(' ', '').replace('\t', '') == '\n':
          pass
        elif line.replace(' ', '').replace('\t', '')[:2] == '//':
          pass
        elif line.upper().find('[CLIENT]')>=0: 
          way = 'c'
          print("<!--[Client] -->")
        elif line.upper().find('[SERVER]')>=0: 
          way = 's'
          print("<!--[Server] -->")
        else:
          try: 
            #construct_pck_class.run(way, line)
            Obj = parser_struct_l2ph()
            Obj.construct(line, way)
            print(etree.tostring(Obj.root, pretty_print=True).decode('latin-1'))
          except:
            std1 = sys.stdout
            sys.stdout = std
            print("error: ", line)
            sys.stdout = std1
            print('<!-- ',line , ' -->')
   with open(name_ini_file+'.xml', 'a') as sys.stdout:
     print("</xml>")
   sys.stdout = std
   print('succesfull')
   

files = { 1:'PacketAion21',
          2:'PacketAion25',
          3:'packetAion27',
          4:'packetsc4',
          5:'packetsc5',
          6:'PacketsFreya',
          7:'PacketsGOD',
          8:'PacketsGracia',
          9:'packetsGraciaEpilogue',
         10:'PacketsGraciaFinal',
         11:'PacketsHighFive',
         12:'packetsInterlude'}
for i in files:
 if i in (4,5,12,):
     name_ini_file = files[i]
     print_to_file.ini_to_XML()