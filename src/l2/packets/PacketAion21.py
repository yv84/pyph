import struct
#--------------------------------------------------------------------------#00
class s_SM_STATUPDATE_HP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('currentHp', 'i4')
              , ('maxHp', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01
class s_SM_STATUPDATE_DP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('currentDp', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#02
class s_SM_CHANNEL_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x02'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('currentChannel', 'i4')
              , ('instanceCount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#04
class s_SM_MACRO_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x04'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
              , ('1', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#05
class s_SM_CHAT_INIT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x05'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('token', 'i4')
              , ('256', '|S256')
                  ]
    return dtype
#--------------------------------------------------------------------------#06
class s_SM_NICKNAME_CHECK_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x06'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('value', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#07
class s_SM_MACRO_RESULT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x07'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('value', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0B
class s_SM_RIFT_ANNOUNCE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0C
class s_SM_PETITION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0D
class s_SM_RECIPE_DELETE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('recipeId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0E
class s_SM_LEARN_RECIPE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('recipeId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0F
class s_SM_FRIEND_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#10
class s_SM_FORTRESS_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x10'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('locationId', 'i4')
              , ('value', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#14
class s_SM_LOGIN_QUEUE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x14'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('waitingPosition', 'i4')
              , ('waitingTime', 'i4')
              , ('waitingCount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#15
class s_SM_DELETE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x15'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
              , ('time', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#1D
class s_SM_UI_SETTINGS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('type', 'i2')
              , ('unk', 'i1')
              , ('256', '|S256')
              , ('U', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#16
class s_SM_SYSTEM_MESSAGE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x16'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i2')
              , ('npcObjId', 'i4')
              , ('msgId', 'i4')
              , ('length', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#18
class s_SM_INVENTORY_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x18'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('25', 'i2')
              , ('size', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#19
class s_SM_INVENTORY_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x19'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('1', 'i1')
              , ('CUBE', 'i1')
              , ('0_0', 'i1')
              , ('0_1', 'i1')
              , ('sizeValue', 'i2')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('OID', 'i4')
              , ('TemplateId', 'i4')
              , ('36', 'i2')
              , ('NameId', 'i4')
              , ('0_0', 'i2')
              , ('22', 'i2')
              , ('0_1', 'i1')
              , ('ItemMask', 'i2')
              , ('ItemCount', 'i8')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('EquipmentSlot', 'i2')
              , ('0_4', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 5
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#1B
class s_SM_DELETE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('itemUniqueId', 'i4')
              , ('unk', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#20
class s_SM_GATHER_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x20'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#21
class s_SM_GATHER_STATUS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x21'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playerOID', 'i4')
              , ('gatherableOID', 'i4')
              , ('unk', 'i2')
              , ('status', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#23
class s_SM_STATUPDATE_MP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x23'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('currentMp', 'i4')
              , ('maxMp', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#26
class s_SM_DP_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x26'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playerOID', 'i4')
              , ('currentDp', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#28
class s_SM_LEGION_UPDATE_NICKNAME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x28'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playerOID', 'i4')
              , ('newNickname', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#27
class s_SM_STATUPDATE_EXP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x27'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('currentExp', 'i8')
              , ('recoverableExp', 'i8')
              , ('maxExp', 'i8')
              , ('curBoostExp', 'i8')
              , ('maxBoostExp', 'i8')
                  ]
    return dtype
#--------------------------------------------------------------------------#2A
class s_SM_ENTER_WORLD_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk_0', 'i1')
              , ('unk_1', 'i1')
              , ('unk_2', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#2B
class s_SM_LEGION_TABS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#33
class s_SM_QUESTION_WINDOW():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x33'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#3B
class s_SM_DIALOG_WINDOW():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('dialogID', 'i2')
              , ('questId', 'i4')
              , ('0', 'i2')
              , ('2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#3D
class s_SM_SELL_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('sellPercentage', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#3E
class s_SM_VIEW_PLAYER_DETAILS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3E'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('unk_0', 'i1')
              , ('sizeValue', 'i1')
              , ('unk_1', 'i1')
                  ]+ list(self.f_size()) +[
               ('unk_2', 'i1')
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('unk_0', 'i4')
              , ('TemplateId', 'i4')
              , ('unk_1', 'i2')
              , ('NameId', 'i4')
              , ('unk_2', 'i2')
              , ('unk_3', 'i2')
              , ('unk_4', 'i1')
              , ('unk_5', 'i1')
              , ('unk_6', 'i2')
              , ('unk_7', 'i2')
              , ('unk_8', 'i1')
              , ('unk_9', 'i2')
              , ('unk_10', 'i1')
              , ('EquipmentSlot', 'i2')
              , ('unk_11', 'i2')
              , ('unk_12', 'i1')
              , ('unk_13', 'i2')
              , ('ItemCount', 'i2')
              , ('unk_14', 'i4')
              , ('unk_15', 'i4')
              , ('unk_16', 'i4')
              , ('unk_17', 'i4')
              , ('unk_18', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 7
   p = self.pck[i:i+1]
   count = struct.unpack('b', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 3
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#40
class s_SM_WEATHER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x40'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('weatherCode', 'i2')
              , ('unk', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#43
class s_SM_UPDATE_PLAYER_APPEARANCE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x43'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playerId', 'i4')
              , ('maskValue', 'i2')
                  ]+ list(self.f_mask()) +[
                  ]
    return dtype
  def f_mask(self):
    for i in range(self.It.__next__()):
      dtype = ('mask_' + str(i) , [
               ('TemplateId', 'i4')
              , ('itemId', 'i4')
              , ('itemColor', 'i4')
              , ('0', 'i2')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
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
#--------------------------------------------------------------------------#44
class s_SM_TIME_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x44'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('time', 'i4')
              , ('NanoTime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#45
class s_SM_GAME_TIME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x45'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('GameTime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#46
class s_SM_Target_SELECTED():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x46'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('level', 'i2')
              , ('maxHp', 'i4')
              , ('currentHp', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#47
class s_SM_LOOKATOBJECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x47'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
              , ('TargetOID', 'i4')
              , ('heading', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#49
class s_SM_SKILL_CANCEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x49'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
              , ('SkillId', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#4A
class s_SM_STIGMA_SKILL_REMOVE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('SkillId', 'i2')
              , ('1_0', 'i1')
              , ('1_1', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#4B
class s_SM_SKILL_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4B'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('sizeValue', 'i2')
                  ]+ list(self.f_size()) +[
               ('messageId', 'i4')
              , ('36', 'i2')
              , ('skillNameId', 'i4')
              , ('unk', 'i2')
              , ('skillLvl', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('SkillId', 'i2')
              , ('SkillLevel', 'i2')
              , ('unk_0', 'i1')
              , ('ExtraLvl', 'i1')
              , ('unk_1', 'i4')
              , ('isStigma', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
   i += 2
   for _ in range(count):
      i += 11
   i += 12
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
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
      i += 6
   i += 4
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#4D
class s_SM_SKILL_ACTIVATION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('SkillId', 'i2')
              , ('unk', 'i4')
              , ('isActive', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#4E
class s_SM_ABNORMAL_STATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4E'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('abnormals', 'i4')
              , ('sizeValue', 'i2')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('EffectorId', 'i4')
              , ('SkillId', 'i2')
              , ('SkillLevel', 'i1')
              , ('TargetSlot', 'i1')
              , ('ElapsedTime', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
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
#--------------------------------------------------------------------------#4F
class s_SM_SKILL_COOLDOWN():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#51
class s_SM_ABNORMAL_EFFECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x51'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('effectedId', 'i4')
              , ('unk_0', 'i1')
              , ('unk_1', 'i4')
              , ('abnormals', 'i4')
              , ('effectsValue', 'i2')
                  ]+ list(self.f_effects()) +[
                  ]
    return dtype
  def f_effects(self):
    for i in range(self.It.__next__()):
      dtype = ('effects_' + str(i) , [
               ('skillId', 'i2')
              , ('skillLevel', 'i1')
              , ('TargetSlot', 'i1')
              , ('elapsedTime', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 15
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 5
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#55
class s_SM_FORTRESS_STATUS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x55'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#57
class s_SM_NAME_CHANGE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x57'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk_0', 'i4')
              , ('unk_1', 'i4')
              , ('playerOID', 'i4')
              , ('oldName', '|S'+str(self.It.__next__()) )
              , ('newName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 14
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
#--------------------------------------------------------------------------#59
class s_SM_GROUP_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x59'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('groupid', 'i4')
              , ('leaderid', 'i4')
              , ('lootruletype', 'i4')
              , ('autodistribution', 'i4')
              , ('common_item_above', 'i4')
              , ('superior_item_above', 'i4')
              , ('heroic_item_above', 'i4')
              , ('fabled_item_above', 'i4')
              , ('ethernal_item_above', 'i4')
              , ('over_ethernal', 'i4')
              , ('over_over_ethernal', 'i4')
              , ('unk_0', 'i4')
              , ('unk_1', 'i2')
              , ('unk_2', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#5F
class s_SM_ABYSS_ARTIFACT_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5F'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('ArtifactCountValue', 'i2')
                  ]+ list(self.f_ArtifactCount()) +[
                  ]
    return dtype
  def f_ArtifactCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ArtifactCount_' + str(i) , [
               ('LocationId', 'i4')
              , ('unk_0', 'i4')
              , ('unk_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#61
class s_SM_QUIT_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x61'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('edit_mode', 'i4')
              , ('unk', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#63
class s_SM_PLAYER_STATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x63'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playerOID', 'i4')
              , ('visualState', 'i1')
              , ('seeState', 'i1')
              , ('unk', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#64
class s_SM_STargetTED_QUEST_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x64'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('1', 'i2')
              , ('sizeValue', 'i2')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('QuestId', 'i2')
              , ('unk_0', 'i2')
              , ('Status', 'i1')
              , ('QuestVars', 'i4')
              , ('unk_1', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
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
#--------------------------------------------------------------------------#65
class s_SM_LEVEL_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x65'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('effect', 'i2')
              , ('level', 'i2')
              , ('unk', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#66
class s_SM_SUMMON_PANEL_REMOVE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x66'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#67
class s_SM_KEY():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x67'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('key', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#68
class s_SM_EXCHANGE_ADD_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x68'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#69
class s_SM_EXCHANGE_REQUEST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x69'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('receiver', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#6A
class s_SM_EXCHANGE_ADD_KINAH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('action', 'i1')
              , ('itemCount', 'i4')
              , ('unk', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6C
class s_SM_EMOTION_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6C'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i1')
              , ('sizeValue', 'i2')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('unk_0', 'i4')
              , ('unk_1', 'i2')
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
#--------------------------------------------------------------------------#6D
class s_SM_EXCHANGE_CONFIRMATION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#6E
class s_SM_Target_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playerOID', 'i4')
              , ('TargetOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#70
class s_SM_PLASTIC_SURGERY():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x70'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#74
class s_SM_LEGION_UPDATE_SELF_INTRO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x74'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#78
class s_SM_QUEST_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x78'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#AB
class s_SM_RIFT_STATUS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#7C
class s_SM_NEARBY_QUESTS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7C'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i1')
              , ('sizeValue', 'i2')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('id', 'i2')
              , ('checkLevelRequirement', 'i2')
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
#--------------------------------------------------------------------------#7F
class s_SM_PING_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#81
class s_SM_CUBE_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x81'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#82
class s_SM_PET():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x82'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#84
class s_SM_ITEM_COOLDOWN():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x84'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#86
class s_SM_PLAY_MOVIE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x86'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#87
class s_SM_UPDATE_NOTE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x87'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#8C
class s_SM_LEGION_ADD_MEMBER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#8D
class s_SM_LEGION_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#90
class s_SM_LEGION_UPDATE_TITLE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x90'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#8E
class s_SM_LEGION_UPDATE_MEMBER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8E'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
              , ('LegionMember_RankId', 'i1')
              , ('ClassId', 'i1')
              , ('Level', 'i1')
              , ('MapId', 'i4')
              , ('Online', 'i1')
              , ('LastOnline', 'i4')
              , ('msgId', 'i4')
              , ('text', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 22
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 9
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#8F
class s_SM_LEGION_LEAVE_MEMBER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#96
class s_SM_SUMMON_PANEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x96'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#98
class s_SM_SUMMON_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x98'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#99
class s_SM_SUMMON_OWNER_REMOVE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x99'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#9A
class s_SM_LEGION_MEMBERLIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#9E
class s_SM_MAIL_SERVICE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#A0
class s_SM_WINDSTREAM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#A1
class s_SM_SUMMON_USESKILL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#A5
class s_SM_PRIVATE_STORE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#A3
class s_SM_FRIEND_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#A4
class s_SM_GROUP_LOOT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#A6
class s_SM_MAY_LOGIN_INTO_GAME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A7
class s_SM_ABYSS_RANK_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#A8
class s_SM_ABYSS_RANKING_LEGIONS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#A9
class s_SM_ABYSS_RANKING_PLAYERS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#AA
class s_SM_PLAYER_ID():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#AF
class s_SM_KISK_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#AD
class s_SM_PONG():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('pong', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#AE
class s_SM_PRIVATE_STORE_NAME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#B1
class s_SM_BROKER_ITEMS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#B3
class s_SM_CRAFT_ANIMATION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#B4
class s_SM_ITEM_USAGE_ANIMATION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playerOID_0', 'i4')
              , ('playerOID_1', 'i4')
              , ('itemOID', 'i4')
              , ('ItemID', 'i4')
              , ('time', 'i4')
              , ('end', 'i1')
              , ('1', 'i1')
              , ('0', 'i1')
              , ('unk', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B5
class s_SM_ASCENSION_MORPH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#B6
class s_SM_DUEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#B7
class s_SM_CUSTOM_SETTINGS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#BC
class s_SM_QUESTIONNAIRE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#BE
class s_SM_DIE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#C1
class s_SM_RESURRECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#C3
class s_SM_WINDSTREAM_ANNOUNCE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#C4
class s_SM_REPURCHASE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#C6
class s_SM_WAREHOUSE_UPDATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#C7
class s_SM_WAREHOUSE_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#C8
class s_SM_UPDATE_WAREHOUSE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#C9
class s_SM_DELETE_WAREHOUSE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#CE
class s_SM_CHARACTER_SELECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('messaype', 'i2')
              , ('CheckWrongCount', 'i1')
              , ('wrongCount', 'i4')
              , ('PASSKEY_WRONG_MAXCOUNT', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D2
class s_SM_LEGION_EMBLEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D4
class s_SM_LEGION_UPDATE_EMBLEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D5
class s_SM_LEGION_EMBLEM_SEND():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
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
              , ('256', '|S256')
                  ]
    return dtype
#--------------------------------------------------------------------------#D9
class s_SM_ABYSS_ARTIFACT_INFO2():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD9'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('sizeValue', 'i2')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('LocationId', 'i4')
              , ('0', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#DB
class s_SM_ABYSS_ARTIFACT_INFO3():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDB'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('sizeValue', 'i2')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('LocationId', 'i4')
              , ('0_0', 'i4')
              , ('0_1', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#DD
class s_SM_BLOCK_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDD'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playerName', '|S'+str(self.It.__next__()) )
              , ('code', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#DE
class s_SM_FRIEND_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDE'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('player', '|S'+str(self.It.__next__()) )
              , ('code', 'i1')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#DF
class s_SM_BLOCK_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDF'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('sizeValue', 'i2')
              , ('0', 'i1')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('Name', '|S'+str(self.It.__next__()) )
              , ('Reason', '|S'+str(self.It.__next__()) )
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
   i += 3
   for _ in range(count):
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
  def parse_list(self):
   i = 1
   i += 1
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
   i += 2
   for _ in range(count):
      s_len = len(self.lst[i])
      yield s_len
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 1
#--------------------------------------------------------------------------#E0
class s_SM_FRIEND_NOTIFY():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE0'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('code', 'i1')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#E2
class s_SM_USE_OBJECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playerOID', 'i4')
              , ('TargetOID', 'i4')
              , ('time', 'i4')
              , ('actionType', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#E3
class s_SM_TELEPORT_MAP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('TeleportId', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#E4
class s_SM_L2AUTH_LOGIN_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE4'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('result', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#E8
class s_SM_RESTORE_CHARACTER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('success', 'i4')
              , ('chaOid', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#E9
class s_SM_DELETE_CHARACTER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('0', 'i4')
              , ('playerOID', 'i4')
              , ('deletionTime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#EA
class s_SM_LOOT_STATUS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
              , ('state', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#EC
class s_SM_RECIPE_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEC'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('CountValue', 'i2')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('ID', 'i4')
              , ('0', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#ED
class s_SM_LOOT_ITEMLIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xED'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk_0', 'i4')
              , ('unk_1', 'i2')
              , ('unk_2', 'i4')
              , ('unk_3', 'i2')
              , ('unk_4', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#EE
class s_SM_SIEGE_LOCATION_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEE'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('infoType', 'i1')
              , ('sizeValue', 'i2')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('LocationId', 'i4')
              , ('legionId', 'i4')
              , ('emblemId', 'i4')
              , ('0xFF', 'i1')
              , ('emblemColor_r', 'i1')
              , ('emblemColor_g', 'i1')
              , ('emblemColor_b', 'i1')
              , ('RaceId', 'i1')
              , ('isVulnerable', 'i1')
              , ('isCanTeleport', 'i1')
              , ('NextState', 'i1')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
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
#--------------------------------------------------------------------------#EF
class s_SM_MANTRA_EFFECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('0', 'i4')
              , ('playerOID', 'i4')
              , ('subEffectId', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#F2
class s_SM_ALLIANCE_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#F5
class s_SM_ALLIANCE_MEMBER_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#F3
class s_SM_FLY_TIME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('currentFp', 'i4')
              , ('maxFp', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F4
class s_SM_LEAVE_GROUP_MEMBER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#F6
class s_SM_SHOW_BRAND():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#F9
class s_SM_ALLIANCE_READY_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FA
class s_SM_TRADELIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFA'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('Category', 'i1')
              , ('buyPriceModifier', 'i4')
              , ('CountValue', 'i2')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('tradeTablId', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 11
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
#--------------------------------------------------------------------------#FB
class s_SM_PRICES():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FC
class s_SM_RECONNECT_KEY():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FF
class s_SM_VERSION_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk_0', 'i1')
              , ('GAMESERVER_ID', 'i1')
              , ('unk_1', 'i4')
              , ('unk_2', 'i4')
              , ('unk_3', 'i4')
              , ('unk_4', 'i4')
              , ('unk_5', 'i4')
              , ('unk_6', 'i1')
              , ('SERVER_COUNTRY_CODE', 'i1')
              , ('unk_7', 'i1')
              , ('SERVER_MODE', 'i1')
              , ('currentTimeMillis', 'i4')
              , ('unk_8', 'i2')
              , ('unk_9', 'i2')
              , ('unk_10', 'i2')
              , ('unk_11', 'i2')
              , ('unk_12', 'i1')
              , ('unk_13', 'i1')
              , ('unk_14', 'i1')
              , ('unk_15', 'i1')
              , ('unk_16', 'i1')
              , ('Ip_0', 'i1')
              , ('Ip_1', 'i1')
              , ('Ip_2', 'i1')
              , ('Ip_3', 'i1')
              , ('Port', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#99999
class s_SM_CUSTOM_PACKET():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#02
class c_CM_GROUP_DISTRIBUTION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x02'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('amount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#04
class c_CM_SHOW_FRIENDLIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x04'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#05
class c_CM_FRIEND_ADD():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x05'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#09
class c_CM_CLIENT_COMMAND_ROLL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x09'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('maxRoll', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0A
class c_CM_VIEW_PLAYER_DETAILS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0D
class c_CM_PING_REQUEST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#0E
class c_CM_PLAYER_STATUS_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('status', 'i1')
              , ('playerOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0F
class c_CM_INVITE_TO_GROUP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0F'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('inviteType', 'i1')
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
#--------------------------------------------------------------------------#12
class c_CM_ABYSS_RANKING_PLAYERS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x12'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('raceId', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#13
class c_CM_MAC_ADDRESS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x13'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('23', '|S23')
              , ('unk_0', '|S'+str(self.It.__next__()) )
              , ('unk_1', '|S'+str(self.It.__next__()) )
              , ('unk', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 25
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
#--------------------------------------------------------------------------#15
class c_CM_REPORT_PLAYER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x15'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('1', '|S1')
              , ('player', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#16
class c_CM_GROUP_LOOT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x16'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
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
#--------------------------------------------------------------------------#17
class c_CM_DISTRIBUTION_SETTINGS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x17'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i4')
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
#--------------------------------------------------------------------------#18
class c_CM_MAY_LOGIN_INTO_GAME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x18'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#1B
class c_CM_SHOW_BRAND():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('brandId', 'i4')
              , ('TargetOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1D
class c_CM_RECONNECT_AUTH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#1E
class c_CM_MACRO_DELETE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('macroPosition', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#1F
class c_CM_CHECK_NICKNAME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1F'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('nick', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#21
class c_CM_BLOCK_SET_REASON():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x21'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetName', '|S'+str(self.It.__next__()) )
              , ('reason', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#24
class c_CM_FUSION_WEAPONS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x24'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('firstitemId', 'i4')
              , ('secondItemId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#25
class c_CM_BREAK_WEAPONS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x25'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i4')
              , ('weaponToBreakUniqueId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#28
class c_CM_SUMMON_EMOTION():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x28'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
              , ('emotionTypeId', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#29
class c_CM_SUMMON_ATTACK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x29'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('summonOID', 'i4')
              , ('TargetOID', 'i4')
              , ('unk_0', 'i1')
              , ('unk_1', 'i2')
              , ('unk_2', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#2A
class c_CM_SHOW_MAP():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#2B
class c_CM_NAME_CHANGE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2B'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('action', 'i1')
              , ('unk_0', 'i1')
              , ('unk_1', 'i2')
              , ('Id', 'i4')
              , ('newName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#2E
class c_CM_GROUP_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk_0', 'i4')
              , ('unk_1', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#32
class c_CM_MOVE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x32'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('source', 'i1')
              , ('destination', 'i1')
              , ('Slot', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#33
class c_CM_SPLIT_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x33'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('sourceItemOID', 'i4')
              , ('itemAmount', 'i4')
              , ('4', '|S4')
              , ('sourceStoraype', 'i1')
              , ('destinationItemOID', 'i4')
              , ('destinationStoraype', 'i1')
              , ('slotNum', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#35
class c_CM_PLAYER_SEARCH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x35'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('44', '|S44')
              , ('region', 'i4')
              , ('classMask', 'i4')
              , ('minLevel', 'i1')
              , ('maxLevel', 'i1')
              , ('lfgOnly', 'i1')
              , ('unk', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#36
class c_CM_DELETE_CHARACTER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x36'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playOk2', 'i4')
              , ('chaOid', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#37
class c_CM_RESTORE_CHARACTER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x37'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playOk2', 'i4')
              , ('chaOid', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#38
class c_CM_STargetT_LOOT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x38'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('action', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#39
class c_CM_LOOT_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x39'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('index', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#3A
class c_CM_TELEPORT_SELECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('locId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#3B
class c_CM_L2AUTH_LOGIN_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playOk2', 'i4')
              , ('playOk1', 'i4')
              , ('accountId', 'i4')
              , ('loginOk', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#3C
class c_CM_CHARACTER_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playOk2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#3D
class c_CM_CREATE_CHARACTER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#42
class c_CM_CHANGE_CHANNEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x42'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('channel', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#44
class c_CM_MAC_ADDRESS2():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x44'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
              , ('6', '|S6')
                  ]
    return dtype
#--------------------------------------------------------------------------#45
class c_CM_MACRO_CREATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x45'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('macroPosition', 'i1')
              , ('macroXML', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#46
class c_CM_SHOW_BLOCKLIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x46'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#47
class c_CM_REPLACE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x47'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('sourceStoraype', 'i1')
              , ('sourceItemOID', 'i4')
              , ('replaceStoraype', 'i1')
              , ('replaceItemOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#48
class c_CM_FRIEND_STATUS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x48'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('status', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#4C
class c_CM_BLOCK_ADD():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4C'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetName', '|S'+str(self.It.__next__()) )
              , ('reason', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#4D
class c_CM_BLOCK_DEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4D'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#4E
class c_CM_LEGION_UPLOAD_INFO():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('totalSize', 'i4')
              , ('unk', 'i1')
              , ('color_r', 'i1')
              , ('color_g', 'i1')
              , ('color_b', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#4F
class c_CM_LEGION_UPLOAD_EMBLEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('size', 'i4')
              , ('256', '|S256')
                  ]
    return dtype
#--------------------------------------------------------------------------#50
class c_CM_MAIL_SUMMON_ZEPHYR():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x50'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('value', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#62
class c_CM_CUSTOM_SETTINGS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x62'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('display', 'i2')
              , ('deny', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#66
class c_CM_ENTER_WORLD():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x66'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#67
class c_CM_LEVEL_READY():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x67'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#68
class c_CM_UI_SETTINGS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x68'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('settingsType', 'i1')
              , ('unk', 'i2')
              , ('size', 'i2')
              , ('256', '|S256')
                  ]
    return dtype
#--------------------------------------------------------------------------#69
class c_CM_OBJECT_SEARCH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x69'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('npcId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6A
class c_CM_MAY_QUIT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#6B
class c_CM_REVIVE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('RessType', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#6D
class c_CM_CHARACTER_EDIT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#6E
class c_CM_VERSION_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk1', 'i4')
              , ('unk2', 'i4')
              , ('unk3', 'i4')
              , ('unk4', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#70
class c_CM_DISCONNECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x70'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#71
class c_CM_QUIT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x71'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('logout', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#95
class c_CM_EXCHANGE_REQUEST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x95'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#96
class c_CM_LEGION_EMBLEM_SEND():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x96'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('legionId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#98
class c_CM_SET_NOTE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x98'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('note', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#99
class c_CM_LEGION_MODIFY_EMBLEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x99'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('legionId', 'i4')
              , ('emblemVer', 'i2')
              , ('unk', 'i1')
              , ('red', 'i1')
              , ('green', 'i1')
              , ('blue', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#9A
class c_CM_SHOW_DIALOG():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('NpcID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#9B
class c_CM_CLOSE_DIALOG():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#9C
class c_CM_DIALOG_SELECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('dialogId', 'i2')
              , ('selectableReward', 'i2')
              , ('lastPage', 'i2')
              , ('questId', 'i4')
              , ('unk', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#9D
class c_CM_LEGION_TABS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('page', 'i4')
              , ('tab', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#A0
class c_CM_QUESTION_RESPONSE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#A1
class c_CM_BUY_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA1'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
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
               ('itemId', 'i4')
              , ('count', 'i4')
              , ('unk2', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 3
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#AA
class c_CM_EXCHANGE_OK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#AB
class c_CM_EXCHANGE_CANCEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#AC
class c_CM_WINDSTREAM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('teleportId', 'i4')
              , ('distance', 'i4')
              , ('validatePos', 'i2')
              , ('unk', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#AE
class c_CM_EXCHANGE_ADD_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('itemOID', 'i4')
              , ('itemCount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B0
class c_CM_EXCHANGE_ADD_KINAH():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('itemCount', 'i4')
              , ('unk', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B1
class c_CM_EXCHANGE_LOCK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#B2
class c_CM_CHAT_MESSAGE_WHISPER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB2'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('message', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#B5
class c_CM_Target_SELECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#B9
class c_CM_CHAT_MESSAGE_PUBLIC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB9'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('type', 'i1')
              , ('message', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#BD
class c_CM_OPEN_STATICDOOR():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('doorId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#BE
class c_CM_LEGION_EMBLEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('legionId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C0
class c_CM_TIME_CHECK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('nanoTime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C1
class c_CM_GATHER():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('action', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C2
class c_CM_PING():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('ping', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#CB
class c_CM_USE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('uniqueitemId', 'i4')
              , ('type', 'i1')
              , ('TargetitemId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#CC
class c_CM_EQUIP_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('action', 'i1')
              , ('slotRead', 'i4')
              , ('itemUniqueId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#CE
class c_CM_ATTACK():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetOID', 'i4')
              , ('attackno', 'i1')
              , ('time', 'i2')
              , ('type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#D0
class c_CM_SKILL_DEACTIVATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('SkillId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D1
class c_CM_REMOVE_ALTERED_STATE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('SkillId', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D3
class c_CM_BROKER_REGISTERED():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('npcId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D4
class c_CM_BUY_BROKER_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('brokerId', 'i4')
              , ('itemUniqueId', 'i4')
              , ('itemCount', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D5
class c_CM_REGISTER_BROKER_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('brokerId', 'i4')
              , ('itemUniqueId', 'i4')
              , ('price', 'i8')
              , ('itemCount', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D6
class c_CM_PRIVATE_STORE_NAME():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD6'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#D7
class c_CM_SUMMON_COMMAND():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('mode', 'i1')
              , ('unk_0', 'i4')
              , ('unk_1', 'i4')
              , ('TargetOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D9
class c_CM_BROKER_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('brokerId', 'i4')
              , ('sortType', 'i1')
              , ('page', 'i2')
              , ('listMask', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#DA
class c_CM_DELETE_ITEM():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#DC
class c_CM_ABYSS_RANKING_LEGIONS():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('raceId', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#DD
class c_CM_PRIVATE_STORE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDD'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('itemCountValue', 'i2')
                  ]+ list(self.f_itemCount()) +[
                  ]
    return dtype
  def f_itemCount(self):
    for i in range(self.It.__next__()):
      dtype = ('itemCount_' + str(i) , [
               ('unk_0', 'i4')
              , ('unk_1', 'i4')
              , ('unk_2', 'i2')
              , ('unk_3', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#DF
class c_CM_FRIEND_DEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDF'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('TargetName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#E0
class c_CM_DUEL_REQUEST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#E3
class c_CM_CRAFT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i1')
              , ('TargetTemplateId', 'i4')
              , ('recipeId', 'i4')
              , ('TargetOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#E4
class c_CM_CLIENT_COMMAND_LOC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#E5
class c_CM_QUESTIONNAIRE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('OID', 'i4')
              , ('unk_0', 'i2')
              , ('choice', 'i2')
              , ('unk_1', 'i2')
              , ('unk_2', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#E6
class c_CM__MAIL_ATTACHMENT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('mailOID', 'i4')
              , ('attachmentType', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#E7
class c_CM_DELETE_MAIL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('mailOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#E9
class c_CM_TITLE_SET():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('titleId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#EA
class c_CM_SEND_MAIL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEA'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('recipientName', '|S'+str(self.It.__next__()) )
              , ('title', '|S'+str(self.It.__next__()) )
              , ('message', '|S'+str(self.It.__next__()) )
              , ('itemOID', 'i4')
              , ('itemCount', 'i4')
              , ('unk_0', 'i4')
              , ('kinahCount', 'i4')
              , ('unk_1', 'i4')
              , ('express', 'i1')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#EC
class c_CM_READ_MAIL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('mailOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#EE
class c_CM_BROKER_CANCEL_REGISTERED():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('npcId', 'i4')
              , ('brokeritemId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#EF
class c_CM_BROKER_SETTLE_LIST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('npcId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F0
class c_CM_BROKER_SETTLE_ACCOUNT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('npcId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F5
class c_CM_ALLIANCE_GROUP_CHANGE():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('playerOID', 'i4')
              , ('allianceGroupId', 'i4')
              , ('secondOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F8
class c_CM_ITEM_REMODEL():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('unk', 'i4')
              , ('keepitemId', 'i4')
              , ('extractitemId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F9
class c_CM_GODSTONE_SOCKET():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('npcId', 'i4')
              , ('weaponId', 'i4')
              , ('stoneId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE
class c_CM_DELETE_QUEST():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('questId', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FF
class c_CM_PLAY_MOVIE_END():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('type', 'i1')
              , ('unk_0', 'i4')
              , ('unk_1', 'i4')
              , ('movieId', 'i2')
              , ('unk_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B5
class c_CM_TARGET_SELECT():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('id2', 'i2')
              , ('ObjectID', 'i4')
              , ('1', '|S1')
                  ]
    return dtype
class Pck_invoke_dict():
 def __init__(self):
   self.Pck_invoke_s = {}
   self.Pck_invoke_c = {}
 def get_Pck_invoke_c(self):
   self.Pck_invoke_s[c_CM_GROUP_DISTRIBUTION().invoke] = c_CM_GROUP_DISTRIBUTION()
   self.Pck_invoke_s[c_CM_SHOW_FRIENDLIST().invoke] = c_CM_SHOW_FRIENDLIST()
   self.Pck_invoke_s[c_CM_FRIEND_ADD().invoke] = c_CM_FRIEND_ADD()
   self.Pck_invoke_s[c_CM_CLIENT_COMMAND_ROLL().invoke] = c_CM_CLIENT_COMMAND_ROLL()
   self.Pck_invoke_s[c_CM_VIEW_PLAYER_DETAILS().invoke] = c_CM_VIEW_PLAYER_DETAILS()
   self.Pck_invoke_s[c_CM_PING_REQUEST().invoke] = c_CM_PING_REQUEST()
   self.Pck_invoke_s[c_CM_PLAYER_STATUS_INFO().invoke] = c_CM_PLAYER_STATUS_INFO()
   self.Pck_invoke_s[c_CM_INVITE_TO_GROUP().invoke] = c_CM_INVITE_TO_GROUP()
   self.Pck_invoke_s[c_CM_ABYSS_RANKING_PLAYERS().invoke] = c_CM_ABYSS_RANKING_PLAYERS()
   self.Pck_invoke_s[c_CM_MAC_ADDRESS().invoke] = c_CM_MAC_ADDRESS()
   self.Pck_invoke_s[c_CM_REPORT_PLAYER().invoke] = c_CM_REPORT_PLAYER()
   self.Pck_invoke_s[c_CM_GROUP_LOOT().invoke] = c_CM_GROUP_LOOT()
   self.Pck_invoke_s[c_CM_DISTRIBUTION_SETTINGS().invoke] = c_CM_DISTRIBUTION_SETTINGS()
   self.Pck_invoke_s[c_CM_MAY_LOGIN_INTO_GAME().invoke] = c_CM_MAY_LOGIN_INTO_GAME()
   self.Pck_invoke_s[c_CM_SHOW_BRAND().invoke] = c_CM_SHOW_BRAND()
   self.Pck_invoke_s[c_CM_RECONNECT_AUTH().invoke] = c_CM_RECONNECT_AUTH()
   self.Pck_invoke_s[c_CM_MACRO_DELETE().invoke] = c_CM_MACRO_DELETE()
   self.Pck_invoke_s[c_CM_CHECK_NICKNAME().invoke] = c_CM_CHECK_NICKNAME()
   self.Pck_invoke_s[c_CM_BLOCK_SET_REASON().invoke] = c_CM_BLOCK_SET_REASON()
   self.Pck_invoke_s[c_CM_FUSION_WEAPONS().invoke] = c_CM_FUSION_WEAPONS()
   self.Pck_invoke_s[c_CM_BREAK_WEAPONS().invoke] = c_CM_BREAK_WEAPONS()
   self.Pck_invoke_s[c_CM_SUMMON_EMOTION().invoke] = c_CM_SUMMON_EMOTION()
   self.Pck_invoke_s[c_CM_SUMMON_ATTACK().invoke] = c_CM_SUMMON_ATTACK()
   self.Pck_invoke_s[c_CM_SHOW_MAP().invoke] = c_CM_SHOW_MAP()
   self.Pck_invoke_s[c_CM_NAME_CHANGE().invoke] = c_CM_NAME_CHANGE()
   self.Pck_invoke_s[c_CM_GROUP_RESPONSE().invoke] = c_CM_GROUP_RESPONSE()
   self.Pck_invoke_s[c_CM_MOVE_ITEM().invoke] = c_CM_MOVE_ITEM()
   self.Pck_invoke_s[c_CM_SPLIT_ITEM().invoke] = c_CM_SPLIT_ITEM()
   self.Pck_invoke_s[c_CM_PLAYER_SEARCH().invoke] = c_CM_PLAYER_SEARCH()
   self.Pck_invoke_s[c_CM_DELETE_CHARACTER().invoke] = c_CM_DELETE_CHARACTER()
   self.Pck_invoke_s[c_CM_RESTORE_CHARACTER().invoke] = c_CM_RESTORE_CHARACTER()
   self.Pck_invoke_s[c_CM_STargetT_LOOT().invoke] = c_CM_STargetT_LOOT()
   self.Pck_invoke_s[c_CM_LOOT_ITEM().invoke] = c_CM_LOOT_ITEM()
   self.Pck_invoke_s[c_CM_TELEPORT_SELECT().invoke] = c_CM_TELEPORT_SELECT()
   self.Pck_invoke_s[c_CM_L2AUTH_LOGIN_CHECK().invoke] = c_CM_L2AUTH_LOGIN_CHECK()
   self.Pck_invoke_s[c_CM_CHARACTER_LIST().invoke] = c_CM_CHARACTER_LIST()
   self.Pck_invoke_s[c_CM_CREATE_CHARACTER().invoke] = c_CM_CREATE_CHARACTER()
   self.Pck_invoke_s[c_CM_CHANGE_CHANNEL().invoke] = c_CM_CHANGE_CHANNEL()
   self.Pck_invoke_s[c_CM_MAC_ADDRESS2().invoke] = c_CM_MAC_ADDRESS2()
   self.Pck_invoke_s[c_CM_MACRO_CREATE().invoke] = c_CM_MACRO_CREATE()
   self.Pck_invoke_s[c_CM_SHOW_BLOCKLIST().invoke] = c_CM_SHOW_BLOCKLIST()
   self.Pck_invoke_s[c_CM_REPLACE_ITEM().invoke] = c_CM_REPLACE_ITEM()
   self.Pck_invoke_s[c_CM_FRIEND_STATUS().invoke] = c_CM_FRIEND_STATUS()
   self.Pck_invoke_s[c_CM_BLOCK_ADD().invoke] = c_CM_BLOCK_ADD()
   self.Pck_invoke_s[c_CM_BLOCK_DEL().invoke] = c_CM_BLOCK_DEL()
   self.Pck_invoke_s[c_CM_LEGION_UPLOAD_INFO().invoke] = c_CM_LEGION_UPLOAD_INFO()
   self.Pck_invoke_s[c_CM_LEGION_UPLOAD_EMBLEM().invoke] = c_CM_LEGION_UPLOAD_EMBLEM()
   self.Pck_invoke_s[c_CM_MAIL_SUMMON_ZEPHYR().invoke] = c_CM_MAIL_SUMMON_ZEPHYR()
   self.Pck_invoke_s[c_CM_CUSTOM_SETTINGS().invoke] = c_CM_CUSTOM_SETTINGS()
   self.Pck_invoke_s[c_CM_ENTER_WORLD().invoke] = c_CM_ENTER_WORLD()
   self.Pck_invoke_s[c_CM_LEVEL_READY().invoke] = c_CM_LEVEL_READY()
   self.Pck_invoke_s[c_CM_UI_SETTINGS().invoke] = c_CM_UI_SETTINGS()
   self.Pck_invoke_s[c_CM_OBJECT_SEARCH().invoke] = c_CM_OBJECT_SEARCH()
   self.Pck_invoke_s[c_CM_MAY_QUIT().invoke] = c_CM_MAY_QUIT()
   self.Pck_invoke_s[c_CM_REVIVE().invoke] = c_CM_REVIVE()
   self.Pck_invoke_s[c_CM_CHARACTER_EDIT().invoke] = c_CM_CHARACTER_EDIT()
   self.Pck_invoke_s[c_CM_VERSION_CHECK().invoke] = c_CM_VERSION_CHECK()
   self.Pck_invoke_s[c_CM_DISCONNECT().invoke] = c_CM_DISCONNECT()
   self.Pck_invoke_s[c_CM_QUIT().invoke] = c_CM_QUIT()
   self.Pck_invoke_s[c_CM_EXCHANGE_REQUEST().invoke] = c_CM_EXCHANGE_REQUEST()
   self.Pck_invoke_s[c_CM_LEGION_EMBLEM_SEND().invoke] = c_CM_LEGION_EMBLEM_SEND()
   self.Pck_invoke_s[c_CM_SET_NOTE().invoke] = c_CM_SET_NOTE()
   self.Pck_invoke_s[c_CM_LEGION_MODIFY_EMBLEM().invoke] = c_CM_LEGION_MODIFY_EMBLEM()
   self.Pck_invoke_s[c_CM_SHOW_DIALOG().invoke] = c_CM_SHOW_DIALOG()
   self.Pck_invoke_s[c_CM_CLOSE_DIALOG().invoke] = c_CM_CLOSE_DIALOG()
   self.Pck_invoke_s[c_CM_DIALOG_SELECT().invoke] = c_CM_DIALOG_SELECT()
   self.Pck_invoke_s[c_CM_LEGION_TABS().invoke] = c_CM_LEGION_TABS()
   self.Pck_invoke_s[c_CM_QUESTION_RESPONSE().invoke] = c_CM_QUESTION_RESPONSE()
   self.Pck_invoke_s[c_CM_BUY_ITEM().invoke] = c_CM_BUY_ITEM()
   self.Pck_invoke_s[c_CM_EXCHANGE_OK().invoke] = c_CM_EXCHANGE_OK()
   self.Pck_invoke_s[c_CM_EXCHANGE_CANCEL().invoke] = c_CM_EXCHANGE_CANCEL()
   self.Pck_invoke_s[c_CM_WINDSTREAM().invoke] = c_CM_WINDSTREAM()
   self.Pck_invoke_s[c_CM_EXCHANGE_ADD_ITEM().invoke] = c_CM_EXCHANGE_ADD_ITEM()
   self.Pck_invoke_s[c_CM_EXCHANGE_ADD_KINAH().invoke] = c_CM_EXCHANGE_ADD_KINAH()
   self.Pck_invoke_s[c_CM_EXCHANGE_LOCK().invoke] = c_CM_EXCHANGE_LOCK()
   self.Pck_invoke_s[c_CM_CHAT_MESSAGE_WHISPER().invoke] = c_CM_CHAT_MESSAGE_WHISPER()
   self.Pck_invoke_s[c_CM_Target_SELECT().invoke] = c_CM_Target_SELECT()
   self.Pck_invoke_s[c_CM_CHAT_MESSAGE_PUBLIC().invoke] = c_CM_CHAT_MESSAGE_PUBLIC()
   self.Pck_invoke_s[c_CM_OPEN_STATICDOOR().invoke] = c_CM_OPEN_STATICDOOR()
   self.Pck_invoke_s[c_CM_LEGION_EMBLEM().invoke] = c_CM_LEGION_EMBLEM()
   self.Pck_invoke_s[c_CM_TIME_CHECK().invoke] = c_CM_TIME_CHECK()
   self.Pck_invoke_s[c_CM_GATHER().invoke] = c_CM_GATHER()
   self.Pck_invoke_s[c_CM_PING().invoke] = c_CM_PING()
   self.Pck_invoke_s[c_CM_USE_ITEM().invoke] = c_CM_USE_ITEM()
   self.Pck_invoke_s[c_CM_EQUIP_ITEM().invoke] = c_CM_EQUIP_ITEM()
   self.Pck_invoke_s[c_CM_ATTACK().invoke] = c_CM_ATTACK()
   self.Pck_invoke_s[c_CM_SKILL_DEACTIVATE().invoke] = c_CM_SKILL_DEACTIVATE()
   self.Pck_invoke_s[c_CM_REMOVE_ALTERED_STATE().invoke] = c_CM_REMOVE_ALTERED_STATE()
   self.Pck_invoke_s[c_CM_BROKER_REGISTERED().invoke] = c_CM_BROKER_REGISTERED()
   self.Pck_invoke_s[c_CM_BUY_BROKER_ITEM().invoke] = c_CM_BUY_BROKER_ITEM()
   self.Pck_invoke_s[c_CM_REGISTER_BROKER_ITEM().invoke] = c_CM_REGISTER_BROKER_ITEM()
   self.Pck_invoke_s[c_CM_PRIVATE_STORE_NAME().invoke] = c_CM_PRIVATE_STORE_NAME()
   self.Pck_invoke_s[c_CM_SUMMON_COMMAND().invoke] = c_CM_SUMMON_COMMAND()
   self.Pck_invoke_s[c_CM_BROKER_LIST().invoke] = c_CM_BROKER_LIST()
   self.Pck_invoke_s[c_CM_DELETE_ITEM().invoke] = c_CM_DELETE_ITEM()
   self.Pck_invoke_s[c_CM_ABYSS_RANKING_LEGIONS().invoke] = c_CM_ABYSS_RANKING_LEGIONS()
   self.Pck_invoke_s[c_CM_PRIVATE_STORE().invoke] = c_CM_PRIVATE_STORE()
   self.Pck_invoke_s[c_CM_FRIEND_DEL().invoke] = c_CM_FRIEND_DEL()
   self.Pck_invoke_s[c_CM_DUEL_REQUEST().invoke] = c_CM_DUEL_REQUEST()
   self.Pck_invoke_s[c_CM_CRAFT().invoke] = c_CM_CRAFT()
   self.Pck_invoke_s[c_CM_CLIENT_COMMAND_LOC().invoke] = c_CM_CLIENT_COMMAND_LOC()
   self.Pck_invoke_s[c_CM_QUESTIONNAIRE().invoke] = c_CM_QUESTIONNAIRE()
   self.Pck_invoke_s[c_CM__MAIL_ATTACHMENT().invoke] = c_CM__MAIL_ATTACHMENT()
   self.Pck_invoke_s[c_CM_DELETE_MAIL().invoke] = c_CM_DELETE_MAIL()
   self.Pck_invoke_s[c_CM_TITLE_SET().invoke] = c_CM_TITLE_SET()
   self.Pck_invoke_s[c_CM_SEND_MAIL().invoke] = c_CM_SEND_MAIL()
   self.Pck_invoke_s[c_CM_READ_MAIL().invoke] = c_CM_READ_MAIL()
   self.Pck_invoke_s[c_CM_BROKER_CANCEL_REGISTERED().invoke] = c_CM_BROKER_CANCEL_REGISTERED()
   self.Pck_invoke_s[c_CM_BROKER_SETTLE_LIST().invoke] = c_CM_BROKER_SETTLE_LIST()
   self.Pck_invoke_s[c_CM_BROKER_SETTLE_ACCOUNT().invoke] = c_CM_BROKER_SETTLE_ACCOUNT()
   self.Pck_invoke_s[c_CM_ALLIANCE_GROUP_CHANGE().invoke] = c_CM_ALLIANCE_GROUP_CHANGE()
   self.Pck_invoke_s[c_CM_ITEM_REMODEL().invoke] = c_CM_ITEM_REMODEL()
   self.Pck_invoke_s[c_CM_GODSTONE_SOCKET().invoke] = c_CM_GODSTONE_SOCKET()
   self.Pck_invoke_s[c_CM_DELETE_QUEST().invoke] = c_CM_DELETE_QUEST()
   self.Pck_invoke_s[c_CM_PLAY_MOVIE_END().invoke] = c_CM_PLAY_MOVIE_END()
   self.Pck_invoke_s[c_CM_TARGET_SELECT().invoke] = c_CM_TARGET_SELECT()
   return self.Pck_invoke_s
 def get_Pck_invoke_s(self):
   self.Pck_invoke_c[s_SM_STATUPDATE_HP().invoke] = s_SM_STATUPDATE_HP()
   self.Pck_invoke_c[s_SM_STATUPDATE_DP().invoke] = s_SM_STATUPDATE_DP()
   self.Pck_invoke_c[s_SM_CHANNEL_INFO().invoke] = s_SM_CHANNEL_INFO()
   self.Pck_invoke_c[s_SM_MACRO_LIST().invoke] = s_SM_MACRO_LIST()
   self.Pck_invoke_c[s_SM_CHAT_INIT().invoke] = s_SM_CHAT_INIT()
   self.Pck_invoke_c[s_SM_NICKNAME_CHECK_RESPONSE().invoke] = s_SM_NICKNAME_CHECK_RESPONSE()
   self.Pck_invoke_c[s_SM_MACRO_RESULT().invoke] = s_SM_MACRO_RESULT()
   self.Pck_invoke_c[s_SM_RIFT_ANNOUNCE().invoke] = s_SM_RIFT_ANNOUNCE()
   self.Pck_invoke_c[s_SM_PETITION().invoke] = s_SM_PETITION()
   self.Pck_invoke_c[s_SM_RECIPE_DELETE().invoke] = s_SM_RECIPE_DELETE()
   self.Pck_invoke_c[s_SM_LEARN_RECIPE().invoke] = s_SM_LEARN_RECIPE()
   self.Pck_invoke_c[s_SM_FRIEND_UPDATE().invoke] = s_SM_FRIEND_UPDATE()
   self.Pck_invoke_c[s_SM_FORTRESS_INFO().invoke] = s_SM_FORTRESS_INFO()
   self.Pck_invoke_c[s_SM_LOGIN_QUEUE().invoke] = s_SM_LOGIN_QUEUE()
   self.Pck_invoke_c[s_SM_DELETE().invoke] = s_SM_DELETE()
   self.Pck_invoke_c[s_SM_UI_SETTINGS().invoke] = s_SM_UI_SETTINGS()
   self.Pck_invoke_c[s_SM_SYSTEM_MESSAGE().invoke] = s_SM_SYSTEM_MESSAGE()
   self.Pck_invoke_c[s_SM_INVENTORY_UPDATE().invoke] = s_SM_INVENTORY_UPDATE()
   self.Pck_invoke_c[s_SM_INVENTORY_INFO().invoke] = s_SM_INVENTORY_INFO()
   self.Pck_invoke_c[s_SM_DELETE_ITEM().invoke] = s_SM_DELETE_ITEM()
   self.Pck_invoke_c[s_SM_GATHER_UPDATE().invoke] = s_SM_GATHER_UPDATE()
   self.Pck_invoke_c[s_SM_GATHER_STATUS().invoke] = s_SM_GATHER_STATUS()
   self.Pck_invoke_c[s_SM_STATUPDATE_MP().invoke] = s_SM_STATUPDATE_MP()
   self.Pck_invoke_c[s_SM_DP_INFO().invoke] = s_SM_DP_INFO()
   self.Pck_invoke_c[s_SM_LEGION_UPDATE_NICKNAME().invoke] = s_SM_LEGION_UPDATE_NICKNAME()
   self.Pck_invoke_c[s_SM_STATUPDATE_EXP().invoke] = s_SM_STATUPDATE_EXP()
   self.Pck_invoke_c[s_SM_ENTER_WORLD_CHECK().invoke] = s_SM_ENTER_WORLD_CHECK()
   self.Pck_invoke_c[s_SM_LEGION_TABS().invoke] = s_SM_LEGION_TABS()
   self.Pck_invoke_c[s_SM_QUESTION_WINDOW().invoke] = s_SM_QUESTION_WINDOW()
   self.Pck_invoke_c[s_SM_DIALOG_WINDOW().invoke] = s_SM_DIALOG_WINDOW()
   self.Pck_invoke_c[s_SM_SELL_ITEM().invoke] = s_SM_SELL_ITEM()
   self.Pck_invoke_c[s_SM_VIEW_PLAYER_DETAILS().invoke] = s_SM_VIEW_PLAYER_DETAILS()
   self.Pck_invoke_c[s_SM_WEATHER().invoke] = s_SM_WEATHER()
   self.Pck_invoke_c[s_SM_UPDATE_PLAYER_APPEARANCE().invoke] = s_SM_UPDATE_PLAYER_APPEARANCE()
   self.Pck_invoke_c[s_SM_TIME_CHECK().invoke] = s_SM_TIME_CHECK()
   self.Pck_invoke_c[s_SM_GAME_TIME().invoke] = s_SM_GAME_TIME()
   self.Pck_invoke_c[s_SM_Target_SELECTED().invoke] = s_SM_Target_SELECTED()
   self.Pck_invoke_c[s_SM_LOOKATOBJECT().invoke] = s_SM_LOOKATOBJECT()
   self.Pck_invoke_c[s_SM_SKILL_CANCEL().invoke] = s_SM_SKILL_CANCEL()
   self.Pck_invoke_c[s_SM_STIGMA_SKILL_REMOVE().invoke] = s_SM_STIGMA_SKILL_REMOVE()
   self.Pck_invoke_c[s_SM_SKILL_LIST().invoke] = s_SM_SKILL_LIST()
   self.Pck_invoke_c[s_SM_SKILL_ACTIVATION().invoke] = s_SM_SKILL_ACTIVATION()
   self.Pck_invoke_c[s_SM_ABNORMAL_STATE().invoke] = s_SM_ABNORMAL_STATE()
   self.Pck_invoke_c[s_SM_SKILL_COOLDOWN().invoke] = s_SM_SKILL_COOLDOWN()
   self.Pck_invoke_c[s_SM_ABNORMAL_EFFECT().invoke] = s_SM_ABNORMAL_EFFECT()
   self.Pck_invoke_c[s_SM_FORTRESS_STATUS().invoke] = s_SM_FORTRESS_STATUS()
   self.Pck_invoke_c[s_SM_NAME_CHANGE().invoke] = s_SM_NAME_CHANGE()
   self.Pck_invoke_c[s_SM_GROUP_INFO().invoke] = s_SM_GROUP_INFO()
   self.Pck_invoke_c[s_SM_ABYSS_ARTIFACT_INFO().invoke] = s_SM_ABYSS_ARTIFACT_INFO()
   self.Pck_invoke_c[s_SM_QUIT_RESPONSE().invoke] = s_SM_QUIT_RESPONSE()
   self.Pck_invoke_c[s_SM_PLAYER_STATE().invoke] = s_SM_PLAYER_STATE()
   self.Pck_invoke_c[s_SM_STargetTED_QUEST_LIST().invoke] = s_SM_STargetTED_QUEST_LIST()
   self.Pck_invoke_c[s_SM_LEVEL_UPDATE().invoke] = s_SM_LEVEL_UPDATE()
   self.Pck_invoke_c[s_SM_SUMMON_PANEL_REMOVE().invoke] = s_SM_SUMMON_PANEL_REMOVE()
   self.Pck_invoke_c[s_SM_KEY().invoke] = s_SM_KEY()
   self.Pck_invoke_c[s_SM_EXCHANGE_ADD_ITEM().invoke] = s_SM_EXCHANGE_ADD_ITEM()
   self.Pck_invoke_c[s_SM_EXCHANGE_REQUEST().invoke] = s_SM_EXCHANGE_REQUEST()
   self.Pck_invoke_c[s_SM_EXCHANGE_ADD_KINAH().invoke] = s_SM_EXCHANGE_ADD_KINAH()
   self.Pck_invoke_c[s_SM_EMOTION_LIST().invoke] = s_SM_EMOTION_LIST()
   self.Pck_invoke_c[s_SM_EXCHANGE_CONFIRMATION().invoke] = s_SM_EXCHANGE_CONFIRMATION()
   self.Pck_invoke_c[s_SM_Target_UPDATE().invoke] = s_SM_Target_UPDATE()
   self.Pck_invoke_c[s_SM_PLASTIC_SURGERY().invoke] = s_SM_PLASTIC_SURGERY()
   self.Pck_invoke_c[s_SM_LEGION_UPDATE_SELF_INTRO().invoke] = s_SM_LEGION_UPDATE_SELF_INTRO()
   self.Pck_invoke_c[s_SM_QUEST_LIST().invoke] = s_SM_QUEST_LIST()
   self.Pck_invoke_c[s_SM_RIFT_STATUS().invoke] = s_SM_RIFT_STATUS()
   self.Pck_invoke_c[s_SM_NEARBY_QUESTS().invoke] = s_SM_NEARBY_QUESTS()
   self.Pck_invoke_c[s_SM_PING_RESPONSE().invoke] = s_SM_PING_RESPONSE()
   self.Pck_invoke_c[s_SM_CUBE_UPDATE().invoke] = s_SM_CUBE_UPDATE()
   self.Pck_invoke_c[s_SM_PET().invoke] = s_SM_PET()
   self.Pck_invoke_c[s_SM_ITEM_COOLDOWN().invoke] = s_SM_ITEM_COOLDOWN()
   self.Pck_invoke_c[s_SM_PLAY_MOVIE().invoke] = s_SM_PLAY_MOVIE()
   self.Pck_invoke_c[s_SM_UPDATE_NOTE().invoke] = s_SM_UPDATE_NOTE()
   self.Pck_invoke_c[s_SM_LEGION_ADD_MEMBER().invoke] = s_SM_LEGION_ADD_MEMBER()
   self.Pck_invoke_c[s_SM_LEGION_INFO().invoke] = s_SM_LEGION_INFO()
   self.Pck_invoke_c[s_SM_LEGION_UPDATE_TITLE().invoke] = s_SM_LEGION_UPDATE_TITLE()
   self.Pck_invoke_c[s_SM_LEGION_UPDATE_MEMBER().invoke] = s_SM_LEGION_UPDATE_MEMBER()
   self.Pck_invoke_c[s_SM_LEGION_LEAVE_MEMBER().invoke] = s_SM_LEGION_LEAVE_MEMBER()
   self.Pck_invoke_c[s_SM_SUMMON_PANEL().invoke] = s_SM_SUMMON_PANEL()
   self.Pck_invoke_c[s_SM_SUMMON_UPDATE().invoke] = s_SM_SUMMON_UPDATE()
   self.Pck_invoke_c[s_SM_SUMMON_OWNER_REMOVE().invoke] = s_SM_SUMMON_OWNER_REMOVE()
   self.Pck_invoke_c[s_SM_LEGION_MEMBERLIST().invoke] = s_SM_LEGION_MEMBERLIST()
   self.Pck_invoke_c[s_SM_MAIL_SERVICE().invoke] = s_SM_MAIL_SERVICE()
   self.Pck_invoke_c[s_SM_WINDSTREAM().invoke] = s_SM_WINDSTREAM()
   self.Pck_invoke_c[s_SM_SUMMON_USESKILL().invoke] = s_SM_SUMMON_USESKILL()
   self.Pck_invoke_c[s_SM_PRIVATE_STORE().invoke] = s_SM_PRIVATE_STORE()
   self.Pck_invoke_c[s_SM_FRIEND_LIST().invoke] = s_SM_FRIEND_LIST()
   self.Pck_invoke_c[s_SM_GROUP_LOOT().invoke] = s_SM_GROUP_LOOT()
   self.Pck_invoke_c[s_SM_MAY_LOGIN_INTO_GAME().invoke] = s_SM_MAY_LOGIN_INTO_GAME()
   self.Pck_invoke_c[s_SM_ABYSS_RANK_UPDATE().invoke] = s_SM_ABYSS_RANK_UPDATE()
   self.Pck_invoke_c[s_SM_ABYSS_RANKING_LEGIONS().invoke] = s_SM_ABYSS_RANKING_LEGIONS()
   self.Pck_invoke_c[s_SM_ABYSS_RANKING_PLAYERS().invoke] = s_SM_ABYSS_RANKING_PLAYERS()
   self.Pck_invoke_c[s_SM_PLAYER_ID().invoke] = s_SM_PLAYER_ID()
   self.Pck_invoke_c[s_SM_KISK_UPDATE().invoke] = s_SM_KISK_UPDATE()
   self.Pck_invoke_c[s_SM_PONG().invoke] = s_SM_PONG()
   self.Pck_invoke_c[s_SM_PRIVATE_STORE_NAME().invoke] = s_SM_PRIVATE_STORE_NAME()
   self.Pck_invoke_c[s_SM_BROKER_ITEMS().invoke] = s_SM_BROKER_ITEMS()
   self.Pck_invoke_c[s_SM_CRAFT_ANIMATION().invoke] = s_SM_CRAFT_ANIMATION()
   self.Pck_invoke_c[s_SM_ITEM_USAGE_ANIMATION().invoke] = s_SM_ITEM_USAGE_ANIMATION()
   self.Pck_invoke_c[s_SM_ASCENSION_MORPH().invoke] = s_SM_ASCENSION_MORPH()
   self.Pck_invoke_c[s_SM_DUEL().invoke] = s_SM_DUEL()
   self.Pck_invoke_c[s_SM_CUSTOM_SETTINGS().invoke] = s_SM_CUSTOM_SETTINGS()
   self.Pck_invoke_c[s_SM_QUESTIONNAIRE().invoke] = s_SM_QUESTIONNAIRE()
   self.Pck_invoke_c[s_SM_DIE().invoke] = s_SM_DIE()
   self.Pck_invoke_c[s_SM_RESURRECT().invoke] = s_SM_RESURRECT()
   self.Pck_invoke_c[s_SM_WINDSTREAM_ANNOUNCE().invoke] = s_SM_WINDSTREAM_ANNOUNCE()
   self.Pck_invoke_c[s_SM_REPURCHASE().invoke] = s_SM_REPURCHASE()
   self.Pck_invoke_c[s_SM_WAREHOUSE_UPDATE().invoke] = s_SM_WAREHOUSE_UPDATE()
   self.Pck_invoke_c[s_SM_WAREHOUSE_INFO().invoke] = s_SM_WAREHOUSE_INFO()
   self.Pck_invoke_c[s_SM_UPDATE_WAREHOUSE_ITEM().invoke] = s_SM_UPDATE_WAREHOUSE_ITEM()
   self.Pck_invoke_c[s_SM_DELETE_WAREHOUSE_ITEM().invoke] = s_SM_DELETE_WAREHOUSE_ITEM()
   self.Pck_invoke_c[s_SM_CHARACTER_SELECT().invoke] = s_SM_CHARACTER_SELECT()
   self.Pck_invoke_c[s_SM_LEGION_EMBLEM().invoke] = s_SM_LEGION_EMBLEM()
   self.Pck_invoke_c[s_SM_LEGION_UPDATE_EMBLEM().invoke] = s_SM_LEGION_UPDATE_EMBLEM()
   self.Pck_invoke_c[s_SM_LEGION_EMBLEM_SEND().invoke] = s_SM_LEGION_EMBLEM_SEND()
   self.Pck_invoke_c[s_SM_LEGION_EMBLEM_SEND().invoke] = s_SM_LEGION_EMBLEM_SEND()
   self.Pck_invoke_c[s_SM_ABYSS_ARTIFACT_INFO2().invoke] = s_SM_ABYSS_ARTIFACT_INFO2()
   self.Pck_invoke_c[s_SM_ABYSS_ARTIFACT_INFO3().invoke] = s_SM_ABYSS_ARTIFACT_INFO3()
   self.Pck_invoke_c[s_SM_BLOCK_RESPONSE().invoke] = s_SM_BLOCK_RESPONSE()
   self.Pck_invoke_c[s_SM_FRIEND_RESPONSE().invoke] = s_SM_FRIEND_RESPONSE()
   self.Pck_invoke_c[s_SM_BLOCK_LIST().invoke] = s_SM_BLOCK_LIST()
   self.Pck_invoke_c[s_SM_FRIEND_NOTIFY().invoke] = s_SM_FRIEND_NOTIFY()
   self.Pck_invoke_c[s_SM_USE_OBJECT().invoke] = s_SM_USE_OBJECT()
   self.Pck_invoke_c[s_SM_TELEPORT_MAP().invoke] = s_SM_TELEPORT_MAP()
   self.Pck_invoke_c[s_SM_L2AUTH_LOGIN_CHECK().invoke] = s_SM_L2AUTH_LOGIN_CHECK()
   self.Pck_invoke_c[s_SM_RESTORE_CHARACTER().invoke] = s_SM_RESTORE_CHARACTER()
   self.Pck_invoke_c[s_SM_DELETE_CHARACTER().invoke] = s_SM_DELETE_CHARACTER()
   self.Pck_invoke_c[s_SM_LOOT_STATUS().invoke] = s_SM_LOOT_STATUS()
   self.Pck_invoke_c[s_SM_RECIPE_LIST().invoke] = s_SM_RECIPE_LIST()
   self.Pck_invoke_c[s_SM_LOOT_ITEMLIST().invoke] = s_SM_LOOT_ITEMLIST()
   self.Pck_invoke_c[s_SM_SIEGE_LOCATION_INFO().invoke] = s_SM_SIEGE_LOCATION_INFO()
   self.Pck_invoke_c[s_SM_MANTRA_EFFECT().invoke] = s_SM_MANTRA_EFFECT()
   self.Pck_invoke_c[s_SM_ALLIANCE_INFO().invoke] = s_SM_ALLIANCE_INFO()
   self.Pck_invoke_c[s_SM_ALLIANCE_MEMBER_INFO().invoke] = s_SM_ALLIANCE_MEMBER_INFO()
   self.Pck_invoke_c[s_SM_FLY_TIME().invoke] = s_SM_FLY_TIME()
   self.Pck_invoke_c[s_SM_LEAVE_GROUP_MEMBER().invoke] = s_SM_LEAVE_GROUP_MEMBER()
   self.Pck_invoke_c[s_SM_SHOW_BRAND().invoke] = s_SM_SHOW_BRAND()
   self.Pck_invoke_c[s_SM_ALLIANCE_READY_CHECK().invoke] = s_SM_ALLIANCE_READY_CHECK()
   self.Pck_invoke_c[s_SM_TRADELIST().invoke] = s_SM_TRADELIST()
   self.Pck_invoke_c[s_SM_PRICES().invoke] = s_SM_PRICES()
   self.Pck_invoke_c[s_SM_RECONNECT_KEY().invoke] = s_SM_RECONNECT_KEY()
   self.Pck_invoke_c[s_SM_VERSION_CHECK().invoke] = s_SM_VERSION_CHECK()
   self.Pck_invoke_c[s_SM_CUSTOM_PACKET().invoke] = s_SM_CUSTOM_PACKET()
   return self.Pck_invoke_c
