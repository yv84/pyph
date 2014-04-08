import struct
#--------------------------------------------------------------------------#0081
class c_CM_TIME_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x81\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('nanoTime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0083
class c_CM_LEGION_EMBLEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x83\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('legionId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0086
class c_CM_GATHER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x86\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('action', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0089
class c_CM_PETITION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x89\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('action', 'i2')
              , ('', 'i4')
              , ('data', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 9
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 4
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#008A
class c_CM_OPEN_STATICDOOR():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x8A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('doorId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#008E
class c_CM_CHAT_MESSAGE_PUBLIC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x8E\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('type', 'i1')
              , ('message', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#008F
class c_CM_CHAT_MESSAGE_WHISPER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x8F\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('message', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0091
class c_CM_SKILL_DEACTIVATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x91\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('skillId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0092
class c_CM_TARGET_SELECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x92\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetOID', 'i4')
              , ('type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0093
class c_CM_ATTACK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x93\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetOID', 'i4')
              , ('attackno', 'i1')
              , ('time', 'i2')
              , ('type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0095
class c_CM_EQUIP_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x95\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('action', 'i1')
              , ('slotRead', 'i4')
              , ('itemUniqueId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0096
class c_CM_REMOVE_ALTERED_STATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x96\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('skillid', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#009B
class c_CM_PLAYER_LISTENER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x9B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#009F
class c_CM_PING():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x9F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#00A1
class c_CM_QUESTION_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xA1\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('questionid', 'i4')
              , ('response', 'i1')
              , ('_0', 'i1')
              , ('_1', 'i2')
              , ('senderid', 'i4')
              , ('_2', 'i4')
              , ('_3', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#00A2
class c_CM_LEGION_EMBLEM_SEND():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xA2\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('legionId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#00A4
class c_CM_CLOSE_DIALOG():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xA4\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#00A5
class c_CM_DIALOG_SELECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xA5\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetOID', 'i4')
              , ('dialogId', 'i2')
              , ('selectableReward', 'i2')
              , ('lastPage', 'i2')
              , ('questId', 'i4')
              , ('unk', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#00A6
class c_CM_BUY_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xA6\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('sellerOID', 'i4')
              , ('unk1', 'i2')
              , ('amountValue', 'i2')
                  ]+ list(self.f_amount()) +[
                  ]
    return dtype
  def f_amount(self):
    for i in range(self.It.__next__()):
      dtype = ('amount_' + str(i) , [
               ('tmpInt1', 'i4')
              , ('count', 'i4')
              , ('unk2', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 9
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 4
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#00A7
class c_CM_SHOW_DIALOG():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xA7\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#00A9
class c_CM_SET_NOTE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xA9\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('note', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#00AA
class c_CM_LEGION_TABS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xAA\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('page', 'i4')
              , ('tab', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#00AC
class c_CM_CHAT_RECRUIT_GROUP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xAC\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#00AE
class c_CM_LEGION_MODIFY_EMBLEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xAE\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('legionId', 'i4')
              , ('emblemVer', 'i2')
              , ('', 'i1')
              , ('red', 'i1')
              , ('green', 'i1')
              , ('blue', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#00B1
class c_CM_EXCHANGE_ADD_KINAH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xB1\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('itemCount', 'i4')
              , ('unk', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#00B2
class c_CM_EXCHANGE_REQUEST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xB2\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#00B3
class c_CM_EXCHANGE_ADD_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xB3\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('itemObjId', 'i4')
              , ('itemCount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#00F3
class c_CM_VERSION_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xF3\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('unk1', 'i4')
              , ('unk2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#00F4
class c_CM_REVIVE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xF4\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('reviveId', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#00F6
class c_CM_QUIT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xF6\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('logout', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#00F7
class c_CM_MAY_QUIT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xF7\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#00F8
class c_CM_LEVEL_READY():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xF8\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#00F9
class c_CM_UI_SETTINGS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xF9\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('tingsType', 'i1')
              , ('', 'i2')
              , ('size', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#00FB
class c_CM_ENTER_WORLD():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xFB\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('objectId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#00FE
class c_CM_OBJECT_SEARCH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xFE\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('npcId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#00FF
class c_CM_CUSTOM_SETTINGS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xFF\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('display', 'i2')
              , ('deny', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0100
class c_CM_QUESTIONNAIRE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x00\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('objectId', 'i4')
              , ('_0', 'i2')
              , ('_1', 'i2')
              , ('_2', 'i2')
              , ('_3', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0104
class c_CM_L2AUTH_LOGIN_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x04\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playOk2', 'i4')
              , ('playOk1', 'i4')
              , ('accountId', 'i4')
              , ('loginOk', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0105
class c_CM_CHARACTER_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x05\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playOk2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0107
class c_CM_TELEPORT_SELECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x07\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
              , ('locId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0108
class c_CM_RESTORE_CHARACTER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x08\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playOk2', 'i4')
              , ('chaOid', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0109
class c_CM_START_LOOT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x09\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
              , ('action', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#010B
class c_CM_DELETE_CHARACTER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x0B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playOk2', 'i4')
              , ('chaOid', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#010C
class c_CM_SPLIT_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x0C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('sourceItemObjId', 'i4')
              , ('itemAmount', 'i4')
              , ('4', 'i4')
              , ('sourceStorageType', 'i1')
              , ('destinationItemObjId', 'i4')
              , ('destinationStorageType', 'i1')
              , ('slotNum', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#010E
class c_CM_LOOT_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x0E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
              , ('index', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#010F
class c_CM_MOVE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x0F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObID', 'i4')
              , ('source', 'i1')
              , ('destination', 'i1')
              , ('slot', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0110
class c_CM_LEGION_UPLOAD_EMBLEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x10\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('size', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0111
class c_CM_MAIL_SUMMON_ZEPHYR():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x11\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('value', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0112
class c_CM_PLAYER_SEARCH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x12\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('50', 'i4')
              , ('region', 'i4')
              , ('classMask', 'i4')
              , ('minLevel', 'i1')
              , ('maxLevel', 'i1')
              , ('lfgOnly', 'i1')
              , ('', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0113
class c_CM_LEGION_UPLOAD_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x13\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('totalSize', 'i4')
              , ('', 'i1')
              , ('color_r', 'i1')
              , ('color_g', 'i1')
              , ('color_b', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0115
class c_CM_BLOCK_ADD():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x15\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetName', '|S'+str(self.It.__next__()) )
              , ('reason', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0118
class c_CM_DISCONNECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x18\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0119
class c_CM_FRIEND_STATUS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x19\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('status', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#011A
class c_CM_BLOCK_DEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x1A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#011B
class c_CM_SHOW_BLOCKLIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x1B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#011C
class c_CM_REPLACE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x1C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('sourceStorageType', 'i1')
              , ('sourceItemObjId', 'i4')
              , ('replaceStorageType', 'i1')
              , ('replaceItemObjId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#011D
class c_CM_MAC_ADDRESS2():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x1D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
              , ('Macaddress_0', 'i1')
              , ('Macaddress_1', 'i1')
              , ('Macaddress_2', 'i1')
              , ('Macaddress_3', 'i1')
              , ('Macaddress_4', 'i1')
              , ('Macaddress_5', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0145
class c_CM_MAC_ADDRESS2():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x45\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
              , ('Macaddress_0', 'i1')
              , ('Macaddress_1', 'i1')
              , ('Macaddress_2', 'i1')
              , ('Macaddress_3', 'i1')
              , ('Macaddress_4', 'i1')
              , ('Macaddress_5', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#011F
class c_CM_CHANGE_CHANNEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x1F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('channel', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0120
class c_CM_CHECK_NICKNAME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x20\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('nick', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0122
class c_CM_MACRO_CREATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x22\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('macroPosition', 'i1')
              , ('macroXML', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0123
class c_CM_MACRO_DELETE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x23\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('macroPosition', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0124
class c_CM_SHOW_BRAND():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x24\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('unk1', 'i4')
              , ('brandId', 'i4')
              , ('targetObjectId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0126
class c_CM_BLOCK_SET_REASON():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x26\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetName', '|S'+str(self.It.__next__()) )
              , ('reason', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0128
class c_CM_DISTRIBUTION_SETTINGS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x28\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('unk1', 'i4')
              , ('rules', 'i4')
              , ('autoDist', 'i4')
              , ('common_item_above', 'i4')
              , ('superior_item_above', 'i4')
              , ('heroic_item_above', 'i4')
              , ('fabled_item_above', 'i4')
              , ('ethernal_item_above', 'i4')
              , ('over_ethernal', 'i4')
              , ('over_over_ethernal', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0129
class c_CM_MAY_LOGIN_INTO_GAME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x29\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#012A
class c_CM_RECONNECT_AUTH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x2A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#012B
class c_CM_GROUP_LOOT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x2B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('groupId', 'i4')
              , ('unk1', 'i4')
              , ('unk2', 'i4')
              , ('itemId', 'i4')
              , ('itemIndex', 'i1')
              , ('npcId', 'i4')
              , ('distributionId', 'i1')
              , ('roll', 'i4')
              , ('bid', 'i8')
                  ]
    return dtype
#--------------------------------------------------------------------------#012C
class c_CM_MAC_ADDRESS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x2C\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('22', 'i4')
              , ('macAddress', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 7
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0114
class c_CM_MAC_ADDRESS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x14\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('23', '|S23')
              , ('MAC', '|S'+str(self.It.__next__()) )
              , ('HWID', '|S'+str(self.It.__next__()) )
              , ('ip_0', 'i1')
              , ('ip_1', 'i1')
              , ('ip_2', 'i1')
              , ('ip_3', 'i1')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 26
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#012F
class c_CM_ABYSS_RANKING_PLAYERS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x2F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('raceId', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0130
class c_CM_IN_GAME_SHOP_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x30\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i1')
              , ('categoryId', 'i4')
              , ('listInCategory', 'i4')
              , ('senderName', '|S'+str(self.It.__next__()) )
              , ('senderMessage', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0132
class c_CM_REPORT_PLAYER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x32\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('1', 'i4')
              , ('player', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 7
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0133
class c_CM_INSTANCE_CD_REQUEST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x33\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('_0', 'i4')
              , ('_1', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0134
class c_CM_NAME_CHANGE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x34\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('action', 'i1')
              , ('_0', 'i1')
              , ('_1', 'i2')
              , ('itemId', 'i4')
              , ('newName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 11
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 6
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0137
class c_CM_SHOW_MAP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x37\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0139
class c_CM_SUMMON_EMOTION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x39\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('objId', 'i4')
              , ('emotionTypeId', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#013B
class c_CM_DREDGION_REQUEST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x3B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('type', 'i4')
              , ('state', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#013D
class c_CM_FUSION_WEAPONS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x3D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('', 'i4')
              , ('firstItemId', 'i4')
              , ('secondItemId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#013E
class c_CM_SUMMON_ATTACK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x3E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('summonObjId', 'i4')
              , ('targetObjId', 'i4')
              , ('unk1', 'i1')
              , ('unk2', 'i2')
              , ('unk3', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0140
class c_CM_PLAY_MOVIE_END():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x40\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('type', 'i1')
              , ('_0', 'i4')
              , ('_1', 'i4')
              , ('movieId', 'i2')
              , ('_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0143
class c_CM_DELETE_QUEST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x43\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('questId', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0149
class c_CM_ITEM_REMODEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x49\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('', 'i4')
              , ('keepItemId', 'i4')
              , ('extractItemId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#014E
class c_CM_GODSTONE_SOCKET():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x4E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('npcId', 'i4')
              , ('weaponId', 'i4')
              , ('stoneId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0150
class c_CM_INVITE_TO_GROUP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x50\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('inviteType', 'i1')
              , ('name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0152
class c_CM_ALLIANCE_GROUP_CHANGE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x52\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerObjectId', 'i4')
              , ('allianceGroupId', 'i4')
              , ('secondObjectId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0153
class c_CM_PLAYER_STATUS_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x53\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('status', 'i1')
              , ('playerObjId', 'i4')
              , ('allianceGroupId', 'i4')
              , ('secondObjectId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0157
class c_CM_VIEW_PLAYER_DETAILS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x57\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#015A
class c_CM_PING_REQUEST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x5A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#015D
class c_CM_SHOW_FRIENDLIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x5D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#015E
class c_CM_CLIENT_COMMAND_ROLL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x5E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('maxRoll', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#015F
class c_CM_GROUP_DISTRIBUTION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x5F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('amount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0161
class c_CM_DUEL_REQUEST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x61\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('objectId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0162
class c_CM_FRIEND_ADD():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x62\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0163
class c_CM_FRIEND_DEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x63\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0165
class c_CM_ABYSS_RANKING_LEGIONS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x65\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('raceId', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0167
class c_CM_DELETE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x67\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('objId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0168
class c_CM_SUMMON_COMMAND():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x68\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('mode', 'i1')
              , ('_0', 'i4')
              , ('_1', 'i4')
              , ('targetObjId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#016A
class c_CM_PRIVATE_STORE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x6A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('itemCountValue', 'i2')
                  ]+ list(self.f_itemCount()) +[
                  ]
    return dtype
  def f_itemCount(self):
    for i in range(self.It.__next__()):
      dtype = ('itemCount_' + str(i) , [
               ('_0', 'i4')
              , ('_1', 'i4')
              , ('_2', 'i2')
              , ('_3', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#016B
class c_CM_PRIVATE_STORE_NAME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x6B\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#016C
class c_CM_BROKER_REGISTERED():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x6C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('npcId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#016D
class c_CM_BUY_BROKER_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x6D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('brokerId', 'i4')
              , ('itemUniqueId', 'i4')
              , ('itemCount', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#016E
class c_CM_BROKER_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x6E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('brokerId', 'i4')
              , ('sortType', 'i1')
              , ('page', 'i2')
              , ('listMask', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#016F
class c_CM_BROKER_SEARCH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x6F\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('brokerId', 'i4')
              , ('sortType', 'i1')
              , ('page', 'i2')
              , ('mask', 'i2')
              , ('items_lengthValue', 'i2')
                  ]+ list(self.f_items_length()) +[
                  ]
    return dtype
  def f_items_length(self):
    for i in range(self.It.__next__()):
      dtype = ('items_length_' + str(i) , [
               ('itemsId', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 6
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#0170
class c_CM_BROKER_SETTLE_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x70\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('npcId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0171
class c_CM_BROKER_SETTLE_ACCOUNT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x71\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('npcId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0172
class c_CM_REGISTER_BROKER_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x72\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('brokerId', 'i4')
              , ('itemUniqueId', 'i4')
              , ('price', 'i8')
              , ('itemCount', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0173
class c_CM_BROKER_CANCEL_REGISTERED():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x73\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('npcId', 'i4')
              , ('brokerItemId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0174
class c_CM_OPEN_MAIL_WINDOW():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x74\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0175
class c_CM_READ_MAIL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x75\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('mailObjId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0177
class c_CM_SEND_MAIL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x77\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('recipientName', '|S'+str(self.It.__next__()) )
              , ('title', '|S'+str(self.It.__next__()) )
              , ('message', '|S'+str(self.It.__next__()) )
              , ('itemObjId', 'i4')
              , ('itemCount', 'i4')
              , ('_0', 'i4')
              , ('kinahCount', 'i4')
              , ('_1', 'i4')
              , ('express', 'i1')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0178
class c_CM_DELETE_MAIL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x78\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('mailObjId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#017B
class c_CM_GET_MAIL_ATTACHMENT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x7B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('mailObjId', 'i4')
              , ('attachmentType', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#017C
class c_CM_CRAFT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x7C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i1')
              , ('targetTemplateId', 'i4')
              , ('recipeId', 'i4')
              , ('targetOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#017D
class c_CM_CLIENT_COMMAND_LOC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x7D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#017E
class c_CM_TITLE_SET():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x7E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('titleId', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01C2
class c_CM_BREAK_WEAPONS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xC2\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('', 'i4')
              , ('weaponToBreakUniqueId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#02B4
class c_CM_EXCHANGE_CANCEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x02\xB4\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#02B5
class c_CM_WINDSTREAM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x02\xB5\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('teleportId', 'i4')
              , ('distance', 'i4')
              , ('state', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#02B6
class c_CM_EXCHANGE_LOCK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x02\xB6\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#02B7
class c_CM_EXCHANGE_OK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x02\xB7\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#02BA
class c_CM_MOTION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x02\xBA\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('', 'i1')
              , ('motionId', 'i2')
              , ('status', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#32
class c_CM_GROUP_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x32'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk1', 'i4')
              , ('unk2', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#9D
class c_CM_EXIT_LOCATION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#A9
class c_CM_LEGION_MODIFY_EMBLEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('legionId', 'i4')
              , ('emblemVer', 'i2')
              , ('', 'i1')
              , ('red', 'i1')
              , ('green', 'i1')
              , ('blue', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#000E
class s_SM_FRIEND_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x0E\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Level', 'i4')
              , ('PlayerClass', 'i4')
              , ('isOnline', 'i1')
              , ('MapId', 'i4')
              , ('LastOnlineTime', 'i4')
              , ('Note', '|S'+str(self.It.__next__()) )
              , ('Status', 'i1')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 17
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
   i += 6
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#000F
class s_SM_PETITION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x0F\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('ActionId', 'i1')
              , ('TotalOnlinePlayers', 'i4')
              , ('UsersWaitingForSupport', 'i2')
              , ('PetitionId', '|S'+str(self.It.__next__()) )
              , ('0x00_0', 'i2')
              , ('TotalPetitions', 'i1')
              , ('RemainingPetitions', 'i1')
              , ('calculateWaitTime', 'i2')
              , ('0x00_1', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 10
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0014
class s_SM_DELETE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x14\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('objectId', 'i4')
              , ('time', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0017
class s_SM_LOGIN_QUEUE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x17\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('waitingPosition', 'i4')
              , ('waitingTime', 'i4')
              , ('waitingCount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0018
class s_SM_INVENTORY_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x18\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0019
class s_SM_SYSTEM_MESSAGE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x19\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x13', 'i2')
              , ('npcObjId', 'i4')
              , ('msgId', 'i4')
              , ('countValue', 'i1')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('String', '|S'+str(self.It.__next__()) )
              , ('npcShout', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 13
   p = self.pck[i:i+1]
   count = struct.unpack('b', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
   i += 1
   for _ in range(count):
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 1
  def parse_list(self):
   i = 1
   i += 5
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
   pointer_list_in = self.lst
   self.lst = []
   def it(lst_in, lst_out):
     for i in lst_in:
       if isinstance(i ,tuple):
         it(i, lst_out)
       else: lst_out.append(i)
   it(pointer_list_in, self.lst)
   i += 1
   for _ in range(count):
      s_len = len(self.lst[i])
      yield s_len
      i += 2
#--------------------------------------------------------------------------#001A
class s_SM_DELETE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x1A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('itemUniqueId', 'i4')
              , ('0', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#001B
class s_SM_INVENTORY_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x1B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#001C
class s_SM_UI_SETTINGS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x1C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('type', 'i2')
              , ('0x1C', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#001D
class s_SM_UPDATE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x1D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#001F
class s_SM_STANCE_STATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x1F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerObjectId', 'i4')
              , ('stateId', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0020
class s_SM_GATHER_STATUS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x20\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerobjid', 'i4')
              , ('gatherableobjid', 'i4')
              , ('0', 'i2')
              , ('status', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0022
class s_SM_STATUPDATE_MP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x22\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('currentMp', 'i4')
              , ('maxMp', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0023
class s_SM_STATUPDATE_HP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x23\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('currentHp', 'i4')
              , ('maxHp', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0024
class s_SM_STATUPDATE_DP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x24\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('currentDp', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0026
class s_SM_STATUPDATE_EXP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x26\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('currentExp', 'i8')
              , ('recoverableExp', 'i8')
              , ('maxExp', 'i8')
              , ('curBoostExp', 'i8')
              , ('maxBoostExp', 'i8')
                  ]
    return dtype
#--------------------------------------------------------------------------#0027
class s_SM_DP_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x27\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerObjectId', 'i4')
              , ('currentDp', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#002A
class s_SM_LEGION_TABS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x2A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x12', 'i4')
              , ('page', 'i4')
              , ('hisSizeValue', 'i4')
                  ]+ list(self.f_hisSize()) +[
               ('0', 'i2')
                  ]
    return dtype
  def f_hisSize(self):
    for i in range(self.It.__next__()):
      dtype = ('hisSize_' + str(i) , [
               ('time', 'i4')
              , ('HistoryId', 'i1')
              , ('0', 'i1')
              , ('134', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 11
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 4
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#002D
class s_SM_ENTER_WORLD_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x2D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x00_0', 'i1')
              , ('0x00_1', 'i1')
              , ('0x00_2', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0032
class s_SM_QUESTION_WINDOW():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x32\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('code', 'i4')
              , ('0x24', 'i2')
              , ('DescriptionId', 'i4')
              , ('0x00_0', 'i2')
              , ('StringvalueOfparam', '|S'+str(self.It.__next__()) )
              , ('0x00_1', 'i4')
              , ('0x00_2', 'i4')
              , ('0x00_3', 'i4')
              , ('0x00_4', 'i4')
              , ('0x00_5', 'i4')
              , ('0x00_6', 'i2')
              , ('0x00_7', 'i1')
              , ('0x00_8', 'i4')
              , ('0x00_9', 'i4')
              , ('0x00_10', 'i4')
              , ('0x00_11', 'i4')
              , ('0x00_12', 'i2')
              , ('0x00_13', 'i1')
              , ('0x00_14', 'i4')
              , ('0x00_15', 'i2')
              , ('0x01', 'i1')
              , ('senderId', 'i4')
              , ('0x06', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 15
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 6
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0033
class s_SM_SKILL_COOLDOWN():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x33\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('cooldownssize', 'i2')
              , ('Key', 'i2')
              , ('left', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#003A
class s_SM_DIALOG_WINDOW():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x3A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
              , ('dialogID', 'i2')
              , ('questId', 'i4')
              , ('0', 'i2')
              , ('2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#003C
class s_SM_SELL_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x3C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
              , ('sellPercentage', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0040
class s_SM_WEATHER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x40\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('weatherCode', 'i2')
              , ('0x0', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0041
class s_SM_VIEW_PLAYER_DETAILS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x41\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjId', 'i4')
              , ('11', 'i1')
              , ('size', 'i1')
              , ('0_0', 'i1')
              , ('0_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0042
class s_SM_UPDATE_PLAYER_APPEARANCE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x42\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerId', 'i4')
              , ('mask', 'i2')
              , ('ItemSkinTemplate', 'i4')
              , ('ItemId', 'i4')
              , ('ItemColor', 'i4')
              , ('0x00', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0044
class s_SM_GAME_TIME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x44\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('GameTime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0046
class s_SM_LOOKATOBJECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x46\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('ObjectId', 'i4')
              , ('targetObjectId', 'i4')
              , ('heading', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0047
class s_SM_TIME_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x47\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('time', 'i4')
              , ('nanoTime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0048
class s_SM_SKILL_CANCEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x48\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('ObjectId', 'i4')
              , ('skillId', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0049
class s_SM_TARGET_SELECTED():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x49\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjId', 'i4')
              , ('level', 'i2')
              , ('maxHp', 'i4')
              , ('currentHp', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#004A
class s_SM_SKILL_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x4A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('size', 'i2')
              , ('SkillId', 'i2')
              , ('SkillLevel', 'i2')
              , ('0x00_0', 'i1')
              , ('ExtraLvl', 'i1')
              , ('0', 'i4')
              , ('isStigma', 'i1')
              , ('messageId', 'i4')
              , ('0x24', 'i2')
              , ('skillNameId', 'i4')
              , ('0x00_1', 'i2')
              , ('skillLvl', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 28
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 13
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#004C
class s_SM_SKILL_ACTIVATION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x4C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('skillId', 'i2')
              , ('unk', 'i4')
              , ('isActive', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#004D
class s_SM_STIGMA_SKILL_REMOVE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x4D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('skillId', 'i4')
              , ('1_0', 'i1')
              , ('1_1', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0050
class s_SM_ABNORMAL_EFFECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x50\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('effectedId', 'i4')
              , ('1', 'i1')
              , ('0_0', 'i4')
              , ('abnormals', 'i4')
              , ('0_1', 'i4')
              , ('size', 'i2')
              , ('SkillId', 'i2')
              , ('SkillLevel', 'i1')
              , ('TargetSlot', 'i1')
              , ('ElapsedTime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0051
class s_SM_ABNORMAL_STATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\x51\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('abnormals', 'i4')
              , ('0x00', 'i4')
              , ('size', 'i2')
              , ('EffectorId', 'i4')
              , ('SkillId', 'i2')
              , ('SkillLevel', 'i1')
              , ('TargetSlot', 'i1')
              , ('ElapsedTime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#00DC
class s_SM_FRIEND_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xDC\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('player', '|S'+str(self.It.__next__()) )
              , ('code', 'i1')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#00DF
class s_SM_BLOCK_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xDF\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerName', '|S'+str(self.It.__next__()) )
              , ('code', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#00E0
class s_SM_FRIEND_NOTIFY():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xE0\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('code', 'i1')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#00FE
class s_SM_VERSION_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00\xFE\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x00_0', 'i1')
              , ('GAMESERVER_ID', 'i1')
              , ('0x000188AD', 'i4')
              , ('0x000188A6', 'i4')
              , ('0x00000000', 'i4')
              , ('0x00018898', 'i4')
              , ('0x4C346D9D', 'i4')
              , ('0x00_1', 'i1')
              , ('SERVER_COUNTRY_CODE', 'i1')
              , ('0x00_2', 'i1')
              , ('SERVER_MODE_0', 'i1')
              , ('SERVER_MODE_1', 'i1')
              , ('SERVER_MODE_2', 'i1')
              , ('SERVER_MODE_3', 'i1')
              , ('int', 'i4')
              , ('0x015E', 'i2')
              , ('0x0A01_0', 'i2')
              , ('0x0A01_1', 'i2')
              , ('0x370A', 'i2')
              , ('0x02', 'i1')
              , ('0x00_3', 'i1')
              , ('0x14', 'i1')
              , ('0x01_0', 'i1')
              , ('0x00_4', 'i1')
              , ('0x00_5', 'i2')
              , ('0x00_6', 'i2')
              , ('0x01_1', 'i1')
              , ('0x00_7', 'i2')
              , ('Ip', 'i4')
              , ('Port', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0104
class s_SM_CHAT_INIT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x04\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('length', 'i4')
              , ('token', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0105
class s_SM_CHANNEL_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x05\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('currentChannel', 'i4')
              , ('instanceCount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0106
class s_SM_MACRO_RESULT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x06\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('code', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0107
class s_SM_MACRO_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x07\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('ObjectId', 'i4')
              , ('0x01', 'i1')
              , ('size', 'i2')
              , ('Key', 'i1')
              , ('Value', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 11
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 6
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0109
class s_SM_NICKNAME_CHECK_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x09\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('value', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#010A
class s_SM_RIFT_STATUS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x0A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
              , ('usedEntries', 'i4')
              , ('maxEntries', 'i4')
              , ('6793', 'i4')
              , ('RIFT_MIN_LEVEL', 'i4')
              , ('maxLevel', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#010D
class s_SM_ABYSS_RANK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x0D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('Ap', 'i8')
              , ('currentRankId', 'i4')
              , ('TopRanking', 'i4')
              , ('100Ap', 'i4')
              , ('AllKill', 'i4')
              , ('MaxRank', 'i4')
              , ('DailyKill', 'i4')
              , ('DailyAP', 'i8')
              , ('WeeklyKill', 'i4')
              , ('WeeklyAP', 'i8')
              , ('LastKill', 'i4')
              , ('LastAP', 'i8')
              , ('0x00', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0110
class s_SM_RECIPE_DELETE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x10\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('recipeId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0111
class s_SM_LEARN_RECIPE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x11\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('recipeId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#012B
class s_SM_LEGION_UPDATE_NICKNAME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x2B\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerObjId', 'i4')
              , ('newNickname', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 7
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0153
class s_SM_PLASTIC_SURGERY():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x53\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerObjId', 'i4')
              , ('check_ticket', 'i1')
              , ('change_sex', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0156
class s_SM_NAME_CHANGE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x56\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('playerObjectId', 'i4')
              , ('oldName', '|S'+str(self.It.__next__()) )
              , ('newName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 15
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0158
class s_SM_GROUP_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x58\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('groupid', 'i4')
              , ('leaderid', 'i4')
              , ('Id_0', 'i4')
              , ('Id_1', 'i4')
              , ('common_item_above', 'i4')
              , ('superior_item_above', 'i4')
              , ('heroic_item_above', 'i4')
              , ('fabled_item_above', 'i4')
              , ('ethernal_item_above', 'i4')
              , ('over_ethernal', 'i4')
              , ('over_over_ethernal', 'i4')
              , ('0x3F00', 'i4')
              , ('0x00_0', 'i4')
              , ('0x00_1', 'i2')
              , ('0x00_2', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#015E
class s_SM_ABYSS_ARTIFACT_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x5E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('validLocationssize', 'i2')
              , ('LocationId', 'i4')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0162
class s_SM_PLAYER_STATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x62\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerObjId', 'i4')
              , ('visualState', 'i1')
              , ('seeState', 'i1')
              , ('0x01', 'i1')
              , ('0x00', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0164
class s_SM_LEVEL_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x64\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
              , ('effect', 'i2')
              , ('level', 'i2')
              , ('0x00', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0166
class s_SM_KEY():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x66\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('key', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0167
class s_SM_STARTED_QUEST_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x67\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x01', 'i2')
              , ('1startedQuestListsize', 'i2')
              , ('startedQuestListsize', 'i1')
              , ('QuestId', 'i2')
              , ('0_0', 'i2')
              , ('Status', 'i1')
              , ('QuestVars', 'i4')
              , ('0_1', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0168
class s_SM_EXCHANGE_REQUEST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x68\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('receiver', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0169
class s_SM_SUMMON_PANEL_REMOVE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x69\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#016B
class s_SM_EXCHANGE_ADD_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x6B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('action', 'i1')
              , ('0', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#016C
class s_SM_EXCHANGE_CONFIRMATION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x6C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('action', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#016D
class s_SM_EXCHANGE_ADD_KINAH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x6D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('action', 'i1')
              , ('int', 'i4')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0171
class s_SM_TARGET_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x71\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('ObjectId', 'i4')
              , ('Target', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0177
class s_SM_LEGION_UPDATE_SELF_INTRO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x77\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerObjId', 'i4')
              , ('selfintro', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 7
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0178
class s_SM_DREDGION_INSTANCE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x78\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('dredgiontype', 'i4')
              , ('players', 'i1')
              , ('instanceid', 'i4')
              , ('401193', 'i4')
              , ('401197', 'i4')
              , ('401675', 'i4')
              , ('401677', 'i4')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('allowed', 'i4')
              , ('timer', 'i2')
              , ('0_2', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0179
class s_SM_INSTANCE_SCORE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x79\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('mapId_0', 'i4')
              , ('instanceTime_0', 'i4')
              , ('3145728', 'i4')
              , ('2097152', 'i4')
              , ('ObjectId', 'i4')
              , ('points_0', 'i4')
              , ('3', 'i4')
              , ('1', 'i4')
              , ('signs', 'i4')
              , ('166count', 'i4')
              , ('0', 'i2')
              , ('mapId_1', 'i4')
              , ('instanceTime_1', 'i4')
              , ('stopTime', 'i4')
              , ('totalPoints', 'i4')
              , ('points_1', 'i4')
              , ('kills', 'i4')
              , ('rank', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#017B
class s_SM_QUEST_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x7B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x01', 'i2')
              , ('1completeQuestListsize', 'i2')
              , ('QuestId_0', 'i2')
              , ('0x00', 'i2')
              , ('CompleteCount', 'i1')
              , ('QuestId_1', 'i2')
              , ('0_0', 'i2')
              , ('Status', 'i1')
              , ('QuestVars', 'i4')
              , ('0_1', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#017E
class s_SM_PING_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x7E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x04', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#017F
class s_SM_NEARBY_QUESTS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x7F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x00', 'i1')
              , ('1size', 'i2')
              , ('id', 'i2')
              , ('0', 'i2')
              , ('2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0186
class s_SM_UPDATE_NOTE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x86\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjId', 'i4')
              , ('note', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 7
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0187
class s_SM_ITEM_COOLDOWN():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x87\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('cooldownssize', 'i2')
              , ('Key', 'i2')
              , ('left', 'i4')
              , ('Value', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
  def parse_list(self):
   i = 1
#--------------------------------------------------------------------------#0189
class s_SM_PLAY_MOVIE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x89\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('type', 'i1')
              , ('0x00_0', 'i4')
              , ('0x00_1', 'i4')
              , ('movieId', 'i2')
              , ('0x00_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#018C
class s_SM_LEGION_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x8C\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('LegionName', '|S'+str(self.It.__next__()) )
              , ('LegionLevel', 'i1')
              , ('LegionRank', 'i4')
              , ('DeputyPermission1', 'i1')
              , ('DeputyPermission2', 'i1')
              , ('CenturionPermission1', 'i1')
              , ('CenturionPermission2', 'i1')
              , ('LegionaryPermission1', 'i1')
              , ('LegionaryPermission2', 'i1')
              , ('VolunteerPermission1', 'i1')
              , ('VolunteerPermission2', 'i1')
              , ('ContributionPoints', 'i4')
              , ('0x00_0', 'i4')
              , ('0x00_1', 'i4')
              , ('0x00_2', 'i4')
              , ('announcemenunixTime', '|S'+str(self.It.__next__()) )
              , ('int', 'i4')
              , ('105', 'i2')
              , ('108', 'i2')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 29
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
   i += 15
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#018E
class s_SM_LEGION_LEAVE_MEMBER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x8E\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerObjId', 'i4')
              , ('0x00_0', 'i1')
              , ('0x00_1', 'i4')
              , ('msgId', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('name1', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 16
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 6
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#018F
class s_SM_LEGION_ADD_MEMBER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x8F\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('ObjectId', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('LegionMember', 'i1')
              , ('isMember', 'i1')
              , ('CommonData', 'i1')
              , ('Level', 'i1')
              , ('Position', 'i4')
              , ('msgId', 'i4')
              , ('text', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 7
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 12
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
   i += 7
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0190
class s_SM_LEGION_UPDATE_TITLE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x90\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('objectId', 'i4')
              , ('legionId', 'i4')
              , ('legionName', '|S'+str(self.It.__next__()) )
              , ('rank', 'i1')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 11
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 4
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0191
class s_SM_LEGION_UPDATE_MEMBER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x91\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('ObjectId', 'i4')
              , ('LegionMember', 'i1')
              , ('CommonData', 'i1')
              , ('Level', 'i1')
              , ('Position', 'i4')
              , ('Online', 'i1')
              , ('LastOnline', 'i4')
              , ('msgId', 'i4')
              , ('text', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 23
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 10
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0192
class s_SM_MOTION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x92\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('unk_0', 'i1')
              , ('unk_1', 'i2')
              , ('unk_2', 'i1')
              , ('unk_3', 'i4')
              , ('unk_4', 'i2')
              , ('unk_5', 'i1')
              , ('motionId', 'i2')
              , ('status', 'i1')
              , ('unk_6', 'i1')
              , ('objectId', 'i4')
              , ('waitingMotion', 'i2')
              , ('runningMotion', 'i2')
              , ('jumpingMotion', 'i2')
              , ('restMotion', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0198
class s_SM_SUMMON_OWNER_REMOVE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x98\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('summonObjId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0199
class s_SM_SUMMON_PANEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x99\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('ObjectId', 'i4')
              , ('Level', 'i2')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('LifeStats', 'i4')
              , ('GameStats_0', 'i4')
              , ('GameStats_1', 'i4')
              , ('GameStats_2', 'i2')
              , ('GameStats_3', 'i2')
              , ('0_2', 'i4')
              , ('0_3', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#019B
class s_SM_SUMMON_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x9B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('Level', 'i1')
              , ('Mode', 'i2')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('LifeStats', 'i4')
              , ('GameStats_0', 'i4')
              , ('GameStats_1', 'i4')
              , ('GameStats_2', 'i2')
              , ('GameStats_3', 'i2')
              , ('GameStats_4', 'i2')
              , ('GameStats_5', 'i2')
              , ('GameStats_6', 'i2')
              , ('GameStats_7', 'i2')
              , ('GameStats_8', 'i2')
              , ('GameStats_9', 'i2')
              , ('GameStats_10', 'i2')
              , ('GameStats_11', 'i4')
              , ('GameStats_12', 'i4')
              , ('GameStats_13', 'i2')
              , ('GameStats_14', 'i2')
              , ('GameStats_15', 'i2')
              , ('GameStats_16', 'i2')
              , ('GameStats_17', 'i2')
              , ('GameStats_18', 'i2')
              , ('GameStats_19', 'i2')
              , ('GameStats_20', 'i2')
              , ('GameStats_21', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#019D
class s_SM_LEGION_MEMBERLIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x9D\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x01', 'i1')
              , ('size', 'i2')
              , ('ObjectId', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('PlayerClass', 'i1')
              , ('Level', 'i4')
              , ('Rank', 'i1')
              , ('WorldId', 'i4')
              , ('legionMemberisOnline', 'i1')
              , ('SelfIntro', '|S'+str(self.It.__next__()) )
              , ('Nickname', '|S'+str(self.It.__next__()) )
              , ('LastOnline', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 10
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 11
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 6
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#019F
class s_SM_INGAMESHOP_BALANCE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x9F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('ActivePlayer', 'i8')
                  ]
    return dtype
#--------------------------------------------------------------------------#019F
class s_SM_TOLL_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\x9F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('tollCount', 'i4')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01A0
class s_SM_SUMMON_USESKILL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xA0\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('summonId', 'i4')
              , ('skillId', 'i2')
              , ('skillLvl', 'i1')
              , ('targetId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01A2
class s_SM_FRIEND_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xA2\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('tSize', 'i2')
              , ('0', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Level', 'i4')
              , ('PlayerClass', 'i4')
              , ('1', 'i1')
              , ('MapId', 'i4')
              , ('LastOnlineTime', 'i4')
              , ('Note', '|S'+str(self.It.__next__()) )
              , ('Status', 'i1')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 17
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 4
   s_len = len(self.lst[i])
   yield s_len
   i += 6
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#01A4
class s_SM_PRIVATE_STORE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xA4\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('storeObjectId', 'i4')
              , ('size', 'i2')
              , ('ItemObjId', 'i4')
              , ('ItemTemplate', 'i4')
              , ('int_0', 'i2')
              , ('int_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01A9
class s_SM_MAY_LOGIN_INTO_GAME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xA9\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x00', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01AA
class s_SM_ACADEMY_BOOTCAMP_STAGE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xAA\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('2', 'i1')
              , ('0', 'i4')
              , ('stagevalue', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01AB
class s_SM_ABYSS_RANKING_LEGIONS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xAB\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('RaceId_0', 'i4')
              , ('Instance', 'i4')
              , ('0x01_0', 'i4')
              , ('0x01_1', 'i4')
              , ('datasize', 'i2')
              , ('LegionRank', 'i4')
              , ('LegionOldRank', 'i4')
              , ('LegionId', 'i4')
              , ('RaceId_1', 'i4')
              , ('LegionLevel', 'i1')
              , ('LegionMembers', 'i4')
              , ('LegionCP', 'i8')
              , ('LegionName', '|S'+str(self.It.__next__()) )
              , ('80LegionName', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 50
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 14
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#01AC
class s_SM_PONG():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xAC\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x00_0', 'i1')
              , ('0x00_1', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01AD
class s_SM_INSTANCE_COOLDOWN():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xAD\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('type', 'i2')
              , ('0x0_0', 'i4')
              , ('0x1_0', 'i2')
              , ('ObjectId', 'i4')
              , ('0x1_1', 'i2')
              , ('instanceId', 'i4')
              , ('0x0_1', 'i4')
              , ('remainingTime', 'i4')
              , ('0x0_2', 'i2')
              , ('Name_0', '|S'+str(self.It.__next__()) )
              , ('0x0_3', 'i2')
              , ('Name_1', '|S'+str(self.It.__next__()) )
              , ('0x0_4', 'i2')
              , ('0x0_5', 'i2')
              , ('0x0_6', 'i2')
              , ('0x0_7', 'i2')
              , ('0x0_8', 'i2')
              , ('0x0_9', 'i2')
              , ('0x0_10', 'i2')
              , ('0x0_11', 'i2')
              , ('0x0_12', 'i2')
              , ('0x0_13', 'i2')
              , ('0x0_14', 'i2')
              , ('0x0_15', 'i2')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 31
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 11
   s_len = len(self.lst[i])
   yield s_len
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#01AE
class s_SM_KISK_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xAE\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('objId', 'i4')
              , ('useMask', 'i4')
              , ('currentMembers', 'i4')
              , ('maxMembers', 'i4')
              , ('remainingRessurects', 'i4')
              , ('maxRessurects', 'i4')
              , ('remainingLifetime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01B1
class s_SM_PRIVATE_STORE_NAME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xB1\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerObjId', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 7
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#01B2
class s_SM_CRAFT_ANIMATION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xB2\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('senderObjectId', 'i4')
              , ('targetObjectId', 'i4')
              , ('skillId', 'i2')
              , ('action', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01B4
class s_SM_ASCENSION_MORPH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xB4\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('inascension', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01B6
class s_SM_CUSTOM_SETTINGS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xB6\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('ObjectId', 'i4')
              , ('0x01', 'i1')
              , ('PlayerSettings_0', 'i2')
              , ('PlayerSettings_1', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#01B7
class s_SM_ITEM_USAGE_ANIMATION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xB7\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerObjId', 'i4')
              , ('targetObjId', 'i4')
              , ('itemObjId', 'i4')
              , ('itemId', 'i4')
              , ('time', 'i4')
              , ('end_0', 'i1')
              , ('1', 'i1')
              , ('unk', 'i4')
              , ('end_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01BF
class s_SM_QUESTIONNAIRE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xBF\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('messageId', 'i4')
              , ('chunk', 'i1')
              , ('count', 'i1')
              , ('length', 'i2')
              , ('html', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 11
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 6
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#01C0
class s_SM_RESURRECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xC0\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('skillId', 'i2')
              , ('0', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#01C1
class s_SM_DIE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xC1\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('hasRebirth', 'i1')
              , ('hasItem', 'i1')
              , ('remainingKiskTime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01C2
class s_SM_WINDSTREAM_LOCATIONS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xC2\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('bidirectional', 'i4')
              , ('mapId', 'i4')
              , ('streamId', 'i4')
              , ('boost', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01C3
class s_SM_WINDSTREAM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xC3\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('unk1', 'i4')
              , ('unk2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01C6
class s_SM_WAREHOUSE_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xC6\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('warehouseType', 'i1')
              , ('firstPacket', 'i1')
              , ('expandLvl', 'i1')
              , ('0', 'i2')
              , ('itemListsize', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#01C7
class s_SM_REPURCHASE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xC7\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
              , ('0_0', 'i4')
              , ('itemssize', 'i2')
              , ('0_1', 'i2')
              , ('ObjectId', 'i4')
              , ('ItemTemplate', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01C8
class s_SM_DELETE_WAREHOUSE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xC8\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('warehouseType', 'i1')
              , ('itemObjId', 'i4')
              , ('14', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01C9
class s_SM_WAREHOUSE_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xC9\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('warehouseType', 'i1')
              , ('13', 'i2')
              , ('1', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#01CA
class s_SM_IN_GAME_SHOP_CATEGORY_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xCA\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('2', 'i4')
              , ('categorysize', 'i2')
              , ('ShopCategorygetId', 'i4')
              , ('ShopCategorygetName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 13
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#01CB
class s_SM_UPDATE_WAREHOUSE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xCB\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#01CC
class s_SM_IN_GAME_SHOP_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xCC\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('ObjectId', 'i4')
              , ('ItemPrice', 'i4')
              , ('0_0', 'i4')
              , ('0_1', 'i2')
              , ('ItemId', 'i4')
              , ('ItemCount', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('0_4', 'i4')
              , ('0_5', 'i4')
              , ('0_6', 'i4')
              , ('0_7', 'i2')
              , ('0_8', 'i1')
              , ('Description', '|S'+str(self.It.__next__()) )
              , ('0_9', 'i2')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 48
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 15
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#01CD
class s_SM_IN_GAME_SHOP_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xCD\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('salesRanking_0', 'i4')
              , ('nrList_0', 'i4')
              , ('itemssize', 'i4')
              , ('inAllItemsnullU0', 'i2')
              , ('ObjectId_0', 'i4')
              , ('salesRanking_1', 'i4')
              , ('nrList_1', 'i4')
              , ('DAOManagergetDAOInGameShopDAOclass', 'i4')
              , ('salesRankingItemssize', 'i2')
              , ('ObjectId_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01CE
class s_SM_TITLE_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xCE\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#01D4
class s_SM_LEGION_EMBLEM_SEND():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xD4\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('size', 'i4')
              , ('emblemData', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01D5
class s_SM_LEGION_EMBLEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xD5\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('legionId', 'i4')
              , ('emblemVer', 'i1')
              , ('isCustom', 'i1')
              , ('emblemSize', 'i4')
              , ('0xFF', 'i1')
              , ('color_r', 'i1')
              , ('color_g', 'i1')
              , ('color_b', 'i1')
              , ('legionName', '|S'+str(self.It.__next__()) )
              , ('0x01', 'i1')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 17
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 10
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#01D7
class s_SM_LEGION_UPDATE_EMBLEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xD7\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('legionId', 'i4')
              , ('emblemVer', 'i1')
              , ('isCustom', 'i1')
              , ('0xFF', 'i1')
              , ('color_r', 'i1')
              , ('color_g', 'i1')
              , ('color_b', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01D8
class s_SM_SIEGE_AETHERIC_FIELDS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xD8\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('locationssize', 'i2')
              , ('LocationId', 'i4')
              , ('1', 'i1')
              , ('0', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01DA
class s_SM_ABYSS_ARTIFACT_INFO3():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xDA\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('validLocationssize', 'i2')
              , ('IntegerparseIntlocIdStr', 'i4')
              , ('0_0', 'i4')
              , ('0_1', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01DE
class s_SM_BLOCK_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xDE\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('listgetSize', 'i2')
              , ('0', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Reason', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 4
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#01E2
class s_SM_TELEPORT_MAP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xE2\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
              , ('teleportgetTeleportId', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#01E5
class s_SM_USE_OBJECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xE5\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerObjId', 'i4')
              , ('targetObjId', 'i4')
              , ('time', 'i4')
              , ('actionType', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01E6
class s_SM_CHARACTER_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xE6\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playOk2', 'i4')
              , ('accountsize', 'i1')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i1')
              , ('0_4', 'i1')
              , ('28', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01E7
class s_SM_L2AUTH_LOGIN_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xE7\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('ok', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 7
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#01E8
class s_SM_DELETE_CHARACTER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xE8\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x00_0', 'i4')
              , ('playerObjId', 'i4')
              , ('deletionTime', 'i4')
              , ('0x10', 'i4')
              , ('0x00_1', 'i4')
              , ('0x00_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01EB
class s_SM_RESTORE_CHARACTER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xEB\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('success', 'i4')
              , ('chaOid', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01EC
class s_SM_LOOT_ITEMLIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xEC\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
              , ('size', 'i1')
              , ('dropIndex', 'i1')
              , ('dropDropTemplate', 'i4')
              , ('int', 'i2')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01ED
class s_SM_LOOT_STATUS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xED\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId', 'i4')
              , ('state', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01EE
class s_SM_MANTRA_EFFECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xEE\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x00', 'i4')
              , ('ObjectId', 'i4')
              , ('subEffectId', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#01EF
class s_SM_RECIPE_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xEF\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('count', 'i2')
              , ('id', 'i4')
              , ('0', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01F1
class s_SM_SIEGE_LOCATION_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xF1\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0_0', 'i1')
              , ('0_1', 'i2')
              , ('infoType', 'i1')
              , ('locationssize', 'i2')
              , ('sLocationId', 'i4')
              , ('legionId', 'i4')
              , ('emblemId', 'i4')
              , ('0xFF', 'i1')
              , ('Color_r', 'i1')
              , ('Color_g', 'i1')
              , ('Color_b', 'i1')
              , ('sRace', 'i1')
              , ('isVulnerable', 'i1')
              , ('isCanTeleport', 'i1')
              , ('sNextState', 'i1')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01F2
class s_SM_FLY_TIME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xF2\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('currentFp', 'i4')
              , ('maxFp', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01F3
class s_SM_FORTRESS_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xF3\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('locationId', 'i4')
              , ('value', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01F7
class s_SM_LEAVE_GROUP_MEMBER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xF7\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x00_0', 'i4')
              , ('0x00_1', 'i4')
              , ('0x00_2', 'i2')
              , ('0x00_3', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01F8
class s_SM_ALLIANCE_READY_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xF8\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('playerObjectId', 'i4')
              , ('statusCode', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01F9
class s_SM_SHOW_BRAND():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xF9\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x01_0', 'i2')
              , ('0x01_1', 'i4')
              , ('brandId', 'i4')
              , ('targetObjectId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01FA
class s_SM_PRICES():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xFA\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('GlobalPrices', 'i1')
              , ('GlobalPricesModifier', 'i1')
              , ('TaxesActivePlayer', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01FD
class s_SM_TRADELIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xFD\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('targetObjectId_0', 'i4')
              , ('isAbyss', 'i1')
              , ('Category', 'i1')
              , ('buyPriceModifier_0', 'i4')
              , ('Count', 'i2')
              , ('Id_0', 'i4')
              , ('limitedItemssize', 'i2')
              , ('Id_1', 'i4')
              , ('Instance_0', 'i2')
              , ('Instance_1', 'i2')
              , ('targetObjectId_1', 'i4')
              , ('1', 'i1')
              , ('buyPriceModifier_1', 'i4')
              , ('0', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#01FF
class s_SM_RECONNECT_KEY():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01\xFF\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('static', 'i1')
              , ('id2', 'i2')
              , ('0x00', 'i1')
              , ('key', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A6
class s_SM_ABYSS_RANK_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('ObjectId', 'i4')
              , ('0', 'i1')
              , ('rankId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A7
class s_SM_GROUP_LOOT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('groupId', 'i4')
              , ('unk1', 'i4')
              , ('unk2', 'i4')
              , ('itemId', 'i4')
              , ('itemIndex', 'i1')
              , ('lootCorpseId', 'i4')
              , ('distributionId', 'i1')
              , ('playerId', 'i4')
              , ('luck', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AA
class s_SM_PLAYER_ID():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAA'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('0x2', 'i2')
              , ('0x0_0', 'i4')
              , ('0x1_0', 'i2')
              , ('ObjectId', 'i4')
              , ('0x1_1', 'i2')
              , ('instanceId', 'i4')
              , ('0x0_1', 'i4')
              , ('remainingTime', 'i4')
              , ('0x0_2', 'i2')
              , ('Name_0', '|S'+str(self.It.__next__()) )
              , ('0x0_3', 'i2')
              , ('Name_1', '|S'+str(self.It.__next__()) )
              , ('0x0_4', 'i2')
              , ('0x0_5', 'i2')
              , ('0x0_6', 'i2')
              , ('0x0_7', 'i2')
              , ('0x0_8', 'i2')
              , ('0x0_9', 'i2')
              , ('0x0_10', 'i2')
              , ('0x0_11', 'i2')
              , ('0x0_12', 'i2')
              , ('0x0_13', 'i2')
              , ('0x0_14', 'i2')
              , ('0x0_15', 'i2')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 30
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 10
   s_len = len(self.lst[i])
   yield s_len
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#AB
class s_SM_STAGE_STEP_STATUS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk1', 'i1')
              , ('0', 'i4')
              , ('mess', 'i2')
              , ('unk2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#BF
class s_SM_LEGION_EMBLEM_SEND():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('size', 'i4')
              , ('emblemData', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D9
class s_SM_ABYSS_ARTIFACT_INFO2():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('size', 'i2')
              , ('LocationId', 'i4')
              , ('0', 'i1')
                  ]
    return dtype
class Pck_invoke_dict():
 def __init__(self):
   self.Pck_invoke_s = {}
   self.Pck_invoke_c = {}
 def get_Pck_invoke_c(self):
   self.Pck_invoke_s[c_CM_TIME_CHECK().invoke] = c_CM_TIME_CHECK()
   self.Pck_invoke_s[c_CM_LEGION_EMBLEM().invoke] = c_CM_LEGION_EMBLEM()
   self.Pck_invoke_s[c_CM_GATHER().invoke] = c_CM_GATHER()
   self.Pck_invoke_s[c_CM_PETITION().invoke] = c_CM_PETITION()
   self.Pck_invoke_s[c_CM_OPEN_STATICDOOR().invoke] = c_CM_OPEN_STATICDOOR()
   self.Pck_invoke_s[c_CM_CHAT_MESSAGE_PUBLIC().invoke] = c_CM_CHAT_MESSAGE_PUBLIC()
   self.Pck_invoke_s[c_CM_CHAT_MESSAGE_WHISPER().invoke] = c_CM_CHAT_MESSAGE_WHISPER()
   self.Pck_invoke_s[c_CM_SKILL_DEACTIVATE().invoke] = c_CM_SKILL_DEACTIVATE()
   self.Pck_invoke_s[c_CM_TARGET_SELECT().invoke] = c_CM_TARGET_SELECT()
   self.Pck_invoke_s[c_CM_ATTACK().invoke] = c_CM_ATTACK()
   self.Pck_invoke_s[c_CM_EQUIP_ITEM().invoke] = c_CM_EQUIP_ITEM()
   self.Pck_invoke_s[c_CM_REMOVE_ALTERED_STATE().invoke] = c_CM_REMOVE_ALTERED_STATE()
   self.Pck_invoke_s[c_CM_PLAYER_LISTENER().invoke] = c_CM_PLAYER_LISTENER()
   self.Pck_invoke_s[c_CM_PING().invoke] = c_CM_PING()
   self.Pck_invoke_s[c_CM_QUESTION_RESPONSE().invoke] = c_CM_QUESTION_RESPONSE()
   self.Pck_invoke_s[c_CM_LEGION_EMBLEM_SEND().invoke] = c_CM_LEGION_EMBLEM_SEND()
   self.Pck_invoke_s[c_CM_CLOSE_DIALOG().invoke] = c_CM_CLOSE_DIALOG()
   self.Pck_invoke_s[c_CM_DIALOG_SELECT().invoke] = c_CM_DIALOG_SELECT()
   self.Pck_invoke_s[c_CM_BUY_ITEM().invoke] = c_CM_BUY_ITEM()
   self.Pck_invoke_s[c_CM_SHOW_DIALOG().invoke] = c_CM_SHOW_DIALOG()
   self.Pck_invoke_s[c_CM_SET_NOTE().invoke] = c_CM_SET_NOTE()
   self.Pck_invoke_s[c_CM_LEGION_TABS().invoke] = c_CM_LEGION_TABS()
   self.Pck_invoke_s[c_CM_CHAT_RECRUIT_GROUP().invoke] = c_CM_CHAT_RECRUIT_GROUP()
   self.Pck_invoke_s[c_CM_LEGION_MODIFY_EMBLEM().invoke] = c_CM_LEGION_MODIFY_EMBLEM()
   self.Pck_invoke_s[c_CM_EXCHANGE_ADD_KINAH().invoke] = c_CM_EXCHANGE_ADD_KINAH()
   self.Pck_invoke_s[c_CM_EXCHANGE_REQUEST().invoke] = c_CM_EXCHANGE_REQUEST()
   self.Pck_invoke_s[c_CM_EXCHANGE_ADD_ITEM().invoke] = c_CM_EXCHANGE_ADD_ITEM()
   self.Pck_invoke_s[c_CM_VERSION_CHECK().invoke] = c_CM_VERSION_CHECK()
   self.Pck_invoke_s[c_CM_REVIVE().invoke] = c_CM_REVIVE()
   self.Pck_invoke_s[c_CM_QUIT().invoke] = c_CM_QUIT()
   self.Pck_invoke_s[c_CM_MAY_QUIT().invoke] = c_CM_MAY_QUIT()
   self.Pck_invoke_s[c_CM_LEVEL_READY().invoke] = c_CM_LEVEL_READY()
   self.Pck_invoke_s[c_CM_UI_SETTINGS().invoke] = c_CM_UI_SETTINGS()
   self.Pck_invoke_s[c_CM_ENTER_WORLD().invoke] = c_CM_ENTER_WORLD()
   self.Pck_invoke_s[c_CM_OBJECT_SEARCH().invoke] = c_CM_OBJECT_SEARCH()
   self.Pck_invoke_s[c_CM_CUSTOM_SETTINGS().invoke] = c_CM_CUSTOM_SETTINGS()
   self.Pck_invoke_s[c_CM_QUESTIONNAIRE().invoke] = c_CM_QUESTIONNAIRE()
   self.Pck_invoke_s[c_CM_L2AUTH_LOGIN_CHECK().invoke] = c_CM_L2AUTH_LOGIN_CHECK()
   self.Pck_invoke_s[c_CM_CHARACTER_LIST().invoke] = c_CM_CHARACTER_LIST()
   self.Pck_invoke_s[c_CM_TELEPORT_SELECT().invoke] = c_CM_TELEPORT_SELECT()
   self.Pck_invoke_s[c_CM_RESTORE_CHARACTER().invoke] = c_CM_RESTORE_CHARACTER()
   self.Pck_invoke_s[c_CM_START_LOOT().invoke] = c_CM_START_LOOT()
   self.Pck_invoke_s[c_CM_DELETE_CHARACTER().invoke] = c_CM_DELETE_CHARACTER()
   self.Pck_invoke_s[c_CM_SPLIT_ITEM().invoke] = c_CM_SPLIT_ITEM()
   self.Pck_invoke_s[c_CM_LOOT_ITEM().invoke] = c_CM_LOOT_ITEM()
   self.Pck_invoke_s[c_CM_MOVE_ITEM().invoke] = c_CM_MOVE_ITEM()
   self.Pck_invoke_s[c_CM_LEGION_UPLOAD_EMBLEM().invoke] = c_CM_LEGION_UPLOAD_EMBLEM()
   self.Pck_invoke_s[c_CM_MAIL_SUMMON_ZEPHYR().invoke] = c_CM_MAIL_SUMMON_ZEPHYR()
   self.Pck_invoke_s[c_CM_PLAYER_SEARCH().invoke] = c_CM_PLAYER_SEARCH()
   self.Pck_invoke_s[c_CM_LEGION_UPLOAD_INFO().invoke] = c_CM_LEGION_UPLOAD_INFO()
   self.Pck_invoke_s[c_CM_BLOCK_ADD().invoke] = c_CM_BLOCK_ADD()
   self.Pck_invoke_s[c_CM_DISCONNECT().invoke] = c_CM_DISCONNECT()
   self.Pck_invoke_s[c_CM_FRIEND_STATUS().invoke] = c_CM_FRIEND_STATUS()
   self.Pck_invoke_s[c_CM_BLOCK_DEL().invoke] = c_CM_BLOCK_DEL()
   self.Pck_invoke_s[c_CM_SHOW_BLOCKLIST().invoke] = c_CM_SHOW_BLOCKLIST()
   self.Pck_invoke_s[c_CM_REPLACE_ITEM().invoke] = c_CM_REPLACE_ITEM()
   self.Pck_invoke_s[c_CM_MAC_ADDRESS2().invoke] = c_CM_MAC_ADDRESS2()
   self.Pck_invoke_s[c_CM_MAC_ADDRESS2().invoke] = c_CM_MAC_ADDRESS2()
   self.Pck_invoke_s[c_CM_CHANGE_CHANNEL().invoke] = c_CM_CHANGE_CHANNEL()
   self.Pck_invoke_s[c_CM_CHECK_NICKNAME().invoke] = c_CM_CHECK_NICKNAME()
   self.Pck_invoke_s[c_CM_MACRO_CREATE().invoke] = c_CM_MACRO_CREATE()
   self.Pck_invoke_s[c_CM_MACRO_DELETE().invoke] = c_CM_MACRO_DELETE()
   self.Pck_invoke_s[c_CM_SHOW_BRAND().invoke] = c_CM_SHOW_BRAND()
   self.Pck_invoke_s[c_CM_BLOCK_SET_REASON().invoke] = c_CM_BLOCK_SET_REASON()
   self.Pck_invoke_s[c_CM_DISTRIBUTION_SETTINGS().invoke] = c_CM_DISTRIBUTION_SETTINGS()
   self.Pck_invoke_s[c_CM_MAY_LOGIN_INTO_GAME().invoke] = c_CM_MAY_LOGIN_INTO_GAME()
   self.Pck_invoke_s[c_CM_RECONNECT_AUTH().invoke] = c_CM_RECONNECT_AUTH()
   self.Pck_invoke_s[c_CM_GROUP_LOOT().invoke] = c_CM_GROUP_LOOT()
   self.Pck_invoke_s[c_CM_MAC_ADDRESS().invoke] = c_CM_MAC_ADDRESS()
   self.Pck_invoke_s[c_CM_MAC_ADDRESS().invoke] = c_CM_MAC_ADDRESS()
   self.Pck_invoke_s[c_CM_ABYSS_RANKING_PLAYERS().invoke] = c_CM_ABYSS_RANKING_PLAYERS()
   self.Pck_invoke_s[c_CM_IN_GAME_SHOP_INFO().invoke] = c_CM_IN_GAME_SHOP_INFO()
   self.Pck_invoke_s[c_CM_REPORT_PLAYER().invoke] = c_CM_REPORT_PLAYER()
   self.Pck_invoke_s[c_CM_INSTANCE_CD_REQUEST().invoke] = c_CM_INSTANCE_CD_REQUEST()
   self.Pck_invoke_s[c_CM_NAME_CHANGE().invoke] = c_CM_NAME_CHANGE()
   self.Pck_invoke_s[c_CM_SHOW_MAP().invoke] = c_CM_SHOW_MAP()
   self.Pck_invoke_s[c_CM_SUMMON_EMOTION().invoke] = c_CM_SUMMON_EMOTION()
   self.Pck_invoke_s[c_CM_DREDGION_REQUEST().invoke] = c_CM_DREDGION_REQUEST()
   self.Pck_invoke_s[c_CM_FUSION_WEAPONS().invoke] = c_CM_FUSION_WEAPONS()
   self.Pck_invoke_s[c_CM_SUMMON_ATTACK().invoke] = c_CM_SUMMON_ATTACK()
   self.Pck_invoke_s[c_CM_PLAY_MOVIE_END().invoke] = c_CM_PLAY_MOVIE_END()
   self.Pck_invoke_s[c_CM_DELETE_QUEST().invoke] = c_CM_DELETE_QUEST()
   self.Pck_invoke_s[c_CM_ITEM_REMODEL().invoke] = c_CM_ITEM_REMODEL()
   self.Pck_invoke_s[c_CM_GODSTONE_SOCKET().invoke] = c_CM_GODSTONE_SOCKET()
   self.Pck_invoke_s[c_CM_INVITE_TO_GROUP().invoke] = c_CM_INVITE_TO_GROUP()
   self.Pck_invoke_s[c_CM_ALLIANCE_GROUP_CHANGE().invoke] = c_CM_ALLIANCE_GROUP_CHANGE()
   self.Pck_invoke_s[c_CM_PLAYER_STATUS_INFO().invoke] = c_CM_PLAYER_STATUS_INFO()
   self.Pck_invoke_s[c_CM_VIEW_PLAYER_DETAILS().invoke] = c_CM_VIEW_PLAYER_DETAILS()
   self.Pck_invoke_s[c_CM_PING_REQUEST().invoke] = c_CM_PING_REQUEST()
   self.Pck_invoke_s[c_CM_SHOW_FRIENDLIST().invoke] = c_CM_SHOW_FRIENDLIST()
   self.Pck_invoke_s[c_CM_CLIENT_COMMAND_ROLL().invoke] = c_CM_CLIENT_COMMAND_ROLL()
   self.Pck_invoke_s[c_CM_GROUP_DISTRIBUTION().invoke] = c_CM_GROUP_DISTRIBUTION()
   self.Pck_invoke_s[c_CM_DUEL_REQUEST().invoke] = c_CM_DUEL_REQUEST()
   self.Pck_invoke_s[c_CM_FRIEND_ADD().invoke] = c_CM_FRIEND_ADD()
   self.Pck_invoke_s[c_CM_FRIEND_DEL().invoke] = c_CM_FRIEND_DEL()
   self.Pck_invoke_s[c_CM_ABYSS_RANKING_LEGIONS().invoke] = c_CM_ABYSS_RANKING_LEGIONS()
   self.Pck_invoke_s[c_CM_DELETE_ITEM().invoke] = c_CM_DELETE_ITEM()
   self.Pck_invoke_s[c_CM_SUMMON_COMMAND().invoke] = c_CM_SUMMON_COMMAND()
   self.Pck_invoke_s[c_CM_PRIVATE_STORE().invoke] = c_CM_PRIVATE_STORE()
   self.Pck_invoke_s[c_CM_PRIVATE_STORE_NAME().invoke] = c_CM_PRIVATE_STORE_NAME()
   self.Pck_invoke_s[c_CM_BROKER_REGISTERED().invoke] = c_CM_BROKER_REGISTERED()
   self.Pck_invoke_s[c_CM_BUY_BROKER_ITEM().invoke] = c_CM_BUY_BROKER_ITEM()
   self.Pck_invoke_s[c_CM_BROKER_LIST().invoke] = c_CM_BROKER_LIST()
   self.Pck_invoke_s[c_CM_BROKER_SEARCH().invoke] = c_CM_BROKER_SEARCH()
   self.Pck_invoke_s[c_CM_BROKER_SETTLE_LIST().invoke] = c_CM_BROKER_SETTLE_LIST()
   self.Pck_invoke_s[c_CM_BROKER_SETTLE_ACCOUNT().invoke] = c_CM_BROKER_SETTLE_ACCOUNT()
   self.Pck_invoke_s[c_CM_REGISTER_BROKER_ITEM().invoke] = c_CM_REGISTER_BROKER_ITEM()
   self.Pck_invoke_s[c_CM_BROKER_CANCEL_REGISTERED().invoke] = c_CM_BROKER_CANCEL_REGISTERED()
   self.Pck_invoke_s[c_CM_OPEN_MAIL_WINDOW().invoke] = c_CM_OPEN_MAIL_WINDOW()
   self.Pck_invoke_s[c_CM_READ_MAIL().invoke] = c_CM_READ_MAIL()
   self.Pck_invoke_s[c_CM_SEND_MAIL().invoke] = c_CM_SEND_MAIL()
   self.Pck_invoke_s[c_CM_DELETE_MAIL().invoke] = c_CM_DELETE_MAIL()
   self.Pck_invoke_s[c_CM_GET_MAIL_ATTACHMENT().invoke] = c_CM_GET_MAIL_ATTACHMENT()
   self.Pck_invoke_s[c_CM_CRAFT().invoke] = c_CM_CRAFT()
   self.Pck_invoke_s[c_CM_CLIENT_COMMAND_LOC().invoke] = c_CM_CLIENT_COMMAND_LOC()
   self.Pck_invoke_s[c_CM_TITLE_SET().invoke] = c_CM_TITLE_SET()
   self.Pck_invoke_s[c_CM_BREAK_WEAPONS().invoke] = c_CM_BREAK_WEAPONS()
   self.Pck_invoke_s[c_CM_EXCHANGE_CANCEL().invoke] = c_CM_EXCHANGE_CANCEL()
   self.Pck_invoke_s[c_CM_WINDSTREAM().invoke] = c_CM_WINDSTREAM()
   self.Pck_invoke_s[c_CM_EXCHANGE_LOCK().invoke] = c_CM_EXCHANGE_LOCK()
   self.Pck_invoke_s[c_CM_EXCHANGE_OK().invoke] = c_CM_EXCHANGE_OK()
   self.Pck_invoke_s[c_CM_MOTION().invoke] = c_CM_MOTION()
   self.Pck_invoke_s[c_CM_GROUP_RESPONSE().invoke] = c_CM_GROUP_RESPONSE()
   self.Pck_invoke_s[c_CM_EXIT_LOCATION().invoke] = c_CM_EXIT_LOCATION()
   self.Pck_invoke_s[c_CM_LEGION_MODIFY_EMBLEM().invoke] = c_CM_LEGION_MODIFY_EMBLEM()
   return self.Pck_invoke_s
 def get_Pck_invoke_s(self):
   self.Pck_invoke_c[s_SM_FRIEND_UPDATE().invoke] = s_SM_FRIEND_UPDATE()
   self.Pck_invoke_c[s_SM_PETITION().invoke] = s_SM_PETITION()
   self.Pck_invoke_c[s_SM_DELETE().invoke] = s_SM_DELETE()
   self.Pck_invoke_c[s_SM_LOGIN_QUEUE().invoke] = s_SM_LOGIN_QUEUE()
   self.Pck_invoke_c[s_SM_INVENTORY_INFO().invoke] = s_SM_INVENTORY_INFO()
   self.Pck_invoke_c[s_SM_SYSTEM_MESSAGE().invoke] = s_SM_SYSTEM_MESSAGE()
   self.Pck_invoke_c[s_SM_DELETE_ITEM().invoke] = s_SM_DELETE_ITEM()
   self.Pck_invoke_c[s_SM_INVENTORY_UPDATE().invoke] = s_SM_INVENTORY_UPDATE()
   self.Pck_invoke_c[s_SM_UI_SETTINGS().invoke] = s_SM_UI_SETTINGS()
   self.Pck_invoke_c[s_SM_UPDATE_ITEM().invoke] = s_SM_UPDATE_ITEM()
   self.Pck_invoke_c[s_SM_STANCE_STATE().invoke] = s_SM_STANCE_STATE()
   self.Pck_invoke_c[s_SM_GATHER_STATUS().invoke] = s_SM_GATHER_STATUS()
   self.Pck_invoke_c[s_SM_STATUPDATE_MP().invoke] = s_SM_STATUPDATE_MP()
   self.Pck_invoke_c[s_SM_STATUPDATE_HP().invoke] = s_SM_STATUPDATE_HP()
   self.Pck_invoke_c[s_SM_STATUPDATE_DP().invoke] = s_SM_STATUPDATE_DP()
   self.Pck_invoke_c[s_SM_STATUPDATE_EXP().invoke] = s_SM_STATUPDATE_EXP()
   self.Pck_invoke_c[s_SM_DP_INFO().invoke] = s_SM_DP_INFO()
   self.Pck_invoke_c[s_SM_LEGION_TABS().invoke] = s_SM_LEGION_TABS()
   self.Pck_invoke_c[s_SM_ENTER_WORLD_CHECK().invoke] = s_SM_ENTER_WORLD_CHECK()
   self.Pck_invoke_c[s_SM_QUESTION_WINDOW().invoke] = s_SM_QUESTION_WINDOW()
   self.Pck_invoke_c[s_SM_SKILL_COOLDOWN().invoke] = s_SM_SKILL_COOLDOWN()
   self.Pck_invoke_c[s_SM_DIALOG_WINDOW().invoke] = s_SM_DIALOG_WINDOW()
   self.Pck_invoke_c[s_SM_SELL_ITEM().invoke] = s_SM_SELL_ITEM()
   self.Pck_invoke_c[s_SM_WEATHER().invoke] = s_SM_WEATHER()
   self.Pck_invoke_c[s_SM_VIEW_PLAYER_DETAILS().invoke] = s_SM_VIEW_PLAYER_DETAILS()
   self.Pck_invoke_c[s_SM_UPDATE_PLAYER_APPEARANCE().invoke] = s_SM_UPDATE_PLAYER_APPEARANCE()
   self.Pck_invoke_c[s_SM_GAME_TIME().invoke] = s_SM_GAME_TIME()
   self.Pck_invoke_c[s_SM_LOOKATOBJECT().invoke] = s_SM_LOOKATOBJECT()
   self.Pck_invoke_c[s_SM_TIME_CHECK().invoke] = s_SM_TIME_CHECK()
   self.Pck_invoke_c[s_SM_SKILL_CANCEL().invoke] = s_SM_SKILL_CANCEL()
   self.Pck_invoke_c[s_SM_TARGET_SELECTED().invoke] = s_SM_TARGET_SELECTED()
   self.Pck_invoke_c[s_SM_SKILL_LIST().invoke] = s_SM_SKILL_LIST()
   self.Pck_invoke_c[s_SM_SKILL_ACTIVATION().invoke] = s_SM_SKILL_ACTIVATION()
   self.Pck_invoke_c[s_SM_STIGMA_SKILL_REMOVE().invoke] = s_SM_STIGMA_SKILL_REMOVE()
   self.Pck_invoke_c[s_SM_ABNORMAL_EFFECT().invoke] = s_SM_ABNORMAL_EFFECT()
   self.Pck_invoke_c[s_SM_ABNORMAL_STATE().invoke] = s_SM_ABNORMAL_STATE()
   self.Pck_invoke_c[s_SM_FRIEND_RESPONSE().invoke] = s_SM_FRIEND_RESPONSE()
   self.Pck_invoke_c[s_SM_BLOCK_RESPONSE().invoke] = s_SM_BLOCK_RESPONSE()
   self.Pck_invoke_c[s_SM_FRIEND_NOTIFY().invoke] = s_SM_FRIEND_NOTIFY()
   self.Pck_invoke_c[s_SM_VERSION_CHECK().invoke] = s_SM_VERSION_CHECK()
   self.Pck_invoke_c[s_SM_CHAT_INIT().invoke] = s_SM_CHAT_INIT()
   self.Pck_invoke_c[s_SM_CHANNEL_INFO().invoke] = s_SM_CHANNEL_INFO()
   self.Pck_invoke_c[s_SM_MACRO_RESULT().invoke] = s_SM_MACRO_RESULT()
   self.Pck_invoke_c[s_SM_MACRO_LIST().invoke] = s_SM_MACRO_LIST()
   self.Pck_invoke_c[s_SM_NICKNAME_CHECK_RESPONSE().invoke] = s_SM_NICKNAME_CHECK_RESPONSE()
   self.Pck_invoke_c[s_SM_RIFT_STATUS().invoke] = s_SM_RIFT_STATUS()
   self.Pck_invoke_c[s_SM_ABYSS_RANK().invoke] = s_SM_ABYSS_RANK()
   self.Pck_invoke_c[s_SM_RECIPE_DELETE().invoke] = s_SM_RECIPE_DELETE()
   self.Pck_invoke_c[s_SM_LEARN_RECIPE().invoke] = s_SM_LEARN_RECIPE()
   self.Pck_invoke_c[s_SM_LEGION_UPDATE_NICKNAME().invoke] = s_SM_LEGION_UPDATE_NICKNAME()
   self.Pck_invoke_c[s_SM_PLASTIC_SURGERY().invoke] = s_SM_PLASTIC_SURGERY()
   self.Pck_invoke_c[s_SM_NAME_CHANGE().invoke] = s_SM_NAME_CHANGE()
   self.Pck_invoke_c[s_SM_GROUP_INFO().invoke] = s_SM_GROUP_INFO()
   self.Pck_invoke_c[s_SM_ABYSS_ARTIFACT_INFO().invoke] = s_SM_ABYSS_ARTIFACT_INFO()
   self.Pck_invoke_c[s_SM_PLAYER_STATE().invoke] = s_SM_PLAYER_STATE()
   self.Pck_invoke_c[s_SM_LEVEL_UPDATE().invoke] = s_SM_LEVEL_UPDATE()
   self.Pck_invoke_c[s_SM_KEY().invoke] = s_SM_KEY()
   self.Pck_invoke_c[s_SM_STARTED_QUEST_LIST().invoke] = s_SM_STARTED_QUEST_LIST()
   self.Pck_invoke_c[s_SM_EXCHANGE_REQUEST().invoke] = s_SM_EXCHANGE_REQUEST()
   self.Pck_invoke_c[s_SM_SUMMON_PANEL_REMOVE().invoke] = s_SM_SUMMON_PANEL_REMOVE()
   self.Pck_invoke_c[s_SM_EXCHANGE_ADD_ITEM().invoke] = s_SM_EXCHANGE_ADD_ITEM()
   self.Pck_invoke_c[s_SM_EXCHANGE_CONFIRMATION().invoke] = s_SM_EXCHANGE_CONFIRMATION()
   self.Pck_invoke_c[s_SM_EXCHANGE_ADD_KINAH().invoke] = s_SM_EXCHANGE_ADD_KINAH()
   self.Pck_invoke_c[s_SM_TARGET_UPDATE().invoke] = s_SM_TARGET_UPDATE()
   self.Pck_invoke_c[s_SM_LEGION_UPDATE_SELF_INTRO().invoke] = s_SM_LEGION_UPDATE_SELF_INTRO()
   self.Pck_invoke_c[s_SM_DREDGION_INSTANCE().invoke] = s_SM_DREDGION_INSTANCE()
   self.Pck_invoke_c[s_SM_INSTANCE_SCORE().invoke] = s_SM_INSTANCE_SCORE()
   self.Pck_invoke_c[s_SM_QUEST_LIST().invoke] = s_SM_QUEST_LIST()
   self.Pck_invoke_c[s_SM_PING_RESPONSE().invoke] = s_SM_PING_RESPONSE()
   self.Pck_invoke_c[s_SM_NEARBY_QUESTS().invoke] = s_SM_NEARBY_QUESTS()
   self.Pck_invoke_c[s_SM_UPDATE_NOTE().invoke] = s_SM_UPDATE_NOTE()
   self.Pck_invoke_c[s_SM_ITEM_COOLDOWN().invoke] = s_SM_ITEM_COOLDOWN()
   self.Pck_invoke_c[s_SM_PLAY_MOVIE().invoke] = s_SM_PLAY_MOVIE()
   self.Pck_invoke_c[s_SM_LEGION_INFO().invoke] = s_SM_LEGION_INFO()
   self.Pck_invoke_c[s_SM_LEGION_LEAVE_MEMBER().invoke] = s_SM_LEGION_LEAVE_MEMBER()
   self.Pck_invoke_c[s_SM_LEGION_ADD_MEMBER().invoke] = s_SM_LEGION_ADD_MEMBER()
   self.Pck_invoke_c[s_SM_LEGION_UPDATE_TITLE().invoke] = s_SM_LEGION_UPDATE_TITLE()
   self.Pck_invoke_c[s_SM_LEGION_UPDATE_MEMBER().invoke] = s_SM_LEGION_UPDATE_MEMBER()
   self.Pck_invoke_c[s_SM_MOTION().invoke] = s_SM_MOTION()
   self.Pck_invoke_c[s_SM_SUMMON_OWNER_REMOVE().invoke] = s_SM_SUMMON_OWNER_REMOVE()
   self.Pck_invoke_c[s_SM_SUMMON_PANEL().invoke] = s_SM_SUMMON_PANEL()
   self.Pck_invoke_c[s_SM_SUMMON_UPDATE().invoke] = s_SM_SUMMON_UPDATE()
   self.Pck_invoke_c[s_SM_LEGION_MEMBERLIST().invoke] = s_SM_LEGION_MEMBERLIST()
   self.Pck_invoke_c[s_SM_INGAMESHOP_BALANCE().invoke] = s_SM_INGAMESHOP_BALANCE()
   self.Pck_invoke_c[s_SM_TOLL_INFO().invoke] = s_SM_TOLL_INFO()
   self.Pck_invoke_c[s_SM_SUMMON_USESKILL().invoke] = s_SM_SUMMON_USESKILL()
   self.Pck_invoke_c[s_SM_FRIEND_LIST().invoke] = s_SM_FRIEND_LIST()
   self.Pck_invoke_c[s_SM_PRIVATE_STORE().invoke] = s_SM_PRIVATE_STORE()
   self.Pck_invoke_c[s_SM_MAY_LOGIN_INTO_GAME().invoke] = s_SM_MAY_LOGIN_INTO_GAME()
   self.Pck_invoke_c[s_SM_ACADEMY_BOOTCAMP_STAGE().invoke] = s_SM_ACADEMY_BOOTCAMP_STAGE()
   self.Pck_invoke_c[s_SM_ABYSS_RANKING_LEGIONS().invoke] = s_SM_ABYSS_RANKING_LEGIONS()
   self.Pck_invoke_c[s_SM_PONG().invoke] = s_SM_PONG()
   self.Pck_invoke_c[s_SM_INSTANCE_COOLDOWN().invoke] = s_SM_INSTANCE_COOLDOWN()
   self.Pck_invoke_c[s_SM_KISK_UPDATE().invoke] = s_SM_KISK_UPDATE()
   self.Pck_invoke_c[s_SM_PRIVATE_STORE_NAME().invoke] = s_SM_PRIVATE_STORE_NAME()
   self.Pck_invoke_c[s_SM_CRAFT_ANIMATION().invoke] = s_SM_CRAFT_ANIMATION()
   self.Pck_invoke_c[s_SM_ASCENSION_MORPH().invoke] = s_SM_ASCENSION_MORPH()
   self.Pck_invoke_c[s_SM_CUSTOM_SETTINGS().invoke] = s_SM_CUSTOM_SETTINGS()
   self.Pck_invoke_c[s_SM_ITEM_USAGE_ANIMATION().invoke] = s_SM_ITEM_USAGE_ANIMATION()
   self.Pck_invoke_c[s_SM_QUESTIONNAIRE().invoke] = s_SM_QUESTIONNAIRE()
   self.Pck_invoke_c[s_SM_RESURRECT().invoke] = s_SM_RESURRECT()
   self.Pck_invoke_c[s_SM_DIE().invoke] = s_SM_DIE()
   self.Pck_invoke_c[s_SM_WINDSTREAM_LOCATIONS().invoke] = s_SM_WINDSTREAM_LOCATIONS()
   self.Pck_invoke_c[s_SM_WINDSTREAM().invoke] = s_SM_WINDSTREAM()
   self.Pck_invoke_c[s_SM_WAREHOUSE_INFO().invoke] = s_SM_WAREHOUSE_INFO()
   self.Pck_invoke_c[s_SM_REPURCHASE().invoke] = s_SM_REPURCHASE()
   self.Pck_invoke_c[s_SM_DELETE_WAREHOUSE_ITEM().invoke] = s_SM_DELETE_WAREHOUSE_ITEM()
   self.Pck_invoke_c[s_SM_WAREHOUSE_UPDATE().invoke] = s_SM_WAREHOUSE_UPDATE()
   self.Pck_invoke_c[s_SM_IN_GAME_SHOP_CATEGORY_LIST().invoke] = s_SM_IN_GAME_SHOP_CATEGORY_LIST()
   self.Pck_invoke_c[s_SM_UPDATE_WAREHOUSE_ITEM().invoke] = s_SM_UPDATE_WAREHOUSE_ITEM()
   self.Pck_invoke_c[s_SM_IN_GAME_SHOP_ITEM().invoke] = s_SM_IN_GAME_SHOP_ITEM()
   self.Pck_invoke_c[s_SM_IN_GAME_SHOP_LIST().invoke] = s_SM_IN_GAME_SHOP_LIST()
   self.Pck_invoke_c[s_SM_TITLE_LIST().invoke] = s_SM_TITLE_LIST()
   self.Pck_invoke_c[s_SM_LEGION_EMBLEM_SEND().invoke] = s_SM_LEGION_EMBLEM_SEND()
   self.Pck_invoke_c[s_SM_LEGION_EMBLEM().invoke] = s_SM_LEGION_EMBLEM()
   self.Pck_invoke_c[s_SM_LEGION_UPDATE_EMBLEM().invoke] = s_SM_LEGION_UPDATE_EMBLEM()
   self.Pck_invoke_c[s_SM_SIEGE_AETHERIC_FIELDS().invoke] = s_SM_SIEGE_AETHERIC_FIELDS()
   self.Pck_invoke_c[s_SM_ABYSS_ARTIFACT_INFO3().invoke] = s_SM_ABYSS_ARTIFACT_INFO3()
   self.Pck_invoke_c[s_SM_BLOCK_LIST().invoke] = s_SM_BLOCK_LIST()
   self.Pck_invoke_c[s_SM_TELEPORT_MAP().invoke] = s_SM_TELEPORT_MAP()
   self.Pck_invoke_c[s_SM_USE_OBJECT().invoke] = s_SM_USE_OBJECT()
   self.Pck_invoke_c[s_SM_CHARACTER_LIST().invoke] = s_SM_CHARACTER_LIST()
   self.Pck_invoke_c[s_SM_L2AUTH_LOGIN_CHECK().invoke] = s_SM_L2AUTH_LOGIN_CHECK()
   self.Pck_invoke_c[s_SM_DELETE_CHARACTER().invoke] = s_SM_DELETE_CHARACTER()
   self.Pck_invoke_c[s_SM_RESTORE_CHARACTER().invoke] = s_SM_RESTORE_CHARACTER()
   self.Pck_invoke_c[s_SM_LOOT_ITEMLIST().invoke] = s_SM_LOOT_ITEMLIST()
   self.Pck_invoke_c[s_SM_LOOT_STATUS().invoke] = s_SM_LOOT_STATUS()
   self.Pck_invoke_c[s_SM_MANTRA_EFFECT().invoke] = s_SM_MANTRA_EFFECT()
   self.Pck_invoke_c[s_SM_RECIPE_LIST().invoke] = s_SM_RECIPE_LIST()
   self.Pck_invoke_c[s_SM_SIEGE_LOCATION_INFO().invoke] = s_SM_SIEGE_LOCATION_INFO()
   self.Pck_invoke_c[s_SM_FLY_TIME().invoke] = s_SM_FLY_TIME()
   self.Pck_invoke_c[s_SM_FORTRESS_INFO().invoke] = s_SM_FORTRESS_INFO()
   self.Pck_invoke_c[s_SM_LEAVE_GROUP_MEMBER().invoke] = s_SM_LEAVE_GROUP_MEMBER()
   self.Pck_invoke_c[s_SM_ALLIANCE_READY_CHECK().invoke] = s_SM_ALLIANCE_READY_CHECK()
   self.Pck_invoke_c[s_SM_SHOW_BRAND().invoke] = s_SM_SHOW_BRAND()
   self.Pck_invoke_c[s_SM_PRICES().invoke] = s_SM_PRICES()
   self.Pck_invoke_c[s_SM_TRADELIST().invoke] = s_SM_TRADELIST()
   self.Pck_invoke_c[s_SM_RECONNECT_KEY().invoke] = s_SM_RECONNECT_KEY()
   self.Pck_invoke_c[s_SM_ABYSS_RANK_UPDATE().invoke] = s_SM_ABYSS_RANK_UPDATE()
   self.Pck_invoke_c[s_SM_GROUP_LOOT().invoke] = s_SM_GROUP_LOOT()
   self.Pck_invoke_c[s_SM_PLAYER_ID().invoke] = s_SM_PLAYER_ID()
   self.Pck_invoke_c[s_SM_STAGE_STEP_STATUS().invoke] = s_SM_STAGE_STEP_STATUS()
   self.Pck_invoke_c[s_SM_LEGION_EMBLEM_SEND().invoke] = s_SM_LEGION_EMBLEM_SEND()
   self.Pck_invoke_c[s_SM_ABYSS_ARTIFACT_INFO2().invoke] = s_SM_ABYSS_ARTIFACT_INFO2()
   return self.Pck_invoke_c
