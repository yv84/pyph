#===============================================================================
# Vladimir Yudintsev 2012
#===============================================================================

#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import gs
import ls
import management
import _thread as thread
import numpy
from lxml import etree
import creator_pck_type_parser_xml_class
import os.path

def main(path = ''):
  print('program started')
  print(os.path.getmtime(os.path.join(path, 'rpgClubEmpire', 'class_la2_gracia_final.xml')) - os.path.getmtime(os.path.join(path, 'rpgClubEmpire', 'class_la2_gracia_final.py')))
  if os.path.getmtime(os.path.join(path, 'rpgClubEmpire', 'class_la2_gracia_final.xml')) > os.path.getmtime(os.path.join(path, 'rpgClubEmpire', 'class_la2_gracia_final.py')):
    creator_pck_type_parser_xml_class.run(path)
  lock = thread.allocate_lock()
  Dest = {}
  Rules = {}
  Server = {}
  M_dict = {}
  files = {}
  files['rpg-club_empire.xml'] = os.path.join(path, 'rpg-club_empire.xml')
  files['management.xml'] = os.path.join(path, 'management.xml')
  print(files)
  for f in files:
   with open(files[f], 'r') as xml_file:
    tree_ = etree.parse(xml_file)
    root_ = tree_.getroot()
    for child in root_:
      if type(child) == etree._Element:
        print(child)
        if child.tag == 'forward':
          for server in child:
            print(server.tag)
            for child in server:
              if child.tag == 'network':
                for child in child:
                  if child.tag == 'ip_local': Dest[child.tag] = '' if str(child.text) in 'None' else child.text
                  if child.tag == 'ip_remote': Dest[child.tag] = '' if str(child.text) in 'None' else child.text
                  if child.tag == 'port_local': Dest[child.tag] = int(child.text)
                  if child.tag == 'port_remote': Dest[child.tag] = int(child.text)
                  if child.tag == 'socks_in': Dest[child.tag] = True if child.text in 'True' else False 
                  if child.tag == 'socks_in': Dest[child.tag] = True if child.text in 'True' else False
              if child.tag == 'rules': 
                for child in child:
                  if child.tag == 'xor': Rules[child.tag] = '' if str(child.text) in 'None' else child.text
                  if child.tag == 'server': Rules[child.tag] = '' if str(child.text) in 'None' else child.text
                  if child.tag == 'chronicles': Rules[child.tag] = '' if str(child.text) in 'None' else child.text
            print(Dest, Rules)
            Server[child]= gs.Forwarder(Dest, Rules)
            thread.start_new_thread(Server[child].server, ())
        if child.tag == 'management':
          for child in child:
            for child in child:
              if child.tag == 'ip_local': M_dict[child.tag] = '' if str(child.text) in 'None' else child.text
              if child.tag == 'port_local': M_dict[child.tag] = int(child.text)
            M = management.management(Server, M_dict['ip_local'],M_dict['port_local'])
            thread.start_new_thread(M.server, ())
    print(Server)
  lock.acquire()
  lock.acquire()
  print('program ended')

class run():
  def __init__(self, path = ''):
    main(path)
    
if __name__ == "__main__":
    main()