import struct
#--------------------------------------------------------------------------#00
class c_Logout():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#01
class c_AttackRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
              , ('AttackID', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#03
class c_RequestStartPledgeWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x03'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('PledgeName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#04
class c_RequestReplyStartPledgeWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x04'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('RequestorName', '|S'+str(self.It.__next__()) )
              , ('Answer', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#05
class c_RequestStopPledgeWar():
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
              , ('PledgeName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#06
class c_RequestReplyStopPledgeWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x06'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('RequestorName', '|S'+str(self.It.__next__()) )
              , ('Answer', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#07
class c_RequestSurrenderPledgeWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x07'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('PledgeName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#08
class c_RequestReplySurrenderPledgeWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x08'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('RequestorName', '|S'+str(self.It.__next__()) )
              , ('Answer', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#09
class c_RequestSetPledgeCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x09'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CrestSize', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0B
class c_RequestGiveNickName():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0B'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Target', '|S'+str(self.It.__next__()) )
              , ('Title', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0C
class c_CharacterCreate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0C'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Race', 'i4')
              , ('Sex', 'i4')
              , ('ClassIDGetClassID', 'i4')
              , ('INT', 'i4')
              , ('STR', 'i4')
              , ('CON', 'i4')
              , ('MEN', 'i4')
              , ('DEX', 'i4')
              , ('WIT', 'i4')
              , ('HairStyle', 'i4')
              , ('HairColor', 'i4')
              , ('Face', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0D
class c_CharacterDelete():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharSlot', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0E
class c_ProtocolVersion():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Version', 'i4')
              , ('256', '|S256')
                  ]
    return dtype
#--------------------------------------------------------------------------#0F
class c_MoveBackwardToLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ToX', 'i4')
              , ('ToY', 'i4')
              , ('ToZ', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
              , ('MoveMovement', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#11
class c_EnterWorld():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x11'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('a24', 'i4')
              , ('U_0', 'i4')
              , ('U_1', 'i4')
              , ('U_2', 'i4')
              , ('U_3', 'i4')
              , ('60', '|S60')
              , ('random', 'i4')
              , ('ip01', 'u1')
              , ('ip02', 'u1')
              , ('ip03', 'u1')
              , ('ip04', 'u1')
              , ('ip11', 'u1')
              , ('ip12', 'u1')
              , ('ip13', 'u1')
              , ('ip14', 'u1')
              , ('ip21', 'u1')
              , ('ip22', 'u1')
              , ('ip23', 'u1')
              , ('ip24', 'u1')
              , ('ip31', 'u1')
              , ('ip32', 'u1')
              , ('ip33', 'u1')
              , ('ip34', 'u1')
              , ('ip41', 'u1')
              , ('ip42', 'u1')
              , ('ip43', 'u1')
              , ('ip44', 'u1')
                  ]
    return dtype
#--------------------------------------------------------------------------#12
class c_CharacterSelect():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x12'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharSlot', 'i4')
              , ('Unknown_0', 'i2')
              , ('Unknown_1', 'i4')
              , ('Unknown_2', 'i4')
              , ('Unknown_3', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#13
class c_NewCharacter():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x13'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#14
class c_RequestItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x14'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#16
class c_RequestUnEquipItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x16'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Slot', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#17
class c_RequestDropItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x17'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Count', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#19
class c_UseItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x19'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1A
class c_TradeRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1B
class c_AddTradeItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TradeID', 'i4')
              , ('ObjectID', 'i4')
              , ('Count', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1C
class c_TradeDone():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1F
class c_Action():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
              , ('ActionID', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#23
class c_RequestBypassToServer():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x23'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Command', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#24
class c_RequestBBSwrite():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x24'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('URL', '|S'+str(self.It.__next__()) )
              , ('Argument1', '|S'+str(self.It.__next__()) )
              , ('Argument2', '|S'+str(self.It.__next__()) )
              , ('Argument3', '|S'+str(self.It.__next__()) )
              , ('Argument4', '|S'+str(self.It.__next__()) )
              , ('Argument5', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
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
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#26
class c_RequestJoinPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x26'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Target', 'i4')
              , ('PledgeType', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#27
class c_RequestAnswerJoinPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x27'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Answer', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#28
class c_RequestWithdrawalPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x28'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#29
class c_RequestOustPledgeMember():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x29'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Target', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#2B
class c_AuthLogin():
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
              , ('LoginName', '|S'+str(self.It.__next__()) )
              , ('PlayKey2', 'i4')
              , ('PlayKey1', 'i4')
              , ('LoginKey1', 'i4')
              , ('LoginKey2', 'i4')
              , ('Unknown_0', 'i4')
              , ('Unknown_1', 'i4')
              , ('Unknown_2', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#2C
class c_RequestGetItemFromPet():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Amount', 'i4')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2E
class c_RequestAllyInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#2F
class c_RequestCrystallizeItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Count', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#30
class c_RequestPrivateStoreManageSell():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x30'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#31
class c_SetPrivateStoreListSell():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x31'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Count', 'i4')
              , ('Price', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#34
class c_RequestSocialAction():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x34'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ActionGetFunc09', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#35
class c_ChangeMoveType2():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x35'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TypeRun', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#36
class c_ChangeWaitType2():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x36'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TypeStand', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#37
class c_RequestSellItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x37'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListID', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#38
class c_Unknown38():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x38'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Unknown_0', 'i4')
              , ('Unknown_1', 'i4')
              , ('Unknown_2', 'i2')
              , ('Unknown_3', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#39
class c_RequestMagicSkillUse():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x39'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('skillIDGetSkill', 'i4')
              , ('CtrlPressed', 'i4')
              , ('ShiftPressed', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#3A
class c_Appearing():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#3B
class c_SendWareHouseDepositList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3B'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#3C
class c_SendWareHouseWithDrawList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3C'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#3D
class c_RequestShortCutReg():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Type', 'i4')
              , ('Slot', 'i4')
              , ('ID', 'i4')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#3F
class c_RequestShortCutDel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#40
class c_RequestBuyItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x40'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListID', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#42
class c_RequestJoinParty():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x42'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('ItemDistribution', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#43
class c_RequestAnswerJoinParty():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x43'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#44
class c_RequestWithDrawalParty():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x44'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#45
class c_RequestOustPartyMember():
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
              , ('Name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#47
class c_CannotMoveAnymore():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x47'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#48
class c_RequestTargetCanceld():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x48'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Unselect', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#49
class c_Say2():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x49'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Text', '|S'+str(self.It.__next__()) )
              , ('Type', 'i4')
              , ('Target', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 4
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#4D
class c_RequestPledgeMemberList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#4F
class c_DummyPacket():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#50
class c_RequestSkillList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x50'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#52
class c_MoveWithDelta():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x52'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#53
class c_RequestGetOnVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x53'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('BoatObjID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#54
class c_RequestGetOffVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x54'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('BoatObjID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#55
class c_AnswerTradeRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x55'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Answer', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#56
class c_RequestActionUse():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x56'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ActionID', 'i4')
              , ('CtrlPressed', 'i4')
              , ('ShiftPressed', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#57
class c_RequestRestart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x57'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#58
class c_RequestSiegeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x58'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#59
class c_ValidatePosition():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x59'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('Data', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5E
class c_RequestShowBoard():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('FlagShow', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5F
class c_RequestEnchantItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#60
class c_RequestDestroyItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x60'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Count', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#62
class c_RequestQuestList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x62'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#63
class c_RequestQuestAbort():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x63'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('QuestID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#65
class c_RequestPledgeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x65'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ClanID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#66
class c_RequestPledgeExtendedInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x66'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('PledgeName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#67
class c_RequestPledgeCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x67'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CrestID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6B
class c_RequestSendFriendMsg():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6B'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Message', '|S'+str(self.It.__next__()) )
              , ('Reciever', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#6C
class c_RequestShowMiniMap():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#6E
class c_RequestRecordInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#6F
class c_RequestHennaEquip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SymbolID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#73
class c_RequestAcquireSkillInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x73'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('skillIDGetSkill', 'i4')
              , ('Level', 'i4')
              , ('Type', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#74
class c_SendBypassBuildCmd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x74'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Command', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#75
class c_RequestMoveToLocationInVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x75'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('BoatObjID', 'i4')
              , ('ToX', 'i4')
              , ('ToY', 'i4')
              , ('ToZ', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#76
class c_CannotMoveAnymoreInVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x76'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('BoatObjID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#77
class c_RequestFriendInvite():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x77'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#78
class c_RequestAnswerFriendInvite():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x78'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#79
class c_RequestFriendList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x79'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#7A
class c_RequestFriendDel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7A'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#7B
class c_CharacterRestore():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharSlot', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#7C
class c_RequestAcquireSkill():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('skillIDGetSkill', 'i4')
              , ('Level', 'i4')
              , ('Type', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#7D
class c_RequestRestartPoint():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PointType', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#7E
class c_RequestGMCommand():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7E'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('TargetName', '|S'+str(self.It.__next__()) )
              , ('Command', 'i4')
              , ('0', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#7F
class c_RequestPartyMatchConfig():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7F'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('AutomaticRegistration', 'i4')
              , ('ShowLevel', 'i4')
              , ('ShowClass', 'i4')
              , ('Memo', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#80
class c_RequestPartyMatchList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x80'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Status', 'i4')
              , ('Unknown_0', 'i4')
              , ('Unknown_1', 'i4')
              , ('Unknown_2', 'i4')
              , ('Unknown_3', 'i4')
              , ('Unknown', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 20
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#81
class c_RequestPartyMatchDetail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x81'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#83
class c_RequestPrivateStoreBuy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x83'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('StorePlayerID', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Count', 'i4')
              , ('Price', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#85
class c_RequestTutorialLinkHtml():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x85'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Bypass', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#86
class c_RequestTutorialPassCmdToServer():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x86'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Bypass', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#87
class c_RequestTutorialQuestionMark():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x87'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Number', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#88
class c_RequestTutorialClientEvent():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x88'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('EventID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#89
class c_RequestPetition():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x89'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Content', '|S'+str(self.It.__next__()) )
              , ('Type', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#8A
class c_RequestPetitionCancel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#8B
class c_RequestGmList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#8C
class c_RequestJoinAlly():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#8D
class c_RequestAnswerJoinAlly():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#8E
class c_AllyLeave():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#8F
class c_AllyDismiss():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8F'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ClanName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#90
class c_RequestDismissAlly():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x90'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#91
class c_RequestSetAllyCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x91'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CrestSize', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#92
class c_RequestAllyCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x92'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CrestID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#93
class c_RequestChangePetName():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x93'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#94
class c_RequestPetUseItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x94'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#95
class c_RequestGiveItemToPet():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x95'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Amount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#96
class c_RequestPrivateStoreQuitSell():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x96'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#97
class c_SetPrivateStoreMsgSell():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x97'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('StoreMsg', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#98
class c_RequestPetGetItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x98'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#99
class c_RequestPrivateStoreManageBuy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x99'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#9A
class c_SetPrivateStoreListBuy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9A'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemIDGetFunc01', 'i4')
              , ('h_0', 'i2')
              , ('h_1', 'i2')
              , ('Count', 'i4')
              , ('Price', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#9C
class c_RequestPrivateStoreQuitBuy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#9D
class c_SetPrivateStoreMsgBuy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9D'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('StoreMsg', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#9F
class c_RequestPrivateStoreSell():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9F'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('StorePlayerID', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('h_0', 'i2')
              , ('h_1', 'i2')
              , ('Count', 'i4')
              , ('Price', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#A6
class c_RequestSkillCoolTime():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#A7
class c_RequestPackageSendableItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A8
class c_RequestPackageSend():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA8'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ID', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#A9
class c_RequestBlock():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA9'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Type', 'i4')
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#AB
class c_RequestSiegeAttackerList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AC
class c_RequestSiegeDefenderList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AD
class c_RequestJoinSiege():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
              , ('IsAttacker', 'i4')
              , ('IsJoining', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AE
class c_RequestConfirmSiegeWaitingList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
              , ('ClanID', 'i4')
              , ('Approved', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B0
class c_MultiSellChoose():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ListID', 'i4')
              , ('EntryID', 'i4')
              , ('Amount', 'i4')
              , ('Enchantment', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#B1
class c_NetPing():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('kID', 'i4')
              , ('Unknown_0', 'i4')
              , ('Unknown_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B3
class c_RequestUserCommand():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Command', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B4
class c_SnoopQuit():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SnoopID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B5
class c_RequestRecipeBookOpen():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('isDwarvenCraft', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B6
class c_RequestRecipeBookDestroy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('RecipeID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B7
class c_RequestRecipeItemMakeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('RecipeID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B8
class c_RequestRecipeItemMakeSelf():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('RecipeID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#BA
class c_RequestRecipeShopMessageSet():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBA'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#BB
class c_RequestRecipeShopListSet():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBB'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('RecipeID', 'i4')
              , ('Cost', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#BC
class c_RequestRecipeShopManageQuit():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#BE
class c_RequestRecipeShopMakeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('RecipeID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#BF
class c_RequestRecipeShopMakeItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
              , ('RecipeID', 'i4')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C0
class c_RequestRecipeShopManagePrev():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#C1
class c_ObserverReturn():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#C2
class c_RequestEvaluate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TargetID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C3
class c_RequestHennaList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C4
class c_RequestHennaItemInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SymbolID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C5
class c_RequestBuySeed():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC5'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ManorID', 'i4')
              , ('CountValue', 'i4')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#C6
class c_DlgAnswer():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('MessageID', 'i4')
              , ('Answer', 'i4')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C7
class c_RequestWearItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC7'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Unknown', 'i4')
              , ('ListID', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemIDGetFunc01', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#C8
class c_RequestSSQStatus():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Page', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#CB
class c_GameGuardReply():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('i_0', 'i4')
              , ('i_1', 'i4')
              , ('i_2', 'i4')
              , ('i_3', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#CC
class c_RequestPledgePower():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Rank', 'i4')
              , ('Action', 'i4')
              , ('Privs', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#CD
class c_RequestMakeMacro():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCD'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('MacroID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Desc', '|S'+str(self.It.__next__()) )
              , ('Acronym', '|S'+str(self.It.__next__()) )
              , ('Icon', 'i1')
              , ('MacroCountValue', 'i1')
                  ]+ list(self.f_MacroCount()) +[
                  ]
    return dtype
  def f_MacroCount(self):
    for i in range(self.It.__next__()):
      dtype = ('MacroCount_' + str(i) , [
               ('Entry', 'i1')
              , ('Type', 'i1')
              , ('D1', 'i4')
              , ('D2', 'i1')
              , ('Command', '|S'+str(self.It.__next__()) )
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 1
   p = self.pck[i:i+1]
   count = struct.unpack('b', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 1
   for _ in range(count):
      i += 7
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
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
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 4
      s_len = len(self.lst[i])
      yield s_len
      i += 1
#--------------------------------------------------------------------------#CE
class c_RequestDeleteMacro():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('MacroID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#CF
class c_RequestBuyProcure():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCF'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListID', 'i4')
              , ('CountValue', 'i4')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('Servise', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#D039
class c_RequestGotoLobby():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x39\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D001
class c_RequestManorList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x01\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D002
class c_RequestProcureCropList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x02\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('ManorID', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#D003
class c_RequestSetSeed():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x03\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ManorID', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemIDGetFunc01', 'i4')
              , ('Sales', 'i4')
              , ('Price', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#D004
class c_RequestSetCrop():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x04\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ManorID', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemIDGetFunc01', 'i4')
              , ('Sales', 'i4')
              , ('Price', 'i4')
              , ('Type', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#D005
class c_RequestWriteHeroWords():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x05\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('HeroWords', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D006
class c_RequestExAskJoinMPCC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x06\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Name', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D007
class c_RequestExAcceptJoinMPCC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x07\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D008
class c_RequestExOustFromMPCC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x08\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Name', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D009
class c_RequestOustFromPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x09\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D00A
class c_RequestDismissPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x0A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Data1', 'i4')
              , ('Data2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D00B
class c_RequestWithdrawPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x0B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Data1', 'i4')
              , ('Data2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D00C
class c_RequestChangePartyLeader():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x0C\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Name', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D00D
class c_RequestAutoSoulShot():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x0D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ItemIDGetFunc01', 'i4')
              , ('Type', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D00E
class c_RequestExEnchantSkillInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x0E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Type', 'i4')
              , ('skillIDGetSkill', 'i4')
              , ('SkillLevel', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D00F
class c_RequestExEnchantSkill():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x0F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('skillIDGetSkill', 'i4')
              , ('SkillLevel', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D010
class c_RequestExPledgeCrestLarge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x10\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('CrestID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D011
class c_RequestExSetPledgeCrestLarge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x11\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('CrestSize', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D012
class c_RequestPledgeSetAcademyMaster():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x12\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Set', 'i4')
              , ('CurrentPlayerName', '|S'+str(self.It.__next__()) )
              , ('TargetPlayer', '|S'+str(self.It.__next__()) )
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
   i += 2
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#D013
class c_RequestPledgePowerGradeList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x13\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D014
class c_RequestPledgeMemberPowerInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x14\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Unknown', 'i4')
              , ('PlayerName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D015
class c_RequestPledgeSetMemberPowerGrade():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x15\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('MemberName', '|S'+str(self.It.__next__()) )
              , ('PowerGrade', 'i4')
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
#--------------------------------------------------------------------------#D016
class c_RequestPledgeMemberInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x16\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Unknown', 'i4')
              , ('PlayerName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D017
class c_RequestPledgeWarList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x17\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Unknown', 'i4')
              , ('Tab', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D018
class c_RequestExFishRanking():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x18\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D019
class c_RequestPCCafeCouponUse():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x19\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Unknown', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D01B
class c_RequestDuelStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x1B\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('PlayerName', '|S'+str(self.It.__next__()) )
              , ('PartyDuel', 'i4')
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
#--------------------------------------------------------------------------#D01C
class c_RequestDuelAnswerStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x1C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('PartyDuel', 'i4')
              , ('Unknown', 'i4')
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D01E
class c_RequestExRqItemLink():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x1E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D021
class c_RequestKeyMapping():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x21\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D024
class c_RequestSaveInventoryOrder():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x24\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Order', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#D025
class c_RequestExitPartyMatchingWaitingRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x25\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D026
class c_RequestConfirmTargetItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x26\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D027
class c_RequestConfirmRefinerItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x27\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('TargetItemObjID', 'i4')
              , ('RefinerItemObjID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D028
class c_RequestConfirmGemStone():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x28\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('TargetItemObjID', 'i4')
              , ('RefinerItemObjID', 'i4')
              , ('GemStoneItemObjID', 'i4')
              , ('GemStoneCount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D029
class c_RequestOlympiadObserverEnd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x29\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D02A
class c_RequestCursedWeaponList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x2A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D02B
class c_RequestCursedWeaponLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x2B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D02C
class c_RequestPledgeReorganizeMember():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x2C\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Unknown', 'i4')
              , ('MemberName', '|S'+str(self.It.__next__()) )
              , ('PledgeType', 'i4')
              , ('Unknown', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 4
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#D02E
class c_RequestExMPCCShowPartyMembersInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x2E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D02F
class c_RequestOlympiadMatchList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x2F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D030
class c_RequestAskJoinPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x30\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('PlayerName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D031
class c_AnswerJoinPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x31\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('RequesterID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D032
class c_RequestListPartyMatchingWaitingRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x32\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D033
class c_RequestExEnchantSkillSafe():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x33\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('skillIDGetSkill', 'i4')
              , ('SkillLevel', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D034
class c_RequestExEnchantSkillUntrain():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x34\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('skillIDGetSkill', 'i4')
              , ('SkillLevel', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D035
class c_RequestExEnchantSkillRouteChange():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x35\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('skillIDGetSkill', 'i4')
              , ('SkillLevel', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D036
class c_ExGetOnAirShip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x36\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('ShipID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D03F
class c_RequestAllCastleInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x3F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D040
class c_RequestAllFortressInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x40\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D041
class c_RequestAllAgitInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x41\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D042
class c_RequestFortressSiegeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x42\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D043
class c_RequestGetBossRecord():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x43\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('BossID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D044
class c_RequestRefine():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x44\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('TargetItemObjID', 'i4')
              , ('RefinerItemObjID', 'i4')
              , ('GemStoneItemObjID', 'i4')
              , ('GemStoneCount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D045
class c_RequestConfirmCancelItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x45\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ItemIDGetFunc01', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D046
class c_RequestRefineCancel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x46\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('TargetItemObjID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D047
class c_RequestExMagicSkillUseGround():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x47\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('skillIDGetSkill', 'i4')
              , ('CtrlPressed', 'i4')
              , ('ShiftPressed', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#D048
class c_RequestDuelSurrender():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x48\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D049
class c_RequestExEnchantSkillInfoDetail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x49\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Type', 'i4')
              , ('skillIDGetSkill', 'i4')
              , ('SkillLevel', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D04E
class c_RequestExCancelAbnormalState():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x4E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('skillIDGetSkill', 'i4')
              , ('SkillLevel', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#00
class s_Die():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('1', 'i4')
              , ('ToHideout', 'i4')
              , ('ToCastle', 'i4')
              , ('ToSiegeHQ', 'i4')
              , ('Sweepable', 'i4')
              , ('RespawnFixed', 'i4')
              , ('ToFortess', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01
class s_Revive():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#05
class s_SpawnItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x05'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Stackable', 'i4')
              , ('Count', 'i4')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#06
class s_SellList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x06'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Money', 'i4')
              , ('Lease', 'i4')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
               ('DefAttrUnholy', 'i4')
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemType1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('ItemType2', 'i2')
              , ('0_0', 'i2')
              , ('ItemBodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('0_1', 'i2')
              , ('0_2', 'i2')
              , ('ReferencePrice2', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#07
class s_BuyList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x07'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Money', 'i4')
              , ('ListID', 'i4')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemType1', 'i2')
              , ('0_0', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('CurrentCount', 'i4')
              , ('ItemType2', 'i2')
              , ('0_1', 'i2')
              , ('BodyPart', 'i4')
              , ('0_2', 'i2')
              , ('0_3', 'i2')
              , ('0_4', 'i2')
              , ('PriceTaxRate', 'i4')
              , ('0_5', 'i4')
              , ('0_6', 'i4')
              , ('0_7', 'i4')
              , ('0_8', 'i4')
              , ('0_9', 'i4')
              , ('0_10', 'i4')
              , ('0_11', 'i4')
              , ('0_12', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#08
class s_DeleteObject():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x08'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#09
class s_CharSelectionInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x09'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i4')
              , ('7', 'i4')
              , ('0', 'i1')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('Name', '|S'+str(self.It.__next__()) )
              , ('CharID', 'i4')
              , ('LoginName', '|S'+str(self.It.__next__()) )
              , ('SessionID', 'i4')
              , ('ClanID', 'i4')
              , ('0_0', 'i4')
              , ('Sex', 'i4')
              , ('Race', 'i4')
              , ('ClassIDGetClassID_0', 'i4')
              , ('1', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('CurrentHP', 'f8')
              , ('CurrentMP', 'f8')
              , ('SP', 'i4')
              , ('Exp', 'i8')
              , ('Level', 'i4')
              , ('Karma', 'i4')
              , ('PkKills', 'i4')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('0_4', 'i4')
              , ('0_5', 'i4')
              , ('0_6', 'i4')
              , ('0_7', 'i4')
              , ('0_8', 'i4')
              , ('Unknown_0', 'i4')
              , ('RightEarring', 'i4')
              , ('LeftEarring', 'i4')
              , ('Necklace', 'i4')
              , ('RightRing', 'i4')
              , ('LeftRing', 'i4')
              , ('Head', 'i4')
              , ('RightHand', 'i4')
              , ('LeftHand', 'i4')
              , ('Gloves', 'i4')
              , ('Chest', 'i4')
              , ('Legs', 'i4')
              , ('Boots', 'i4')
              , ('Unknown_1', 'i4')
              , ('Unknown_2', 'i4')
              , ('Hair', 'i4')
              , ('Face_0', 'i4')
              , ('Unknown_3', 'i4')
              , ('Unknown_4', 'i4')
              , ('0_9', 'i4')
              , ('0_10', 'i4')
              , ('0_11', 'i4')
              , ('0_12', 'i4')
              , ('0_13', 'i4')
              , ('0_14', 'i4')
              , ('HairStyle', 'i4')
              , ('HairColor', 'i4')
              , ('Face_1', 'i4')
              , ('MaxHP', 'f8')
              , ('MaxMP', 'f8')
              , ('DeleteDays', 'i4')
              , ('ClassIDGetClassID_1', 'i4')
              , ('ActiveID', 'i4')
              , ('EnchantEffect', 'i1')
              , ('AugmentIDGetAugmentID', 'i4')
              , ('TransformID', 'i4')
              , ('0_15', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 9
   for _ in range(count):
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 265
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
   pointer_list_in = self.lst
   self.lst = []
   def it(lst_in, lst_out):
     for i in lst_in:
       if isinstance(i ,tuple):
         it(i, lst_out)
       else: lst_out.append(i)
   it(pointer_list_in, self.lst)
   i += 3
   for _ in range(count):
      s_len = len(self.lst[i])
      yield s_len
      i += 2
      s_len = len(self.lst[i])
      yield s_len
      i += 63
#--------------------------------------------------------------------------#0A
class s_LoginFail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ErrorCode', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0B
class s_CharSelected():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0B'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('CharID', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('SessionID', 'i4')
              , ('ClanID', 'i4')
              , ('0_0', 'i4')
              , ('Sex', 'i4')
              , ('Race', 'i4')
              , ('ClassIDGetClassID_0', 'i4')
              , ('1', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('CurrentHP', 'f8')
              , ('CurrentMP', 'f8')
              , ('SP', 'i4')
              , ('Exp', 'i8')
              , ('Level', 'i4')
              , ('Karma', 'i4')
              , ('PkKills', 'i4')
              , ('INT', 'i4')
              , ('STR', 'i4')
              , ('CON', 'i4')
              , ('MEN', 'i4')
              , ('DEX', 'i4')
              , ('WIT', 'i4')
              , ('GameTime', 'i4')
              , ('0_1', 'i4')
              , ('ClassIDGetClassID_1', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('0_4', 'i4')
              , ('0_5', 'i4')
              , ('64', '|S64')
              , ('0_6', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 4
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0C
class s_NpcInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0C'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('NpcTypeIdGetNpcId', 'i4')
              , ('IsAttackable', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('0_0', 'i4')
              , ('MatkSpd', 'i4')
              , ('PatkSpd', 'i4')
              , ('RunSpd', 'i4')
              , ('WalkSpd', 'i4')
              , ('SwimRunSpd', 'i4')
              , ('SwimWalkSpd', 'i4')
              , ('FlRunSpd', 'i4')
              , ('FlWalkSpd', 'i4')
              , ('FlyRunSpd', 'i4')
              , ('FlyWalkSpd', 'i4')
              , ('MoveMultiplier', 'f8')
              , ('AtkSpdMultiplier', 'f8')
              , ('CollisionRadius_0', 'f8')
              , ('CollisionHeight_0', 'f8')
              , ('IDRhand', 'i4')
              , ('0_1', 'i4')
              , ('IDLhand', 'i4')
              , ('1', 'i1')
              , ('isRunning', 'i1')
              , ('isInCombat', 'i1')
              , ('isALikeDead', 'i1')
              , ('Invisible', 'i1')
              , ('VisibleName', '|S'+str(self.It.__next__()) )
              , ('VisibleTitle', '|S'+str(self.It.__next__()) )
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('0_4', 'i4')
              , ('AbnormalEffect', 'i4')
              , ('ClanID', 'i4')
              , ('CrestID', 'i4')
              , ('0_5', 'i4')
              , ('0_6', 'i4')
              , ('0_7', 'i1')
              , ('Team', 'i1')
              , ('CollisionRadius_1', 'f8')
              , ('CollisionHeight_1', 'f8')
              , ('0_8', 'i4')
              , ('0_9', 'i4')
              , ('0_10', 'i4')
              , ('0_11', 'i4')
              , ('01_0', 'i1')
              , ('01_1', 'i1')
              , ('0_12', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 121
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 30
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#0D
class s_NewCharacterSuccess():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0D'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('Race', 'i4')
              , ('ClassIDGetClassID', 'i4')
              , ('70_0', 'i4')
              , ('BaseSTR', 'i4')
              , ('10_0', 'i4')
              , ('70_1', 'i4')
              , ('BaseDEX', 'i4')
              , ('10_1', 'i4')
              , ('70_2', 'i4')
              , ('BaseCON', 'i4')
              , ('10_2', 'i4')
              , ('70_3', 'i4')
              , ('BaseINT', 'i4')
              , ('10_3', 'i4')
              , ('70_4', 'i4')
              , ('BaseWIT', 'i4')
              , ('10_4', 'i4')
              , ('70_5', 'i4')
              , ('BaseMEN', 'i4')
              , ('10_5', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#0F
class s_CharCreateOk():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#10
class s_CharCreateFail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x10'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ErrorCode', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#11
class s_ItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x11'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ShowWindow', 'i2')
              , ('ItemCountValue', 'i2')
                  ]+ list(self.f_ItemCount()) +[
                  ]
    return dtype
  def f_ItemCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemCount_' + str(i) , [
               ('ItemTypeID', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('LocationSlot', 'i4')
              , ('Amount', 'i8')
              , ('ItemType2', 'i2')
              , ('CustomType1', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('CustType2', 'i2')
              , ('AugmentIDGetAugmentID', 'i4')
              , ('Mana', 'i4')
              , ('AttackElement', 'i2')
              , ('AttackElementPower', 'i2')
              , ('FireDefElementPower', 'i2')
              , ('WaterDefElementPower', 'i2')
              , ('WindDefElementPower', 'i2')
              , ('EarthDefElementPower', 'i2')
              , ('HolyDefElementPower', 'i2')
              , ('UnholyDefElementPower', 'i2')
              , ('RemainingTime', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#12
class s_SunRise():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x12'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#13
class s_SunSet():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x13'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#14
class s_TradeStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x14'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemType1', 'i2')
              , ('ObjectId', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('ItemType2', 'i2')
              , ('0_0', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('0_1', 'i2')
              , ('0_2', 'i2')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#16
class s_DropItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x16'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PlayerID', 'i4')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Stackable', 'i4')
              , ('Count', 'i8')
              , ('1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#17
class s_GetItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x17'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PlayerID', 'i4')
              , ('ObjectID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#18
class s_StatusUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x18'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('AttribCountValue', 'i4')
                  ]+ list(self.f_AttribCount()) +[
                  ]
    return dtype
  def f_AttribCount(self):
    for i in range(self.It.__next__()):
      dtype = ('AttribCount_' + str(i) , [
               ('AttrIDGetFSup', 'i4')
              , ('AttrValue', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#19
class s_NpcHtmlMessage():
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
              , ('ID', 'i4')
              , ('HTML', '|S'+str(self.It.__next__()) )
              , ('0', 'i4')
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#1A
class s_TradeOwnAdd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('1', 'i2')
              , ('ItemType1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('ItemType2', 'i2')
              , ('0_0', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('0_1', 'i2')
              , ('h', 'i2')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1B
class s_TradeOtherAdd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('1', 'i2')
              , ('ItemType1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('ItemType2', 'i2')
              , ('0_0', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('0_1', 'i2')
              , ('h', 'i2')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1C
class s_TradeDone():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Num', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1D
class s_CharDeleteSuccess():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#1E
class s_CharDeleteFail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ErrorCode', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1F
class s_ActionFailed():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#20
class s_ServerClose():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x20'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#21
class s_InventoryUpdate():
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
              , ('CountValue', 'i2')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('UpdateType', 'i2')
              , ('ItemType1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('LocationSlot', 'i4')
              , ('Quantity', 'i4')
              , ('ItemType2', 'i2')
              , ('CustomType1', 'i2')
              , ('Equipped', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('CustType2', 'i2')
              , ('AugmentIDGetAugmentID', 'i2')
              , ('0_0', 'i2')
              , ('Mana', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
              , ('0_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#22
class s_TeleportToLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x22'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TargetID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#23
class s_TargetSelected():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x23'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('TargetID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#24
class s_TargetUnselected():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x24'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TargetID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#25
class s_AutoAttackStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x25'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TargetID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#26
class s_AutoAttackStop():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x26'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TargetID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#27
class s_SocialAction():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x27'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('ActionGetFunc09', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#28
class s_ChangeMoveType():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x28'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('Running', 'i4')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#29
class s_ChangeWaitType():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x29'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('MoveType', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2A
class s_ManagePledgePower():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('Privs', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2C
class s_AskJoinPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2C'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('RequestorID', 'i4')
              , ('PledgeName', '|S'+str(self.It.__next__()) )
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#2D
class s_JoinPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PledgeID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2E
class s_KeyPacket():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('1_0', 'i1')
              , ('16', '|S16')
              , ('1_1', 'i4')
              , ('1_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2F
class s_MoveToLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('ToX', 'i4')
              , ('ToY', 'i4')
              , ('ToZ', 'i4')
              , ('OriginX', 'i4')
              , ('OriginY', 'i4')
              , ('OriginZ', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#30
class s_SummonSay():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x30'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('ChatID', 'i4')
              , ('SummonNpcIDGetNpcId', 'i4')
              , ('Msg', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#31
class s_CharInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x31'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('ObjectID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Race', 'i4')
              , ('Sex', 'i4')
              , ('ClassIDGetClassID', 'i4')
              , ('Unknown_0', 'i4')
              , ('Head', 'i4')
              , ('RightHand', 'i4')
              , ('LeftHand', 'i4')
              , ('Gloves', 'i4')
              , ('Chest', 'i4')
              , ('Legs', 'i4')
              , ('Boots', 'i4')
              , ('Unknown_1', 'i4')
              , ('Unknown_2', 'i4')
              , ('Hair', 'i4')
              , ('Face_0', 'i4')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('0_4', 'i4')
              , ('0_5', 'i4')
              , ('0_6', 'i4')
              , ('0_7', 'i4')
              , ('0_8', 'i2')
              , ('0_9', 'i2')
              , ('0_10', 'i2')
              , ('0_11', 'i2')
              , ('AugmentIDGetAugmentID', 'i2')
              , ('0_12', 'i2')
              , ('0_13', 'i2')
              , ('0_14', 'i2')
              , ('0_15', 'i2')
              , ('0_16', 'i2')
              , ('0_17', 'i2')
              , ('0_18', 'i2')
              , ('0_19', 'i2')
              , ('0_20', 'i2')
              , ('0_21', 'i2')
              , ('0_22', 'i2')
              , ('0_23', 'i2')
              , ('0_24', 'i2')
              , ('Unknown_3', 'i4')
              , ('0_25', 'i2')
              , ('0_26', 'i2')
              , ('0_27', 'i2')
              , ('0_28', 'i2')
              , ('0_29', 'i2')
              , ('0_30', 'i2')
              , ('0_31', 'i2')
              , ('0_32', 'i2')
              , ('0_33', 'i2')
              , ('0_34', 'i2')
              , ('0_35', 'i2')
              , ('0_36', 'i2')
              , ('0_37', 'i2')
              , ('0_38', 'i2')
              , ('0_39', 'i2')
              , ('0_40', 'i2')
              , ('0_41', 'i2')
              , ('0_42', 'i2')
              , ('0_43', 'i2')
              , ('0_44', 'i2')
              , ('0_45', 'i2')
              , ('0_46', 'i2')
              , ('0_47', 'i2')
              , ('0_48', 'i2')
              , ('PvpFlag_0', 'i4')
              , ('Karma_0', 'i4')
              , ('CastSpd', 'i4')
              , ('AtkSpd', 'i4')
              , ('PvpFlag_1', 'i4')
              , ('Karma_1', 'i4')
              , ('RunSpd', 'i4')
              , ('WalkSpd', 'i4')
              , ('SwimRunSpd', 'i4')
              , ('SwimWalkSpd', 'i4')
              , ('FlRunSpd', 'i4')
              , ('FlWalkSpd', 'i4')
              , ('FlyRunSpd', 'i4')
              , ('FlyWalkSpd', 'i4')
              , ('MoveMultiplier', 'f8')
              , ('AtkSpdMultiplier', 'f8')
              , ('CollisionRadius', 'f8')
              , ('CollisionHeight', 'f8')
              , ('HairStyle', 'i4')
              , ('HairColor', 'i4')
              , ('Face_1', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('ClanID', 'i4')
              , ('ClanCrestID', 'i4')
              , ('AllyID', 'i4')
              , ('AllyCrestID', 'i4')
              , ('0_49', 'i4')
              , ('isSitting', 'i1')
              , ('isRunning', 'i1')
              , ('isInCombat', 'i1')
              , ('isAlikeDead', 'i1')
              , ('Invisible', 'i1')
              , ('MountType', 'i1')
              , ('PrivateStoreType', 'i1')
              , ('CubicsSizeValue', 'i2')
                  ]+ list(self.f_CubicsSize()) +[
               ('0_50', 'i1')
              , ('AbnormalEffect', 'i4')
              , ('RecomLeft', 'i1')
              , ('RecomHave', 'i2')
              , ('MountNpcID', 'i4')
              , ('MaxCP', 'i4')
              , ('CurrentCP', 'i4')
              , ('isMount', 'i1')
              , ('Team', 'i1')
              , ('ClanCrestLargeID', 'i4')
              , ('isNoble', 'i1')
              , ('isHero', 'i1')
              , ('isFishing', 'i1')
              , ('FishX', 'i4')
              , ('FishY', 'i4')
              , ('FishZ', 'i4')
              , ('NameColor', 'i4')
              , ('0_51', 'i4')
              , ('PledgeClass', 'i4')
              , ('0_52', 'i4')
              , ('TitleColor', 'i4')
              , ('CursedWeapon', 'i4')
              , ('0_53', 'i4')
              , ('TranformationID', 'i4')
                  ]
    return dtype
  def f_CubicsSize(self):
    for i in range(self.It.__next__()):
      dtype = ('CubicsSize_' + str(i) , [
               ('CubicID', 'i2')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 20
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 280
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 27
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 88
   s_len = len(self.lst[i])
   yield s_len
   i += 13
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#32
class s_UserInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x32'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('isInAirShip', 'i4')
              , ('ObjectID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Race', 'i4')
              , ('Sex', 'i4')
              , ('ClassIDGetClassID_0', 'i4')
              , ('Level', 'i4')
              , ('Exp', 'i8')
              , ('STR', 'i4')
              , ('DEX', 'i4')
              , ('CON', 'i4')
              , ('INT', 'i4')
              , ('WIT', 'i4')
              , ('MEN', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrentHP', 'i4')
              , ('MaxMP', 'i4')
              , ('CurrentMP', 'i4')
              , ('Sp', 'i4')
              , ('CurrentLoad', 'i4')
              , ('MaxLoad', 'i4')
              , ('WeaponEquipment', 'i4')
              , ('OIDUnder', 'i4')
              , ('OIDRear', 'i4')
              , ('OIDLear', 'i4')
              , ('OIDNeck', 'i4')
              , ('OIDFinger', 'i4')
              , ('OIDLfinger', 'i4')
              , ('OIDHead', 'i4')
              , ('OIDRhand', 'i4')
              , ('OIDLhand', 'i4')
              , ('OIDGloves', 'i4')
              , ('OIDChest', 'i4')
              , ('OIDLegs', 'i4')
              , ('OIDFeet', 'i4')
              , ('OIDBack', 'i4')
              , ('OIDLrhand', 'i4')
              , ('OIDHair', 'i4')
              , ('OIDHair2', 'i4')
              , ('OIDRbracelet', 'i4')
              , ('OIDLbracelet', 'i4')
              , ('OIDDeco', 'i4')
              , ('OIDDeco2', 'i4')
              , ('OIDDeco3', 'i4')
              , ('OIDDeco4', 'i4')
              , ('OIDDeco5', 'i4')
              , ('OIDDeco6', 'i4')
              , ('OIDBelt', 'i4')
              , ('IDUnder', 'i4')
              , ('IDRear', 'i4')
              , ('IDLear', 'i4')
              , ('IDNeck', 'i4')
              , ('IDFinger', 'i4')
              , ('IDLfinger', 'i4')
              , ('IDHead', 'i4')
              , ('IDRhand', 'i4')
              , ('IDLhand', 'i4')
              , ('IDGloves', 'i4')
              , ('IDChest', 'i4')
              , ('IDLegs', 'i4')
              , ('IDFeet', 'i4')
              , ('IDBack', 'i4')
              , ('IDLrhand', 'i4')
              , ('IDHair', 'i4')
              , ('IDHair2', 'i4')
              , ('IDRbracelet', 'i4')
              , ('IDLbracelet', 'i4')
              , ('IDDeco', 'i4')
              , ('IDDeco2', 'i4')
              , ('IDDeco3', 'i4')
              , ('IDDeco4', 'i4')
              , ('IDDeco5', 'i4')
              , ('IDDeco6', 'i4')
              , ('IDBelt', 'i4')
              , ('AugIDUnder', 'i4')
              , ('AugIDRear', 'i4')
              , ('AugIDLear', 'i4')
              , ('AugIDNeck', 'i4')
              , ('AugIDFinger', 'i4')
              , ('AugIDLfinger', 'i4')
              , ('AugIDHead', 'i4')
              , ('AugIDRhand', 'i4')
              , ('AugIDLhand', 'i4')
              , ('AugIDGloves', 'i4')
              , ('AugIDChest', 'i4')
              , ('AugIDLegs', 'i4')
              , ('AugIDFeet', 'i4')
              , ('AugIDBack', 'i4')
              , ('AugIDLrhand', 'i4')
              , ('AugIDHair', 'i4')
              , ('AugIDHair2', 'i4')
              , ('AugIDRbracelet', 'i4')
              , ('AugIDLbracelet', 'i4')
              , ('AugIDDeco', 'i4')
              , ('AugIDDeco2', 'i4')
              , ('AugIDDeco3', 'i4')
              , ('AugIDDeco4', 'i4')
              , ('AugIDDeco5', 'i4')
              , ('AugIDDeco6', 'i4')
              , ('AugIDBelt', 'i4')
              , ('TalismanSlots', 'i4')
              , ('01', 'i4')
              , ('Patk', 'i4')
              , ('PatkSpd_0', 'i4')
              , ('Pdef', 'i4')
              , ('EvasionRate', 'i4')
              , ('Accuracy', 'i4')
              , ('CriticalHit', 'i4')
              , ('Matk', 'i4')
              , ('MatkSpd', 'i4')
              , ('PatkSpd_1', 'i4')
              , ('Mdef', 'i4')
              , ('PvPFlag', 'i4')
              , ('Karma', 'i4')
              , ('RunSpd', 'i4')
              , ('WalkSpd', 'i4')
              , ('SwimRunSpd', 'i4')
              , ('SwimWalkSpd', 'i4')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('FlyRunSpd', 'i4')
              , ('FlyWalkSpd', 'i4')
              , ('MoveMul', 'f8')
              , ('AtkSpeedMul', 'f8')
              , ('ColRadius', 'f8')
              , ('ColHeight', 'f8')
              , ('HairStyle', 'i4')
              , ('HairColor', 'i4')
              , ('Face', 'i4')
              , ('isGM', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('ClanID', 'i4')
              , ('ClanCrestID', 'i4')
              , ('AllyID', 'i4')
              , ('AllyCrestID', 'i4')
              , ('Relation', 'i4')
              , ('MounType', 'i1')
              , ('PrivateStoreType', 'i1')
              , ('DwarvenCraft', 'i1')
              , ('PkKills', 'i4')
              , ('PvpKills', 'i4')
              , ('CubicsSizeValue', 'i2')
                  ]+ list(self.f_CubicsSize()) +[
               ('0_2', 'i1')
              , ('AbnormalEffect', 'i4')
              , ('FlayingMounted', 'i1')
              , ('ClanPrivileges', 'i4')
              , ('RecomLeft', 'i2')
              , ('RecomHave', 'i2')
              , ('MountNpcID', 'i4')
              , ('InventoryLimit', 'i2')
              , ('ClassIDGetClassID_1', 'i4')
              , ('0_3', 'i4')
              , ('MaxCP', 'i4')
              , ('CurrentCP', 'i4')
              , ('isMount', 'i1')
              , ('Team', 'i1')
              , ('ClanCrestLargeID', 'i4')
              , ('isNoble', 'i1')
              , ('isHero', 'i1')
              , ('isFishing', 'i1')
              , ('FishingX', 'i4')
              , ('FishingY', 'i4')
              , ('FishingZ', 'i4')
              , ('NameColor', 'i4')
              , ('isRunning', 'i1')
              , ('PledgeClass', 'i4')
              , ('PledgeType', 'i4')
              , ('TitleColor', 'i4')
              , ('CursedWeaponEquipID', 'i4')
              , ('TranformationID', 'i4')
              , ('AtkElementAttr', 'i2')
              , ('AttackElementVal', 'i2')
              , ('DefAttrFire', 'i2')
              , ('DefAttrWater', 'i2')
              , ('DefAttrWind', 'i2')
              , ('DefAttrEarth', 'i2')
              , ('DefAttrHoly', 'i2')
              , ('DefAttrDark', 'i2')
              , ('AgathionId', 'i4')
              , ('Fame', 'i4')
              , ('Unknown', 'i4')
              , ('VitalityPoints', 'i4')
              , ('0_4', 'i4')
              , ('0_5', 'i4')
              , ('0_6', 'i4')
              , ('0_7', 'i4')
                  ]
    return dtype
  def f_CubicsSize(self):
    for i in range(self.It.__next__()):
      dtype = ('CubicsSize_' + str(i) , [
               ('CubicID', 'i2')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 20
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 528
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 31
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 128
   s_len = len(self.lst[i])
   yield s_len
   i += 11
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#33
class s_Attack():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x33'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('AttackerID', 'i4')
              , ('TargetID', 'i4')
              , ('Damage', 'i4')
              , ('Flags', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('HitsSizeValue', 'i2')
                  ]+ list(self.f_HitsSize()) +[
                  ]
    return dtype
  def f_HitsSize(self):
    for i in range(self.It.__next__()):
      dtype = ('HitsSize_' + str(i) , [
               ('TargetID', 'i4')
              , ('Damage', 'i4')
              , ('Flags', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 25
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 7
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#39
class s_AskJoinParty():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x39'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('RequestorName', '|S'+str(self.It.__next__()) )
              , ('ItemDistribution', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#3A
class s_JoinParty():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#40
class s_Unknown40():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x40'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Unknown_0', 'i4')
              , ('Unknown_1', 'i4')
              , ('Unknown_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#41
class s_WareHouseDepositList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x41'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('WhType', 'i2')
              , ('PlayerAdena', 'i4')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
               ('DefAttrUnholy', 'i4')
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemType1', 'i2')
              , ('ObjectID_0', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('ItemType2', 'i2')
              , ('CustomType1', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('CustomType2', 'i2')
              , ('0_0', 'i2')
              , ('ObjectID_1', 'i4')
              , ('AugmentIDGetAugmentID_0', 'i2')
              , ('0_1', 'i2')
              , ('AugmentIDGetAugmentID_1', 'i2')
              , ('0_2', 'i2')
              , ('Mana', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#42
class s_WareHouseWithdrawList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x42'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('WhType', 'i2')
              , ('PlayerAdena', 'i4')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
               ('DefAttrUnholy', 'i4')
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemType1', 'i2')
              , ('ObjectID_0', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('ItemType2', 'i2')
              , ('CustomType1', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('CustomType2', 'i2')
              , ('0_0', 'i2')
              , ('ObjectID_1', 'i4')
              , ('AugmentIDGetAugmentID_0', 'i2')
              , ('0_1', 'i2')
              , ('AugmentIDGetAugmentID_1', 'i2')
              , ('0_2', 'i2')
              , ('Mana', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#44
class s_ShortCutRegister():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x44'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#47
class s_StopMove():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x47'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#48
class s_MagicSkillUse():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x48'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('TargetID', 'i4')
              , ('skillIDGetSkill', 'i4')
              , ('SkillLevel', 'i4')
              , ('HitTime', 'i4')
              , ('ReuseDelay', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Unknown', 'i4')
              , ('TargetX', 'i4')
              , ('TargetY', 'i4')
              , ('TargetZ', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#49
class s_MagicSkillCanceled():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x49'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#4A
class s_CreatureSay():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4A'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('TextType', 'i4')
              , ('CharName', '|S'+str(self.It.__next__()) )
              , ('Text', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
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
#--------------------------------------------------------------------------#4B
class s_EquipUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Change', 'i4')
              , ('ObjectID', 'i4')
              , ('BodyPart', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#4C
class s_DoorInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('DoorID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#4D
class s_DoorStatusUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Open', 'i4')
              , ('Damage', 'i4')
              , ('Enemy', 'i4')
              , ('DoorID', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrentHP', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#4E
class s_PartySmallWindowAll():
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
              , ('LeaderObjectID', 'i4')
              , ('LootDistribution', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('MemberObjId', 'i4')
              , ('MemberName', '|S'+str(self.It.__next__()) )
              , ('CurrentCP', 'i4')
              , ('MaxCP', 'i4')
              , ('CurrentHP', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrentMP', 'i4')
              , ('MaxMP', 'i4')
              , ('Level', 'i4')
              , ('ClassIDGetClassID', 'i4')
              , ('0_0', 'i4')
              , ('Race', 'i4')
              , ('0_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 44
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 12
#--------------------------------------------------------------------------#4F
class s_PartySmallWindowAdd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4F'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('LeaderObjectID', 'i4')
              , ('d', 'i4')
              , ('MemberObjID', 'i4')
              , ('MemberName', '|S'+str(self.It.__next__()) )
              , ('CurrentCP', 'i4')
              , ('MaxCP', 'i4')
              , ('CurrentHP', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrentMP', 'i4')
              , ('MaxMP', 'i4')
              , ('Level', 'i4')
              , ('ClassIDGetClassID', 'i4')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#50
class s_PartySmallWindowDeleteAll():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x50'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#51
class s_PartySmallWindowDelete():
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
              , ('MemberObjID', 'i4')
              , ('MemberName', '|S'+str(self.It.__next__()) )
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#52
class s_PartySmallWindowUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x52'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('MemberObjId', 'i4')
              , ('MemberName', '|S'+str(self.It.__next__()) )
              , ('CurrentCP', 'i4')
              , ('MaxCP', 'i4')
              , ('CurrentHP', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrentMP', 'i4')
              , ('MaxMP', 'i4')
              , ('Level', 'i4')
              , ('ClassIDGetClassID', 'i4')
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#54
class s_MagicSkillLaunched():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x54'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CasterObjectID', 'i4')
              , ('SkillIDGetSkill', 'i4')
              , ('SkillLevel', 'i4')
              , ('numberOfTargets', 'i4')
              , ('TargetID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5A
class s_PledgeShowMemberListAll():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5A'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('MainOrSubPledge', 'i4')
              , ('ClanID', 'i4')
              , ('PledgeType', 'i4')
              , ('ClanName', '|S'+str(self.It.__next__()) )
              , ('LeaderName', '|S'+str(self.It.__next__()) )
              , ('ClanCrestID', 'i4')
              , ('ClanLevel', 'i4')
              , ('HasCastle', 'i4')
              , ('HasHideOut', 'i4')
              , ('0_0', 'i4')
              , ('Rank', 'i4')
              , ('ReputationScore', 'i4')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
              , ('AllyID', 'i4')
              , ('AllyName', '|S'+str(self.It.__next__()) )
              , ('AllyCrestID', 'i4')
              , ('isAtWar', 'i4')
              , ('SubPledgeMembersCountValue', 'i4')
                  ]+ list(self.f_SubPledgeMembersCount()) +[
                  ]
    return dtype
  def f_SubPledgeMembersCount(self):
    for i in range(self.It.__next__()):
      dtype = ('SubPledgeMembersCount_' + str(i) , [
               ('MemberName', '|S'+str(self.It.__next__()) )
              , ('MemberLevel', 'i4')
              , ('MemberClassIDGetClassID', 'i4')
              , ('Sex', 'i4')
              , ('Race', 'i4')
              , ('MemberObjID', 'i4')
              , ('Sponsor', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 40
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 24
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 11
   s_len = len(self.lst[i])
   yield s_len
   i += 3
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 7
#--------------------------------------------------------------------------#5B
class s_PledgeShowMemberListUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5B'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Level', 'i4')
              , ('ClassIDGetClassID', 'i4')
              , ('Sex', 'i4')
              , ('Race', 'i4')
              , ('ObjectID', 'i4')
              , ('PledgeType', 'i4')
              , ('Sponsor', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#5C
class s_PledgeShowMemberListAdd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5C'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Level', 'i4')
              , ('ClassIDGetClassID', 'i4')
              , ('0', 'i4')
              , ('1', 'i4')
              , ('isOnLine', 'i4')
              , ('PledgeType', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#5D
class s_PledgeShowMemberListDelete():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5D'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#5F
class s_SkillList():
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
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('isPassive', 'i4')
              , ('Level', 'i4')
              , ('skillIDGetSkill', 'i4')
              , ('c', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#60
class s_VehicleInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x60'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('BoatObjID', 'i4')
              , ('BoatX', 'i4')
              , ('BoatY', 'i4')
              , ('BoatZ', 'i4')
              , ('BoatHeading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#61
class s_StopRotation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x61'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('Degree', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#63
class s_StartPledgeWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x63'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('PlayerName', '|S'+str(self.It.__next__()) )
              , ('PledgeName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#65
class s_StopPledgeWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x65'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('PledgeName', '|S'+str(self.It.__next__()) )
              , ('PlayerName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#67
class s_SurrenderPledgeWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x67'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('PledgeName', '|S'+str(self.It.__next__()) )
              , ('PlayerName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#6A
class s_PledgeCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CrestID', 'i4')
              , ('CrestSize', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6B
class s_SetupGauge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Date', 'i4')
              , ('Time_0', 'i4')
              , ('Time_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6C
class s_VehicleDeparture():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('BoatObjID', 'i4')
              , ('Speed1', 'i4')
              , ('Speed2', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6D
class s_VehicleCheckLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('BoatObjID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6E
class s_GetOnVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('BoatObjID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6F
class s_GetOffVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('BoatObjID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#70
class s_SendTradeRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x70'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SenderID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#71
class s_RestartResponse():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x71'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('1', 'i4')
              , ('Message', '|S'+str(self.It.__next__()) )
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#72
class s_MoveToPawn():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x72'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CreatureObjId', 'i4')
              , ('TargetObjID', 'i4')
              , ('Distance', 'i4')
              , ('CreatureX', 'i4')
              , ('CreatureY', 'i4')
              , ('CreatureZ', 'i4')
              , ('TargetX', 'i4')
              , ('TargetY', 'i4')
              , ('TargetZ', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#73
class s_SSQInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x73'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('State', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#74
class s_GameGuardQuery():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x74'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('0x27533dd9', 'i4')
              , ('0x2e72a51d', 'i4')
              , ('0x2017038b', 'i4')
              , ('0xc35b1ea3', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#75
class s_FriendList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x75'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('0', 'i2')
              , ('FriendID', 'i4')
              , ('FriendName', '|S'+str(self.It.__next__()) )
              , ('isOnLine', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      i += 6
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 4
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 2
      s_len = len(self.lst[i])
      yield s_len
      i += 2
#--------------------------------------------------------------------------#78
class s_L2FriendSay():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x78'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('0', 'i4')
              , ('Receiver', '|S'+str(self.It.__next__()) )
              , ('Sender', '|S'+str(self.It.__next__()) )
              , ('Message', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
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
#--------------------------------------------------------------------------#79
class s_ValidateLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x79'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#7A
class s_StartRotation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharId', 'i4')
              , ('Degree', 'i4')
              , ('Side', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#7B
class s_ShowBoard():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7B'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('1', 'i1')
              , ('bbshome', '|S'+str(self.It.__next__()) )
              , ('bbsgetfav', '|S'+str(self.It.__next__()) )
              , ('bbsloc', '|S'+str(self.It.__next__()) )
              , ('bbsclan', '|S'+str(self.It.__next__()) )
              , ('bbsmemo', '|S'+str(self.It.__next__()) )
              , ('bbsmail', '|S'+str(self.It.__next__()) )
              , ('bbsfriends', '|S'+str(self.It.__next__()) )
              , ('bbs_add_fav', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 1
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#7C
class s_ChooseInventoryItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ItemIDGetFunc01', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#7E
class s_MoveToLocationInVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('BoatObjID', 'i4')
              , ('ToX', 'i4')
              , ('ToY', 'i4')
              , ('ToZ', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#7F
class s_StopMoveInVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('BoatObjID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#80
class s_ValidateLocationInVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x80'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('0x50100002', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#83
class s_FriendAddRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x83'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('RequestorName', '|S'+str(self.It.__next__()) )
              , ('0', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#84
class s_LeaveWorld():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x84'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#85
class s_AbnormalStatusUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x85'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('EffectSizeValue', 'i2')
                  ]+ list(self.f_EffectSize()) +[
                  ]
    return dtype
  def f_EffectSize(self):
    for i in range(self.It.__next__()):
      dtype = ('EffectSize_' + str(i) , [
               ('skillIDGetSkill', 'i4')
              , ('SkillLevel', 'i2')
              , ('Duration', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#86
class s_QuestList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x86'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
               ('128', '|S128')
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('QuestId', 'i4')
              , ('Cond', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#87
class s_EnchantResult():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x87'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Result', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#88
class s_PledgeShowMemberListDeleteAll():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x88'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#89
class s_PledgeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x89'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ClanID', 'i4')
              , ('ClanName', '|S'+str(self.It.__next__()) )
              , ('AllyName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
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
#--------------------------------------------------------------------------#8C
class s_Ride():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Mount', 'i4')
              , ('RideType', 'i4')
              , ('RideClassId', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#8E
class s_PledgeShowInfoUpdate():
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
              , ('ClanID', 'i4')
              , ('0_0', 'i4')
              , ('ClanLevel', 'i4')
              , ('HasCastle', 'i4')
              , ('HasHideOut', 'i4')
              , ('0_1', 'i4')
              , ('ReputationScore', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('0_4', 'i4')
              , ('0_5', 'i4')
              , ('Bil', '|S'+str(self.It.__next__()) )
              , ('0_6', 'i4')
              , ('0_7', 'i4')
              , ('0_8', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 44
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 11
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#90
class s_AcquireSkillList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x90'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('FishingSkills', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('skillIDGetSkill', 'i4')
              , ('NextLevel', 'i4')
              , ('MaxLevel', 'i4')
              , ('SpCost', 'i4')
              , ('Requirements', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#91
class s_AcquireSkillInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x91'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('skillIDGetSkill', 'i4')
              , ('Level', 'i4')
              , ('SpCost', 'i4')
              , ('Mode', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('Type', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('Requirements', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 16
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 4
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#95
class s_GMViewCharacterInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x95'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('ObjectID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Race', 'i4')
              , ('Sex', 'i4')
              , ('ClassIDGetClassID_0', 'i4')
              , ('Level', 'i4')
              , ('Exp', 'i8')
              , ('STR', 'i4')
              , ('DEX', 'i4')
              , ('CON', 'i4')
              , ('INT', 'i4')
              , ('WIT', 'i4')
              , ('MEN', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrentHP', 'i4')
              , ('MaxMP', 'i4')
              , ('CurrentMP', 'i4')
              , ('SP', 'i4')
              , ('CurrentLoad', 'i4')
              , ('MaxLoad', 'i4')
              , ('PkKills_0', 'i4')
              , ('Unknown_0', 'i4')
              , ('RightEarring_0', 'i4')
              , ('LeftEarring_0', 'i4')
              , ('Necklace_0', 'i4')
              , ('RightRing_0', 'i4')
              , ('LeftRing_0', 'i4')
              , ('Head_0', 'i4')
              , ('RightHand_0', 'i4')
              , ('LeftHand_0', 'i4')
              , ('Gloves_0', 'i4')
              , ('Chest_0', 'i4')
              , ('Legs_0', 'i4')
              , ('Boots_0', 'i4')
              , ('Unknown_1', 'i4')
              , ('Unknown_2', 'i4')
              , ('Hair_0', 'i4')
              , ('Face_0', 'i4')
              , ('Unknown_3', 'i4')
              , ('Unknown_4', 'i4')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('0_4', 'i4')
              , ('0_5', 'i4')
              , ('Unknown_5', 'i4')
              , ('RightEarring_1', 'i4')
              , ('LeftEarring_1', 'i4')
              , ('Necklace_1', 'i4')
              , ('RightRing_1', 'i4')
              , ('LeftRing_1', 'i4')
              , ('Head_1', 'i4')
              , ('RightHand_1', 'i4')
              , ('LeftHand_1', 'i4')
              , ('Gloves_1', 'i4')
              , ('Chest_1', 'i4')
              , ('Legs_1', 'i4')
              , ('Boots_1', 'i4')
              , ('Unknown_6', 'i4')
              , ('Unknown_7', 'i4')
              , ('Hair_1', 'i4')
              , ('Face_1', 'i4')
              , ('Unknown_8', 'i4')
              , ('Unknown_9', 'i4')
              , ('0_6', 'i4')
              , ('0_7', 'i4')
              , ('0_8', 'i4')
              , ('0_9', 'i4')
              , ('0_10', 'i4')
              , ('0_11', 'i4')
              , ('0_12', 'i2')
              , ('0_13', 'i2')
              , ('0_14', 'i2')
              , ('0_15', 'i2')
              , ('0_16', 'i2')
              , ('0_17', 'i2')
              , ('0_18', 'i2')
              , ('0_19', 'i2')
              , ('0_20', 'i2')
              , ('0_21', 'i2')
              , ('0_22', 'i2')
              , ('0_23', 'i2')
              , ('0_24', 'i2')
              , ('0_25', 'i2')
              , ('AugmentIDGetAugmentID', 'i2')
              , ('0_26', 'i2')
              , ('0_27', 'i2')
              , ('0_28', 'i2')
              , ('0_29', 'i2')
              , ('0_30', 'i2')
              , ('0_31', 'i2')
              , ('0_32', 'i2')
              , ('0_33', 'i2')
              , ('0_34', 'i2')
              , ('0_35', 'i2')
              , ('0_36', 'i2')
              , ('0_37', 'i2')
              , ('0_38', 'i2')
              , ('Unknown_10', 'i4')
              , ('0_39', 'i2')
              , ('0_40', 'i2')
              , ('0_41', 'i2')
              , ('0_42', 'i2')
              , ('0_43', 'i2')
              , ('0_44', 'i2')
              , ('0_45', 'i2')
              , ('0_46', 'i2')
              , ('0_47', 'i2')
              , ('0_48', 'i2')
              , ('0_49', 'i2')
              , ('0_50', 'i2')
              , ('0_51', 'i2')
              , ('0_52', 'i2')
              , ('0_53', 'i2')
              , ('0_54', 'i2')
              , ('0_55', 'i2')
              , ('0_56', 'i2')
              , ('0_57', 'i2')
              , ('0_58', 'i2')
              , ('PAtk', 'i4')
              , ('AtkSpd_0', 'i4')
              , ('PDef', 'i4')
              , ('Evasion', 'i4')
              , ('Accuracy', 'i4')
              , ('CritRate', 'i4')
              , ('MAtk', 'i4')
              , ('CastSpd', 'i4')
              , ('AtkSpd_1', 'i4')
              , ('MDef', 'i4')
              , ('PvpFlag', 'i4')
              , ('Karma', 'i4')
              , ('RunSpd', 'i4')
              , ('WalkSpd', 'i4')
              , ('SwimRunSpd', 'i4')
              , ('SwimWalkSpd', 'i4')
              , ('FlRunSpd', 'i4')
              , ('FlWalkSpd', 'i4')
              , ('FlyRunSpd', 'i4')
              , ('FlyWalkSpd', 'i4')
              , ('MoveMultiplier', 'f8')
              , ('AtkSpdMultiplier', 'f8')
              , ('CollisionRadius', 'f8')
              , ('CollisionHeight', 'f8')
              , ('HairStyle', 'i4')
              , ('HairColor', 'i4')
              , ('Face_2', 'i4')
              , ('AccessLevel', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('ClanID', 'i4')
              , ('ClanCrestID', 'i4')
              , ('AllyID', 'i4')
              , ('MounType', 'i1')
              , ('PrivateStoreType', 'i1')
              , ('DwarvenCraft', 'i1')
              , ('PkKills_1', 'i4')
              , ('PvpKills', 'i4')
              , ('RecomLeft', 'i2')
              , ('RecomHave', 'i2')
              , ('ClassIDGetClassID_1', 'i4')
              , ('0_59', 'i4')
              , ('MaxCP', 'i4')
              , ('CurrentCP', 'i4')
              , ('isRunning', 'i1')
              , ('321', 'i1')
              , ('PledgeClass', 'i4')
              , ('isNoble', 'i1')
              , ('isHero', 'i1')
              , ('NameColor', 'i4')
              , ('TitleColor', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 20
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 508
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 147
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#96
class s_GMViewPledgeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x96'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('CharName', '|S'+str(self.It.__next__()) )
              , ('ClanID', 'i4')
              , ('0_0', 'i4')
              , ('ClanName', '|S'+str(self.It.__next__()) )
              , ('ClanLeaderName', '|S'+str(self.It.__next__()) )
              , ('CrestID', 'i4')
              , ('Level', 'i4')
              , ('HasCastle', 'i4')
              , ('HasHideOut', 'i4')
              , ('0_1', 'i4')
              , ('Rank', 'i4')
              , ('ReputationScore', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('AllyID', 'i4')
              , ('AllyName', '|S'+str(self.It.__next__()) )
              , ('AllyCrestID', 'i4')
              , ('isAtWar', 'i4')
              , ('MembersCountValue', 'i4')
                  ]+ list(self.f_MembersCount()) +[
                  ]
    return dtype
  def f_MembersCount(self):
    for i in range(self.It.__next__()):
      dtype = ('MembersCount_' + str(i) , [
               ('MemberName', '|S'+str(self.It.__next__()) )
              , ('MemberLevel', 'i4')
              , ('ClassIDGetClassID', 'i4')
              , ('Sex', 'i4')
              , ('Race', 'i4')
              , ('MemberObjID', 'i4')
              , ('Sponsor', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 8
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 40
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 24
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 3
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 11
   s_len = len(self.lst[i])
   yield s_len
   i += 3
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 7
#--------------------------------------------------------------------------#97
class s_GMViewSkillInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x97'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('CharName', '|S'+str(self.It.__next__()) )
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('isPassive', 'i4')
              , ('SkillLevel', 'i4')
              , ('skillIDGetSkill', 'i4')
              , ('0', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#99
class s_GMViewQuestInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x99'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('CharName', '|S'+str(self.It.__next__()) )
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('QuestID', 'i4')
              , ('Cond', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#9A
class s_GMViewItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9A'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('PlayerName', '|S'+str(self.It.__next__()) )
              , ('InventoryLimit', 'i4')
              , ('1', 'i2')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('Type1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('LocationSlot', 'i4')
              , ('Count', 'i4')
              , ('Type2', 'i2')
              , ('CustomType1', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('CustomType2', 'i2')
              , ('AugmentIDGetAugmentID', 'i2')
              , ('0', 'i2')
              , ('Mana', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 6
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 3
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#9B
class s_GMViewWarehouseWithdrawList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9B'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('PlayerName', '|S'+str(self.It.__next__()) )
              , ('Money', 'i4')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('Type1', 'i2')
              , ('ObjectID_0', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('Type2', 'i2')
              , ('CustomType1', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('SoulShotCount', 'i2')
              , ('SpiritShotCount', 'i2')
              , ('AugmentIDGetAugmentID_0', 'i2')
              , ('0_0', 'i2')
              , ('AugmentIDGetAugmentID_1', 'i2')
              , ('0_1', 'i2')
              , ('ObjectID_1', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
              , ('Mana', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 4
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#9C
class s_ListPartyWaiting():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9C'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Level', 'i4')
              , ('ClassIDGetClassID', 'i4')
              , ('0_0', 'i4')
              , ('ClanID', 'i4')
              , ('0_1', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 32
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 9
#--------------------------------------------------------------------------#9D
class s_PartyMatchDetail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9D'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('isShowLevel', 'i4')
              , ('isShowClass', 'i4')
              , ('0', 'i4')
              , ('PartyMemo', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 16
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 4
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#9E
class s_PlaySound():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9E'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Unknown_0', 'i4')
              , ('SoundFile', '|S'+str(self.It.__next__()) )
              , ('Unknown_1', 'i4')
              , ('Unknown_2', 'i4')
              , ('Unknown_3', 'i4')
              , ('Unknown_4', 'i4')
              , ('Unknown_5', 'i4')
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#9F
class s_StaticObject():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('StaticObjectID', 'i4')
              , ('ObjectID', 'i4')
              , ('Type', 'i4')
              , ('isTargetable', 'i4')
              , ('MeshIndex', 'i4')
              , ('isClosed', 'i4')
              , ('isEnemy', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrentHP', 'i4')
              , ('isSHowHP', 'i4')
              , ('DamageGrade', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A0
class s_PrivateStoreManageListSell():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA0'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('PlayerObjID', 'i4')
              , ('isPackageSale', 'i4')
              , ('Money', 'i4')
              , ('ItemsCountValue', 'i4')
                  ]+ list(self.f_ItemsCount()) +[
               ('SellCountValue', 'i4')
                  ]+ list(self.f_SellCount()) +[
                  ]
    return dtype
  def f_ItemsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemsCount_' + str(i) , [
               ('Type2', 'i4')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('0_0', 'i2')
              , ('Enchant', 'i2')
              , ('0_1', 'i2')
              , ('BodyPart', 'i4')
              , ('Price', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
                  ])
      yield dtype 
  def f_SellCount(self):
    for i in range(self.It.__next__()):
      dtype = ('SellCount_' + str(i) , [
               ('Type2', 'i4')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('0_0', 'i2')
              , ('Enchant', 'i2')
              , ('0_1', 'i2')
              , ('BodyPart', 'i4')
              , ('Price', 'i4')
              , ('ReferencePrice', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      i += 62
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 3
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 17
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#A1
class s_PrivateStoreListSell():
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
              , ('PlayerObjID', 'i4')
              , ('isPackageSale', 'i4')
              , ('Money', 'i4')
              , ('ItemsCountValue', 'i4')
                  ]+ list(self.f_ItemsCount()) +[
                  ]
    return dtype
  def f_ItemsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemsCount_' + str(i) , [
               ('Type2', 'i4')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('0_0', 'i2')
              , ('Enchant', 'i2')
              , ('0_1', 'i2')
              , ('BodyPart', 'i4')
              , ('Price', 'i4')
              , ('ReferencePrice', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 3
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#A2
class s_PrivateStoreMsgSell():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA2'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('StoreMsg', '|S'+str(self.It.__next__()) )
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#A3
class s_ShowMiniMap():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('MapID', 'i4')
              , ('SevenSignsPeriod', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A6
class s_TutorialShowHtml():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA6'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Html', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#A9
class s_TutorialClose():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#A7
class s_TutorialShowQuestionMark():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Blink', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AF
class s_AllyCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CrestID', 'i4')
              , ('CrestSize', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B1
class s_PetStatusShow():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SummonType', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B2
class s_PetInfo():
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
              , ('SummonType', 'i4')
              , ('ObjectID', 'i4')
              , ('SummonNpcID', 'i4')
              , ('0_0', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('0_1', 'i4')
              , ('CastSpd_0', 'i4')
              , ('AtkSpd_0', 'i4')
              , ('RunSpd_0', 'i4')
              , ('WalkSpd', 'i4')
              , ('SwimRunSpd', 'i4')
              , ('SwimWalkSpd', 'i4')
              , ('FlRunSpd', 'i4')
              , ('FlWalkSpd', 'i4')
              , ('FlyRunSpd', 'i4')
              , ('FlyWalkSpd', 'i4')
              , ('MoveMultiplier', 'f8')
              , ('AtkSpdMultiplier', 'f8')
              , ('CollisionRadius', 'f8')
              , ('CollisionHeight', 'f8')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('0_4', 'i4')
              , ('1_0', 'i1')
              , ('isRunning', 'i1')
              , ('isInCombat', 'i1')
              , ('isAlikeDead', 'i1')
              , ('isSummoned', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('1_1', 'i4')
              , ('PvpFlag', 'i4')
              , ('Karma', 'i4')
              , ('CurrentFed', 'i4')
              , ('MaxFed', 'i4')
              , ('CurrentHP', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrentMP', 'i4')
              , ('MaxMP', 'i4')
              , ('SP', 'i4')
              , ('Level', 'i4')
              , ('Exp', 'i8')
              , ('ExpForThisLevel', 'i8')
              , ('ExpForNextLevel', 'i8')
              , ('CurrentLoad', 'i4')
              , ('MaxLoad', 'i4')
              , ('PAtk', 'i4')
              , ('PDef', 'i4')
              , ('MAtk', 'i4')
              , ('MDef', 'i4')
              , ('Accuracy', 'i4')
              , ('Evasion', 'i4')
              , ('CritRate', 'i4')
              , ('RunSpd_1', 'i4')
              , ('AtkSpd_1', 'i4')
              , ('CastSpd_1', 'i4')
              , ('0_5', 'i4')
              , ('isStrider', 'i2')
              , ('0_6', 'i1')
              , ('0_7', 'i2')
              , ('0_8', 'i1')
              , ('SoulShotsPerHit', 'i4')
              , ('SpiritShotsPerHit', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 125
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 31
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#B3
class s_PetItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB3'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('Type1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('Type2', 'i2')
              , ('255', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('0_0', 'i2')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('0_4', 'i4')
              , ('0_5', 'i4')
              , ('0_6', 'i4')
              , ('0_7', 'i4')
              , ('0_8', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#B4
class s_PetInventoryUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB4'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('Change', 'i2')
              , ('Type1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('Type2', 'i2')
              , ('0_0', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('Enchant', 'i2')
              , ('0_1', 'i2')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('0_4', 'i4')
              , ('0_5', 'i4')
              , ('0_6', 'i4')
              , ('0_7', 'i4')
              , ('0_8', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#B6
class s_PetStatusUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB6'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('SummonType', 'i4')
              , ('ObjectID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('CurrentFed', 'i4')
              , ('MaxFed', 'i4')
              , ('CurrenHP', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrenMP', 'i4')
              , ('MaxMP', 'i4')
              , ('Level', 'i4')
              , ('Exp', 'i8')
              , ('ExpForThisLevel', 'i8')
              , ('ExpForNextLevel', 'i8')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 20
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#B7
class s_PetDelete():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PetID', 'i4')
              , ('PetObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B9
class s_MyTargetSelected():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Color', 'i2')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#BA
class s_PartyMemberPosition():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBA'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('MemberCountValue', 'i4')
                  ]+ list(self.f_MemberCount()) +[
                  ]
    return dtype
  def f_MemberCount(self):
    for i in range(self.It.__next__()):
      dtype = ('MemberCount_' + str(i) , [
               ('ObjectID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#BB
class s_AskJoinAlly():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBB'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('RequestorObjID', 'i4')
              , ('RequestorName', '|S'+str(self.It.__next__()) )
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#BE
class s_PrivateStoreListBuy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBE'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('PlayerID', 'i4')
              , ('Money', 'i4')
              , ('ItemsCountValue', 'i4')
                  ]+ list(self.f_ItemsCount()) +[
                  ]
    return dtype
  def f_ItemsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemsCount_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Enchant', 'i2')
              , ('Count_0', 'i4')
              , ('ReferencePrice', 'i4')
              , ('0', 'i2')
              , ('BodyPart', 'i4')
              , ('Type2', 'i2')
              , ('Price', 'i4')
              , ('Count_1', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#BF
class s_PrivateStoreMsgBuy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBF'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('StoreMsg', '|S'+str(self.It.__next__()) )
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#C7
class s_SkillCoolTime():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC7'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('skillIDGetSkill', 'i4')
              , ('0', 'i4')
              , ('ReuseDelay', 'i4')
              , ('ReuseLeft', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#C8
class s_PackageToList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#C9
class s_SiegeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC9'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
              , ('isClanLeader', 'i4')
              , ('OwnerID', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('ClanLeaderName', '|S'+str(self.It.__next__()) )
              , ('AllyID', 'i4')
              , ('AllyName', '|S'+str(self.It.__next__()) )
              , ('Time_ms', 'i4')
              , ('Siege_Time', 'i4')
              , ('0', 'i4')
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
   i += s_len
   i += 4
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
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#CA
class s_SiegeAttackerList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#CB
class s_SiegeDefenderList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#CC
class s_NicknameChanged():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCC'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#CD
class s_PledgeStatusChanged():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ClanLeaderID', 'i4')
              , ('ClanID', 'i4')
              , ('0_0', 'i4')
              , ('ClanLevel', 'i4')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#CE
class s_RelationChanged():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Relation', 'i4')
              , ('AutoAttackable', 'i4')
              , ('Karma', 'i4')
              , ('PvpFlag', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D1
class s_SetSummonRemainTime():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('MaxTime', 'i4')
              , ('RemainingTime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D2
class s_PackageSendableList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD2'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Money', 'i4')
              , ('ItemsCountValue', 'i4')
                  ]+ list(self.f_ItemsCount()) +[
                  ]
    return dtype
  def f_ItemsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemsCount_' + str(i) , [
               ('Type1', 'i2')
              , ('ObjectID_0', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('Type2', 'i2')
              , ('CustomType1', 'i2')
              , ('BodyPart', 'i4')
              , ('Enchant', 'i2')
              , ('CustomType2', 'i2')
              , ('0', 'i2')
              , ('ObjectID_1', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#D3
class s_Earthquake():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('intensity', 'i4')
              , ('Duration', 'i4')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D4
class s_FlyToLoaction():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('ToX', 'i4')
              , ('ToY', 'i4')
              , ('ToZ', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
              , ('FlyType', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D6
class s_SpecialCamera():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
              , ('Distantion', 'i4')
              , ('Yaw', 'i4')
              , ('Pitch', 'i4')
              , ('Time', 'i4')
              , ('Duration', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D7
class s_NormalCamera():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#D9
class s_NetPing():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('kID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#DA
class s_Dice():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Number', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#DB
class s_Snoop():
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
              , ('ConvoID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('0', 'i4')
              , ('Type', 'i4')
              , ('Speaker', '|S'+str(self.It.__next__()) )
              , ('Msg', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 8
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
   i += 3
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#DC
class s_RecipeBookItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDC'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('isDwarvenCraft', 'i4')
              , ('MaxMP', 'i4')
              , ('RecipesCountValue', 'i4')
                  ]+ list(self.f_RecipesCount()) +[
                  ]
    return dtype
  def f_RecipesCount(self):
    for i in range(self.It.__next__()):
      dtype = ('RecipesCount_' + str(i) , [
               ('RecipeID', 'i4')
              , ('Inc', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#DD
class s_RecipeItemMakeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
              , ('isDwarvenRecipe', 'i4')
              , ('CurrentMP', 'i4')
              , ('MaxMP', 'i4')
              , ('isSuccess', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#DF
class s_RecipeShopSellList():
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
              , ('ObjectID', 'i4')
              , ('CurrentMP', 'i4')
              , ('max_MP', 'i4')
              , ('Money', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('RecipeID', 'i4')
              , ('0', 'i4')
              , ('Cost', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 16
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 4
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#E0
class s_RecipeShopItemInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ShopID', 'i4')
              , ('RecipeID', 'i4')
              , ('CurrentMP', 'i4')
              , ('MaxMP', 'i4')
              , ('-1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#E1
class s_RecipeShopMsg():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE1'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('StoreName', '|S'+str(self.It.__next__()) )
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#E2
class s_ShowCalculator():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CalculatorID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#E3
class s_MonRaceInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE3'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Unknown_0', 'i4')
              , ('Unknown_1', 'i4')
              , ('CountValue', 'i4')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('MonsterObjID', 'i4')
              , ('NpcID', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
              , ('EndX', 'i4')
              , ('EndY', 'i4')
              , ('EndZ', 'i4')
              , ('CollisionHeight', 'f8')
              , ('CollisionRadius', 'f8')
              , ('120', 'i4')
              , ('1', 'i1')
              , ('2', 'i1')
              , ('3', 'i1')
              , ('4', 'i1')
              , ('5', 'i1')
              , ('6', 'i1')
              , ('7', 'i1')
              , ('8', 'i1')
              , ('9', 'i1')
              , ('10', 'i1')
              , ('11', 'i1')
              , ('12', 'i1')
              , ('13', 'i1')
              , ('14', 'i1')
              , ('15', 'i1')
              , ('16', 'i1')
              , ('17', 'i1')
              , ('18', 'i1')
              , ('19', 'i1')
              , ('20', 'i1')
              , ('0', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#E4
class s_HennaItemInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SymbolID', 'i4')
              , ('ItemDyeID', 'i4')
              , ('DyeRequire', 'i4')
              , ('Price', 'i4')
              , ('Draw', 'i4')
              , ('Adena', 'i4')
              , ('INT', 'i4')
              , ('INTHenna', 'i1')
              , ('STR', 'i4')
              , ('STRHenna', 'i1')
              , ('CON', 'i4')
              , ('CONHenna', 'i1')
              , ('MEN', 'i4')
              , ('MENHenna', 'i1')
              , ('DEX', 'i4')
              , ('DEXHenna', 'i1')
              , ('WIT', 'i4')
              , ('WITHenna', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#E5
class s_HennaInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE5'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('INT', 'i1')
              , ('STR', 'i1')
              , ('CON', 'i1')
              , ('MEN', 'i1')
              , ('DEX', 'i1')
              , ('WIT', 'i1')
              , ('3', 'i4')
              , ('SlotCountValue', 'i4')
                  ]+ list(self.f_SlotCount()) +[
                  ]
    return dtype
  def f_SlotCount(self):
    for i in range(self.It.__next__()):
      dtype = ('SlotCount_' + str(i) , [
               ('SymbolID_0', 'i4')
              , ('SymbolID_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 10
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 7
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#E8
class s_SendMacroList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE8'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Revision', 'i4')
              , ('0', 'i1')
              , ('CountValue', 'i1')
              , ('isCheck', 'i1')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('MacroID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Descr', '|S'+str(self.It.__next__()) )
              , ('Acronym', '|S'+str(self.It.__next__()) )
              , ('Icon', 'i1')
              , ('LenghtValue', 'i1')
                  ]+ list(self.f_Lenght()) +[
                  ])
      yield dtype 
  def f_Lenght(self):
    for i in range(self.It.__next__()):
      dtype = ('Lenght_' + str(i) , [
               ('Inc', 'i1')
              , ('Type', 'i1')
              , ('SkillID', 'i4')
              , ('ShortCutID', 'i1')
              , ('CmdName', '|S'+str(self.It.__next__()) )
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 5
   p = self.pck[i:i+1]
   count = struct.unpack('b', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 2
   for _ in range(count):
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 1
      p = self.pck[i:i+1]
      count = struct.unpack('b', p)[0]
      if count > 100: raise PacketError
      yield count
      i += 1
      for _ in range(count):
         i += 7
         s_len = f_s_len(self.pck[i:])
         yield s_len
         i += s_len
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 2
      count = self.lst[i]
      if count > 100: raise PacketError
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
         i += 4
         s_len = len(self.lst[i])
         yield s_len
         i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 1
#--------------------------------------------------------------------------#E9
class s_BuyListSeed():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE9'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Money', 'i4')
              , ('ManorID', 'i4')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemType1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('itemType2', 'i2')
              , ('h', 'i2')
              , ('price', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#EA
class s_ShowTownMap():
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
              , ('Texture', '|S'+str(self.It.__next__()) )
              , ('X', 'i4')
              , ('Y', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#EB
class s_ObservationMode():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('0_0', 'i1')
              , ('192', 'i1')
              , ('0_1', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#EC
class s_ObservationReturn():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#ED
class s_ChairSit():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xED'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('StaticObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#EE
class s_HennaEquipList():
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
              , ('Money', 'i4')
              , ('Slots', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('SymbolID', 'i4')
              , ('ItemDyeID', 'i4')
              , ('DyeRequire', 'i4')
              , ('Price', 'i4')
              , ('1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#EF
class s_SellListProcure():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEF'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Money', 'i4')
              , ('0', 'i4')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemType1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('ItemType2', 'i2')
              , ('0', 'i2')
              , ('Price', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#F0
class s_GMHennaInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF0'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('INT', 'i1')
              , ('STR', 'i1')
              , ('CON', 'i1')
              , ('MEN', 'i1')
              , ('DEX', 'i1')
              , ('WIT', 'i1')
              , ('3', 'i4')
              , ('SlotCountValue', 'i4')
                  ]+ list(self.f_SlotCount()) +[
                  ]
    return dtype
  def f_SlotCount(self):
    for i in range(self.It.__next__()):
      dtype = ('SlotCount_' + str(i) , [
               ('SymbolID_0', 'i4')
              , ('SymbolID_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 10
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 7
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#F1
class s_RadarControl():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ShowRadar', 'i4')
              , ('Type', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F3
class s_ConfirmDlg():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF3'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('RequestID', 'i4')
              , ('2', 'i4')
              , ('0', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('1', 'i4')
              , ('Unknown', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#F4
class s_PartySpelled():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF4'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('isSummon', 'i4')
              , ('ObjecID', 'i4')
              , ('EffectSizeValue', 'i4')
                  ]+ list(self.f_EffectSize()) +[
                  ]
    return dtype
  def f_EffectSize(self):
    for i in range(self.It.__next__()):
      dtype = ('EffectSize_' + str(i) , [
               ('skillIDGetSkill', 'i4')
              , ('SkillLevel', 'i2')
              , ('Duration', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#F5
class s_ShopPreviewList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF5'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('192', 'i1')
              , ('19', 'i1')
              , ('0_0', 'i1')
              , ('0_1', 'i1')
              , ('Money', 'i4')
              , ('ListID', 'i4')
              , ('ListSizeValue', 'i2')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ItemIDGetFunc01', 'i4')
              , ('Type2', 'i2')
              , ('BodyPart', 'i2')
              , ('WearPrice', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 6
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#F7
class s_CameraMode():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Mode', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F8
class s_ShowXMasSeal():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Item', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F9
class s_EtcStatusUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('EffectLevel', 'i4')
              , ('WeightPenalty', 'i4')
              , ('isChatBanned', 'i4')
              , ('isDangerArea', 'i4')
              , ('ExpertisePenalty', 'i4')
              , ('CharmOfCourage', 'i4')
              , ('DeathPenaltyBuffLevel', 'i4')
              , ('Souls', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FA
class s_ShortBuffStatusUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SkillID', 'i4')
              , ('SkillLevel', 'i4')
              , ('Duration', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FB
class s_SSQStatus():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FD
class s_AgitDecoInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE01
class s_ExRegMax():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x01\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('1', 'i4')
              , ('Count', 'i4')
              , ('Time', 'i4')
              , ('Max', 'f8')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE0C
class s_ExAutoSoulShot():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x0C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ItemIDGetFunc01', 'i4')
              , ('Type', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE12
class s_ExOpenMPCC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x12\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE13
class s_ExCloseMPCC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x13\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE14
class s_ExShowCastleInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x14\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('CastlesSizeValue', 'i4')
                  ]+ list(self.f_CastlesSize()) +[
                  ]
    return dtype
  def f_CastlesSize(self):
    for i in range(self.It.__next__()):
      dtype = ('CastlesSize_' + str(i) , [
               ('CastleID', 'i4')
              , ('CastleName', '|S'+str(self.It.__next__()) )
              , ('TaxPercent', 'i4')
              , ('Time', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 8
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 3
#--------------------------------------------------------------------------#FE15
class s_ExShowFortressInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x15\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('FortIdID', 'i4')
              , ('OwnerClan', '|S'+str(self.It.__next__()) )
              , ('IsInProgress', 'i4')
              , ('Time', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 8
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 3
#--------------------------------------------------------------------------#FE16
class s_ExShowAgitInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x16\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ClanHallsSizeValue', 'i4')
                  ]+ list(self.f_ClanHallsSize()) +[
                  ]
    return dtype
  def f_ClanHallsSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ClanHallsSize_' + str(i) , [
               ('ClanHallID', 'i4')
              , ('HallName', '|S'+str(self.It.__next__()) )
              , ('LeaderName', '|S'+str(self.It.__next__()) )
              , ('Grade', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 4
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 2
#--------------------------------------------------------------------------#FE17
class s_ExShowFortressSiegeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x17\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE18
class s_ExPartyPetWindowAdd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x18\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('SummonObjID', 'i4')
              , ('NpcID', 'i4')
              , ('SummonType', 'i4')
              , ('OwnerID', 'i4')
              , ('SummonName', '|S'+str(self.It.__next__()) )
              , ('CurrentHP', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrentMP', 'i4')
              , ('MaxMP', 'i4')
              , ('Level', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 18
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#FE19
class s_ExPartyPetWindowUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x19\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('SummonObjID', 'i4')
              , ('NpcID', 'i4')
              , ('SummonType', 'i4')
              , ('OwnerID', 'i4')
              , ('SummonName', '|S'+str(self.It.__next__()) )
              , ('CurrentHP', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrentMP', 'i4')
              , ('MaxMP', 'i4')
              , ('Level', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 18
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#FE1A
class s_ExAskJoinMPCC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x1A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('RequestorName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#FE1B
class s_ExPledgeCrestLarge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x1B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('0', 'i4')
              , ('CrestID', 'i4')
              , ('CrestSize', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE1E
class s_ExFishingStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x1E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ObjectID', 'i4')
              , ('FishType', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('0_0', 'i1')
              , ('0_1', 'i1')
              , ('isNightLure', 'i1')
              , ('0_2', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE1F
class s_ExFishingEnd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x1F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('CharID', 'i4')
              , ('isWin', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE20
class s_ExShowQuestInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x20\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE21
class s_ExShowQuestMark():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x21\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('QuestID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE22
class s_ExSendManorList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x22\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('Inc', 'i4')
              , ('Manor', '|S'+str(self.It.__next__()) )
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 1
#--------------------------------------------------------------------------#FE23
class s_ExShowSeedInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x23\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('0_0', 'i1')
              , ('ManorID', 'i4')
              , ('0_1', 'i4')
              , ('SeedsSizeValue', 'i4')
                  ]+ list(self.f_SeedsSize()) +[
                  ]
    return dtype
  def f_SeedsSize(self):
    for i in range(self.It.__next__()):
      dtype = ('SeedsSize_' + str(i) , [
               ('SeedID', 'i4')
              , ('CanProduce', 'i4')
              , ('StartProduce', 'i4')
              , ('SeedPrice', 'i4')
              , ('SeedLevel', 'i4')
              , ('1_0', 'i1')
              , ('RewardItemBySeed_0', 'i4')
              , ('1_1', 'i1')
              , ('RewardItemBySeed_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 11
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 4
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#FE24
class s_ExShowCropInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x24\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('0_0', 'i1')
              , ('ManorID', 'i4')
              , ('0_1', 'i4')
              , ('CropsSizeValue', 'i4')
                  ]+ list(self.f_CropsSize()) +[
                  ]
    return dtype
  def f_CropsSize(self):
    for i in range(self.It.__next__()):
      dtype = ('CropsSize_' + str(i) , [
               ('CropID', 'i4')
              , ('CropAmount', 'i4')
              , ('StartAmount', 'i4')
              , ('Price', 'i4')
              , ('Reward', 'i1')
              , ('SeedLevelByCrop2', 'i4')
              , ('1_0', 'i1')
              , ('RewardItemCrop', 'i4')
              , ('1_1', 'i1')
              , ('RewardItemCrop2', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 11
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 4
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#FE25
class s_ExShowManorDefaultInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x25\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('0', 'i1')
              , ('CropsSizeValue', 'i4')
                  ]+ list(self.f_CropsSize()) +[
                  ]
    return dtype
  def f_CropsSize(self):
    for i in range(self.It.__next__()):
      dtype = ('CropsSize_' + str(i) , [
               ('CropID', 'i4')
              , ('SeedLevelByCrop2', 'i4')
              , ('SeedBasicPriceByCrop2', 'i4')
              , ('CropBasicPrice2', 'i4')
              , ('1_0', 'i1')
              , ('RewardItem3_0', 'i4')
              , ('1_1', 'i1')
              , ('RewardItem3_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#FE26
class s_ExShowSeedSetting():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x26\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE27
class s_ExFishingStartCombat():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x27\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ObjectID', 'i4')
              , ('Time', 'i4')
              , ('HP', 'i4')
              , ('Mode', 'i1')
              , ('LureType', 'i1')
              , ('DeceptiveMode', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE28
class s_ExFishingHPRegen():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x28\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ObjectID', 'i4')
              , ('Time', 'i4')
              , ('FishHP', 'i4')
              , ('HPstopRise', 'i1')
              , ('GoodUse', 'i1')
              , ('Anim', 'i1')
              , ('Penalty', 'i4')
              , ('BarColor', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE29
class s_ExEnchantSkillList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x29\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Type', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('skillIDGetSkill', 'i4')
              , ('NextLevel', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#FE2A
class s_ExEnchantSkillInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x2A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Type', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('skillIDGetSkill', 'i4')
              , ('Level', 'i4')
              , ('Rate', 'i4')
              , ('SpCost', 'i4')
              , ('ExpCost', 'i8')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#FE2B
class s_ExShowCropSetting():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x2B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE2C
class s_ExShowSellCropList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x2C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE2E
class s_ExMailArrived():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x2E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE2F
class s_ExStorageMaxCount():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x2F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('InventoryLimit', 'i4')
              , ('WareHouseLimit', 'i4')
              , ('FreightLimit', 'i4')
              , ('PrivateSellStoreLimit', 'i4')
              , ('PrivateBuyStoreLimit', 'i4')
              , ('DwarfRecipeLimit', 'i4')
              , ('CommonRecipeLimit', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE32
class s_ExPCCafePointInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x32\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Unknown_0', 'i4')
              , ('Unknown_1', 'i4')
              , ('Unknown_2', 'i1')
              , ('Unknown_3', 'i4')
              , ('Unknown_4', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE33
class s_ExSetCompassZoneCode():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x33\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ZoneType', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE34
class s_ExGetBossRecord():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x34\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Unknown_0', 'i4')
              , ('Unknown_1', 'i4')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE35
class s_ExAskJoinPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x35\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('CharName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#FE38
class s_ExShowAdventurerGuideBook():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x38\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE3A
class s_PledgeSkillList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x3A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListSizeValue', 'i4')
              , ('0', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('skillIDGetSkill', 'i4')
              , ('Level', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#FE3B
class s_PledgeSkillListAdd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x3B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('skillIDGetSkill', 'i4')
              , ('Level', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE3C
class s_PledgePowerGradeList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x3C\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('Rank', 'i4')
              , ('Party', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#FE3D
class s_PledgeReceivePowerInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x3D\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('MemberPowerGrade', 'i4')
              , ('MemberName', '|S'+str(self.It.__next__()) )
              , ('MemberClanRankPrivs', 'i4')
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
#--------------------------------------------------------------------------#FE3E
class s_PledgeReceiveMemberInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x3E\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('MemberPledgeType', 'i4')
              , ('MemberName', '|S'+str(self.It.__next__()) )
              , ('MemberTitle', '|S'+str(self.It.__next__()) )
              , ('MemberPowerGrade', 'i4')
              , ('ClanName', '|S'+str(self.It.__next__()) )
              , ('SponsorName', '|S'+str(self.It.__next__()) )
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
   i += s_len
   i += 4
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
   i += 2
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#FE3F
class s_PledgeReceiveWarList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x3F\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('EnemyAttaker', 'i4')
              , ('0', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('clanName', '|S'+str(self.It.__next__()) )
              , ('tab_0', 'i4')
              , ('tab_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 10
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 8
  def parse_list(self):
   i = 1
   i += 3
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 3
#--------------------------------------------------------------------------#FE40
class s_PledgeReceiveSubPledgeCreated():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x40\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('1', 'i4')
              , ('SubPledgeID', 'i4')
              , ('SubPledgeName', '|S'+str(self.It.__next__()) )
              , ('SubPledgeLeaderName', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 10
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
#--------------------------------------------------------------------------#FE41
class s_ExRedSky():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x41\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Duration', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE44
class s_ShowPCCafeCouponShowUI():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x44\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE45
class s_ExSearchOrc():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x45\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('64', '|S64')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE46
class s_ExCursedWeaponList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x46\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('CursedWeaponID', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#FE47
class s_ExCursedWeaponLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x47\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('CursedWeaponID', 'i4')
              , ('Activated', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#FE48
class s_ExRestartClient():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x48\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ItemObjID', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('Count', 'i4')
              , ('Type2', 'i2')
              , ('BodyPart', 'i4')
              , ('Enchant', 'i2')
              , ('CustomType2', 'i2')
              , ('AugmentIDGetAugmentID', 'i2')
              , ('0_0', 'i2')
              , ('0_1', 'i2')
              , ('Mana', 'i4')
              , ('AttackAttrElement', 'i4')
              , ('AttackAttrElementVal', 'i4')
              , ('DefAttrFire', 'i4')
              , ('DefAttrWater', 'i4')
              , ('DefAttrWind', 'i4')
              , ('DefAttrEarth', 'i4')
              , ('DefAttrHoly', 'i4')
              , ('DefAttrUnholy', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE49
class s_ExRequestHackShield():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x49\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE4A
class s_ExUseSharedGroupItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x4A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Unknown_0', 'i4')
              , ('Unknown_1', 'i4')
              , ('Unknown_2', 'i4')
              , ('Unknown_3', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE4B
class s_ExMPCCShowPartyMemberInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x4B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE4C
class s_ExDuelAskStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x4C\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('RequestorName', '|S'+str(self.It.__next__()) )
              , ('PartyDuel', 'i4')
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
#--------------------------------------------------------------------------#FE4D
class s_ExDuelReady():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x4D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE4E
class s_ExDuelStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x4E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE4F
class s_ExDuelEnd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x4F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE50
class s_ExDuelUpdateUserInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x50\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('CharName', '|S'+str(self.It.__next__()) )
              , ('ObjectID', 'i4')
              , ('ClassIDGetClassID', 'i4')
              , ('Level', 'i4')
              , ('CurrentHP', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrentMP', 'i4')
              , ('MaxMP', 'i4')
              , ('CurrentCP', 'i4')
              , ('MaxCP', 'i4')
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
#--------------------------------------------------------------------------#FE51
class s_ExShowVariationMakeWindow():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x51\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE52
class s_ExShowVariationCancelWindow():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x52\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE53
class s_ExPutItemResultForVariationMake():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x53\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ItemObjID', 'i4')
              , ('Unknown_0', 'i4')
              , ('Unknown_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE54
class s_ExPutIntensiveResultForVariationMake():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x54\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('RefinerItemObjID', 'i4')
              , ('LifeStoneItemID', 'i4')
              , ('GemStoneItemID', 'i4')
              , ('GemStoneCount', 'i4')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE55
class s_ExPutCommissionResultForVariationMake():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x55\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('GemStoneObjID', 'i4')
              , ('Unknown_0', 'i4')
              , ('GemStoneCount', 'i4')
              , ('Unknown_1', 'i4')
              , ('Unknown_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE56
class s_ExVariationResult():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x56\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('AugmentIDGetAugmentID', 'i2')
              , ('0', 'i2')
              , ('Unknown_0', 'i4')
              , ('Unknown_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE57
class s_ExPutItemResultForVariationCancel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x57\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('0x40a97712', 'i4')
              , ('ItemObjID', 'i4')
              , ('39', 'i4')
              , ('8198', 'i4')
              , ('Price', 'i8')
              , ('1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE58
class s_ExVariationCancelResult():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x58\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('CloseWindow', 'i4')
              , ('Unknown', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE5C
class s_ExPlayScene():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x5C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE5D
class s_ExSpawnEmitter():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x5D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('NpcObjID', 'i4')
              , ('CharID', 'i4')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE5E
class s_ExEnchantSkillInfoDetail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x5E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('0L', 'i8')
              , ('0_4', 'i4')
              , ('ItemCount', 'i4')
              , ('0_5', 'i4')
              , ('ItemIDGetFunc01', 'i4')
              , ('0_6', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE5F
class s_ExBasicActionList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x5F\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('ActionID', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#FE62
class s_ExChooseInventoryAttributeItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x62\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ItemIDGetFunc01', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE6A
class s_ExPartyPetWindowDelete():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x6A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('SummonObjID', 'i4')
              , ('OwnerID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
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
   i += 3
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#FE78
class s_ExShowProcureCropDetail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x78\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('CropID', 'i4')
              , ('CastleCropssizeValue', 'i4')
                  ]+ list(self.f_CastleCropssize()) +[
                  ]
    return dtype
  def f_CastleCropssize(self):
    for i in range(self.It.__next__()):
      dtype = ('CastleCropssize_' + str(i) , [
               ('ManorID', 'i4')
              , ('CropAmount', 'i4')
              , ('CropPrice', 'i4')
              , ('CropReward', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#FE79
class s_ExHeroList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x79\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('HeroName', '|S'+str(self.It.__next__()) )
              , ('ClassIDGetClassID', 'i4')
              , ('ClanName', '|S'+str(self.It.__next__()) )
              , ('ClanCrest', 'i4')
              , ('AllyName', '|S'+str(self.It.__next__()) )
              , ('AllyCrest', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 8
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise PacketError
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
      s_len = len(self.lst[i])
      yield s_len
      i += 2
      s_len = len(self.lst[i])
      yield s_len
      i += 3
#--------------------------------------------------------------------------#FE7A
class s_OlympiadUserInfoSpectator():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x7A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Side', 'i1')
              , ('ObjectID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('ClassIDGetClassID', 'i4')
              , ('CurrentHP', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrentCP', 'i4')
              , ('MaxCP', 'i4')
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
#--------------------------------------------------------------------------#FE7B
class s_ExOlympiadSpelledInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x7B\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ObjectID', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('skillID', 'i4')
              , ('Data', 'i2')
              , ('Duration', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise PacketError
   yield count
#--------------------------------------------------------------------------#FE7C
class s_ExOlympiadMode():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x7C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Mode', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE84
class s_ExGetBookMarkInfoPacket():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x84\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('0', 'i4')
              , ('bookmarkslot', 'i4')
              , ('SizeValue', 'i4')
                  ]+ list(self.f_Size()) +[
                  ]
    return dtype
  def f_Size(self):
    for i in range(self.It.__next__()):
      dtype = ('Size_' + str(i) , [
               ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Icon', 'i4')
              , ('Tag', '|S'+str(self.It.__next__()) )
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 10
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise PacketError
   yield count
   i += 4
   for _ in range(count):
      i += 12
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
  def parse_list(self):
   i = 1
   i += 3
   count = self.lst[i]
   if count > 100: raise PacketError
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
      i += 3
      s_len = len(self.lst[i])
      yield s_len
      i += 2
      s_len = len(self.lst[i])
      yield s_len
      i += 1
#--------------------------------------------------------------------------#FEAA
class s_UnknownFEAA():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xAA\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEAC
class s_ExBrExtraUserInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xAC\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('CharOID', 'i4')
              , ('Val', 'i4')
                  ]
    return dtype
class Pck_invoke_dict():
 def __init__(self):
   self.Pck_invoke_s = {}
   self.Pck_invoke_c = {}
 def get_Pck_invoke_c(self):
   self.Pck_invoke_s[c_Logout().invoke] = c_Logout()
   self.Pck_invoke_s[c_AttackRequest().invoke] = c_AttackRequest()
   self.Pck_invoke_s[c_RequestStartPledgeWar().invoke] = c_RequestStartPledgeWar()
   self.Pck_invoke_s[c_RequestReplyStartPledgeWar().invoke] = c_RequestReplyStartPledgeWar()
   self.Pck_invoke_s[c_RequestStopPledgeWar().invoke] = c_RequestStopPledgeWar()
   self.Pck_invoke_s[c_RequestReplyStopPledgeWar().invoke] = c_RequestReplyStopPledgeWar()
   self.Pck_invoke_s[c_RequestSurrenderPledgeWar().invoke] = c_RequestSurrenderPledgeWar()
   self.Pck_invoke_s[c_RequestReplySurrenderPledgeWar().invoke] = c_RequestReplySurrenderPledgeWar()
   self.Pck_invoke_s[c_RequestSetPledgeCrest().invoke] = c_RequestSetPledgeCrest()
   self.Pck_invoke_s[c_RequestGiveNickName().invoke] = c_RequestGiveNickName()
   self.Pck_invoke_s[c_CharacterCreate().invoke] = c_CharacterCreate()
   self.Pck_invoke_s[c_CharacterDelete().invoke] = c_CharacterDelete()
   self.Pck_invoke_s[c_ProtocolVersion().invoke] = c_ProtocolVersion()
   self.Pck_invoke_s[c_MoveBackwardToLocation().invoke] = c_MoveBackwardToLocation()
   self.Pck_invoke_s[c_EnterWorld().invoke] = c_EnterWorld()
   self.Pck_invoke_s[c_CharacterSelect().invoke] = c_CharacterSelect()
   self.Pck_invoke_s[c_NewCharacter().invoke] = c_NewCharacter()
   self.Pck_invoke_s[c_RequestItemList().invoke] = c_RequestItemList()
   self.Pck_invoke_s[c_RequestUnEquipItem().invoke] = c_RequestUnEquipItem()
   self.Pck_invoke_s[c_RequestDropItem().invoke] = c_RequestDropItem()
   self.Pck_invoke_s[c_UseItem().invoke] = c_UseItem()
   self.Pck_invoke_s[c_TradeRequest().invoke] = c_TradeRequest()
   self.Pck_invoke_s[c_AddTradeItem().invoke] = c_AddTradeItem()
   self.Pck_invoke_s[c_TradeDone().invoke] = c_TradeDone()
   self.Pck_invoke_s[c_Action().invoke] = c_Action()
   self.Pck_invoke_s[c_RequestBypassToServer().invoke] = c_RequestBypassToServer()
   self.Pck_invoke_s[c_RequestBBSwrite().invoke] = c_RequestBBSwrite()
   self.Pck_invoke_s[c_RequestJoinPledge().invoke] = c_RequestJoinPledge()
   self.Pck_invoke_s[c_RequestAnswerJoinPledge().invoke] = c_RequestAnswerJoinPledge()
   self.Pck_invoke_s[c_RequestWithdrawalPledge().invoke] = c_RequestWithdrawalPledge()
   self.Pck_invoke_s[c_RequestOustPledgeMember().invoke] = c_RequestOustPledgeMember()
   self.Pck_invoke_s[c_AuthLogin().invoke] = c_AuthLogin()
   self.Pck_invoke_s[c_RequestGetItemFromPet().invoke] = c_RequestGetItemFromPet()
   self.Pck_invoke_s[c_RequestAllyInfo().invoke] = c_RequestAllyInfo()
   self.Pck_invoke_s[c_RequestCrystallizeItem().invoke] = c_RequestCrystallizeItem()
   self.Pck_invoke_s[c_RequestPrivateStoreManageSell().invoke] = c_RequestPrivateStoreManageSell()
   self.Pck_invoke_s[c_SetPrivateStoreListSell().invoke] = c_SetPrivateStoreListSell()
   self.Pck_invoke_s[c_RequestSocialAction().invoke] = c_RequestSocialAction()
   self.Pck_invoke_s[c_ChangeMoveType2().invoke] = c_ChangeMoveType2()
   self.Pck_invoke_s[c_ChangeWaitType2().invoke] = c_ChangeWaitType2()
   self.Pck_invoke_s[c_RequestSellItem().invoke] = c_RequestSellItem()
   self.Pck_invoke_s[c_Unknown38().invoke] = c_Unknown38()
   self.Pck_invoke_s[c_RequestMagicSkillUse().invoke] = c_RequestMagicSkillUse()
   self.Pck_invoke_s[c_Appearing().invoke] = c_Appearing()
   self.Pck_invoke_s[c_SendWareHouseDepositList().invoke] = c_SendWareHouseDepositList()
   self.Pck_invoke_s[c_SendWareHouseWithDrawList().invoke] = c_SendWareHouseWithDrawList()
   self.Pck_invoke_s[c_RequestShortCutReg().invoke] = c_RequestShortCutReg()
   self.Pck_invoke_s[c_RequestShortCutDel().invoke] = c_RequestShortCutDel()
   self.Pck_invoke_s[c_RequestBuyItem().invoke] = c_RequestBuyItem()
   self.Pck_invoke_s[c_RequestJoinParty().invoke] = c_RequestJoinParty()
   self.Pck_invoke_s[c_RequestAnswerJoinParty().invoke] = c_RequestAnswerJoinParty()
   self.Pck_invoke_s[c_RequestWithDrawalParty().invoke] = c_RequestWithDrawalParty()
   self.Pck_invoke_s[c_RequestOustPartyMember().invoke] = c_RequestOustPartyMember()
   self.Pck_invoke_s[c_CannotMoveAnymore().invoke] = c_CannotMoveAnymore()
   self.Pck_invoke_s[c_RequestTargetCanceld().invoke] = c_RequestTargetCanceld()
   self.Pck_invoke_s[c_Say2().invoke] = c_Say2()
   self.Pck_invoke_s[c_RequestPledgeMemberList().invoke] = c_RequestPledgeMemberList()
   self.Pck_invoke_s[c_DummyPacket().invoke] = c_DummyPacket()
   self.Pck_invoke_s[c_RequestSkillList().invoke] = c_RequestSkillList()
   self.Pck_invoke_s[c_MoveWithDelta().invoke] = c_MoveWithDelta()
   self.Pck_invoke_s[c_RequestGetOnVehicle().invoke] = c_RequestGetOnVehicle()
   self.Pck_invoke_s[c_RequestGetOffVehicle().invoke] = c_RequestGetOffVehicle()
   self.Pck_invoke_s[c_AnswerTradeRequest().invoke] = c_AnswerTradeRequest()
   self.Pck_invoke_s[c_RequestActionUse().invoke] = c_RequestActionUse()
   self.Pck_invoke_s[c_RequestRestart().invoke] = c_RequestRestart()
   self.Pck_invoke_s[c_RequestSiegeInfo().invoke] = c_RequestSiegeInfo()
   self.Pck_invoke_s[c_ValidatePosition().invoke] = c_ValidatePosition()
   self.Pck_invoke_s[c_RequestShowBoard().invoke] = c_RequestShowBoard()
   self.Pck_invoke_s[c_RequestEnchantItem().invoke] = c_RequestEnchantItem()
   self.Pck_invoke_s[c_RequestDestroyItem().invoke] = c_RequestDestroyItem()
   self.Pck_invoke_s[c_RequestQuestList().invoke] = c_RequestQuestList()
   self.Pck_invoke_s[c_RequestQuestAbort().invoke] = c_RequestQuestAbort()
   self.Pck_invoke_s[c_RequestPledgeInfo().invoke] = c_RequestPledgeInfo()
   self.Pck_invoke_s[c_RequestPledgeExtendedInfo().invoke] = c_RequestPledgeExtendedInfo()
   self.Pck_invoke_s[c_RequestPledgeCrest().invoke] = c_RequestPledgeCrest()
   self.Pck_invoke_s[c_RequestSendFriendMsg().invoke] = c_RequestSendFriendMsg()
   self.Pck_invoke_s[c_RequestShowMiniMap().invoke] = c_RequestShowMiniMap()
   self.Pck_invoke_s[c_RequestRecordInfo().invoke] = c_RequestRecordInfo()
   self.Pck_invoke_s[c_RequestHennaEquip().invoke] = c_RequestHennaEquip()
   self.Pck_invoke_s[c_RequestAcquireSkillInfo().invoke] = c_RequestAcquireSkillInfo()
   self.Pck_invoke_s[c_SendBypassBuildCmd().invoke] = c_SendBypassBuildCmd()
   self.Pck_invoke_s[c_RequestMoveToLocationInVehicle().invoke] = c_RequestMoveToLocationInVehicle()
   self.Pck_invoke_s[c_CannotMoveAnymoreInVehicle().invoke] = c_CannotMoveAnymoreInVehicle()
   self.Pck_invoke_s[c_RequestFriendInvite().invoke] = c_RequestFriendInvite()
   self.Pck_invoke_s[c_RequestAnswerFriendInvite().invoke] = c_RequestAnswerFriendInvite()
   self.Pck_invoke_s[c_RequestFriendList().invoke] = c_RequestFriendList()
   self.Pck_invoke_s[c_RequestFriendDel().invoke] = c_RequestFriendDel()
   self.Pck_invoke_s[c_CharacterRestore().invoke] = c_CharacterRestore()
   self.Pck_invoke_s[c_RequestAcquireSkill().invoke] = c_RequestAcquireSkill()
   self.Pck_invoke_s[c_RequestRestartPoint().invoke] = c_RequestRestartPoint()
   self.Pck_invoke_s[c_RequestGMCommand().invoke] = c_RequestGMCommand()
   self.Pck_invoke_s[c_RequestPartyMatchConfig().invoke] = c_RequestPartyMatchConfig()
   self.Pck_invoke_s[c_RequestPartyMatchList().invoke] = c_RequestPartyMatchList()
   self.Pck_invoke_s[c_RequestPartyMatchDetail().invoke] = c_RequestPartyMatchDetail()
   self.Pck_invoke_s[c_RequestPrivateStoreBuy().invoke] = c_RequestPrivateStoreBuy()
   self.Pck_invoke_s[c_RequestTutorialLinkHtml().invoke] = c_RequestTutorialLinkHtml()
   self.Pck_invoke_s[c_RequestTutorialPassCmdToServer().invoke] = c_RequestTutorialPassCmdToServer()
   self.Pck_invoke_s[c_RequestTutorialQuestionMark().invoke] = c_RequestTutorialQuestionMark()
   self.Pck_invoke_s[c_RequestTutorialClientEvent().invoke] = c_RequestTutorialClientEvent()
   self.Pck_invoke_s[c_RequestPetition().invoke] = c_RequestPetition()
   self.Pck_invoke_s[c_RequestPetitionCancel().invoke] = c_RequestPetitionCancel()
   self.Pck_invoke_s[c_RequestGmList().invoke] = c_RequestGmList()
   self.Pck_invoke_s[c_RequestJoinAlly().invoke] = c_RequestJoinAlly()
   self.Pck_invoke_s[c_RequestAnswerJoinAlly().invoke] = c_RequestAnswerJoinAlly()
   self.Pck_invoke_s[c_AllyLeave().invoke] = c_AllyLeave()
   self.Pck_invoke_s[c_AllyDismiss().invoke] = c_AllyDismiss()
   self.Pck_invoke_s[c_RequestDismissAlly().invoke] = c_RequestDismissAlly()
   self.Pck_invoke_s[c_RequestSetAllyCrest().invoke] = c_RequestSetAllyCrest()
   self.Pck_invoke_s[c_RequestAllyCrest().invoke] = c_RequestAllyCrest()
   self.Pck_invoke_s[c_RequestChangePetName().invoke] = c_RequestChangePetName()
   self.Pck_invoke_s[c_RequestPetUseItem().invoke] = c_RequestPetUseItem()
   self.Pck_invoke_s[c_RequestGiveItemToPet().invoke] = c_RequestGiveItemToPet()
   self.Pck_invoke_s[c_RequestPrivateStoreQuitSell().invoke] = c_RequestPrivateStoreQuitSell()
   self.Pck_invoke_s[c_SetPrivateStoreMsgSell().invoke] = c_SetPrivateStoreMsgSell()
   self.Pck_invoke_s[c_RequestPetGetItem().invoke] = c_RequestPetGetItem()
   self.Pck_invoke_s[c_RequestPrivateStoreManageBuy().invoke] = c_RequestPrivateStoreManageBuy()
   self.Pck_invoke_s[c_SetPrivateStoreListBuy().invoke] = c_SetPrivateStoreListBuy()
   self.Pck_invoke_s[c_RequestPrivateStoreQuitBuy().invoke] = c_RequestPrivateStoreQuitBuy()
   self.Pck_invoke_s[c_SetPrivateStoreMsgBuy().invoke] = c_SetPrivateStoreMsgBuy()
   self.Pck_invoke_s[c_RequestPrivateStoreSell().invoke] = c_RequestPrivateStoreSell()
   self.Pck_invoke_s[c_RequestSkillCoolTime().invoke] = c_RequestSkillCoolTime()
   self.Pck_invoke_s[c_RequestPackageSendableItemList().invoke] = c_RequestPackageSendableItemList()
   self.Pck_invoke_s[c_RequestPackageSend().invoke] = c_RequestPackageSend()
   self.Pck_invoke_s[c_RequestBlock().invoke] = c_RequestBlock()
   self.Pck_invoke_s[c_RequestSiegeAttackerList().invoke] = c_RequestSiegeAttackerList()
   self.Pck_invoke_s[c_RequestSiegeDefenderList().invoke] = c_RequestSiegeDefenderList()
   self.Pck_invoke_s[c_RequestJoinSiege().invoke] = c_RequestJoinSiege()
   self.Pck_invoke_s[c_RequestConfirmSiegeWaitingList().invoke] = c_RequestConfirmSiegeWaitingList()
   self.Pck_invoke_s[c_MultiSellChoose().invoke] = c_MultiSellChoose()
   self.Pck_invoke_s[c_NetPing().invoke] = c_NetPing()
   self.Pck_invoke_s[c_RequestUserCommand().invoke] = c_RequestUserCommand()
   self.Pck_invoke_s[c_SnoopQuit().invoke] = c_SnoopQuit()
   self.Pck_invoke_s[c_RequestRecipeBookOpen().invoke] = c_RequestRecipeBookOpen()
   self.Pck_invoke_s[c_RequestRecipeBookDestroy().invoke] = c_RequestRecipeBookDestroy()
   self.Pck_invoke_s[c_RequestRecipeItemMakeInfo().invoke] = c_RequestRecipeItemMakeInfo()
   self.Pck_invoke_s[c_RequestRecipeItemMakeSelf().invoke] = c_RequestRecipeItemMakeSelf()
   self.Pck_invoke_s[c_RequestRecipeShopMessageSet().invoke] = c_RequestRecipeShopMessageSet()
   self.Pck_invoke_s[c_RequestRecipeShopListSet().invoke] = c_RequestRecipeShopListSet()
   self.Pck_invoke_s[c_RequestRecipeShopManageQuit().invoke] = c_RequestRecipeShopManageQuit()
   self.Pck_invoke_s[c_RequestRecipeShopMakeInfo().invoke] = c_RequestRecipeShopMakeInfo()
   self.Pck_invoke_s[c_RequestRecipeShopMakeItem().invoke] = c_RequestRecipeShopMakeItem()
   self.Pck_invoke_s[c_RequestRecipeShopManagePrev().invoke] = c_RequestRecipeShopManagePrev()
   self.Pck_invoke_s[c_ObserverReturn().invoke] = c_ObserverReturn()
   self.Pck_invoke_s[c_RequestEvaluate().invoke] = c_RequestEvaluate()
   self.Pck_invoke_s[c_RequestHennaList().invoke] = c_RequestHennaList()
   self.Pck_invoke_s[c_RequestHennaItemInfo().invoke] = c_RequestHennaItemInfo()
   self.Pck_invoke_s[c_RequestBuySeed().invoke] = c_RequestBuySeed()
   self.Pck_invoke_s[c_DlgAnswer().invoke] = c_DlgAnswer()
   self.Pck_invoke_s[c_RequestWearItem().invoke] = c_RequestWearItem()
   self.Pck_invoke_s[c_RequestSSQStatus().invoke] = c_RequestSSQStatus()
   self.Pck_invoke_s[c_GameGuardReply().invoke] = c_GameGuardReply()
   self.Pck_invoke_s[c_RequestPledgePower().invoke] = c_RequestPledgePower()
   self.Pck_invoke_s[c_RequestMakeMacro().invoke] = c_RequestMakeMacro()
   self.Pck_invoke_s[c_RequestDeleteMacro().invoke] = c_RequestDeleteMacro()
   self.Pck_invoke_s[c_RequestBuyProcure().invoke] = c_RequestBuyProcure()
   self.Pck_invoke_s[c_RequestGotoLobby().invoke] = c_RequestGotoLobby()
   self.Pck_invoke_s[c_RequestManorList().invoke] = c_RequestManorList()
   self.Pck_invoke_s[c_RequestProcureCropList().invoke] = c_RequestProcureCropList()
   self.Pck_invoke_s[c_RequestSetSeed().invoke] = c_RequestSetSeed()
   self.Pck_invoke_s[c_RequestSetCrop().invoke] = c_RequestSetCrop()
   self.Pck_invoke_s[c_RequestWriteHeroWords().invoke] = c_RequestWriteHeroWords()
   self.Pck_invoke_s[c_RequestExAskJoinMPCC().invoke] = c_RequestExAskJoinMPCC()
   self.Pck_invoke_s[c_RequestExAcceptJoinMPCC().invoke] = c_RequestExAcceptJoinMPCC()
   self.Pck_invoke_s[c_RequestExOustFromMPCC().invoke] = c_RequestExOustFromMPCC()
   self.Pck_invoke_s[c_RequestOustFromPartyRoom().invoke] = c_RequestOustFromPartyRoom()
   self.Pck_invoke_s[c_RequestDismissPartyRoom().invoke] = c_RequestDismissPartyRoom()
   self.Pck_invoke_s[c_RequestWithdrawPartyRoom().invoke] = c_RequestWithdrawPartyRoom()
   self.Pck_invoke_s[c_RequestChangePartyLeader().invoke] = c_RequestChangePartyLeader()
   self.Pck_invoke_s[c_RequestAutoSoulShot().invoke] = c_RequestAutoSoulShot()
   self.Pck_invoke_s[c_RequestExEnchantSkillInfo().invoke] = c_RequestExEnchantSkillInfo()
   self.Pck_invoke_s[c_RequestExEnchantSkill().invoke] = c_RequestExEnchantSkill()
   self.Pck_invoke_s[c_RequestExPledgeCrestLarge().invoke] = c_RequestExPledgeCrestLarge()
   self.Pck_invoke_s[c_RequestExSetPledgeCrestLarge().invoke] = c_RequestExSetPledgeCrestLarge()
   self.Pck_invoke_s[c_RequestPledgeSetAcademyMaster().invoke] = c_RequestPledgeSetAcademyMaster()
   self.Pck_invoke_s[c_RequestPledgePowerGradeList().invoke] = c_RequestPledgePowerGradeList()
   self.Pck_invoke_s[c_RequestPledgeMemberPowerInfo().invoke] = c_RequestPledgeMemberPowerInfo()
   self.Pck_invoke_s[c_RequestPledgeSetMemberPowerGrade().invoke] = c_RequestPledgeSetMemberPowerGrade()
   self.Pck_invoke_s[c_RequestPledgeMemberInfo().invoke] = c_RequestPledgeMemberInfo()
   self.Pck_invoke_s[c_RequestPledgeWarList().invoke] = c_RequestPledgeWarList()
   self.Pck_invoke_s[c_RequestExFishRanking().invoke] = c_RequestExFishRanking()
   self.Pck_invoke_s[c_RequestPCCafeCouponUse().invoke] = c_RequestPCCafeCouponUse()
   self.Pck_invoke_s[c_RequestDuelStart().invoke] = c_RequestDuelStart()
   self.Pck_invoke_s[c_RequestDuelAnswerStart().invoke] = c_RequestDuelAnswerStart()
   self.Pck_invoke_s[c_RequestExRqItemLink().invoke] = c_RequestExRqItemLink()
   self.Pck_invoke_s[c_RequestKeyMapping().invoke] = c_RequestKeyMapping()
   self.Pck_invoke_s[c_RequestSaveInventoryOrder().invoke] = c_RequestSaveInventoryOrder()
   self.Pck_invoke_s[c_RequestExitPartyMatchingWaitingRoom().invoke] = c_RequestExitPartyMatchingWaitingRoom()
   self.Pck_invoke_s[c_RequestConfirmTargetItem().invoke] = c_RequestConfirmTargetItem()
   self.Pck_invoke_s[c_RequestConfirmRefinerItem().invoke] = c_RequestConfirmRefinerItem()
   self.Pck_invoke_s[c_RequestConfirmGemStone().invoke] = c_RequestConfirmGemStone()
   self.Pck_invoke_s[c_RequestOlympiadObserverEnd().invoke] = c_RequestOlympiadObserverEnd()
   self.Pck_invoke_s[c_RequestCursedWeaponList().invoke] = c_RequestCursedWeaponList()
   self.Pck_invoke_s[c_RequestCursedWeaponLocation().invoke] = c_RequestCursedWeaponLocation()
   self.Pck_invoke_s[c_RequestPledgeReorganizeMember().invoke] = c_RequestPledgeReorganizeMember()
   self.Pck_invoke_s[c_RequestExMPCCShowPartyMembersInfo().invoke] = c_RequestExMPCCShowPartyMembersInfo()
   self.Pck_invoke_s[c_RequestOlympiadMatchList().invoke] = c_RequestOlympiadMatchList()
   self.Pck_invoke_s[c_RequestAskJoinPartyRoom().invoke] = c_RequestAskJoinPartyRoom()
   self.Pck_invoke_s[c_AnswerJoinPartyRoom().invoke] = c_AnswerJoinPartyRoom()
   self.Pck_invoke_s[c_RequestListPartyMatchingWaitingRoom().invoke] = c_RequestListPartyMatchingWaitingRoom()
   self.Pck_invoke_s[c_RequestExEnchantSkillSafe().invoke] = c_RequestExEnchantSkillSafe()
   self.Pck_invoke_s[c_RequestExEnchantSkillUntrain().invoke] = c_RequestExEnchantSkillUntrain()
   self.Pck_invoke_s[c_RequestExEnchantSkillRouteChange().invoke] = c_RequestExEnchantSkillRouteChange()
   self.Pck_invoke_s[c_ExGetOnAirShip().invoke] = c_ExGetOnAirShip()
   self.Pck_invoke_s[c_RequestAllCastleInfo().invoke] = c_RequestAllCastleInfo()
   self.Pck_invoke_s[c_RequestAllFortressInfo().invoke] = c_RequestAllFortressInfo()
   self.Pck_invoke_s[c_RequestAllAgitInfo().invoke] = c_RequestAllAgitInfo()
   self.Pck_invoke_s[c_RequestFortressSiegeInfo().invoke] = c_RequestFortressSiegeInfo()
   self.Pck_invoke_s[c_RequestGetBossRecord().invoke] = c_RequestGetBossRecord()
   self.Pck_invoke_s[c_RequestRefine().invoke] = c_RequestRefine()
   self.Pck_invoke_s[c_RequestConfirmCancelItem().invoke] = c_RequestConfirmCancelItem()
   self.Pck_invoke_s[c_RequestRefineCancel().invoke] = c_RequestRefineCancel()
   self.Pck_invoke_s[c_RequestExMagicSkillUseGround().invoke] = c_RequestExMagicSkillUseGround()
   self.Pck_invoke_s[c_RequestDuelSurrender().invoke] = c_RequestDuelSurrender()
   self.Pck_invoke_s[c_RequestExEnchantSkillInfoDetail().invoke] = c_RequestExEnchantSkillInfoDetail()
   self.Pck_invoke_s[c_RequestExCancelAbnormalState().invoke] = c_RequestExCancelAbnormalState()
   return self.Pck_invoke_s
 def get_Pck_invoke_s(self):
   self.Pck_invoke_c[s_Die().invoke] = s_Die()
   self.Pck_invoke_c[s_Revive().invoke] = s_Revive()
   self.Pck_invoke_c[s_SpawnItem().invoke] = s_SpawnItem()
   self.Pck_invoke_c[s_SellList().invoke] = s_SellList()
   self.Pck_invoke_c[s_BuyList().invoke] = s_BuyList()
   self.Pck_invoke_c[s_DeleteObject().invoke] = s_DeleteObject()
   self.Pck_invoke_c[s_CharSelectionInfo().invoke] = s_CharSelectionInfo()
   self.Pck_invoke_c[s_LoginFail().invoke] = s_LoginFail()
   self.Pck_invoke_c[s_CharSelected().invoke] = s_CharSelected()
   self.Pck_invoke_c[s_NpcInfo().invoke] = s_NpcInfo()
   self.Pck_invoke_c[s_NewCharacterSuccess().invoke] = s_NewCharacterSuccess()
   self.Pck_invoke_c[s_CharCreateOk().invoke] = s_CharCreateOk()
   self.Pck_invoke_c[s_CharCreateFail().invoke] = s_CharCreateFail()
   self.Pck_invoke_c[s_ItemList().invoke] = s_ItemList()
   self.Pck_invoke_c[s_SunRise().invoke] = s_SunRise()
   self.Pck_invoke_c[s_SunSet().invoke] = s_SunSet()
   self.Pck_invoke_c[s_TradeStart().invoke] = s_TradeStart()
   self.Pck_invoke_c[s_DropItem().invoke] = s_DropItem()
   self.Pck_invoke_c[s_GetItem().invoke] = s_GetItem()
   self.Pck_invoke_c[s_StatusUpdate().invoke] = s_StatusUpdate()
   self.Pck_invoke_c[s_NpcHtmlMessage().invoke] = s_NpcHtmlMessage()
   self.Pck_invoke_c[s_TradeOwnAdd().invoke] = s_TradeOwnAdd()
   self.Pck_invoke_c[s_TradeOtherAdd().invoke] = s_TradeOtherAdd()
   self.Pck_invoke_c[s_TradeDone().invoke] = s_TradeDone()
   self.Pck_invoke_c[s_CharDeleteSuccess().invoke] = s_CharDeleteSuccess()
   self.Pck_invoke_c[s_CharDeleteFail().invoke] = s_CharDeleteFail()
   self.Pck_invoke_c[s_ActionFailed().invoke] = s_ActionFailed()
   self.Pck_invoke_c[s_ServerClose().invoke] = s_ServerClose()
   self.Pck_invoke_c[s_InventoryUpdate().invoke] = s_InventoryUpdate()
   self.Pck_invoke_c[s_TeleportToLocation().invoke] = s_TeleportToLocation()
   self.Pck_invoke_c[s_TargetSelected().invoke] = s_TargetSelected()
   self.Pck_invoke_c[s_TargetUnselected().invoke] = s_TargetUnselected()
   self.Pck_invoke_c[s_AutoAttackStart().invoke] = s_AutoAttackStart()
   self.Pck_invoke_c[s_AutoAttackStop().invoke] = s_AutoAttackStop()
   self.Pck_invoke_c[s_SocialAction().invoke] = s_SocialAction()
   self.Pck_invoke_c[s_ChangeMoveType().invoke] = s_ChangeMoveType()
   self.Pck_invoke_c[s_ChangeWaitType().invoke] = s_ChangeWaitType()
   self.Pck_invoke_c[s_ManagePledgePower().invoke] = s_ManagePledgePower()
   self.Pck_invoke_c[s_AskJoinPledge().invoke] = s_AskJoinPledge()
   self.Pck_invoke_c[s_JoinPledge().invoke] = s_JoinPledge()
   self.Pck_invoke_c[s_KeyPacket().invoke] = s_KeyPacket()
   self.Pck_invoke_c[s_MoveToLocation().invoke] = s_MoveToLocation()
   self.Pck_invoke_c[s_SummonSay().invoke] = s_SummonSay()
   self.Pck_invoke_c[s_CharInfo().invoke] = s_CharInfo()
   self.Pck_invoke_c[s_UserInfo().invoke] = s_UserInfo()
   self.Pck_invoke_c[s_Attack().invoke] = s_Attack()
   self.Pck_invoke_c[s_AskJoinParty().invoke] = s_AskJoinParty()
   self.Pck_invoke_c[s_JoinParty().invoke] = s_JoinParty()
   self.Pck_invoke_c[s_Unknown40().invoke] = s_Unknown40()
   self.Pck_invoke_c[s_WareHouseDepositList().invoke] = s_WareHouseDepositList()
   self.Pck_invoke_c[s_WareHouseWithdrawList().invoke] = s_WareHouseWithdrawList()
   self.Pck_invoke_c[s_ShortCutRegister().invoke] = s_ShortCutRegister()
   self.Pck_invoke_c[s_StopMove().invoke] = s_StopMove()
   self.Pck_invoke_c[s_MagicSkillUse().invoke] = s_MagicSkillUse()
   self.Pck_invoke_c[s_MagicSkillCanceled().invoke] = s_MagicSkillCanceled()
   self.Pck_invoke_c[s_CreatureSay().invoke] = s_CreatureSay()
   self.Pck_invoke_c[s_EquipUpdate().invoke] = s_EquipUpdate()
   self.Pck_invoke_c[s_DoorInfo().invoke] = s_DoorInfo()
   self.Pck_invoke_c[s_DoorStatusUpdate().invoke] = s_DoorStatusUpdate()
   self.Pck_invoke_c[s_PartySmallWindowAll().invoke] = s_PartySmallWindowAll()
   self.Pck_invoke_c[s_PartySmallWindowAdd().invoke] = s_PartySmallWindowAdd()
   self.Pck_invoke_c[s_PartySmallWindowDeleteAll().invoke] = s_PartySmallWindowDeleteAll()
   self.Pck_invoke_c[s_PartySmallWindowDelete().invoke] = s_PartySmallWindowDelete()
   self.Pck_invoke_c[s_PartySmallWindowUpdate().invoke] = s_PartySmallWindowUpdate()
   self.Pck_invoke_c[s_MagicSkillLaunched().invoke] = s_MagicSkillLaunched()
   self.Pck_invoke_c[s_PledgeShowMemberListAll().invoke] = s_PledgeShowMemberListAll()
   self.Pck_invoke_c[s_PledgeShowMemberListUpdate().invoke] = s_PledgeShowMemberListUpdate()
   self.Pck_invoke_c[s_PledgeShowMemberListAdd().invoke] = s_PledgeShowMemberListAdd()
   self.Pck_invoke_c[s_PledgeShowMemberListDelete().invoke] = s_PledgeShowMemberListDelete()
   self.Pck_invoke_c[s_SkillList().invoke] = s_SkillList()
   self.Pck_invoke_c[s_VehicleInfo().invoke] = s_VehicleInfo()
   self.Pck_invoke_c[s_StopRotation().invoke] = s_StopRotation()
   self.Pck_invoke_c[s_StartPledgeWar().invoke] = s_StartPledgeWar()
   self.Pck_invoke_c[s_StopPledgeWar().invoke] = s_StopPledgeWar()
   self.Pck_invoke_c[s_SurrenderPledgeWar().invoke] = s_SurrenderPledgeWar()
   self.Pck_invoke_c[s_PledgeCrest().invoke] = s_PledgeCrest()
   self.Pck_invoke_c[s_SetupGauge().invoke] = s_SetupGauge()
   self.Pck_invoke_c[s_VehicleDeparture().invoke] = s_VehicleDeparture()
   self.Pck_invoke_c[s_VehicleCheckLocation().invoke] = s_VehicleCheckLocation()
   self.Pck_invoke_c[s_GetOnVehicle().invoke] = s_GetOnVehicle()
   self.Pck_invoke_c[s_GetOffVehicle().invoke] = s_GetOffVehicle()
   self.Pck_invoke_c[s_SendTradeRequest().invoke] = s_SendTradeRequest()
   self.Pck_invoke_c[s_RestartResponse().invoke] = s_RestartResponse()
   self.Pck_invoke_c[s_MoveToPawn().invoke] = s_MoveToPawn()
   self.Pck_invoke_c[s_SSQInfo().invoke] = s_SSQInfo()
   self.Pck_invoke_c[s_GameGuardQuery().invoke] = s_GameGuardQuery()
   self.Pck_invoke_c[s_FriendList().invoke] = s_FriendList()
   self.Pck_invoke_c[s_L2FriendSay().invoke] = s_L2FriendSay()
   self.Pck_invoke_c[s_ValidateLocation().invoke] = s_ValidateLocation()
   self.Pck_invoke_c[s_StartRotation().invoke] = s_StartRotation()
   self.Pck_invoke_c[s_ShowBoard().invoke] = s_ShowBoard()
   self.Pck_invoke_c[s_ChooseInventoryItem().invoke] = s_ChooseInventoryItem()
   self.Pck_invoke_c[s_MoveToLocationInVehicle().invoke] = s_MoveToLocationInVehicle()
   self.Pck_invoke_c[s_StopMoveInVehicle().invoke] = s_StopMoveInVehicle()
   self.Pck_invoke_c[s_ValidateLocationInVehicle().invoke] = s_ValidateLocationInVehicle()
   self.Pck_invoke_c[s_FriendAddRequest().invoke] = s_FriendAddRequest()
   self.Pck_invoke_c[s_LeaveWorld().invoke] = s_LeaveWorld()
   self.Pck_invoke_c[s_AbnormalStatusUpdate().invoke] = s_AbnormalStatusUpdate()
   self.Pck_invoke_c[s_QuestList().invoke] = s_QuestList()
   self.Pck_invoke_c[s_EnchantResult().invoke] = s_EnchantResult()
   self.Pck_invoke_c[s_PledgeShowMemberListDeleteAll().invoke] = s_PledgeShowMemberListDeleteAll()
   self.Pck_invoke_c[s_PledgeInfo().invoke] = s_PledgeInfo()
   self.Pck_invoke_c[s_Ride().invoke] = s_Ride()
   self.Pck_invoke_c[s_PledgeShowInfoUpdate().invoke] = s_PledgeShowInfoUpdate()
   self.Pck_invoke_c[s_AcquireSkillList().invoke] = s_AcquireSkillList()
   self.Pck_invoke_c[s_AcquireSkillInfo().invoke] = s_AcquireSkillInfo()
   self.Pck_invoke_c[s_GMViewCharacterInfo().invoke] = s_GMViewCharacterInfo()
   self.Pck_invoke_c[s_GMViewPledgeInfo().invoke] = s_GMViewPledgeInfo()
   self.Pck_invoke_c[s_GMViewSkillInfo().invoke] = s_GMViewSkillInfo()
   self.Pck_invoke_c[s_GMViewQuestInfo().invoke] = s_GMViewQuestInfo()
   self.Pck_invoke_c[s_GMViewItemList().invoke] = s_GMViewItemList()
   self.Pck_invoke_c[s_GMViewWarehouseWithdrawList().invoke] = s_GMViewWarehouseWithdrawList()
   self.Pck_invoke_c[s_ListPartyWaiting().invoke] = s_ListPartyWaiting()
   self.Pck_invoke_c[s_PartyMatchDetail().invoke] = s_PartyMatchDetail()
   self.Pck_invoke_c[s_PlaySound().invoke] = s_PlaySound()
   self.Pck_invoke_c[s_StaticObject().invoke] = s_StaticObject()
   self.Pck_invoke_c[s_PrivateStoreManageListSell().invoke] = s_PrivateStoreManageListSell()
   self.Pck_invoke_c[s_PrivateStoreListSell().invoke] = s_PrivateStoreListSell()
   self.Pck_invoke_c[s_PrivateStoreMsgSell().invoke] = s_PrivateStoreMsgSell()
   self.Pck_invoke_c[s_ShowMiniMap().invoke] = s_ShowMiniMap()
   self.Pck_invoke_c[s_TutorialShowHtml().invoke] = s_TutorialShowHtml()
   self.Pck_invoke_c[s_TutorialClose().invoke] = s_TutorialClose()
   self.Pck_invoke_c[s_TutorialShowQuestionMark().invoke] = s_TutorialShowQuestionMark()
   self.Pck_invoke_c[s_AllyCrest().invoke] = s_AllyCrest()
   self.Pck_invoke_c[s_PetStatusShow().invoke] = s_PetStatusShow()
   self.Pck_invoke_c[s_PetInfo().invoke] = s_PetInfo()
   self.Pck_invoke_c[s_PetItemList().invoke] = s_PetItemList()
   self.Pck_invoke_c[s_PetInventoryUpdate().invoke] = s_PetInventoryUpdate()
   self.Pck_invoke_c[s_PetStatusUpdate().invoke] = s_PetStatusUpdate()
   self.Pck_invoke_c[s_PetDelete().invoke] = s_PetDelete()
   self.Pck_invoke_c[s_MyTargetSelected().invoke] = s_MyTargetSelected()
   self.Pck_invoke_c[s_PartyMemberPosition().invoke] = s_PartyMemberPosition()
   self.Pck_invoke_c[s_AskJoinAlly().invoke] = s_AskJoinAlly()
   self.Pck_invoke_c[s_PrivateStoreListBuy().invoke] = s_PrivateStoreListBuy()
   self.Pck_invoke_c[s_PrivateStoreMsgBuy().invoke] = s_PrivateStoreMsgBuy()
   self.Pck_invoke_c[s_SkillCoolTime().invoke] = s_SkillCoolTime()
   self.Pck_invoke_c[s_PackageToList().invoke] = s_PackageToList()
   self.Pck_invoke_c[s_SiegeInfo().invoke] = s_SiegeInfo()
   self.Pck_invoke_c[s_SiegeAttackerList().invoke] = s_SiegeAttackerList()
   self.Pck_invoke_c[s_SiegeDefenderList().invoke] = s_SiegeDefenderList()
   self.Pck_invoke_c[s_NicknameChanged().invoke] = s_NicknameChanged()
   self.Pck_invoke_c[s_PledgeStatusChanged().invoke] = s_PledgeStatusChanged()
   self.Pck_invoke_c[s_RelationChanged().invoke] = s_RelationChanged()
   self.Pck_invoke_c[s_SetSummonRemainTime().invoke] = s_SetSummonRemainTime()
   self.Pck_invoke_c[s_PackageSendableList().invoke] = s_PackageSendableList()
   self.Pck_invoke_c[s_Earthquake().invoke] = s_Earthquake()
   self.Pck_invoke_c[s_FlyToLoaction().invoke] = s_FlyToLoaction()
   self.Pck_invoke_c[s_SpecialCamera().invoke] = s_SpecialCamera()
   self.Pck_invoke_c[s_NormalCamera().invoke] = s_NormalCamera()
   self.Pck_invoke_c[s_NetPing().invoke] = s_NetPing()
   self.Pck_invoke_c[s_Dice().invoke] = s_Dice()
   self.Pck_invoke_c[s_Snoop().invoke] = s_Snoop()
   self.Pck_invoke_c[s_RecipeBookItemList().invoke] = s_RecipeBookItemList()
   self.Pck_invoke_c[s_RecipeItemMakeInfo().invoke] = s_RecipeItemMakeInfo()
   self.Pck_invoke_c[s_RecipeShopSellList().invoke] = s_RecipeShopSellList()
   self.Pck_invoke_c[s_RecipeShopItemInfo().invoke] = s_RecipeShopItemInfo()
   self.Pck_invoke_c[s_RecipeShopMsg().invoke] = s_RecipeShopMsg()
   self.Pck_invoke_c[s_ShowCalculator().invoke] = s_ShowCalculator()
   self.Pck_invoke_c[s_MonRaceInfo().invoke] = s_MonRaceInfo()
   self.Pck_invoke_c[s_HennaItemInfo().invoke] = s_HennaItemInfo()
   self.Pck_invoke_c[s_HennaInfo().invoke] = s_HennaInfo()
   self.Pck_invoke_c[s_SendMacroList().invoke] = s_SendMacroList()
   self.Pck_invoke_c[s_BuyListSeed().invoke] = s_BuyListSeed()
   self.Pck_invoke_c[s_ShowTownMap().invoke] = s_ShowTownMap()
   self.Pck_invoke_c[s_ObservationMode().invoke] = s_ObservationMode()
   self.Pck_invoke_c[s_ObservationReturn().invoke] = s_ObservationReturn()
   self.Pck_invoke_c[s_ChairSit().invoke] = s_ChairSit()
   self.Pck_invoke_c[s_HennaEquipList().invoke] = s_HennaEquipList()
   self.Pck_invoke_c[s_SellListProcure().invoke] = s_SellListProcure()
   self.Pck_invoke_c[s_GMHennaInfo().invoke] = s_GMHennaInfo()
   self.Pck_invoke_c[s_RadarControl().invoke] = s_RadarControl()
   self.Pck_invoke_c[s_ConfirmDlg().invoke] = s_ConfirmDlg()
   self.Pck_invoke_c[s_PartySpelled().invoke] = s_PartySpelled()
   self.Pck_invoke_c[s_ShopPreviewList().invoke] = s_ShopPreviewList()
   self.Pck_invoke_c[s_CameraMode().invoke] = s_CameraMode()
   self.Pck_invoke_c[s_ShowXMasSeal().invoke] = s_ShowXMasSeal()
   self.Pck_invoke_c[s_EtcStatusUpdate().invoke] = s_EtcStatusUpdate()
   self.Pck_invoke_c[s_ShortBuffStatusUpdate().invoke] = s_ShortBuffStatusUpdate()
   self.Pck_invoke_c[s_SSQStatus().invoke] = s_SSQStatus()
   self.Pck_invoke_c[s_AgitDecoInfo().invoke] = s_AgitDecoInfo()
   self.Pck_invoke_c[s_ExRegMax().invoke] = s_ExRegMax()
   self.Pck_invoke_c[s_ExAutoSoulShot().invoke] = s_ExAutoSoulShot()
   self.Pck_invoke_c[s_ExOpenMPCC().invoke] = s_ExOpenMPCC()
   self.Pck_invoke_c[s_ExCloseMPCC().invoke] = s_ExCloseMPCC()
   self.Pck_invoke_c[s_ExShowCastleInfo().invoke] = s_ExShowCastleInfo()
   self.Pck_invoke_c[s_ExShowFortressInfo().invoke] = s_ExShowFortressInfo()
   self.Pck_invoke_c[s_ExShowAgitInfo().invoke] = s_ExShowAgitInfo()
   self.Pck_invoke_c[s_ExShowFortressSiegeInfo().invoke] = s_ExShowFortressSiegeInfo()
   self.Pck_invoke_c[s_ExPartyPetWindowAdd().invoke] = s_ExPartyPetWindowAdd()
   self.Pck_invoke_c[s_ExPartyPetWindowUpdate().invoke] = s_ExPartyPetWindowUpdate()
   self.Pck_invoke_c[s_ExAskJoinMPCC().invoke] = s_ExAskJoinMPCC()
   self.Pck_invoke_c[s_ExPledgeCrestLarge().invoke] = s_ExPledgeCrestLarge()
   self.Pck_invoke_c[s_ExFishingStart().invoke] = s_ExFishingStart()
   self.Pck_invoke_c[s_ExFishingEnd().invoke] = s_ExFishingEnd()
   self.Pck_invoke_c[s_ExShowQuestInfo().invoke] = s_ExShowQuestInfo()
   self.Pck_invoke_c[s_ExShowQuestMark().invoke] = s_ExShowQuestMark()
   self.Pck_invoke_c[s_ExSendManorList().invoke] = s_ExSendManorList()
   self.Pck_invoke_c[s_ExShowSeedInfo().invoke] = s_ExShowSeedInfo()
   self.Pck_invoke_c[s_ExShowCropInfo().invoke] = s_ExShowCropInfo()
   self.Pck_invoke_c[s_ExShowManorDefaultInfo().invoke] = s_ExShowManorDefaultInfo()
   self.Pck_invoke_c[s_ExShowSeedSetting().invoke] = s_ExShowSeedSetting()
   self.Pck_invoke_c[s_ExFishingStartCombat().invoke] = s_ExFishingStartCombat()
   self.Pck_invoke_c[s_ExFishingHPRegen().invoke] = s_ExFishingHPRegen()
   self.Pck_invoke_c[s_ExEnchantSkillList().invoke] = s_ExEnchantSkillList()
   self.Pck_invoke_c[s_ExEnchantSkillInfo().invoke] = s_ExEnchantSkillInfo()
   self.Pck_invoke_c[s_ExShowCropSetting().invoke] = s_ExShowCropSetting()
   self.Pck_invoke_c[s_ExShowSellCropList().invoke] = s_ExShowSellCropList()
   self.Pck_invoke_c[s_ExMailArrived().invoke] = s_ExMailArrived()
   self.Pck_invoke_c[s_ExStorageMaxCount().invoke] = s_ExStorageMaxCount()
   self.Pck_invoke_c[s_ExPCCafePointInfo().invoke] = s_ExPCCafePointInfo()
   self.Pck_invoke_c[s_ExSetCompassZoneCode().invoke] = s_ExSetCompassZoneCode()
   self.Pck_invoke_c[s_ExGetBossRecord().invoke] = s_ExGetBossRecord()
   self.Pck_invoke_c[s_ExAskJoinPartyRoom().invoke] = s_ExAskJoinPartyRoom()
   self.Pck_invoke_c[s_ExShowAdventurerGuideBook().invoke] = s_ExShowAdventurerGuideBook()
   self.Pck_invoke_c[s_PledgeSkillList().invoke] = s_PledgeSkillList()
   self.Pck_invoke_c[s_PledgeSkillListAdd().invoke] = s_PledgeSkillListAdd()
   self.Pck_invoke_c[s_PledgePowerGradeList().invoke] = s_PledgePowerGradeList()
   self.Pck_invoke_c[s_PledgeReceivePowerInfo().invoke] = s_PledgeReceivePowerInfo()
   self.Pck_invoke_c[s_PledgeReceiveMemberInfo().invoke] = s_PledgeReceiveMemberInfo()
   self.Pck_invoke_c[s_PledgeReceiveWarList().invoke] = s_PledgeReceiveWarList()
   self.Pck_invoke_c[s_PledgeReceiveSubPledgeCreated().invoke] = s_PledgeReceiveSubPledgeCreated()
   self.Pck_invoke_c[s_ExRedSky().invoke] = s_ExRedSky()
   self.Pck_invoke_c[s_ShowPCCafeCouponShowUI().invoke] = s_ShowPCCafeCouponShowUI()
   self.Pck_invoke_c[s_ExSearchOrc().invoke] = s_ExSearchOrc()
   self.Pck_invoke_c[s_ExCursedWeaponList().invoke] = s_ExCursedWeaponList()
   self.Pck_invoke_c[s_ExCursedWeaponLocation().invoke] = s_ExCursedWeaponLocation()
   self.Pck_invoke_c[s_ExRestartClient().invoke] = s_ExRestartClient()
   self.Pck_invoke_c[s_ExRequestHackShield().invoke] = s_ExRequestHackShield()
   self.Pck_invoke_c[s_ExUseSharedGroupItem().invoke] = s_ExUseSharedGroupItem()
   self.Pck_invoke_c[s_ExMPCCShowPartyMemberInfo().invoke] = s_ExMPCCShowPartyMemberInfo()
   self.Pck_invoke_c[s_ExDuelAskStart().invoke] = s_ExDuelAskStart()
   self.Pck_invoke_c[s_ExDuelReady().invoke] = s_ExDuelReady()
   self.Pck_invoke_c[s_ExDuelStart().invoke] = s_ExDuelStart()
   self.Pck_invoke_c[s_ExDuelEnd().invoke] = s_ExDuelEnd()
   self.Pck_invoke_c[s_ExDuelUpdateUserInfo().invoke] = s_ExDuelUpdateUserInfo()
   self.Pck_invoke_c[s_ExShowVariationMakeWindow().invoke] = s_ExShowVariationMakeWindow()
   self.Pck_invoke_c[s_ExShowVariationCancelWindow().invoke] = s_ExShowVariationCancelWindow()
   self.Pck_invoke_c[s_ExPutItemResultForVariationMake().invoke] = s_ExPutItemResultForVariationMake()
   self.Pck_invoke_c[s_ExPutIntensiveResultForVariationMake().invoke] = s_ExPutIntensiveResultForVariationMake()
   self.Pck_invoke_c[s_ExPutCommissionResultForVariationMake().invoke] = s_ExPutCommissionResultForVariationMake()
   self.Pck_invoke_c[s_ExVariationResult().invoke] = s_ExVariationResult()
   self.Pck_invoke_c[s_ExPutItemResultForVariationCancel().invoke] = s_ExPutItemResultForVariationCancel()
   self.Pck_invoke_c[s_ExVariationCancelResult().invoke] = s_ExVariationCancelResult()
   self.Pck_invoke_c[s_ExPlayScene().invoke] = s_ExPlayScene()
   self.Pck_invoke_c[s_ExSpawnEmitter().invoke] = s_ExSpawnEmitter()
   self.Pck_invoke_c[s_ExEnchantSkillInfoDetail().invoke] = s_ExEnchantSkillInfoDetail()
   self.Pck_invoke_c[s_ExBasicActionList().invoke] = s_ExBasicActionList()
   self.Pck_invoke_c[s_ExChooseInventoryAttributeItem().invoke] = s_ExChooseInventoryAttributeItem()
   self.Pck_invoke_c[s_ExPartyPetWindowDelete().invoke] = s_ExPartyPetWindowDelete()
   self.Pck_invoke_c[s_ExShowProcureCropDetail().invoke] = s_ExShowProcureCropDetail()
   self.Pck_invoke_c[s_ExHeroList().invoke] = s_ExHeroList()
   self.Pck_invoke_c[s_OlympiadUserInfoSpectator().invoke] = s_OlympiadUserInfoSpectator()
   self.Pck_invoke_c[s_ExOlympiadSpelledInfo().invoke] = s_ExOlympiadSpelledInfo()
   self.Pck_invoke_c[s_ExOlympiadMode().invoke] = s_ExOlympiadMode()
   self.Pck_invoke_c[s_ExGetBookMarkInfoPacket().invoke] = s_ExGetBookMarkInfoPacket()
   self.Pck_invoke_c[s_UnknownFEAA().invoke] = s_UnknownFEAA()
   self.Pck_invoke_c[s_ExBrExtraUserInfo().invoke] = s_ExBrExtraUserInfo()
   return self.Pck_invoke_c
