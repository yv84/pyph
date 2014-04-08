import struct
#--------------------------------------------------------------------------#00
class c_ProtocolVersion():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ProtocolVersion', 'i4')
              , ('0256fixed', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01
class c_MoveBackwardToLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ToX', 'i4')
              , ('ToY', 'i4')
              , ('ToZ', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
              , ('moveByMouse', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#02
class c_Say():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x02'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Msg', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#03
class c_EnterWorld():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x03'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
              , ('d_4', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#04
class c_Action():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x04'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
              , ('ShiftFlag', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#08
class c_RequestAuthLogin():
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
              , ('LoginName', '|S'+str(self.It.__next__()) )
              , ('PlayKey2', 'i4')
              , ('PlayKey1', 'i4')
              , ('LoginKey1', 'i4')
              , ('LoginKey2', 'i4')
              , ('d', 'i4')
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
class c_LogoutRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x09'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0A
class c_Attack():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
              , ('ShiftFlag', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0B
class c_CharCreate():
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
              , ('Race', 'i4')
              , ('Sex', 'i4')
              , ('ClassID', 'i4')
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
#--------------------------------------------------------------------------#0C
class c_CharDelete():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharSlot', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0D
class c_CharSelected():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharSlot', 'i4')
              , ('h', 'i2')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0E
class c_NewCharacter():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0F
class c_RequestItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#10
class c_RequestEquipItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x10'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Slot', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#11
class c_RequestUnEquipItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x11'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Slot', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#12
class c_RequestDropItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x12'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Count', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#14
class c_UseItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x14'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#15
class c_TradeRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x15'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#16
class c_AddTradeItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x16'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TradeID', 'i4')
              , ('ObjectID', 'i4')
              , ('Count', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#17
class c_TradeDone():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x17'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1A
class c_RequestTeleport():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
              , ('d_4', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1B
class c_RequestSocialAction():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Action', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1C
class c_ChangeMoveType():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TypeRun', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1D
class c_ChangeWaitType():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TypeStand', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1E
class c_RequestSellItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1E'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListID', 'i4')
              , ('SellCountValue', 'i4')
                  ]+ list(self.f_SellCount()) +[
                  ]
    return dtype
  def f_SellCount(self):
    for i in range(self.It.__next__()):
      dtype = ('SellCount_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#1F
class c_RequestBuyItem():
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
              , ('ListID', 'i4')
              , ('BuyCountValue', 'i4')
                  ]+ list(self.f_BuyCount()) +[
                  ]
    return dtype
  def f_BuyCount(self):
    for i in range(self.It.__next__()):
      dtype = ('BuyCount_' + str(i) , [
               ('ItemID', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#20
class c_RequestLinkHtml():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x20'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('HtmlLink', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#21
class c_RequestBypassToServer():
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
              , ('Cmd', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#22
class c_RequestBBSwrite():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x22'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Url', '|S'+str(self.It.__next__()) )
              , ('Arg1', '|S'+str(self.It.__next__()) )
              , ('Arg2', '|S'+str(self.It.__next__()) )
              , ('Arg3', '|S'+str(self.It.__next__()) )
              , ('Arg4', '|S'+str(self.It.__next__()) )
              , ('Arg5', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#23
class c_RequestCreatePledge():
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
#--------------------------------------------------------------------------#24
class c_RequestJoinPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x24'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Target', 'i4')
              , ('pledgetype', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#25
class c_RequestAnswerJoinPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x25'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Answer', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#26
class c_RequestWithDrawalPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x26'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#27
class c_RequestOustPledgeMember():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x27'
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
#--------------------------------------------------------------------------#28
class c_RequestDismissPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x28'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#29
class c_RequestJoinParty():
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
#--------------------------------------------------------------------------#2A
class c_RequestAnswerJoinParty():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2B
class c_RequestWithDrawalParty():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#2C
class c_RequestOustPartyMember():
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
#--------------------------------------------------------------------------#2D
class c_RequestDismissParty():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#2E
class c_RequestMagicSkillList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('c_0', 'i1')
              , ('c_1', 'i1')
              , ('c_2', 'i1')
              , ('CharID', 'i4')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2F
class c_RequestMagicSkillUse():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('MagicID', 'i4')
              , ('CtrlPressed', 'i4')
              , ('ShiftPressed', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#30
class c_Appearing():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x30'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#31
class c_SendWareHouseDepositList():
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
              , ('CountValue', 'i4')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#32
class c_SendWareHouseWithDrawList():
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
              , ('CountValue', 'i4')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#33
class c_RequestShortCutReg():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x33'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Type', 'i4')
              , ('Slot', 'i4')
              , ('ID', 'i4')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#34
class c_RequestShortCutUse():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x34'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('c', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#35
class c_RequestShortCutDel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x35'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#36
class c_CannotMoveAnymore():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x36'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#37
class c_RequestTargetCancel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x37'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('unselect', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#38
class c_Say2():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x38'
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
#--------------------------------------------------------------------------#3C
class c_RequestPledgeMemberList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#3E
class c_RequestMagicList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#3F
class c_RequestSkillList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#40
class c_AnswerTradeRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x40'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#41
class c_MoveWithDelta():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x41'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('dx', 'i4')
              , ('dy', 'i4')
              , ('dz', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#42
class c_GetOnVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x42'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#43
class c_GetOffVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x43'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#44
class c_AnswerTradeRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x44'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('answer', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#45
class c_RequestActionUse():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x45'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ActionID', 'i4')
              , ('CtrlPressed', 'i4')
              , ('ShiftPressed', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#46
class c_RequestRestart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x46'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#47
class c_RequestSiegeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x47'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#48
class c_ValidatePosition():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x48'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('Data', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#49
class c_RequestSEKCustom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x49'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SlotNum', 'i4')
              , ('Direct', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#4A
class c_StartRotating():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Degree', 'i4')
              , ('Side', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#4B
class c_FinishRotating():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Degree', 'i4')
              , ('u', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#4D
class c_RequestStartPledgeWar():
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
#--------------------------------------------------------------------------#4E
class c_RequestReplyStartPledgeWar():
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
              , ('PledgeName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#4F
class c_RequestStopPledgeWar():
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
#--------------------------------------------------------------------------#50
class c_RequestReplyStopPledgeWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x50'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('PledgeName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#51
class c_RequestSurrenderPledgeWar():
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
#--------------------------------------------------------------------------#52
class c_RequestReplySurrenderPledgeWar():
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
              , ('PledgeName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#53
class c_RequestSetPledgeCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x53'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('IconCrest', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#55
class c_RequestGiveNickName():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x55'
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
#--------------------------------------------------------------------------#57
class c_RequestShowboard():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x57'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('flagShow', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#58
class c_RequestEnchantItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x58'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#59
class c_RequestDestroyItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x59'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Count', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5B
class c_SendBypassBuildCmd():
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
#--------------------------------------------------------------------------#5C
class c_RequestGetOnVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5D
class c_RequestGetOffVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5E
class c_RequestFriendInvite():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5E'
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
class c_RequestAnswerFriendInvite():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#60
class c_RequestFriendList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x60'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#61
class c_RequestFriendDel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x61'
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
#--------------------------------------------------------------------------#62
class c_CharacterRestore():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x62'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharSlot', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#63
class c_RequestQuestList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x63'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#64
class c_RequestQuestAbort():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x64'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('QuestID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#66
class c_RequestPledgeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x66'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ClanID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#67
class c_RequestPledgeExtendedInfo():
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
              , ('pledgeName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#68
class c_RequestPledgeCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x68'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CrestID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#69
class c_RequestSurrenderPersonally():
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
#--------------------------------------------------------------------------#6A
class c_RequestRide():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Rideflag', 'i4')
              , ('StrWyv', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6B
class c_RequestAcquireSkillInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
              , ('Level', 'i4')
              , ('Fisherman', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6C
class c_RequestAcquireSkill():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
              , ('Level', 'i4')
              , ('Fisherman', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6D
class c_RequestRestartPoint():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PointType', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6E
class c_RequestGMCommand():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6E'
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
#--------------------------------------------------------------------------#6F
class c_RequestPartyMatchConfig():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6F'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('AutomatRegistr', 'i4')
              , ('ShowLevel', 'i4')
              , ('ShowClass', 'i4')
              , ('memo', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#70
class c_RequestPartyMatchList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x70'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Status', 'i4')
              , ('un_0', 'i4')
              , ('un_1', 'i4')
              , ('un_2', 'i4')
              , ('un_3', 'i4')
              , ('un', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#71
class c_RequestPartyMatchDetail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x71'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('un', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#72
class c_RequestCrystallizeItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x72'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Count', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#73
class c_RequestPrivateStoreManage():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x73'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#74
class c_SetPrivateStoreListSell():
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
              , ('Package', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#75
class c_RequestPrivateStoreManageCancel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x75'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#76
class c_RequestPrivateStoreQuit():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x76'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#77
class c_SetPrivateStoreMsg():
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
#--------------------------------------------------------------------------#78
class c_RequestPrivateStoreList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x78'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#79
class c_SendPrivateStoreBuyList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x79'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('StorePlayerID', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('object', 'i4')
              , ('count', 'i4')
              , ('price', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#7A
class c_ReviveReply():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#7B
class c_RequestTutorialLinkHtml():
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
              , ('Link', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#7C
class c_RequestTutorialPassCmdToServer():
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
              , ('cmd', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#7D
class c_RequestTutorialQuestionMark():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#7E
class c_RequestTutorialClientEvent():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#7F
class c_RequestPetition():
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
#--------------------------------------------------------------------------#80
class c_RequestPetitionCancel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x80'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#81
class c_RequestGMList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x81'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#82
class c_RequestJoinAlly():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x82'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#83
class c_RequestAnswerJoinAlly():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x83'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#84
class c_RequestAllyLeave():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x84'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#85
class c_RequestAllyDismiss():
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
#--------------------------------------------------------------------------#86
class c_RequestDismissAlly():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x86'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#87
class c_RequestSetAllyCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x87'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('IconAllyCrest', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#88
class c_RequestAllyCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x88'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CrestID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#89
class c_RequestChangePetName():
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
#--------------------------------------------------------------------------#8A
class c_RequestPetUseItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#8B
class c_RequestGiveItemToPet():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Amount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#8C
class c_RequestGetItemFromPet():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Amount', 'i4')
              , ('un', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#8E
class c_RequestAllyInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#8F
class c_RequestPetGetItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#90
class c_RequestPrivateStoreManageBuy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x90'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#91
class c_SetPrivateStoreListBuy():
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
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('ItemID', 'i4')
              , ('h_0', 'i2')
              , ('h_1', 'i2')
              , ('Count', 'i4')
              , ('price', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#92
class c_RequestPrivateStoreBuyManageCancel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x92'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#93
class c_RequestPrivateStoreQuitBuy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x93'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#94
class c_SetPrivateStoreMsgBuy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x94'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('StoreMessage', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#95
class c_RequestPrivateStoreBuyList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x95'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#96
class c_SendPrivateStoreBuyList():
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
              , ('StorePlayerID', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('objectID', 'i4')
              , ('ItemID', 'i4')
              , ('h_0', 'i2')
              , ('h_1', 'i2')
              , ('count', 'i4')
              , ('price', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#97
class c_SendTimeCheckPacket():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x97'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#98
class c_RequestStartAllianceWar():
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
              , ('alName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#99
class c_ReplyStartAllianceWar():
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
              , ('alName', '|S'+str(self.It.__next__()) )
              , ('d', 'i4')
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
#--------------------------------------------------------------------------#9A
class c_RequestStopAllianceWar():
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
              , ('alName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#9B
class c_ReplyStopAllianceWar():
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
              , ('alName', '|S'+str(self.It.__next__()) )
              , ('d', 'i4')
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
#--------------------------------------------------------------------------#9C
class c_RequestSurrenderAllianceWar():
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
              , ('alName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#9D
class c_RequestSkillCoolTime():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#9E
class c_RequestPackageSendableItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#9F
class c_RequestPackageSend():
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
              , ('d', 'i4')
              , ('CountValue', 'i4')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('d_0', 'i4')
              , ('d_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#A0
class c_RequestBlock():
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
              , ('type', 'i4')
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
#--------------------------------------------------------------------------#A1
class c_RequestCastleSiegeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A2
class c_RequestSiegeAttackerList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A3
class c_RequestSiegeDefenderList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A4
class c_RequestJoinSiege():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
              , ('IsAttacker', 'i4')
              , ('IsJoining', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A5
class c_RequestConfirmSiegeWaitingList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
              , ('ClanID', 'i4')
              , ('Approved', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A6
class c_RequestSetCastleSiegeTime():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CastleIDU', 'i4')
              , ('timeU', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A7
class c_RequestMultiSellChoose():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ListID', 'i4')
              , ('EntryID', 'i4')
              , ('Amount', 'i4')
              , ('ench', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#A8
class c_NetPing():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('kID', 'i4')
              , ('PING', 'i4')
              , ('dta', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A9
class c_RequestRemainTime():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#AA
class c_BypassUserCmd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('cmd', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AB
class c_SnoopQuit():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('snoopID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AC
class c_RequestRecipeBookOpen():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('isntDwarvCraft', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AD
class c_RequestRecipeBookDestroy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('RecipeID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AE
class c_RequestRecipeItemMakeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('_id', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AF
class c_RequestRecipeItemMakeSelf():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('_id', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B0
class c_RequestRecipeShopManageList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#B1
class c_RequestRecipeShopMessageSet():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB1'
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
#--------------------------------------------------------------------------#B2
class c_RequestRecipeShopListSet():
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
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('RecipeID', 'i4')
              , ('Cost', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#B3
class c_RequestRecipeShopManageQuit():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#B4
class c_RequestRecipeShopManageCancel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#B5
class c_RequestRecipeShopMakeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PlayerObjectID', 'i4')
              , ('RecipeID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B6
class c_RequestRecipeShopMakeItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('_id', 'i4')
              , ('RecipeID', 'i4')
              , ('un', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B7
class c_RequestRecipeShopPrev():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B8
class c_ObserverReturn():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
              , ('ShiftFlag', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#B9
class c_RequestEvaluate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('targetID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#BA
class c_RequestHennaList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('un', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#BB
class c_RequestHennaItemInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SymbolID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#BC
class c_RequestHennaEquip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SymbolID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#BD
class c_RequestHennaUnequipList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('un', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#BE
class c_RequestHennaUnequipInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SymbolID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#BF
class c_RequestHennaUnequip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SymbolID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C0
class c_RequestPledgePower():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Rank', 'i4')
              , ('Action', 'i4')
              , ('Privs', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C1
class c_RequestMakeMacro():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC1'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('macroID', 'i4')
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
               ('entry', 'i1')
              , ('Type', 'i1')
              , ('d1', 'i4')
              , ('d2', 'i1')
              , ('Cmd', '|S'+str(self.It.__next__()) )
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
   if count > 100: raise Exception('PacketError')
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
      i += 4
      s_len = len(self.lst[i])
      yield s_len
      i += 1
#--------------------------------------------------------------------------#C2
class c_RequestDeleteMacro():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('macroID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C3
class c_RequestProcureCrop():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC3'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('_Id', 'i4')
              , ('class', 'i4')
              , ('num', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#C4
class c_RequestBuySeed():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC4'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('d_0', 'i4')
              , ('d_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#C5
class c_DlgAnswer():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('messageID', 'i4')
              , ('answer', 'i4')
              , ('un', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C6
class c_RequestWearItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC6'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('un', 'i4')
              , ('ListId', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('itemID', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#C7
class c_RequestSSQStatus():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Page', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#C8
class c_PetitionVote():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC8'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('s', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#CA
class c_GameGuardReply():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#CC
class c_RequestSendFriendMsg():
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
#--------------------------------------------------------------------------#CD
class c_RequestOpenMinimap():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#CE
class c_RequestSendMsnChatLog():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCE'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('msg', '|S'+str(self.It.__next__()) )
              , ('receiver', '|S'+str(self.It.__next__()) )
              , ('d', 'i4')
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
#--------------------------------------------------------------------------#CF
class c_RequestAutoSoulShot():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ItemID', 'i4')
              , ('FlagON', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#EE
class c_RequestChangePartyLeader():
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
#--------------------------------------------------------------------------#3900
class c_SuperCmdCharacterInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x39\x00\x00'
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
#--------------------------------------------------------------------------#3901
class c_SuperCmdSummonCmd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x39\x01\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('SummonName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#3902
class c_SuperCmdServerStatus():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x39\x02\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#3903
class c_SuperCmdL2ParamSetting():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x39\x03\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('p1', 'i4')
              , ('p2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D001
class c_RequestOustFromPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x01\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('_id', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D002
class c_RequestDismissPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x02\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('d1', 'i4')
              , ('d2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D003
class c_RequestWithdrawPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x03\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('d1', 'i4')
              , ('d2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D004
class c_RequestHandOverPartyMaster():
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
              , ('s', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D005
class c_RequestAutoSoulShot():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x05\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ItemID', 'i4')
              , ('FlagON', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D006
class c_RequestExEnchantSkillInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x06\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('skillID', 'i4')
              , ('skillLvl', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D007
class c_RequestExEnchantSkill():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x07\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('skillID', 'i4')
              , ('skillLvl', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D008
class c_RequestManorList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x08\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D009
class c_RequestProcureCropList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x09\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('City', 'i4')
              , ('ItemCount', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#D00A
class c_RequestSetSeed():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x0A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('data1', 'i4')
              , ('sizeValue', 'i4')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('l0', 'i4')
              , ('l1', 'i4')
              , ('l2', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#D00B
class c_RequestSetCrop():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x0B\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('data', 'i4')
              , ('sizeValue', 'i4')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('l0', 'i4')
              , ('l1', 'i4')
              , ('l2', 'i4')
              , ('l3', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#D00D
class c_RequestExAskJoinMPCC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x0D\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
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
#--------------------------------------------------------------------------#D00E
class c_RequestExAcceptJoinMPCC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x0E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D00F
class c_RequestExOustFromMPCC():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x0F\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
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
#--------------------------------------------------------------------------#D010
class c_RequestExPledgeCrestLarge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x10\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('crestID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D011
class c_RequestExSetPledgeCrestLarge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x11\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('IconCrestData', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#D012
class c_RequestOlympiadObserverEnd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x12\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D013
class c_RequestOlympiadMatchList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x13\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D014
class c_RequestAskJoinPartyRoom():
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
              , ('player', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D015
class c_AnswerJoinPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x15\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('requesterID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D016
class c_RequestListPartyMatchingWaitingRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x16\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D017
class c_RequestExitPartyMatchingWaitingRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x17\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D018
class c_RequestGetBossRecord():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x18\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('bossID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D019
class c_RequestPledgeSetAcademyMaster():
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
              , ('set', 'i4')
              , ('curPlayer', '|S'+str(self.It.__next__()) )
              , ('targetPlayer', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D01A
class c_RequestPledgePowerGradeList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x1A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D01B
class c_RequestPledgeMemberPowerInfo():
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
              , ('un1', 'i4')
              , ('player', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D01C
class c_RequestPledgeSetMemberPowerGrade():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x1C\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('member', '|S'+str(self.It.__next__()) )
              , ('powerGrade', 'i4')
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
#--------------------------------------------------------------------------#D01D
class c_RequestPledgeMemberInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x1D\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('un1', 'i4')
              , ('player', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D01E
class c_RequestPledgeWarList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x1E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('un1', 'i4')
              , ('tab', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D01F
class c_RequestExFishRanking():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x1F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D020
class c_RequestPCCafeCouponUse():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x20\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D022
class c_RequestCursedWeaponList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x22\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D023
class c_RequestCursedWeaponLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x23\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D024
class c_RequestPledgeReorganizeMember():
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
              , ('d_0', 'i4')
              , ('s_0', '|S'+str(self.It.__next__()) )
              , ('d_1', 'i4')
              , ('s_1', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#00
class s_KeyInit():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('01', 'i1')
              , ('Key', 'i8')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#01
class s_MoveToLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x01'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('ToX', 'i4')
              , ('ToY', 'i4')
              , ('ToZ', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#02
class s_NpcSay():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x02'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('npcID', 'i4')
              , ('ClassID', 'i4')
              , ('d', 'i4')
              , ('msg', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#03
class s_CharInfo():
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
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('ObjectID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Race', 'i4')
              , ('Sex', 'i4')
              , ('ClassID', 'i4')
              , ('DHair', 'i4')
              , ('Head', 'i4')
              , ('RHand', 'i4')
              , ('LHand', 'i4')
              , ('Gloves', 'i4')
              , ('Chest', 'i4')
              , ('Legs', 'i4')
              , ('Feet', 'i4')
              , ('Back', 'i4')
              , ('LRHand', 'i4')
              , ('Hair', 'i4')
              , ('PvpFlag_0', 'i4')
              , ('Karma_0', 'i4')
              , ('MSpeed', 'i4')
              , ('PSpeed', 'i4')
              , ('PvpFlag_1', 'i4')
              , ('Karma_1', 'i4')
              , ('runSpd', 'i4')
              , ('walkSpd', 'i4')
              , ('swimRSpd', 'i4')
              , ('swimWSpd', 'i4')
              , ('flRunSpd', 'i4')
              , ('flWalkSpd', 'i4')
              , ('flyRSpd', 'i4')
              , ('flyWSpd', 'i4')
              , ('SpdMul', 'f8')
              , ('ASpdMul', 'f8')
              , ('collisRadius', 'f8')
              , ('collisHeight', 'f8')
              , ('HairStyle', 'i4')
              , ('HairColor', 'i4')
              , ('Face', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('clanID', 'i4')
              , ('clanCrest', 'i4')
              , ('allyID', 'i4')
              , ('allyCrest', 'i4')
              , ('siegeFlag', 'i4')
              , ('isStand', 'i1')
              , ('isRun_0', 'i1')
              , ('isInFight', 'i1')
              , ('isAlikeDead', 'i1')
              , ('Invis', 'i1')
              , ('Mount', 'i1')
              , ('shop', 'i1')
              , ('cubicsValue', 'i2')
                  ]+ list(self.f_cubics()) +[
               ('findparty', 'i1')
              , ('abnEffects', 'i4')
              , ('RecomLeft', 'i1')
              , ('RecomHave', 'i2')
              , ('classID', 'i4')
              , ('maxCP', 'i4')
              , ('curCP', 'i4')
              , ('isMounted', 'i1')
              , ('Team', 'i1')
              , ('clanBigCrestId', 'i4')
              , ('isNoble', 'i1')
              , ('isHero', 'i1')
              , ('isFishing', 'i1')
              , ('fishX', 'i4')
              , ('fishY', 'i4')
              , ('fishZ', 'i4')
              , ('NameColor', 'i4')
              , ('isRun_1', 'i1')
              , ('d', 'i4')
              , ('PItem', 'i4')
              , ('PledgeClass', 'i4')
              , ('UPledgeColor', 'i4')
              , ('TitleColor', 'i4')
              , ('Cursed', 'i4')
                  ]
    return dtype
  def f_cubics(self):
    for i in range(self.It.__next__()):
      dtype = ('cubics_' + str(i) , [
               ('cubID', 'i2')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 20
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 156
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 27
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 36
   s_len = len(self.lst[i])
   yield s_len
   i += 13
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#04
class s_UserInfo():
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
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('ObjectID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Race', 'i4')
              , ('Sex', 'i4')
              , ('ClassID', 'i4')
              , ('Level', 'i4')
              , ('Exp', 'i4')
              , ('STR', 'i4')
              , ('DEX', 'i4')
              , ('CON', 'i4')
              , ('INT', 'i4')
              , ('WIT', 'i4')
              , ('MEN', 'i4')
              , ('MaxHP', 'i4')
              , ('CurHP', 'i4')
              , ('MaxMP', 'i4')
              , ('CurMP', 'i4')
              , ('SP', 'i4')
              , ('CurLoad', 'i4')
              , ('MaxLoad', 'i4')
              , ('d_0', 'i4')
              , ('DHair_0', 'i4')
              , ('Rear_0', 'i4')
              , ('Lear_0', 'i4')
              , ('Neck_0', 'i4')
              , ('RFinger_0', 'i4')
              , ('LFinger_0', 'i4')
              , ('Head_0', 'i4')
              , ('RHand_0', 'i4')
              , ('LHand_0', 'i4')
              , ('Gloves_0', 'i4')
              , ('Chest_0', 'i4')
              , ('Legs_0', 'i4')
              , ('Feet_0', 'i4')
              , ('Back_0', 'i4')
              , ('LRHand_0', 'i4')
              , ('Hair_0', 'i4')
              , ('DHair_1', 'i4')
              , ('Rear_1', 'i4')
              , ('Lear_1', 'i4')
              , ('Neck_1', 'i4')
              , ('RFinger_1', 'i4')
              , ('LFinger_1', 'i4')
              , ('Head_1', 'i4')
              , ('RHand_1', 'i4')
              , ('LHand_1', 'i4')
              , ('Gloves_1', 'i4')
              , ('Chest_1', 'i4')
              , ('Legs_1', 'i4')
              , ('Feet_1', 'i4')
              , ('Back_1', 'i4')
              , ('LRHand_1', 'i4')
              , ('Hair_1', 'i4')
              , ('Patk', 'i4')
              , ('Paspd_0', 'i4')
              , ('Pdef', 'i4')
              , ('evasion', 'i4')
              , ('accur', 'i4')
              , ('crithit', 'i4')
              , ('Matk', 'i4')
              , ('Maspd', 'i4')
              , ('Paspd_1', 'i4')
              , ('Mdef', 'i4')
              , ('PvpFlag', 'i4')
              , ('Karma', 'i4')
              , ('runSpd', 'i4')
              , ('walkSpd', 'i4')
              , ('swimRSpd', 'i4')
              , ('swimWSpd', 'i4')
              , ('flRSpd', 'i4')
              , ('flWSpd', 'i4')
              , ('flyRSpd', 'i4')
              , ('flyWSpd', 'i4')
              , ('MoveMul', 'f8')
              , ('aspdMul', 'f8')
              , ('collisRadius', 'f8')
              , ('collisHeight', 'f8')
              , ('HairStyle', 'i4')
              , ('HairColor', 'i4')
              , ('Face', 'i4')
              , ('AccessLvl', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('clanID', 'i4')
              , ('clanCrestId', 'i4')
              , ('AllyID', 'i4')
              , ('AllyCrestId', 'i4')
              , ('ClanLeader', 'i4')
              , ('Mount_0', 'i1')
              , ('shop', 'i1')
              , ('DwarfCraft', 'i1')
              , ('PKkills', 'i4')
              , ('PVPkills', 'i4')
              , ('cubicsValue', 'i2')
                  ]+ list(self.f_cubics()) +[
               ('findparty', 'i1')
              , ('abnEffects', 'i4')
              , ('c', 'i1')
              , ('clanPrivil', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
              , ('d_4', 'i4')
              , ('d_5', 'i4')
              , ('d_6', 'i4')
              , ('d_7', 'i4')
              , ('RecomLeft', 'i2')
              , ('RecomHave', 'i2')
              , ('d_8', 'i4')
              , ('InventLimit', 'i2')
              , ('classId', 'i4')
              , ('sEff', 'i4')
              , ('maxCP', 'i4')
              , ('curCP', 'i4')
              , ('Mount_1', 'i1')
              , ('Team', 'i1')
              , ('clanBigCrestId', 'i4')
              , ('Noble', 'i1')
              , ('Hero', 'i1')
              , ('Fishing', 'i1')
              , ('fishX', 'i4')
              , ('fishY', 'i4')
              , ('fishZ', 'i4')
              , ('NameColor', 'i4')
                  ]
    return dtype
  def f_cubics(self):
    for i in range(self.It.__next__()):
      dtype = ('cubics_' + str(i) , [
               ('cubID', 'i2')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 20
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 332
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 31
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 80
   s_len = len(self.lst[i])
   yield s_len
   i += 11
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#05
class s_Attack():
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
              , ('AttackerID', 'i4')
              , ('TargetID', 'i4')
              , ('Damage', 'i4')
              , ('Flags', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('ListHitsValue', 'i2')
                  ]+ list(self.f_ListHits()) +[
                  ]
    return dtype
  def f_ListHits(self):
    for i in range(self.It.__next__()):
      dtype = ('ListHits_' + str(i) , [
               ('targetId', 'i4')
              , ('damage', 'i4')
              , ('flags', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 25
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 7
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#06
class s_Die():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x06'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharID', 'i4')
              , ('d', 'i4')
              , ('HAsHideout', 'i4')
              , ('HasCastle', 'i4')
              , ('flags', 'i4')
              , ('sweepable', 'i4')
              , ('access', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#07
class s_Revive():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x07'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#08
class s_AttackOutOfRange():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x08'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#09
class s_AttackinCoolTime():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x09'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0A
class s_AttackDeadTarget():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#0B
class s_SpawnItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Stackable', 'i4')
              , ('Count', 'i4')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0C
class s_DropItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PlayerID', 'i4')
              , ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Stackable', 'i4')
              , ('Count', 'i4')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0D
class s_GetItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PlayerID', 'i4')
              , ('ObjectID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0E
class s_StatusUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0E'
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
               ('AttrID', 'i4')
              , ('AttrValue', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#0F
class s_NpcHtmlMessage():
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
              , ('MessageID', 'i4')
              , ('HTML', '|S'+str(self.It.__next__()) )
              , ('d', 'i4')
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
#--------------------------------------------------------------------------#10
class s_SellList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x10'
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
              , ('SellListValue', 'i2')
                  ]+ list(self.f_SellList()) +[
                  ]
    return dtype
  def f_SellList(self):
    for i in range(self.It.__next__()):
      dtype = ('SellList_' + str(i) , [
               ('ItemType1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Count', 'i4')
              , ('ItemType2', 'i2')
              , ('h_0', 'i2')
              , ('ItemBodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('h_1', 'i2')
              , ('h_2', 'i2')
              , ('refPrice', 'i4')
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
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#11
class s_BuyList():
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
              , ('Money', 'i4')
              , ('ListID', 'i4')
              , ('ListCountValue', 'i2')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('ItemType1', 'i2')
              , ('ObjectId', 'i4')
              , ('ItemID', 'i4')
              , ('maxcnt', 'i4')
              , ('ItemType2', 'i2')
              , ('h_0', 'i2')
              , ('ItemBodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('h_1', 'i2')
              , ('h_2', 'i2')
              , ('PriceToSell', 'i4')
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
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#12
class s_DeleteObject():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x12'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#13
class s_CharSelectInfo():
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
              , ('CountValue', 'i4')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('Name', '|S'+str(self.It.__next__()) )
              , ('CharID', 'i4')
              , ('LoginName', '|S'+str(self.It.__next__()) )
              , ('SessionID', 'i4')
              , ('ClanID', 'i4')
              , ('d_0', 'i4')
              , ('Sex', 'i4')
              , ('Race', 'i4')
              , ('ClassID_0', 'i4')
              , ('active', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('cur_HP', 'f8')
              , ('cur_MP', 'f8')
              , ('SP', 'i4')
              , ('Exp', 'i4')
              , ('Level', 'i4')
              , ('Karma', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
              , ('d_4', 'i4')
              , ('d_5', 'i4')
              , ('d_6', 'i4')
              , ('d_7', 'i4')
              , ('d_8', 'i4')
              , ('d_9', 'i4')
              , ('Under_0', 'i4')
              , ('Rear_0', 'i4')
              , ('Lear_0', 'i4')
              , ('Neck_0', 'i4')
              , ('RFinger_0', 'i4')
              , ('LFinger_0', 'i4')
              , ('Head_0', 'i4')
              , ('RHand_0', 'i4')
              , ('LHand_0', 'i4')
              , ('Gloves_0', 'i4')
              , ('Chest_0', 'i4')
              , ('Legs_0', 'i4')
              , ('Feet_0', 'i4')
              , ('Back_0', 'i4')
              , ('LRHand_0', 'i4')
              , ('Hair_0', 'i4')
              , ('Under_1', 'i4')
              , ('Rear_1', 'i4')
              , ('Lear_1', 'i4')
              , ('Neck_1', 'i4')
              , ('RFinger_1', 'i4')
              , ('LFinger_1', 'i4')
              , ('Head_1', 'i4')
              , ('RHand_1', 'i4')
              , ('LHand_1', 'i4')
              , ('Gloves_1', 'i4')
              , ('Chest_1', 'i4')
              , ('Legs_1', 'i4')
              , ('Feet_1', 'i4')
              , ('Back_1', 'i4')
              , ('LRHand_1', 'i4')
              , ('Hair_1', 'i4')
              , ('HairStyle', 'i4')
              , ('HairColor', 'i4')
              , ('Face', 'i4')
              , ('Max_HP', 'f8')
              , ('Max_MP', 'f8')
              , ('DELdays', 'i4')
              , ('ClassID_1', 'i4')
              , ('autSel', 'i4')
              , ('EnchEffect', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
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
      i += 277
  def parse_list(self):
   i = 1
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
      s_len = len(self.lst[i])
      yield s_len
      i += 67
#--------------------------------------------------------------------------#14
class s_LoginFail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x14'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('reason', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#15
class s_CharSelected():
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
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('CharID', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('SessionID', 'i4')
              , ('ClanID', 'i4')
              , ('d_0', 'i4')
              , ('Sex', 'i4')
              , ('Race', 'i4')
              , ('ClassID', 'i4')
              , ('active', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Cur_HP', 'f8')
              , ('Cur_MP', 'f8')
              , ('SP', 'i4')
              , ('EXP', 'i4')
              , ('Level', 'i4')
              , ('Karma', 'i4')
              , ('d_1', 'i4')
              , ('INT', 'i4')
              , ('STR', 'i4')
              , ('CON', 'i4')
              , ('MEN', 'i4')
              , ('DEX', 'i4')
              , ('WIT', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
              , ('d_4', 'i4')
              , ('d_5', 'i4')
              , ('d_6', 'i4')
              , ('d_7', 'i4')
              , ('d_8', 'i4')
              , ('d_9', 'i4')
              , ('d_10', 'i4')
              , ('d_11', 'i4')
              , ('d_12', 'i4')
              , ('d_13', 'i4')
              , ('d_14', 'i4')
              , ('d_15', 'i4')
              , ('d_16', 'i4')
              , ('d_17', 'i4')
              , ('d_18', 'i4')
              , ('d_19', 'i4')
              , ('d_20', 'i4')
              , ('d_21', 'i4')
              , ('d_22', 'i4')
              , ('d_23', 'i4')
              , ('d_24', 'i4')
              , ('d_25', 'i4')
              , ('d_26', 'i4')
              , ('d_27', 'i4')
              , ('d_28', 'i4')
              , ('d_29', 'i4')
              , ('d_30', 'i4')
              , ('d_31', 'i4')
              , ('d_32', 'i4')
              , ('d_33', 'i4')
              , ('inGameTime', 'i4')
              , ('d_34', 'i4')
              , ('d_35', 'i4')
              , ('d_36', 'i4')
              , ('d_37', 'i4')
              , ('d_38', 'i4')
              , ('d_39', 'i4')
              , ('d_40', 'i4')
              , ('d_41', 'i4')
              , ('d_42', 'i4')
              , ('d_43', 'i4')
              , ('d_44', 'i4')
              , ('d_45', 'i4')
              , ('d_46', 'i4')
              , ('d_47', 'i4')
              , ('d_48', 'i4')
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
#--------------------------------------------------------------------------#16
class s_NpcInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x16'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('NpcTypeId', 'i4')
              , ('IsAttackable', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('d_0', 'i4')
              , ('Maspd', 'i4')
              , ('Paspd_0', 'i4')
              , ('runSpd', 'i4')
              , ('walkSpd', 'i4')
              , ('swimRSpd', 'i4')
              , ('swimWSpd', 'i4')
              , ('flRSpd', 'i4')
              , ('flWSpd', 'i4')
              , ('FlyRSpd', 'i4')
              , ('FlyWSpd', 'i4')
              , ('ProperMul', 'f8')
              , ('Paspd_1', 'f8')
              , ('CollisRadius', 'f8')
              , ('CollisHeight', 'f8')
              , ('RHand', 'i4')
              , ('d_1', 'i4')
              , ('LHand', 'i4')
              , ('nameabove', 'i1')
              , ('isRun', 'i1')
              , ('isInFight', 'i1')
              , ('isAlikeDead', 'i1')
              , ('isSummoned', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('d_2', 'i4')
              , ('d_3', 'i4')
              , ('karmaU', 'i4')
              , ('abnEffect', 'i4')
              , ('d_4', 'i4')
              , ('d_5', 'i4')
              , ('d_6', 'i4')
              , ('d_7', 'i4')
              , ('c', 'i1')
              , ('Team', 'i1')
              , ('collisRadius', 'f8')
              , ('collisHeight', 'f8')
              , ('d_8', 'i4')
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
#--------------------------------------------------------------------------#17
class s_CharTemplates():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x17'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('Race', 'i4')
              , ('classID', 'i4')
              , ('d_0', 'i4')
              , ('base_STR', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('base_DEX', 'i4')
              , ('d_3', 'i4')
              , ('d_4', 'i4')
              , ('base_CON', 'i4')
              , ('d_5', 'i4')
              , ('d_6', 'i4')
              , ('base_INT', 'i4')
              , ('d_7', 'i4')
              , ('d_8', 'i4')
              , ('base_WIT', 'i4')
              , ('d_9', 'i4')
              , ('d_10', 'i4')
              , ('base_MEN', 'i4')
              , ('d_11', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#18
class s_NewCharFail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x18'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#19
class s_CharCreateSuccess():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x19'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ok', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1A
class s_CharCreateFail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('reason', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#1B
class s_ItemListPacket():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1B'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('window', 'i2')
              , ('ListCountValue', 'i2')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('itemType1', 'i2')
              , ('ObjectId', 'i4')
              , ('ItemID', 'i4')
              , ('count', 'i4')
              , ('itemType2', 'i2')
              , ('CustType1', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('CustType2', 'i2')
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
#--------------------------------------------------------------------------#1C
class s_SunRise():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#1D
class s_SunSet():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#1E
class s_TradeStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1E'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectId', 'i4')
              , ('ListCountValue', 'i2')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('itemType1', 'i2')
              , ('ObjectId', 'i4')
              , ('ItemId', 'i4')
              , ('Count', 'i4')
              , ('itemType2', 'i2')
              , ('h_0', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('h_1', 'i2')
              , ('h_2', 'i2')
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
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#1F
class s_TradeStartOk():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x1F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#20
class s_TradeOwnAdd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x20'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('itemType1', 'i2')
              , ('ObjectId', 'i4')
              , ('ItemId', 'i4')
              , ('Count', 'i4')
              , ('itemType2', 'i2')
              , ('h_0', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('h_1', 'i2')
              , ('h_2', 'i2')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#21
class s_TradeOtherAdd():
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
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('itemType1', 'i2')
              , ('ObjectId', 'i4')
              , ('ItemId', 'i4')
              , ('Count', 'i4')
              , ('itemType2', 'i2')
              , ('h_0', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('h_1', 'i2')
              , ('h_2', 'i2')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#22
class s_TradeDone():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x22'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('num', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#23
class s_CharDeleteSuccess():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x23'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#24
class s_CharDeleteFail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x24'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('reason', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#25
class s_ActionFail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x25'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#26
class s_SeverClose():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x26'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#27
class s_InventoryUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x27'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('1add2mod3remove', 'i2')
              , ('itemType1', 'i2')
              , ('ObjectId', 'i4')
              , ('ItemId', 'i4')
              , ('Count', 'i4')
              , ('itemType2', 'i2')
              , ('cusType1', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('cusType2', 'i2')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#28
class s_TeleportToLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x28'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('targetId', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#29
class s_TargetSelected():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x29'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('TargetID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2A
class s_TargetUnselected():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TargetID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2B
class s_AutoAttackStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TargetID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2C
class s_AutoAttackStop():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TargetID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2D
class s_SocialAction():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PlayerID', 'i4')
              , ('Action', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2E
class s_ChangeMoveType():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('charID', 'i4')
              , ('MoveType', 'i4')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2F
class s_ChangeWaitType():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('objectID', 'i4')
              , ('WaitType', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#30
class s_ManagePledgePower():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x30'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('privils', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#31
class s_CreatePledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x31'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#32
class s_AskJoinPledge():
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
              , ('requestorId', 'i4')
              , ('pledgeName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#33
class s_JoinPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x33'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('pledgeId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#34
class s_WithdrawalPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x34'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('pledgeId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#35
class s_OustPledgeMember():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x35'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#36
class s_SetOustPledgeMember():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x36'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#37
class s_DismissPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x37'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('pledgeId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#38
class s_SetDismissPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x38'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
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
              , ('requestorName', '|S'+str(self.It.__next__()) )
              , ('itemDistribution', 'i4')
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
              , ('response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#3B
class s_WithdrawalParty():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('partyID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#3C
class s_OustPartyMember():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#3D
class s_SetOustPartyMember():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#3E
class s_DismissParty():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('partyID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#3F
class s_SetDismissParty():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#40
class s_MagicAndSkillList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x40'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('CharID', 'i4')
              , ('d', 'i4')
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
              , ('WHtype', 'i2')
              , ('PlayerAdena', 'i4')
              , ('ListItemstValue', 'i2')
                  ]+ list(self.f_ListItemst()) +[
                  ]
    return dtype
  def f_ListItemst(self):
    for i in range(self.It.__next__()):
      dtype = ('ListItemst_' + str(i) , [
               ('itemType1', 'i2')
              , ('ObjectId_0', 'i4')
              , ('ItemId', 'i4')
              , ('Count', 'i4')
              , ('itemType2', 'i2')
              , ('h_0', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLvl', 'i2')
              , ('h_1', 'i2')
              , ('h_2', 'i2')
              , ('ObjectId_1', 'i4')
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
              , ('WHtype', 'i2')
              , ('PlayerAdena', 'i4')
              , ('ListItemstValue', 'i2')
                  ]+ list(self.f_ListItemst()) +[
                  ]
    return dtype
  def f_ListItemst(self):
    for i in range(self.It.__next__()):
      dtype = ('ListItemst_' + str(i) , [
               ('itemType1', 'i2')
              , ('ObjectId_0', 'i4')
              , ('ItemId', 'i4')
              , ('Count', 'i4')
              , ('itemType2', 'i2')
              , ('h_0', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLvl', 'i2')
              , ('h_1', 'i2')
              , ('h_2', 'i2')
              , ('ObjectId_1', 'i4')
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
#--------------------------------------------------------------------------#43
class s_WareHouseDone():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x43'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('whId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#44
class s_ShortCutRegister():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x44'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Type', 'i4')
              , ('Slot', 'i4')
              , ('_id', 'i4')
              , ('d_0', 'i4')
              , ('c', 'i1')
              , ('d_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#45
class s_ShortCutInit():
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
               ('c', 'i1')
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('type', 'i4')
              , ('slot', 'i4')
              , ('_id', 'i4')
              , ('lvl', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#46
class s_ShortCutDelete():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x46'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('shortcutId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#47
class s_StopMove():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x47'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectId', 'i4')
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
              , ('charID', 'i4')
              , ('targetID', 'i4')
              , ('skillID', 'i4')
              , ('skillLvl', 'i4')
              , ('hitTime', 'i4')
              , ('reuseDelay', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('count', 'i2')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#49
class s_MagicSkillCanceled():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x49'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('objectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#4A
class s_Say2():
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
              , ('textType', 'i4')
              , ('charName', '|S'+str(self.It.__next__()) )
              , ('Message', '|S'+str(self.It.__next__()) )
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
              , ('change', 'i4')
              , ('objectID', 'i4')
              , ('BodyPart', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#4C
class s_DoorInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('objectID', 'i4')
              , ('DoorID', 'i4')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#4D
class s_DoorStatusUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x4D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('objectID', 'i4')
              , ('Open', 'i4')
              , ('Damage', 'i4')
              , ('enemy', 'i4')
              , ('DoorID', 'i4')
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
              , ('objectID', 'i4')
              , ('Party', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('objID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('cur_CP', 'i4')
              , ('max_CP', 'i4')
              , ('cur_HP', 'i4')
              , ('max_HP', 'i4')
              , ('cur_MP', 'i4')
              , ('max_MP', 'i4')
              , ('lvl', 'i4')
              , ('classId', 'i4')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
   i += 4
   for _ in range(count):
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 40
  def parse_list(self):
   i = 1
   i += 2
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 11
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
              , ('playerObjId', 'i4')
              , ('d_0', 'i4')
              , ('memObjId', 'i4')
              , ('memName', '|S'+str(self.It.__next__()) )
              , ('cur_CP', 'i4')
              , ('max_CP', 'i4')
              , ('cur_HP', 'i4')
              , ('max_HP', 'i4')
              , ('cur_MP', 'i4')
              , ('max_MP', 'i4')
              , ('lvl', 'i4')
              , ('classId', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
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
              , ('memObjId', 'i4')
              , ('memberName', '|S'+str(self.It.__next__()) )
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
              , ('memObjId', 'i4')
              , ('memberName', '|S'+str(self.It.__next__()) )
              , ('cur_CP', 'i4')
              , ('max_CP', 'i4')
              , ('cur_HP', 'i4')
              , ('max_HP', 'i4')
              , ('cur_MP', 'i4')
              , ('max_MP', 'i4')
              , ('lvl', 'i4')
              , ('classId', 'i4')
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
#--------------------------------------------------------------------------#53
class s_PledgeShowMemberListAll():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x53'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('mainOrSubpledge', 'i4')
              , ('clanID', 'i4')
              , ('pledgeType', 'i4')
              , ('clanName', '|S'+str(self.It.__next__()) )
              , ('LeaderName', '|S'+str(self.It.__next__()) )
              , ('clanCrestId', 'i4')
              , ('clanLvl', 'i4')
              , ('hasCastle', 'i4')
              , ('hasHideOut', 'i4')
              , ('Rank', 'i4')
              , ('reputation', 'i4')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('AllyID', 'i4')
              , ('AllyName', '|S'+str(self.It.__next__()) )
              , ('AllyCrestId', 'i4')
              , ('isAtWar', 'i4')
              , ('memberCountValue', 'i4')
                  ]+ list(self.f_memberCount()) +[
                  ]
    return dtype
  def f_memberCount(self):
    for i in range(self.It.__next__()):
      dtype = ('memberCount_' + str(i) , [
               ('memberName', '|S'+str(self.It.__next__()) )
              , ('memLvl', 'i4')
              , ('memClassId', 'i4')
              , ('d_0', 'i4')
              , ('memObjId', 'i4')
              , ('isOnLine', 'i4')
              , ('d_1', 'i4')
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
   i += 36
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
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
   i += 10
   s_len = len(self.lst[i])
   yield s_len
   i += 3
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
      i += 7
#--------------------------------------------------------------------------#54
class s_PledgeShowMemberListUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x54'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('playerName', '|S'+str(self.It.__next__()) )
              , ('Lvl', 'i4')
              , ('ClassId', 'i4')
              , ('d', 'i4')
              , ('objectID', 'i4')
              , ('isOnLine', 'i4')
              , ('pledgeType', 'i4')
              , ('hasSponsor', 'i4')
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
#--------------------------------------------------------------------------#55
class s_PledgeShowMemberListAdd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x55'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Lvl', 'i4')
              , ('ClassId', 'i4')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('isOnLine', 'i4')
              , ('pledgeType', 'i4')
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
#--------------------------------------------------------------------------#56
class s_PledgeShowMemberListDelete():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x56'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('playerName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#57
class s_MagicList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x57'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#58
class s_SkillList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x58'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('isPassive', 'i4')
              , ('lvl', 'i4')
              , ('SkillID', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#59
class s_VehicleInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x59'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('boatObjId', 'i4')
              , ('BoatX', 'i4')
              , ('BoatY', 'i4')
              , ('BoatZ', 'i4')
              , ('BoatHeading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5A
class s_VehicleDeparture():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('boatObjId', 'i4')
              , ('spd1', 'i4')
              , ('spd2', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5B
class s_VehicleCheckLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('boatObjId', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('BoatHeading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5C
class s_GetOnVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectId', 'i4')
              , ('boatObjId', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5D
class s_GetOffVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectId', 'i4')
              , ('boatObjId', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5E
class s_TradeRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('senderID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5F
class s_RestartResponse():
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
              , ('ok', 'i4')
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
#--------------------------------------------------------------------------#60
class s_MoveToPawn():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x60'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('charID', 'i4')
              , ('targetId', 'i4')
              , ('distance', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#61
class s_ValidateLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x61'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('charID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#62
class s_StartRotating():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x62'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('charId', 'i4')
              , ('degree', 'i4')
              , ('side', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#63
class s_FinishRotating():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x63'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('objectId', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#64
class s_SystemMessage():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x64'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('MsgID', 'i4')
              , ('typesCount', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#65
class s_StartPledgeWar():
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
              , ('char', '|S'+str(self.It.__next__()) )
              , ('pledgename', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#66
class s_ReplyStartPledgeWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x66'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#67
class s_StopPledgeWar():
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
              , ('pledgename', '|S'+str(self.It.__next__()) )
              , ('char', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#68
class s_ReplyStopPledgeWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x68'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#69
class s_SurrenderPledgeWar():
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
              , ('pledgename', '|S'+str(self.It.__next__()) )
              , ('char', '|S'+str(self.It.__next__()) )
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
class s_ReplySurrenderPledgeWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6B
class s_SetPledgeCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#6C
class s_PledgeCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('crestID', 'i4')
              , ('IconCrest', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#6D
class s_SetupGauge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('dat1', 'i4')
              , ('time_0', 'i4')
              , ('time_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#6E
class s_ShowBoard():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6E'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('show', 'i1')
              , ('s1', '|S'+str(self.It.__next__()) )
              , ('s2', '|S'+str(self.It.__next__()) )
              , ('s3', '|S'+str(self.It.__next__()) )
              , ('s4', '|S'+str(self.It.__next__()) )
              , ('s5', '|S'+str(self.It.__next__()) )
              , ('s6', '|S'+str(self.It.__next__()) )
              , ('s7', '|S'+str(self.It.__next__()) )
              , ('s8', '|S'+str(self.It.__next__()) )
              , ('curpage', '|S'+str(self.It.__next__()) )
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
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#6F
class s_ChooseInventoryItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ItemId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#70
class s_Dummy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x70'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#71
class s_MoveToLocationInVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x71'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('pcID', 'i4')
              , ('boatID', 'i4')
              , ('ToX', 'i4')
              , ('ToY', 'i4')
              , ('ToZ', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#72
class s_StopMoveInVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x72'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('objId', 'i4')
              , ('boatId', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#73
class s_ValidateLocationInVehicle():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x73'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PlayerID', 'i4')
              , ('d', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#74
class s_TradeUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x74'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#75
class s_TradePressOwnOk():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x75'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#76
class s_MagicSkillLaunched():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x76'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('charID', 'i4')
              , ('skillID', 'i4')
              , ('skillLvl', 'i4')
              , ('failed', 'i4')
              , ('targetId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#77
class s_FriendAddRequestResult():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x77'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#78
class s_FriendAdd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x78'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#79
class s_FriendRemove():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x79'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#7A
class s_FriendList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7A'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#7B
class s_FriendStatus():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#7C
class s_TradePressOtherOk():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#7D
class s_FriendAddRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7D'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('requestorName', '|S'+str(self.It.__next__()) )
              , ('d', 'i4')
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
#--------------------------------------------------------------------------#7E
class s_LogOutOk():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#7F
class s_MagicEffectIcons():
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
              , ('ListCountValue', 'i2')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('skillID', 'i4')
              , ('Lvl', 'i2')
              , ('Duration', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#80
class s_QuestList():
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
              , ('CountValue', 'i2')
                  ]+ list(self.f_Count()) +[
               ('AllQCountValue', 'i2')
                  ]+ list(self.f_AllQCount()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('QuestId', 'i4')
              , ('cond', 'i4')
                  ])
      yield dtype 
  def f_AllQCount(self):
    for i in range(self.It.__next__()):
      dtype = ('AllQCount_' + str(i) , [
               ('drObId', 'i4')
              , ('drId', 'i4')
              , ('drItCn', 'i4')
              , ('d', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
   i += 2
   for _ in range(count):
      i += 8
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
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
      i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#81
class s_EnchantResult():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x81'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('result', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#82
class s_PledgeShowMemberListDeleteAll():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x82'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#83
class s_PledgeInfo():
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
              , ('clanId', 'i4')
              , ('clanName', '|S'+str(self.It.__next__()) )
              , ('allyName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#84
class s_PledgeExtendedInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x84'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#85
class s_SurrenderPersonally():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x85'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#86
class s_Ride():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x86'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('_id', 'i4')
              , ('bRide', 'i4')
              , ('rideType', 'i4')
              , ('rideClassId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#87
class s_Dummy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x87'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#88
class s_PledgeShowInfoUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x88'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('clanId', 'i4')
              , ('d_0', 'i4')
              , ('clanLvl', 'i4')
              , ('hasCastle', 'i4')
              , ('hasHideOut', 'i4')
              , ('d_1', 'i4')
              , ('reputation', 'i4')
              , ('d_2', 'i4')
              , ('D', 'i4')
              , ('d_3', 'i4')
              , ('bil', '|S'+str(self.It.__next__()) )
              , ('d_4', 'i4')
              , ('d_5', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 40
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 10
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#89
class s_ClientAction():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x89'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#8A
class s_AcquireSkillList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8A'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('orig', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('_id', 'i4')
              , ('nxtLvl', 'i4')
              , ('maxLvl', 'i4')
              , ('spCost', 'i4')
              , ('require', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#8B
class s_AcquireSkillInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8B'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('_id', 'i4')
              , ('level', 'i4')
              , ('spCost', 'i4')
              , ('Mode', 'i4')
              , ('CountValue', 'i4')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('type', 'i4')
              , ('itemId', 'i4')
              , ('count', 'i4')
              , ('d', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 16
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
#--------------------------------------------------------------------------#8C
class s_ServerObjectInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#8D
class s_GMHide():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('_id', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#8E
class s_AcquireSkillDone():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x8E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#8F
class s_GMViewCharacterInfo():
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
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('ObjId', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Race', 'i4')
              , ('Sex', 'i4')
              , ('ClassId_0', 'i4')
              , ('Lvl', 'i4')
              , ('Exp', 'i8')
              , ('STR', 'i4')
              , ('DEX', 'i4')
              , ('CON', 'i4')
              , ('INT', 'i4')
              , ('WIT', 'i4')
              , ('MEN', 'i4')
              , ('max_HP', 'i4')
              , ('cur_HP', 'i4')
              , ('max_MP', 'i4')
              , ('cur_MP', 'i4')
              , ('SP', 'i4')
              , ('cur_Load', 'i4')
              , ('max_Load', 'i4')
              , ('d_0', 'i4')
              , ('Under_0', 'i4')
              , ('Rear_0', 'i4')
              , ('Lear_0', 'i4')
              , ('Neck_0', 'i4')
              , ('RFinger_0', 'i4')
              , ('LFinger_0', 'i4')
              , ('Head_0', 'i4')
              , ('RHand_0', 'i4')
              , ('LHand_0', 'i4')
              , ('Gloves_0', 'i4')
              , ('Chest_0', 'i4')
              , ('Legs_0', 'i4')
              , ('Feet_0', 'i4')
              , ('Back_0', 'i4')
              , ('LRHand_0', 'i4')
              , ('Hair_0', 'i4')
              , ('Under_1', 'i4')
              , ('Rear_1', 'i4')
              , ('Lear_1', 'i4')
              , ('Neck_1', 'i4')
              , ('RFinger_1', 'i4')
              , ('LFinger_1', 'i4')
              , ('Head_1', 'i4')
              , ('RHand_1', 'i4')
              , ('LHand_1', 'i4')
              , ('Gloves_1', 'i4')
              , ('Chest_1', 'i4')
              , ('Legs_1', 'i4')
              , ('Feet_1', 'i4')
              , ('Back_1', 'i4')
              , ('LRHand_1', 'i4')
              , ('Hair_1', 'i4')
              , ('Patk', 'i4')
              , ('Paspd_0', 'i4')
              , ('PDef', 'i4')
              , ('Evasion', 'i4')
              , ('Accuracy', 'i4')
              , ('Crithit', 'i4')
              , ('Matk', 'i4')
              , ('Maspd', 'i4')
              , ('Paspd_1', 'i4')
              , ('MDef', 'i4')
              , ('PvpFlag', 'i4')
              , ('Karma', 'i4')
              , ('runSpd', 'i4')
              , ('walkSpd', 'i4')
              , ('swimRSpd', 'i4')
              , ('swimWSpd', 'i4')
              , ('flRSpd', 'i4')
              , ('flWSpd', 'i4')
              , ('flyRSpd', 'i4')
              , ('flyWSpd', 'i4')
              , ('moveMul', 'f8')
              , ('aspdMul', 'f8')
              , ('collisRadius', 'f8')
              , ('collisHeight', 'f8')
              , ('HairStyle', 'i4')
              , ('HairColor', 'i4')
              , ('Face', 'i4')
              , ('isGM', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('clanId', 'i4')
              , ('clanCrestId', 'i4')
              , ('allyId', 'i4')
              , ('Mount', 'i1')
              , ('store', 'i1')
              , ('DwarfCraft', 'i1')
              , ('PKkills', 'i4')
              , ('PVPkills', 'i4')
              , ('RecomLeft', 'i2')
              , ('RecomHave', 'i2')
              , ('ClassId_1', 'i4')
              , ('d_1', 'i4')
              , ('max_CP', 'i4')
              , ('cur_CP', 'i4')
              , ('isRun', 'i1')
              , ('FaceId', 'i4')
              , ('FaceIt', 'i4')
              , ('pledgeClass', 'i4')
              , ('d_2', 'i4')
              , ('NameColor', 'i4')
              , ('d_3', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 20
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 336
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 80
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#90
class s_GMViewPledgeInfo():
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
              , ('charName', '|S'+str(self.It.__next__()) )
              , ('clanId', 'i4')
              , ('clanName', '|S'+str(self.It.__next__()) )
              , ('LeaderName', '|S'+str(self.It.__next__()) )
              , ('CrestId', 'i4')
              , ('clanLvl', 'i4')
              , ('hasCastle', 'i4')
              , ('hasHideOut', 'i4')
              , ('d_0', 'i4')
              , ('charLvl', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('allyId', 'i4')
              , ('allyName', '|S'+str(self.It.__next__()) )
              , ('allyCrestId', 'i4')
              , ('isAtWar', 'i4')
              , ('membersCountValue', 'i4')
                  ]+ list(self.f_membersCount()) +[
                  ]
    return dtype
  def f_membersCount(self):
    for i in range(self.It.__next__()):
      dtype = ('membersCount_' + str(i) , [
               ('memberName', '|S'+str(self.It.__next__()) )
              , ('memLvl', 'i4')
              , ('memClassId', 'i4')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('isOnline', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 4
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 36
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
   i += 4
   for _ in range(count):
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 20
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 2
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 10
   s_len = len(self.lst[i])
   yield s_len
   i += 3
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
      i += 6
#--------------------------------------------------------------------------#91
class s_GMViewSkillInfo():
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
              , ('charName', '|S'+str(self.It.__next__()) )
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('isPassive', 'i4')
              , ('skillLVL', 'i4')
              , ('skillID', 'i4')
              , ('c', 'i1')
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#92
class s_GMViewMagicInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x92'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#93
class s_GMViewQuestInfo():
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
              , ('charName', '|S'+str(self.It.__next__()) )
              , ('questCountValue', 'i2')
                  ]+ list(self.f_questCount()) +[
               ('DropListValue', 'i2')
                  ]+ list(self.f_DropList()) +[
                  ]
    return dtype
  def f_questCount(self):
    for i in range(self.It.__next__()):
      dtype = ('questCount_' + str(i) , [
               ('questId', 'i4')
              , ('cond', 'i4')
                  ])
      yield dtype 
  def f_DropList(self):
    for i in range(self.It.__next__()):
      dtype = ('DropList_' + str(i) , [
               ('dropID', 'i4')
              , ('dropItemId', 'i4')
              , ('dropCount', 'i4')
              , ('d', 'i4')
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
   if count > 100: raise Exception('PacketError')
   yield count
   i += 2
   for _ in range(count):
      i += 8
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
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
      i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#94
class s_GMViewItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x94'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('playerName', '|S'+str(self.It.__next__()) )
              , ('InventLimit', 'i4')
              , ('window', 'i2')
              , ('ItemsCountValue', 'i2')
                  ]+ list(self.f_ItemsCount()) +[
                  ]
    return dtype
  def f_ItemsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemsCount_' + str(i) , [
               ('type1', 'i2')
              , ('ObjectId', 'i4')
              , ('ItemId', 'i4')
              , ('count', 'i4')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLvl', 'i2')
              , ('custType2', 'i2')
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 3
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#95
class s_GMViewWarehouseWithdrawList():
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
              , ('playerName', '|S'+str(self.It.__next__()) )
              , ('Money', 'i4')
              , ('itemCountValue', 'i2')
                  ]+ list(self.f_itemCount()) +[
                  ]
    return dtype
  def f_itemCount(self):
    for i in range(self.It.__next__()):
      dtype = ('itemCount_' + str(i) , [
               ('type1', 'i2')
              , ('ObjectId_0', 'i4')
              , ('ItemId', 'i4')
              , ('count', 'i4')
              , ('type2', 'i2')
              , ('h', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLvl', 'i2')
              , ('ssCount', 'i2')
              , ('spsCount', 'i2')
              , ('ObjectId_1', 'i4')
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   s_len = len(self.lst[i])
   yield s_len
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#96
class s_ListPartyWating():
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
              , ('plcountValue', 'i4')
                  ]+ list(self.f_plcount()) +[
                  ]
    return dtype
  def f_plcount(self):
    for i in range(self.It.__next__()):
      dtype = ('plcount_' + str(i) , [
               ('plObjectId', 'i4')
              , ('playerName', '|S'+str(self.It.__next__()) )
              , ('lvl', 'i4')
              , ('classId', 'i4')
              , ('d_0', 'i4')
              , ('clanId', 'i4')
              , ('d_1', 'i4')
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
   if count > 100: raise Exception('PacketError')
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 9
#--------------------------------------------------------------------------#97
class s_PartyRoomInfo():
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
              , ('plObjectId', 'i4')
              , ('showLvl', 'i4')
              , ('showClass', 'i4')
              , ('d', 'i4')
              , ('partyMemo', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#98
class s_PlaySound():
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
              , ('d_0', 'i4')
              , ('soundFile', '|S'+str(self.It.__next__()) )
              , ('ship', 'i4')
              , ('shipObjId', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('d_1', 'i4')
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
#--------------------------------------------------------------------------#99
class s_StaticObject():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x99'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('StaticObjectID', 'i4')
              , ('ObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#9A
class s_PrivateStoreManageList():
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
              , ('playerObjID', 'i4')
              , ('packSell', 'i4')
              , ('adena', 'i4')
              , ('ItemCountValue', 'i4')
                  ]+ list(self.f_ItemCount()) +[
               ('SellCountValue', 'i4')
                  ]+ list(self.f_SellCount()) +[
                  ]
    return dtype
  def f_ItemCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemCount_' + str(i) , [
               ('type2', 'i4')
              , ('objId', 'i4')
              , ('ItemId', 'i4')
              , ('count', 'i4')
              , ('h_0', 'i2')
              , ('Enchant', 'i2')
              , ('h_1', 'i2')
              , ('BodyPart', 'i4')
              , ('price', 'i4')
                  ])
      yield dtype 
  def f_SellCount(self):
    for i in range(self.It.__next__()):
      dtype = ('SellCount_' + str(i) , [
               ('type2', 'i4')
              , ('objId', 'i4')
              , ('ItemId', 'i4')
              , ('count', 'i4')
              , ('h_0', 'i2')
              , ('Enchant', 'i2')
              , ('h_1', 'i2')
              , ('BodyPart', 'i4')
              , ('price', 'i4')
              , ('storePrice', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
   i += 4
   for _ in range(count):
      i += 30
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 3
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
      i += 9
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#9B
class s_PrivateStoreList():
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
              , ('ObjectId', 'i4')
              , ('packSale', 'i4')
              , ('adena', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('type2', 'i4')
              , ('objId', 'i4')
              , ('ItemId', 'i4')
              , ('count', 'i4')
              , ('h_0', 'i2')
              , ('Enchant', 'i2')
              , ('h_1', 'i2')
              , ('BodyPart', 'i4')
              , ('price', 'i4')
              , ('storePrice', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 3
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#9C
class s_PrivateStoreMsg():
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
              , ('ObjectId', 'i4')
              , ('storeMsg', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#9D
class s_ShowMinimap():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('mapId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#9E
class s_ReviveRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#9F
class s_AbnormalVisualEffect():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x9F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#A0
class s_TutorialShowHtml():
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
#--------------------------------------------------------------------------#A1
class s_TutorialShowQuestionMark():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('blnk', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A2
class s_TutorialEnableClientEvent():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A3
class s_TutorialCloseHtml():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#A4
class s_ShowRadar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
              , ('d_4', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A5
class s_DeleteRadar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A6
class s_MyTargetSelected():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('objectID', 'i4')
              , ('color', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#A7
class s_PartyMemberPosition():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA7'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('membercountValue', 'i4')
                  ]+ list(self.f_membercount()) +[
                  ]
    return dtype
  def f_membercount(self):
    for i in range(self.It.__next__()):
      dtype = ('membercount_' + str(i) , [
               ('objID', 'i4')
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#A8
class s_AskJoinAlliance():
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
              , ('requestorID', 'i4')
              , ('requestorName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#A9
class s_JoinAlliance():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AA
class s_WithdrawAlliance():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AB
class s_OustAllianceMemberPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AC
class s_DismissAlliance():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#AD
class s_SetAllianceCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#AE
class s_AllianceCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CrestID', 'i4')
              , ('IconCrest', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#AF
class s_ServerCloseSocket():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#B0
class s_PetStatusShow():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('summonType', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B1
class s_PetInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB1'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('summonType', 'i4')
              , ('ObjectID', 'i4')
              , ('templ', 'i4')
              , ('d_0', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('d_1', 'i4')
              , ('Maspd_0', 'i4')
              , ('Paspd_0', 'i4')
              , ('runSpd_0', 'i4')
              , ('walkSpd', 'i4')
              , ('swimRSpd', 'i4')
              , ('swimWSpd', 'i4')
              , ('flRSpd', 'i4')
              , ('flWSpd', 'i4')
              , ('flyRSpd', 'i4')
              , ('flyWSpd', 'i4')
              , ('prMul', 'f8')
              , ('AspdMul', 'f8')
              , ('collisRadius', 'f8')
              , ('collisHeight', 'f8')
              , ('RHand', 'i4')
              , ('d_2', 'i4')
              , ('LHand', 'i4')
              , ('nameAbove', 'i1')
              , ('isRun', 'i1')
              , ('isInFight', 'i1')
              , ('isAlikeDead', 'i1')
              , ('isSummon', 'i1')
              , ('summonName', '|S'+str(self.It.__next__()) )
              , ('summonTitle', '|S'+str(self.It.__next__()) )
              , ('d_3', 'i4')
              , ('sumPVPflag', 'i4')
              , ('sumKarmaU', 'i4')
              , ('cur_Fed', 'i4')
              , ('max_Fed', 'i4')
              , ('cur_HP', 'i4')
              , ('max_HP', 'i4')
              , ('cur_MP', 'i4')
              , ('max_MP', 'i4')
              , ('SP', 'i4')
              , ('LVL', 'i4')
              , ('Exp', 'i8')
              , ('ExpThisLvl', 'i8')
              , ('ExpNextLvl', 'i8')
              , ('totalLoad', 'i4')
              , ('maxLoad', 'i4')
              , ('PAtk', 'i4')
              , ('PDef', 'i4')
              , ('MAtk', 'i4')
              , ('MDef', 'i4')
              , ('Accuracy', 'i4')
              , ('Evasion', 'i4')
              , ('Crit', 'i4')
              , ('runSpd_1', 'i4')
              , ('Paspd_1', 'i4')
              , ('Maspd_1', 'i4')
              , ('bleedPoisFlame', 'i4')
              , ('Ride', 'i2')
              , ('c', 'i1')
              , ('h', 'i2')
              , ('TeamAura', 'i1')
              , ('usedSS', 'i4')
              , ('usedSpS', 'i4')
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
#--------------------------------------------------------------------------#B2
class s_PetItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ItemCount', 'i2')
              , ('type1', 'i2')
              , ('objID', 'i4')
              , ('ItemID', 'i4')
              , ('count', 'i4')
              , ('type2', 'i2')
              , ('h_0', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('Enchant', 'i2')
              , ('h_1', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#B3
class s_PetInventoryUpdate():
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
              , ('ItemCountValue', 'i2')
                  ]+ list(self.f_ItemCount()) +[
                  ]
    return dtype
  def f_ItemCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemCount_' + str(i) , [
               ('change', 'i2')
              , ('type1', 'i2')
              , ('objID', 'i4')
              , ('ItemID', 'i4')
              , ('count', 'i4')
              , ('type2', 'i2')
              , ('h_0', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('Enchant', 'i2')
              , ('h_1', 'i2')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#B4
class s_AllianceInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#B5
class s_PetStatusUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB5'
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
              , ('cur_Fed', 'i4')
              , ('max_Fed', 'i4')
              , ('cur_HP', 'i4')
              , ('max_HP', 'i4')
              , ('cur_MP', 'i4')
              , ('max_MP', 'i4')
              , ('Level', 'i4')
              , ('Exp', 'i8')
              , ('ExpThisLvl', 'i8')
              , ('ExpNextLvl', 'i8')
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
#--------------------------------------------------------------------------#B6
class s_PetDelete():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PetID', 'i4')
              , ('PetNumber', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#B7
class s_PrivateStoreBuyManageList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB7'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Adena', 'i4')
              , ('ItemsCountValue', 'i4')
                  ]+ list(self.f_ItemsCount()) +[
               ('ByuCountValue', 'i4')
                  ]+ list(self.f_ByuCount()) +[
                  ]
    return dtype
  def f_ItemsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemsCount_' + str(i) , [
               ('ItemID', 'i4')
              , ('h_0', 'i2')
              , ('count', 'i4')
              , ('refPrice', 'i4')
              , ('h_1', 'i2')
              , ('BodyPart', 'i4')
              , ('type2', 'i2')
                  ])
      yield dtype 
  def f_ByuCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ByuCount_' + str(i) , [
               ('ItemID', 'i4')
              , ('h_0', 'i2')
              , ('count', 'i4')
              , ('refPrice_0', 'i4')
              , ('h_1', 'i2')
              , ('BodyPart', 'i4')
              , ('type2', 'i2')
              , ('yourPrice', 'i4')
              , ('refPrice_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
   i += 4
   for _ in range(count):
      i += 22
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
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
      i += 7
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#B8
class s_PrivateBuyListBuy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB8'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('adena', 'i4')
              , ('ItemsCountValue', 'i4')
                  ]+ list(self.f_ItemsCount()) +[
                  ]
    return dtype
  def f_ItemsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemsCount_' + str(i) , [
               ('objID', 'i4')
              , ('ItemID', 'i4')
              , ('Enchant', 'i2')
              , ('count_0', 'i4')
              , ('refPrice', 'i4')
              , ('h', 'i2')
              , ('BodyPart', 'i4')
              , ('type2', 'i2')
              , ('BuyersPrice', 'i4')
              , ('count_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#B9
class s_PrivateStoreMsgBuy():
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
              , ('ObjectID', 'i4')
              , ('storeMsg', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#BA
class s_VehicleStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#BB
class s_RequestTimeCheck():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#BC
class s_StartAllianceWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBC'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('s_0', '|S'+str(self.It.__next__()) )
              , ('s_1', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#BD
class s_ReplyStartAllianceWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#BE
class s_StopAllianceWar():
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
              , ('s_0', '|S'+str(self.It.__next__()) )
              , ('s_1', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#BF
class s_ReplyStopAllianceWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#C0
class s_SurrenderAllianceWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#C1
class s_SkillCoolTime():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C2
class s_PackageToList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC2'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('s', '|S'+str(self.It.__next__()) )
              , ('d_1', 'i4')
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
#--------------------------------------------------------------------------#C3
class s_PackageSendableList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('h', 'i2')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C4
class s_EarthQuake():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Intensivity', 'i4')
              , ('Duration', 'i4')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C5
class s_FlyToLoaction():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjID', 'i4')
              , ('ToX', 'i4')
              , ('ToY', 'i4')
              , ('ToZ', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C6
class s_BlockList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#C7
class s_SpecialCamera():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('_id', 'i4')
              , ('Distantion', 'i4')
              , ('Yaw', 'i4')
              , ('Pitch', 'i4')
              , ('Time', 'i4')
              , ('Duration', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C8
class s_NormalCamera():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#C9
class s_CastleSiegeInfo():
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
              , ('ActLeader', 'i4')
              , ('OwnerID', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('ClanLeader', '|S'+str(self.It.__next__()) )
              , ('allyID', 'i4')
              , ('allyName', '|S'+str(self.It.__next__()) )
              , ('time_ms', 'i4')
              , ('siege_time', 'i4')
              , ('num', 'i4')
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
class s_CastleSiegeAttackerList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCA'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('count_0', 'i4')
              , ('count_1', 'i4')
              , ('ClanID', 'i4')
              , ('clanName', '|S'+str(self.It.__next__()) )
              , ('leaderName', '|S'+str(self.It.__next__()) )
              , ('crestID', 'i4')
              , ('d_3', 'i4')
              , ('allyID', 'i4')
              , ('allyName', '|S'+str(self.It.__next__()) )
              , ('allyLeader', '|S'+str(self.It.__next__()) )
              , ('allyCrestID', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 28
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 12
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 7
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 4
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#CB
class s_CastleSiegeDefenderList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCB'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('count_0', 'i4')
              , ('count_1', 'i4')
              , ('ClanID_0', 'i4')
              , ('clanName_0', '|S'+str(self.It.__next__()) )
              , ('leaderName_0', '|S'+str(self.It.__next__()) )
              , ('crestID_0', 'i4')
              , ('signedTime_0', 'i4')
              , ('SiegeType_0', 'i4')
              , ('allyID_0', 'i4')
              , ('allyName_0', '|S'+str(self.It.__next__()) )
              , ('allyLeader_0', '|S'+str(self.It.__next__()) )
              , ('allyCrestID_0', 'i4')
              , ('ClanID_1', 'i4')
              , ('clanName_1', '|S'+str(self.It.__next__()) )
              , ('leaderName_1', '|S'+str(self.It.__next__()) )
              , ('crestID_1', 'i4')
              , ('signedTime_1', 'i4')
              , ('SiegeType_1', 'i4')
              , ('allyID_1', 'i4')
              , ('allyName_1', '|S'+str(self.It.__next__()) )
              , ('allyLeader_1', '|S'+str(self.It.__next__()) )
              , ('allyCrestID_1', 'i4')
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 28
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 16
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
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
   i += 16
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 7
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 3
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#CC
class s_NickNameChanged():
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
              , ('objID', 'i4')
              , ('NeedName', '|S'+str(self.It.__next__()) )
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
              , ('LeaderID', 'i4')
              , ('ClanID', 'i4')
              , ('d_0', 'i4')
              , ('clanLVL', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#CE
class s_RelationChanged():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCE'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('objId', 'i4')
              , ('relation', 'i4')
              , ('autoattackable', 'i4')
              , ('karma', 'i4')
              , ('pvpflag', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#CF
class s_EventTrigger():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('_id', 'i4')
              , ('On', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#D0
class s_MultiSellList_():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Script', '|SScript')
                  ]
    return dtype
#--------------------------------------------------------------------------#D1
class s_SetSummonRemainTime():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D2
class s_SkillRemainSec():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
              , ('d_4', 'i4')
              , ('d_5', 'i4')
              , ('d_6', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D3
class s_NetPing():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('kID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D4
class s_Dice():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PlayerID', 'i4')
              , ('ItemID', 'i4')
              , ('Number', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D5
class s_Snoop():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD5'
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
              , ('d', 'i4')
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
#--------------------------------------------------------------------------#D6
class s_RecipeBookItemList():
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
              , ('isDwarven', 'i4')
              , ('max_MP', 'i4')
              , ('recipesCountValue', 'i4')
                  ]+ list(self.f_recipesCount()) +[
                  ]
    return dtype
  def f_recipesCount(self):
    for i in range(self.It.__next__()):
      dtype = ('recipesCount_' + str(i) , [
               ('recipeId', 'i4')
              , ('recipeNum', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#D7
class s_RecipeItemMakeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('_id', 'i4')
              , ('IsDwarven', 'i4')
              , ('cur_MP', 'i4')
              , ('max_MP', 'i4')
              , ('Success', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D8
class s_RecipeShopManageList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD8'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Adena', 'i4')
              , ('IsDwarven', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
               ('ListcountValue', 'i4')
                  ]+ list(self.f_Listcount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('RecipeID', 'i4')
              , ('recipeNum', 'i4')
                  ])
      yield dtype 
  def f_Listcount(self):
    for i in range(self.It.__next__()):
      dtype = ('Listcount_' + str(i) , [
               ('RecipeID', 'i4')
              , ('d', 'i4')
              , ('Cost', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 12
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
   i += 4
   for _ in range(count):
      i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 3
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
      i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#D9
class s_RecipeShopSellList():
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
              , ('ObjectID', 'i4')
              , ('cur_MP', 'i4')
              , ('max_MP', 'i4')
              , ('Adena', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('RecipeID', 'i4')
              , ('d', 'i4')
              , ('Cost', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 16
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
#--------------------------------------------------------------------------#DA
class s_RecipeShopItemInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ShopID', 'i4')
              , ('RecipeID', 'i4')
              , ('cur_MP', 'i4')
              , ('max_MP', 'i4')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#DB
class s_RecipeShopMsg():
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
#--------------------------------------------------------------------------#DC
class s_ShowCalculator():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CalculatorID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#DD
class s_MonRaceInfo():
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
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('CountValue', 'i4')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
               ('monsterObjID', 'i4')
              , ('npcId', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
              , ('ToX', 'i4')
              , ('ToY', 'i4')
              , ('ToZ', 'i4')
              , ('collisHeight', 'f8')
              , ('collisRadius', 'f8')
              , ('d_0', 'i4')
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
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
              , ('d_4', 'i4')
              , ('d_5', 'i4')
              , ('d_6', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#DE
class s_ShowTownMap():
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
              , ('texture', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#DF
class s_ObservationMode():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('c_0', 'i1')
              , ('c_1', 'i1')
              , ('c_2', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#E0
class s_ObservationReturn():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#E1
class s_ChairSit():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ActiveObjectID', 'i4')
              , ('StaticObjectID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#E2
class s_HennaEquipList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE2'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('PlayerAdena', 'i4')
              , ('Slots', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('SymbolID', 'i4')
              , ('ItemDyeID', 'i4')
              , ('dyeRequire', 'i4')
              , ('adenaRequire', 'i4')
              , ('d', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#E3
class s_HennaItemInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SymbolID', 'i4')
              , ('ItemID', 'i4')
              , ('DyeRequire', 'i4')
              , ('Price', 'i4')
              , ('Draw', 'i4')
              , ('Adena', 'i4')
              , ('cur_INT', 'i4')
              , ('equip_INT', 'i1')
              , ('cur_STR', 'i4')
              , ('equip_STR', 'i1')
              , ('cur_CON', 'i4')
              , ('equip_CON', 'i1')
              , ('cur_MEN', 'i4')
              , ('equip_MEN', 'i1')
              , ('cur_DEX', 'i4')
              , ('equip_DEX', 'i1')
              , ('cur_WIT', 'i4')
              , ('equip_WIT', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#E4
class s_HennaInfo():
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
              , ('INT', 'i1')
              , ('STR', 'i1')
              , ('CON', 'i1')
              , ('MEN', 'i1')
              , ('DEX', 'i1')
              , ('WIT', 'i1')
              , ('SlotCountValue', 'i4')
                  ]+ list(self.f_SlotCount()) +[
                  ]
    return dtype
  def f_SlotCount(self):
    for i in range(self.It.__next__()):
      dtype = ('SlotCount_' + str(i) , [
               ('slot', 'i4')
              , ('SymbolID', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 6
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#E5
class s_HennaUnequipList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#E6
class s_HennaUnequipInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#E7
class s_SendMacroList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE7'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('Revision', 'i4')
              , ('c_0', 'i1')
              , ('Count', 'i1')
              , ('c_1', 'i1')
              , ('MacroID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Descr', '|S'+str(self.It.__next__()) )
              , ('Acronym', '|S'+str(self.It.__next__()) )
              , ('Icon', 'i1')
              , ('LenghtValue', 'i1')
                  ]+ list(self.f_Lenght()) +[
                  ]
    return dtype
  def f_Lenght(self):
    for i in range(self.It.__next__()):
      dtype = ('Lenght_' + str(i) , [
               ('idx', 'i1')
              , ('type', 'i1')
              , ('SkillID', 'i4')
              , ('ShortcutID', 'i1')
              , ('cmdName', '|S'+str(self.It.__next__()) )
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 11
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
   if count > 100: raise Exception('PacketError')
   yield count
   i += 1
   for _ in range(count):
      i += 7
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
  def parse_list(self):
   i = 1
   i += 5
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
      i += 4
      s_len = len(self.lst[i])
      yield s_len
      i += 1
#--------------------------------------------------------------------------#E8
class s_BuyListSeed():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('money', 'i4')
              , ('ListID', 'i4')
              , ('ListCount', 'i2')
              , ('itemType1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Count', 'i4')
              , ('itemType2', 'i2')
              , ('h', 'i2')
              , ('price', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#E9
class s_SellListProcure():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('money', 'i4')
              , ('d', 'i4')
              , ('ListCount', 'i2')
              , ('itemType1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Count', 'i4')
              , ('itemType2', 'i2')
              , ('h', 'i2')
              , ('price', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#EA
class s_GMHennaInfo():
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
              , ('INT', 'i1')
              , ('STR', 'i1')
              , ('CON', 'i1')
              , ('MEN', 'i1')
              , ('DEX', 'i1')
              , ('WIT', 'i1')
              , ('SlotCountValue', 'i4')
                  ]+ list(self.f_SlotCount()) +[
                  ]
    return dtype
  def f_SlotCount(self):
    for i in range(self.It.__next__()):
      dtype = ('SlotCount_' + str(i) , [
               ('slot', 'i4')
              , ('SymbolID', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 6
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#EB
class s_RadarControl():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ShowRadar', 'i4')
              , ('Type', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#EC
class s_ClientSetTime():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xEC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#ED
class s_ConfirmDlg():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xED'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('requestID', 'i4')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('d_2', 'i4')
              , ('d_3', 'i4')
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
#--------------------------------------------------------------------------#EE
class s_PartySpelled():
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
              , ('Summon', 'i4')
              , ('ObjecID', 'i4')
              , ('EffectCountValue', 'i4')
                  ]+ list(self.f_EffectCount()) +[
                  ]
    return dtype
  def f_EffectCount(self):
    for i in range(self.It.__next__()):
      dtype = ('EffectCount_' + str(i) , [
               ('SkillID', 'i4')
              , ('Data', 'i2')
              , ('Duration', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 8
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#EF
class s_ShopPreviewList():
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
              , ('c_0', 'i1')
              , ('c_1', 'i1')
              , ('c_2', 'i1')
              , ('c_3', 'i1')
              , ('money', 'i4')
              , ('ListID', 'i4')
              , ('ListCountValue', 'i2')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('ItemId', 'i4')
              , ('type2', 'i2')
              , ('BodyPart', 'i2')
              , ('wearPrice', 'i4')
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
#--------------------------------------------------------------------------#F0
class s_ShopPreviewInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#F1
class s_CameraMode():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Mode', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F2
class s_ShowXMasSeal():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F3
class s_EtcStatusUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF3'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
              , ('d_4', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F4
class s_ShortBuffStatusUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F5
class s_SSQStatus_():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF5'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Script', '|SScript')
                  ]
    return dtype
#--------------------------------------------------------------------------#F6
class s_PetitionVote():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#F7
class s_AgitDecoInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F8
class s_SSQInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Sky', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#F9
class s_GameGuardQuery():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FA
class s_FriendList():
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
              , ('FriendCountValue', 'i4')
                  ]+ list(self.f_FriendCount()) +[
                  ]
    return dtype
  def f_FriendCount(self):
    for i in range(self.It.__next__()):
      dtype = ('FriendCount_' + str(i) , [
               ('friendID', 'i4')
              , ('friendName', '|S'+str(self.It.__next__()) )
              , ('isOnLine', 'i4')
              , ('ObjecID', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 3
#--------------------------------------------------------------------------#FB
class s_Friend():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFB'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FC
class s_FriendStatus():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFC'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FD
class s_FriendSay():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFD'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('d', 'i4')
              , ('sender', '|S'+str(self.It.__next__()) )
              , ('receiver', '|S'+str(self.It.__next__()) )
              , ('message', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#FE12
class s_ExAutoSoulShot():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x12\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('itemID', 'i4')
              , ('type', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE13
class s_ExFishingStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x13\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('charObjID', 'i4')
              , ('fishType', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('isNightLure', 'i1')
              , ('c', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE14
class s_ExFishingEnd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x14\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('charObjectId', 'i4')
              , ('isWin', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE15
class s_ExFishingStartCombat():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x15\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('charObjID', 'i4')
              , ('time', 'i4')
              , ('HP', 'i4')
              , ('Fighting', 'i1')
              , ('LureType', 'i1')
              , ('isFishDeceptive', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE16
class s_ExFishingHpRegen():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x16\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('charObjID', 'i4')
              , ('time', 'i4')
              , ('fish_HP', 'i4')
              , ('HPstoprise', 'i1')
              , ('GoodUse', 'i1')
              , ('anim', 'i1')
              , ('penalty', 'i4')
              , ('BarColor', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE17
class s_ExEnchantSkillList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x17\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('id', 'i4')
              , ('nextLevel', 'i4')
              , ('SP', 'i4')
              , ('Exp', 'i8')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FE18
class s_ExEnchantSkillInfo():
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
              , ('_id', 'i4')
              , ('lvl', 'i4')
              , ('SPcost', 'i4')
              , ('XPcost', 'i8')
              , ('rate', 'i4')
              , ('reqsCountValue', 'i4')
                  ]+ list(self.f_reqsCount()) +[
                  ]
    return dtype
  def f_reqsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('reqsCount_' + str(i) , [
               ('type', 'i4')
              , ('id', 'i4')
              , ('count', 'i4')
              , ('d', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 26
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 6
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FE19
class s_ExQuestInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x19\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE1B
class s_ExSendManorList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x1B\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('idx', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 1
#--------------------------------------------------------------------------#FE21
class s_ManorList1():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x21\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('d', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('ObjectID', 'i4')
              , ('itemID', 'i4')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('c_0', 'i1')
              , ('c_1', 'i1')
              , ('d_2', 'i4')
              , ('Reward', 'i4')
              , ('BuyCount', 'i4')
              , ('BuyPrice', 'i4')
              , ('c_2', 'i1')
              , ('ItemCount', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FE22
class s_ManorList2():
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
              , ('ItemID', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('City', 'i4')
              , ('Count', 'i4')
              , ('Price', 'i4')
              , ('c', 'i1')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 6
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FE23
class s_ExHeroList():
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
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('heroName', '|S'+str(self.It.__next__()) )
              , ('ClassId', 'i4')
              , ('clanName', '|S'+str(self.It.__next__()) )
              , ('clanCrest', 'i4')
              , ('allyName', '|S'+str(self.It.__next__()) )
              , ('allyCrest', 'i4')
              , ('count', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
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
      s_len = len(self.lst[i])
      yield s_len
      i += 2
      s_len = len(self.lst[i])
      yield s_len
      i += 3
#--------------------------------------------------------------------------#FE28
class s_ExPledgeCrestLarge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x28\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('d', 'i4')
              , ('crestID', 'i4')
              , ('IconCrest', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE29
class s_ExOlympiadUserInfo():
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
              , ('Side', 'i1')
              , ('charObjID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('ClassId', 'i4')
              , ('cur_HP', 'i4')
              , ('max_HP', 'i4')
              , ('cur_CP', 'i4')
              , ('max_CP', 'i4')
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
#--------------------------------------------------------------------------#FE2A
class s_ExOlympiadSpelledInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x2A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('charObjID', 'i4')
              , ('Count', 'i4')
              , ('skillID', 'i4')
              , ('dat', 'i2')
              , ('duration', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE2B
class s_ExOlympiadMode():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x2B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('mode', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE2D
class s_ExMailArrived():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x2D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE2E
class s_ExStorageMaxCount():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x2E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('inventory', 'i4')
              , ('warehouse', 'i4')
              , ('freight', 'i4')
              , ('privateSell', 'i4')
              , ('privateBuy', 'i4')
              , ('receipeD', 'i4')
              , ('recipe', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE31
class s_ExPCCafePointInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x31\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('c_0', 'i1')
              , ('d_2', 'i4')
              , ('c_1', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE32
class s_ExSetCompassZoneCode():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x32\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('d', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE33
class s_ExGetBossRecord():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x33\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('ListSize', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE34
class s_ExAskJoinPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x34\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('charName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#FE37
class s_ExShowAdventurerGuideBook():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x37\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE39
class s_PledgeSkillList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x39\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('SkillID', 'i4')
              , ('Level', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FE3A
class s_PledgeSkillListAdd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x3A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('SkillID', 'i4')
              , ('Level', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE3B
class s_PledgePowerGradeList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x3B\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListcountValue', 'i4')
                  ]+ list(self.f_Listcount()) +[
                  ]
    return dtype
  def f_Listcount(self):
    for i in range(self.It.__next__()):
      dtype = ('Listcount_' + str(i) , [
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FE3C
class s_PledgeReceivePowerInfo():
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
              , ('membPowerGrade', 'i4')
              , ('memberName', '|S'+str(self.It.__next__()) )
              , ('privileges', 'i4')
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
#--------------------------------------------------------------------------#FE3D
class s_PledgeReceiveMemberInfo():
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
              , ('memberPledge', 'i4')
              , ('memName', '|S'+str(self.It.__next__()) )
              , ('memTitle', '|S'+str(self.It.__next__()) )
              , ('memPowerGrade', 'i4')
              , ('clanName', '|S'+str(self.It.__next__()) )
              , ('Apprent', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#FE3E
class s_PledgeReceiveWarList():
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
              , ('Enemyattaker', 'i4')
              , ('page', 'i4')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('clanName', '|S'+str(self.It.__next__()) )
              , ('d_0', 'i4')
              , ('d_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 10
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
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
      i += 3
#--------------------------------------------------------------------------#FE3F
class s_PledgeReceiveSubPledgeCreated():
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
              , ('d', 'i4')
              , ('subPledgeID', 'i4')
              , ('subPledgeName', '|S'+str(self.It.__next__()) )
              , ('leaderName', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#FE40
class s_ExRedSky():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x40\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('duration', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE43
class s_ShowPCCafeCouponShowUI():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x43\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE44
class s_ExOrcMove():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x44\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE45
class s_ExCursedWeaponList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x45\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('cursWeapID', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FE46
class s_ExCursedWeaponLocation():
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
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('cursWeapID', 'i4')
              , ('d', 'i4')
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FE47
class s_ExRestartClient():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x47\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
class Pck_invoke_dict():
 def __init__(self):
   self.Pck_invoke_s = {}
   self.Pck_invoke_c = {}
 def get_Pck_invoke_c(self):
   self.Pck_invoke_s[c_ProtocolVersion().invoke] = c_ProtocolVersion()
   self.Pck_invoke_s[c_MoveBackwardToLocation().invoke] = c_MoveBackwardToLocation()
   self.Pck_invoke_s[c_Say().invoke] = c_Say()
   self.Pck_invoke_s[c_EnterWorld().invoke] = c_EnterWorld()
   self.Pck_invoke_s[c_Action().invoke] = c_Action()
   self.Pck_invoke_s[c_RequestAuthLogin().invoke] = c_RequestAuthLogin()
   self.Pck_invoke_s[c_LogoutRequest().invoke] = c_LogoutRequest()
   self.Pck_invoke_s[c_Attack().invoke] = c_Attack()
   self.Pck_invoke_s[c_CharCreate().invoke] = c_CharCreate()
   self.Pck_invoke_s[c_CharDelete().invoke] = c_CharDelete()
   self.Pck_invoke_s[c_CharSelected().invoke] = c_CharSelected()
   self.Pck_invoke_s[c_NewCharacter().invoke] = c_NewCharacter()
   self.Pck_invoke_s[c_RequestItemList().invoke] = c_RequestItemList()
   self.Pck_invoke_s[c_RequestEquipItem().invoke] = c_RequestEquipItem()
   self.Pck_invoke_s[c_RequestUnEquipItem().invoke] = c_RequestUnEquipItem()
   self.Pck_invoke_s[c_RequestDropItem().invoke] = c_RequestDropItem()
   self.Pck_invoke_s[c_UseItem().invoke] = c_UseItem()
   self.Pck_invoke_s[c_TradeRequest().invoke] = c_TradeRequest()
   self.Pck_invoke_s[c_AddTradeItem().invoke] = c_AddTradeItem()
   self.Pck_invoke_s[c_TradeDone().invoke] = c_TradeDone()
   self.Pck_invoke_s[c_RequestTeleport().invoke] = c_RequestTeleport()
   self.Pck_invoke_s[c_RequestSocialAction().invoke] = c_RequestSocialAction()
   self.Pck_invoke_s[c_ChangeMoveType().invoke] = c_ChangeMoveType()
   self.Pck_invoke_s[c_ChangeWaitType().invoke] = c_ChangeWaitType()
   self.Pck_invoke_s[c_RequestSellItem().invoke] = c_RequestSellItem()
   self.Pck_invoke_s[c_RequestBuyItem().invoke] = c_RequestBuyItem()
   self.Pck_invoke_s[c_RequestLinkHtml().invoke] = c_RequestLinkHtml()
   self.Pck_invoke_s[c_RequestBypassToServer().invoke] = c_RequestBypassToServer()
   self.Pck_invoke_s[c_RequestBBSwrite().invoke] = c_RequestBBSwrite()
   self.Pck_invoke_s[c_RequestCreatePledge().invoke] = c_RequestCreatePledge()
   self.Pck_invoke_s[c_RequestJoinPledge().invoke] = c_RequestJoinPledge()
   self.Pck_invoke_s[c_RequestAnswerJoinPledge().invoke] = c_RequestAnswerJoinPledge()
   self.Pck_invoke_s[c_RequestWithDrawalPledge().invoke] = c_RequestWithDrawalPledge()
   self.Pck_invoke_s[c_RequestOustPledgeMember().invoke] = c_RequestOustPledgeMember()
   self.Pck_invoke_s[c_RequestDismissPledge().invoke] = c_RequestDismissPledge()
   self.Pck_invoke_s[c_RequestJoinParty().invoke] = c_RequestJoinParty()
   self.Pck_invoke_s[c_RequestAnswerJoinParty().invoke] = c_RequestAnswerJoinParty()
   self.Pck_invoke_s[c_RequestWithDrawalParty().invoke] = c_RequestWithDrawalParty()
   self.Pck_invoke_s[c_RequestOustPartyMember().invoke] = c_RequestOustPartyMember()
   self.Pck_invoke_s[c_RequestDismissParty().invoke] = c_RequestDismissParty()
   self.Pck_invoke_s[c_RequestMagicSkillList().invoke] = c_RequestMagicSkillList()
   self.Pck_invoke_s[c_RequestMagicSkillUse().invoke] = c_RequestMagicSkillUse()
   self.Pck_invoke_s[c_Appearing().invoke] = c_Appearing()
   self.Pck_invoke_s[c_SendWareHouseDepositList().invoke] = c_SendWareHouseDepositList()
   self.Pck_invoke_s[c_SendWareHouseWithDrawList().invoke] = c_SendWareHouseWithDrawList()
   self.Pck_invoke_s[c_RequestShortCutReg().invoke] = c_RequestShortCutReg()
   self.Pck_invoke_s[c_RequestShortCutUse().invoke] = c_RequestShortCutUse()
   self.Pck_invoke_s[c_RequestShortCutDel().invoke] = c_RequestShortCutDel()
   self.Pck_invoke_s[c_CannotMoveAnymore().invoke] = c_CannotMoveAnymore()
   self.Pck_invoke_s[c_RequestTargetCancel().invoke] = c_RequestTargetCancel()
   self.Pck_invoke_s[c_Say2().invoke] = c_Say2()
   self.Pck_invoke_s[c_RequestPledgeMemberList().invoke] = c_RequestPledgeMemberList()
   self.Pck_invoke_s[c_RequestMagicList().invoke] = c_RequestMagicList()
   self.Pck_invoke_s[c_RequestSkillList().invoke] = c_RequestSkillList()
   self.Pck_invoke_s[c_AnswerTradeRequest().invoke] = c_AnswerTradeRequest()
   self.Pck_invoke_s[c_MoveWithDelta().invoke] = c_MoveWithDelta()
   self.Pck_invoke_s[c_GetOnVehicle().invoke] = c_GetOnVehicle()
   self.Pck_invoke_s[c_GetOffVehicle().invoke] = c_GetOffVehicle()
   self.Pck_invoke_s[c_AnswerTradeRequest().invoke] = c_AnswerTradeRequest()
   self.Pck_invoke_s[c_RequestActionUse().invoke] = c_RequestActionUse()
   self.Pck_invoke_s[c_RequestRestart().invoke] = c_RequestRestart()
   self.Pck_invoke_s[c_RequestSiegeInfo().invoke] = c_RequestSiegeInfo()
   self.Pck_invoke_s[c_ValidatePosition().invoke] = c_ValidatePosition()
   self.Pck_invoke_s[c_RequestSEKCustom().invoke] = c_RequestSEKCustom()
   self.Pck_invoke_s[c_StartRotating().invoke] = c_StartRotating()
   self.Pck_invoke_s[c_FinishRotating().invoke] = c_FinishRotating()
   self.Pck_invoke_s[c_RequestStartPledgeWar().invoke] = c_RequestStartPledgeWar()
   self.Pck_invoke_s[c_RequestReplyStartPledgeWar().invoke] = c_RequestReplyStartPledgeWar()
   self.Pck_invoke_s[c_RequestStopPledgeWar().invoke] = c_RequestStopPledgeWar()
   self.Pck_invoke_s[c_RequestReplyStopPledgeWar().invoke] = c_RequestReplyStopPledgeWar()
   self.Pck_invoke_s[c_RequestSurrenderPledgeWar().invoke] = c_RequestSurrenderPledgeWar()
   self.Pck_invoke_s[c_RequestReplySurrenderPledgeWar().invoke] = c_RequestReplySurrenderPledgeWar()
   self.Pck_invoke_s[c_RequestSetPledgeCrest().invoke] = c_RequestSetPledgeCrest()
   self.Pck_invoke_s[c_RequestGiveNickName().invoke] = c_RequestGiveNickName()
   self.Pck_invoke_s[c_RequestShowboard().invoke] = c_RequestShowboard()
   self.Pck_invoke_s[c_RequestEnchantItem().invoke] = c_RequestEnchantItem()
   self.Pck_invoke_s[c_RequestDestroyItem().invoke] = c_RequestDestroyItem()
   self.Pck_invoke_s[c_SendBypassBuildCmd().invoke] = c_SendBypassBuildCmd()
   self.Pck_invoke_s[c_RequestGetOnVehicle().invoke] = c_RequestGetOnVehicle()
   self.Pck_invoke_s[c_RequestGetOffVehicle().invoke] = c_RequestGetOffVehicle()
   self.Pck_invoke_s[c_RequestFriendInvite().invoke] = c_RequestFriendInvite()
   self.Pck_invoke_s[c_RequestAnswerFriendInvite().invoke] = c_RequestAnswerFriendInvite()
   self.Pck_invoke_s[c_RequestFriendList().invoke] = c_RequestFriendList()
   self.Pck_invoke_s[c_RequestFriendDel().invoke] = c_RequestFriendDel()
   self.Pck_invoke_s[c_CharacterRestore().invoke] = c_CharacterRestore()
   self.Pck_invoke_s[c_RequestQuestList().invoke] = c_RequestQuestList()
   self.Pck_invoke_s[c_RequestQuestAbort().invoke] = c_RequestQuestAbort()
   self.Pck_invoke_s[c_RequestPledgeInfo().invoke] = c_RequestPledgeInfo()
   self.Pck_invoke_s[c_RequestPledgeExtendedInfo().invoke] = c_RequestPledgeExtendedInfo()
   self.Pck_invoke_s[c_RequestPledgeCrest().invoke] = c_RequestPledgeCrest()
   self.Pck_invoke_s[c_RequestSurrenderPersonally().invoke] = c_RequestSurrenderPersonally()
   self.Pck_invoke_s[c_RequestRide().invoke] = c_RequestRide()
   self.Pck_invoke_s[c_RequestAcquireSkillInfo().invoke] = c_RequestAcquireSkillInfo()
   self.Pck_invoke_s[c_RequestAcquireSkill().invoke] = c_RequestAcquireSkill()
   self.Pck_invoke_s[c_RequestRestartPoint().invoke] = c_RequestRestartPoint()
   self.Pck_invoke_s[c_RequestGMCommand().invoke] = c_RequestGMCommand()
   self.Pck_invoke_s[c_RequestPartyMatchConfig().invoke] = c_RequestPartyMatchConfig()
   self.Pck_invoke_s[c_RequestPartyMatchList().invoke] = c_RequestPartyMatchList()
   self.Pck_invoke_s[c_RequestPartyMatchDetail().invoke] = c_RequestPartyMatchDetail()
   self.Pck_invoke_s[c_RequestCrystallizeItem().invoke] = c_RequestCrystallizeItem()
   self.Pck_invoke_s[c_RequestPrivateStoreManage().invoke] = c_RequestPrivateStoreManage()
   self.Pck_invoke_s[c_SetPrivateStoreListSell().invoke] = c_SetPrivateStoreListSell()
   self.Pck_invoke_s[c_RequestPrivateStoreManageCancel().invoke] = c_RequestPrivateStoreManageCancel()
   self.Pck_invoke_s[c_RequestPrivateStoreQuit().invoke] = c_RequestPrivateStoreQuit()
   self.Pck_invoke_s[c_SetPrivateStoreMsg().invoke] = c_SetPrivateStoreMsg()
   self.Pck_invoke_s[c_RequestPrivateStoreList().invoke] = c_RequestPrivateStoreList()
   self.Pck_invoke_s[c_SendPrivateStoreBuyList().invoke] = c_SendPrivateStoreBuyList()
   self.Pck_invoke_s[c_ReviveReply().invoke] = c_ReviveReply()
   self.Pck_invoke_s[c_RequestTutorialLinkHtml().invoke] = c_RequestTutorialLinkHtml()
   self.Pck_invoke_s[c_RequestTutorialPassCmdToServer().invoke] = c_RequestTutorialPassCmdToServer()
   self.Pck_invoke_s[c_RequestTutorialQuestionMark().invoke] = c_RequestTutorialQuestionMark()
   self.Pck_invoke_s[c_RequestTutorialClientEvent().invoke] = c_RequestTutorialClientEvent()
   self.Pck_invoke_s[c_RequestPetition().invoke] = c_RequestPetition()
   self.Pck_invoke_s[c_RequestPetitionCancel().invoke] = c_RequestPetitionCancel()
   self.Pck_invoke_s[c_RequestGMList().invoke] = c_RequestGMList()
   self.Pck_invoke_s[c_RequestJoinAlly().invoke] = c_RequestJoinAlly()
   self.Pck_invoke_s[c_RequestAnswerJoinAlly().invoke] = c_RequestAnswerJoinAlly()
   self.Pck_invoke_s[c_RequestAllyLeave().invoke] = c_RequestAllyLeave()
   self.Pck_invoke_s[c_RequestAllyDismiss().invoke] = c_RequestAllyDismiss()
   self.Pck_invoke_s[c_RequestDismissAlly().invoke] = c_RequestDismissAlly()
   self.Pck_invoke_s[c_RequestSetAllyCrest().invoke] = c_RequestSetAllyCrest()
   self.Pck_invoke_s[c_RequestAllyCrest().invoke] = c_RequestAllyCrest()
   self.Pck_invoke_s[c_RequestChangePetName().invoke] = c_RequestChangePetName()
   self.Pck_invoke_s[c_RequestPetUseItem().invoke] = c_RequestPetUseItem()
   self.Pck_invoke_s[c_RequestGiveItemToPet().invoke] = c_RequestGiveItemToPet()
   self.Pck_invoke_s[c_RequestGetItemFromPet().invoke] = c_RequestGetItemFromPet()
   self.Pck_invoke_s[c_RequestAllyInfo().invoke] = c_RequestAllyInfo()
   self.Pck_invoke_s[c_RequestPetGetItem().invoke] = c_RequestPetGetItem()
   self.Pck_invoke_s[c_RequestPrivateStoreManageBuy().invoke] = c_RequestPrivateStoreManageBuy()
   self.Pck_invoke_s[c_SetPrivateStoreListBuy().invoke] = c_SetPrivateStoreListBuy()
   self.Pck_invoke_s[c_RequestPrivateStoreBuyManageCancel().invoke] = c_RequestPrivateStoreBuyManageCancel()
   self.Pck_invoke_s[c_RequestPrivateStoreQuitBuy().invoke] = c_RequestPrivateStoreQuitBuy()
   self.Pck_invoke_s[c_SetPrivateStoreMsgBuy().invoke] = c_SetPrivateStoreMsgBuy()
   self.Pck_invoke_s[c_RequestPrivateStoreBuyList().invoke] = c_RequestPrivateStoreBuyList()
   self.Pck_invoke_s[c_SendPrivateStoreBuyList().invoke] = c_SendPrivateStoreBuyList()
   self.Pck_invoke_s[c_SendTimeCheckPacket().invoke] = c_SendTimeCheckPacket()
   self.Pck_invoke_s[c_RequestStartAllianceWar().invoke] = c_RequestStartAllianceWar()
   self.Pck_invoke_s[c_ReplyStartAllianceWar().invoke] = c_ReplyStartAllianceWar()
   self.Pck_invoke_s[c_RequestStopAllianceWar().invoke] = c_RequestStopAllianceWar()
   self.Pck_invoke_s[c_ReplyStopAllianceWar().invoke] = c_ReplyStopAllianceWar()
   self.Pck_invoke_s[c_RequestSurrenderAllianceWar().invoke] = c_RequestSurrenderAllianceWar()
   self.Pck_invoke_s[c_RequestSkillCoolTime().invoke] = c_RequestSkillCoolTime()
   self.Pck_invoke_s[c_RequestPackageSendableItemList().invoke] = c_RequestPackageSendableItemList()
   self.Pck_invoke_s[c_RequestPackageSend().invoke] = c_RequestPackageSend()
   self.Pck_invoke_s[c_RequestBlock().invoke] = c_RequestBlock()
   self.Pck_invoke_s[c_RequestCastleSiegeInfo().invoke] = c_RequestCastleSiegeInfo()
   self.Pck_invoke_s[c_RequestSiegeAttackerList().invoke] = c_RequestSiegeAttackerList()
   self.Pck_invoke_s[c_RequestSiegeDefenderList().invoke] = c_RequestSiegeDefenderList()
   self.Pck_invoke_s[c_RequestJoinSiege().invoke] = c_RequestJoinSiege()
   self.Pck_invoke_s[c_RequestConfirmSiegeWaitingList().invoke] = c_RequestConfirmSiegeWaitingList()
   self.Pck_invoke_s[c_RequestSetCastleSiegeTime().invoke] = c_RequestSetCastleSiegeTime()
   self.Pck_invoke_s[c_RequestMultiSellChoose().invoke] = c_RequestMultiSellChoose()
   self.Pck_invoke_s[c_NetPing().invoke] = c_NetPing()
   self.Pck_invoke_s[c_RequestRemainTime().invoke] = c_RequestRemainTime()
   self.Pck_invoke_s[c_BypassUserCmd().invoke] = c_BypassUserCmd()
   self.Pck_invoke_s[c_SnoopQuit().invoke] = c_SnoopQuit()
   self.Pck_invoke_s[c_RequestRecipeBookOpen().invoke] = c_RequestRecipeBookOpen()
   self.Pck_invoke_s[c_RequestRecipeBookDestroy().invoke] = c_RequestRecipeBookDestroy()
   self.Pck_invoke_s[c_RequestRecipeItemMakeInfo().invoke] = c_RequestRecipeItemMakeInfo()
   self.Pck_invoke_s[c_RequestRecipeItemMakeSelf().invoke] = c_RequestRecipeItemMakeSelf()
   self.Pck_invoke_s[c_RequestRecipeShopManageList().invoke] = c_RequestRecipeShopManageList()
   self.Pck_invoke_s[c_RequestRecipeShopMessageSet().invoke] = c_RequestRecipeShopMessageSet()
   self.Pck_invoke_s[c_RequestRecipeShopListSet().invoke] = c_RequestRecipeShopListSet()
   self.Pck_invoke_s[c_RequestRecipeShopManageQuit().invoke] = c_RequestRecipeShopManageQuit()
   self.Pck_invoke_s[c_RequestRecipeShopManageCancel().invoke] = c_RequestRecipeShopManageCancel()
   self.Pck_invoke_s[c_RequestRecipeShopMakeInfo().invoke] = c_RequestRecipeShopMakeInfo()
   self.Pck_invoke_s[c_RequestRecipeShopMakeItem().invoke] = c_RequestRecipeShopMakeItem()
   self.Pck_invoke_s[c_RequestRecipeShopPrev().invoke] = c_RequestRecipeShopPrev()
   self.Pck_invoke_s[c_ObserverReturn().invoke] = c_ObserverReturn()
   self.Pck_invoke_s[c_RequestEvaluate().invoke] = c_RequestEvaluate()
   self.Pck_invoke_s[c_RequestHennaList().invoke] = c_RequestHennaList()
   self.Pck_invoke_s[c_RequestHennaItemInfo().invoke] = c_RequestHennaItemInfo()
   self.Pck_invoke_s[c_RequestHennaEquip().invoke] = c_RequestHennaEquip()
   self.Pck_invoke_s[c_RequestHennaUnequipList().invoke] = c_RequestHennaUnequipList()
   self.Pck_invoke_s[c_RequestHennaUnequipInfo().invoke] = c_RequestHennaUnequipInfo()
   self.Pck_invoke_s[c_RequestHennaUnequip().invoke] = c_RequestHennaUnequip()
   self.Pck_invoke_s[c_RequestPledgePower().invoke] = c_RequestPledgePower()
   self.Pck_invoke_s[c_RequestMakeMacro().invoke] = c_RequestMakeMacro()
   self.Pck_invoke_s[c_RequestDeleteMacro().invoke] = c_RequestDeleteMacro()
   self.Pck_invoke_s[c_RequestProcureCrop().invoke] = c_RequestProcureCrop()
   self.Pck_invoke_s[c_RequestBuySeed().invoke] = c_RequestBuySeed()
   self.Pck_invoke_s[c_DlgAnswer().invoke] = c_DlgAnswer()
   self.Pck_invoke_s[c_RequestWearItem().invoke] = c_RequestWearItem()
   self.Pck_invoke_s[c_RequestSSQStatus().invoke] = c_RequestSSQStatus()
   self.Pck_invoke_s[c_PetitionVote().invoke] = c_PetitionVote()
   self.Pck_invoke_s[c_GameGuardReply().invoke] = c_GameGuardReply()
   self.Pck_invoke_s[c_RequestSendFriendMsg().invoke] = c_RequestSendFriendMsg()
   self.Pck_invoke_s[c_RequestOpenMinimap().invoke] = c_RequestOpenMinimap()
   self.Pck_invoke_s[c_RequestSendMsnChatLog().invoke] = c_RequestSendMsnChatLog()
   self.Pck_invoke_s[c_RequestAutoSoulShot().invoke] = c_RequestAutoSoulShot()
   self.Pck_invoke_s[c_RequestChangePartyLeader().invoke] = c_RequestChangePartyLeader()
   self.Pck_invoke_s[c_SuperCmdCharacterInfo().invoke] = c_SuperCmdCharacterInfo()
   self.Pck_invoke_s[c_SuperCmdSummonCmd().invoke] = c_SuperCmdSummonCmd()
   self.Pck_invoke_s[c_SuperCmdServerStatus().invoke] = c_SuperCmdServerStatus()
   self.Pck_invoke_s[c_SuperCmdL2ParamSetting().invoke] = c_SuperCmdL2ParamSetting()
   self.Pck_invoke_s[c_RequestOustFromPartyRoom().invoke] = c_RequestOustFromPartyRoom()
   self.Pck_invoke_s[c_RequestDismissPartyRoom().invoke] = c_RequestDismissPartyRoom()
   self.Pck_invoke_s[c_RequestWithdrawPartyRoom().invoke] = c_RequestWithdrawPartyRoom()
   self.Pck_invoke_s[c_RequestHandOverPartyMaster().invoke] = c_RequestHandOverPartyMaster()
   self.Pck_invoke_s[c_RequestAutoSoulShot().invoke] = c_RequestAutoSoulShot()
   self.Pck_invoke_s[c_RequestExEnchantSkillInfo().invoke] = c_RequestExEnchantSkillInfo()
   self.Pck_invoke_s[c_RequestExEnchantSkill().invoke] = c_RequestExEnchantSkill()
   self.Pck_invoke_s[c_RequestManorList().invoke] = c_RequestManorList()
   self.Pck_invoke_s[c_RequestProcureCropList().invoke] = c_RequestProcureCropList()
   self.Pck_invoke_s[c_RequestSetSeed().invoke] = c_RequestSetSeed()
   self.Pck_invoke_s[c_RequestSetCrop().invoke] = c_RequestSetCrop()
   self.Pck_invoke_s[c_RequestExAskJoinMPCC().invoke] = c_RequestExAskJoinMPCC()
   self.Pck_invoke_s[c_RequestExAcceptJoinMPCC().invoke] = c_RequestExAcceptJoinMPCC()
   self.Pck_invoke_s[c_RequestExOustFromMPCC().invoke] = c_RequestExOustFromMPCC()
   self.Pck_invoke_s[c_RequestExPledgeCrestLarge().invoke] = c_RequestExPledgeCrestLarge()
   self.Pck_invoke_s[c_RequestExSetPledgeCrestLarge().invoke] = c_RequestExSetPledgeCrestLarge()
   self.Pck_invoke_s[c_RequestOlympiadObserverEnd().invoke] = c_RequestOlympiadObserverEnd()
   self.Pck_invoke_s[c_RequestOlympiadMatchList().invoke] = c_RequestOlympiadMatchList()
   self.Pck_invoke_s[c_RequestAskJoinPartyRoom().invoke] = c_RequestAskJoinPartyRoom()
   self.Pck_invoke_s[c_AnswerJoinPartyRoom().invoke] = c_AnswerJoinPartyRoom()
   self.Pck_invoke_s[c_RequestListPartyMatchingWaitingRoom().invoke] = c_RequestListPartyMatchingWaitingRoom()
   self.Pck_invoke_s[c_RequestExitPartyMatchingWaitingRoom().invoke] = c_RequestExitPartyMatchingWaitingRoom()
   self.Pck_invoke_s[c_RequestGetBossRecord().invoke] = c_RequestGetBossRecord()
   self.Pck_invoke_s[c_RequestPledgeSetAcademyMaster().invoke] = c_RequestPledgeSetAcademyMaster()
   self.Pck_invoke_s[c_RequestPledgePowerGradeList().invoke] = c_RequestPledgePowerGradeList()
   self.Pck_invoke_s[c_RequestPledgeMemberPowerInfo().invoke] = c_RequestPledgeMemberPowerInfo()
   self.Pck_invoke_s[c_RequestPledgeSetMemberPowerGrade().invoke] = c_RequestPledgeSetMemberPowerGrade()
   self.Pck_invoke_s[c_RequestPledgeMemberInfo().invoke] = c_RequestPledgeMemberInfo()
   self.Pck_invoke_s[c_RequestPledgeWarList().invoke] = c_RequestPledgeWarList()
   self.Pck_invoke_s[c_RequestExFishRanking().invoke] = c_RequestExFishRanking()
   self.Pck_invoke_s[c_RequestPCCafeCouponUse().invoke] = c_RequestPCCafeCouponUse()
   self.Pck_invoke_s[c_RequestCursedWeaponList().invoke] = c_RequestCursedWeaponList()
   self.Pck_invoke_s[c_RequestCursedWeaponLocation().invoke] = c_RequestCursedWeaponLocation()
   self.Pck_invoke_s[c_RequestPledgeReorganizeMember().invoke] = c_RequestPledgeReorganizeMember()
   return self.Pck_invoke_s
 def get_Pck_invoke_s(self):
   self.Pck_invoke_c[s_KeyInit().invoke] = s_KeyInit()
   self.Pck_invoke_c[s_MoveToLocation().invoke] = s_MoveToLocation()
   self.Pck_invoke_c[s_NpcSay().invoke] = s_NpcSay()
   self.Pck_invoke_c[s_CharInfo().invoke] = s_CharInfo()
   self.Pck_invoke_c[s_UserInfo().invoke] = s_UserInfo()
   self.Pck_invoke_c[s_Attack().invoke] = s_Attack()
   self.Pck_invoke_c[s_Die().invoke] = s_Die()
   self.Pck_invoke_c[s_Revive().invoke] = s_Revive()
   self.Pck_invoke_c[s_AttackOutOfRange().invoke] = s_AttackOutOfRange()
   self.Pck_invoke_c[s_AttackinCoolTime().invoke] = s_AttackinCoolTime()
   self.Pck_invoke_c[s_AttackDeadTarget().invoke] = s_AttackDeadTarget()
   self.Pck_invoke_c[s_SpawnItem().invoke] = s_SpawnItem()
   self.Pck_invoke_c[s_DropItem().invoke] = s_DropItem()
   self.Pck_invoke_c[s_GetItem().invoke] = s_GetItem()
   self.Pck_invoke_c[s_StatusUpdate().invoke] = s_StatusUpdate()
   self.Pck_invoke_c[s_NpcHtmlMessage().invoke] = s_NpcHtmlMessage()
   self.Pck_invoke_c[s_SellList().invoke] = s_SellList()
   self.Pck_invoke_c[s_BuyList().invoke] = s_BuyList()
   self.Pck_invoke_c[s_DeleteObject().invoke] = s_DeleteObject()
   self.Pck_invoke_c[s_CharSelectInfo().invoke] = s_CharSelectInfo()
   self.Pck_invoke_c[s_LoginFail().invoke] = s_LoginFail()
   self.Pck_invoke_c[s_CharSelected().invoke] = s_CharSelected()
   self.Pck_invoke_c[s_NpcInfo().invoke] = s_NpcInfo()
   self.Pck_invoke_c[s_CharTemplates().invoke] = s_CharTemplates()
   self.Pck_invoke_c[s_NewCharFail().invoke] = s_NewCharFail()
   self.Pck_invoke_c[s_CharCreateSuccess().invoke] = s_CharCreateSuccess()
   self.Pck_invoke_c[s_CharCreateFail().invoke] = s_CharCreateFail()
   self.Pck_invoke_c[s_ItemListPacket().invoke] = s_ItemListPacket()
   self.Pck_invoke_c[s_SunRise().invoke] = s_SunRise()
   self.Pck_invoke_c[s_SunSet().invoke] = s_SunSet()
   self.Pck_invoke_c[s_TradeStart().invoke] = s_TradeStart()
   self.Pck_invoke_c[s_TradeStartOk().invoke] = s_TradeStartOk()
   self.Pck_invoke_c[s_TradeOwnAdd().invoke] = s_TradeOwnAdd()
   self.Pck_invoke_c[s_TradeOtherAdd().invoke] = s_TradeOtherAdd()
   self.Pck_invoke_c[s_TradeDone().invoke] = s_TradeDone()
   self.Pck_invoke_c[s_CharDeleteSuccess().invoke] = s_CharDeleteSuccess()
   self.Pck_invoke_c[s_CharDeleteFail().invoke] = s_CharDeleteFail()
   self.Pck_invoke_c[s_ActionFail().invoke] = s_ActionFail()
   self.Pck_invoke_c[s_SeverClose().invoke] = s_SeverClose()
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
   self.Pck_invoke_c[s_CreatePledge().invoke] = s_CreatePledge()
   self.Pck_invoke_c[s_AskJoinPledge().invoke] = s_AskJoinPledge()
   self.Pck_invoke_c[s_JoinPledge().invoke] = s_JoinPledge()
   self.Pck_invoke_c[s_WithdrawalPledge().invoke] = s_WithdrawalPledge()
   self.Pck_invoke_c[s_OustPledgeMember().invoke] = s_OustPledgeMember()
   self.Pck_invoke_c[s_SetOustPledgeMember().invoke] = s_SetOustPledgeMember()
   self.Pck_invoke_c[s_DismissPledge().invoke] = s_DismissPledge()
   self.Pck_invoke_c[s_SetDismissPledge().invoke] = s_SetDismissPledge()
   self.Pck_invoke_c[s_AskJoinParty().invoke] = s_AskJoinParty()
   self.Pck_invoke_c[s_JoinParty().invoke] = s_JoinParty()
   self.Pck_invoke_c[s_WithdrawalParty().invoke] = s_WithdrawalParty()
   self.Pck_invoke_c[s_OustPartyMember().invoke] = s_OustPartyMember()
   self.Pck_invoke_c[s_SetOustPartyMember().invoke] = s_SetOustPartyMember()
   self.Pck_invoke_c[s_DismissParty().invoke] = s_DismissParty()
   self.Pck_invoke_c[s_SetDismissParty().invoke] = s_SetDismissParty()
   self.Pck_invoke_c[s_MagicAndSkillList().invoke] = s_MagicAndSkillList()
   self.Pck_invoke_c[s_WareHouseDepositList().invoke] = s_WareHouseDepositList()
   self.Pck_invoke_c[s_WareHouseWithdrawList().invoke] = s_WareHouseWithdrawList()
   self.Pck_invoke_c[s_WareHouseDone().invoke] = s_WareHouseDone()
   self.Pck_invoke_c[s_ShortCutRegister().invoke] = s_ShortCutRegister()
   self.Pck_invoke_c[s_ShortCutInit().invoke] = s_ShortCutInit()
   self.Pck_invoke_c[s_ShortCutDelete().invoke] = s_ShortCutDelete()
   self.Pck_invoke_c[s_StopMove().invoke] = s_StopMove()
   self.Pck_invoke_c[s_MagicSkillUse().invoke] = s_MagicSkillUse()
   self.Pck_invoke_c[s_MagicSkillCanceled().invoke] = s_MagicSkillCanceled()
   self.Pck_invoke_c[s_Say2().invoke] = s_Say2()
   self.Pck_invoke_c[s_EquipUpdate().invoke] = s_EquipUpdate()
   self.Pck_invoke_c[s_DoorInfo().invoke] = s_DoorInfo()
   self.Pck_invoke_c[s_DoorStatusUpdate().invoke] = s_DoorStatusUpdate()
   self.Pck_invoke_c[s_PartySmallWindowAll().invoke] = s_PartySmallWindowAll()
   self.Pck_invoke_c[s_PartySmallWindowAdd().invoke] = s_PartySmallWindowAdd()
   self.Pck_invoke_c[s_PartySmallWindowDeleteAll().invoke] = s_PartySmallWindowDeleteAll()
   self.Pck_invoke_c[s_PartySmallWindowDelete().invoke] = s_PartySmallWindowDelete()
   self.Pck_invoke_c[s_PartySmallWindowUpdate().invoke] = s_PartySmallWindowUpdate()
   self.Pck_invoke_c[s_PledgeShowMemberListAll().invoke] = s_PledgeShowMemberListAll()
   self.Pck_invoke_c[s_PledgeShowMemberListUpdate().invoke] = s_PledgeShowMemberListUpdate()
   self.Pck_invoke_c[s_PledgeShowMemberListAdd().invoke] = s_PledgeShowMemberListAdd()
   self.Pck_invoke_c[s_PledgeShowMemberListDelete().invoke] = s_PledgeShowMemberListDelete()
   self.Pck_invoke_c[s_MagicList().invoke] = s_MagicList()
   self.Pck_invoke_c[s_SkillList().invoke] = s_SkillList()
   self.Pck_invoke_c[s_VehicleInfo().invoke] = s_VehicleInfo()
   self.Pck_invoke_c[s_VehicleDeparture().invoke] = s_VehicleDeparture()
   self.Pck_invoke_c[s_VehicleCheckLocation().invoke] = s_VehicleCheckLocation()
   self.Pck_invoke_c[s_GetOnVehicle().invoke] = s_GetOnVehicle()
   self.Pck_invoke_c[s_GetOffVehicle().invoke] = s_GetOffVehicle()
   self.Pck_invoke_c[s_TradeRequest().invoke] = s_TradeRequest()
   self.Pck_invoke_c[s_RestartResponse().invoke] = s_RestartResponse()
   self.Pck_invoke_c[s_MoveToPawn().invoke] = s_MoveToPawn()
   self.Pck_invoke_c[s_ValidateLocation().invoke] = s_ValidateLocation()
   self.Pck_invoke_c[s_StartRotating().invoke] = s_StartRotating()
   self.Pck_invoke_c[s_FinishRotating().invoke] = s_FinishRotating()
   self.Pck_invoke_c[s_SystemMessage().invoke] = s_SystemMessage()
   self.Pck_invoke_c[s_StartPledgeWar().invoke] = s_StartPledgeWar()
   self.Pck_invoke_c[s_ReplyStartPledgeWar().invoke] = s_ReplyStartPledgeWar()
   self.Pck_invoke_c[s_StopPledgeWar().invoke] = s_StopPledgeWar()
   self.Pck_invoke_c[s_ReplyStopPledgeWar().invoke] = s_ReplyStopPledgeWar()
   self.Pck_invoke_c[s_SurrenderPledgeWar().invoke] = s_SurrenderPledgeWar()
   self.Pck_invoke_c[s_ReplySurrenderPledgeWar().invoke] = s_ReplySurrenderPledgeWar()
   self.Pck_invoke_c[s_SetPledgeCrest().invoke] = s_SetPledgeCrest()
   self.Pck_invoke_c[s_PledgeCrest().invoke] = s_PledgeCrest()
   self.Pck_invoke_c[s_SetupGauge().invoke] = s_SetupGauge()
   self.Pck_invoke_c[s_ShowBoard().invoke] = s_ShowBoard()
   self.Pck_invoke_c[s_ChooseInventoryItem().invoke] = s_ChooseInventoryItem()
   self.Pck_invoke_c[s_Dummy().invoke] = s_Dummy()
   self.Pck_invoke_c[s_MoveToLocationInVehicle().invoke] = s_MoveToLocationInVehicle()
   self.Pck_invoke_c[s_StopMoveInVehicle().invoke] = s_StopMoveInVehicle()
   self.Pck_invoke_c[s_ValidateLocationInVehicle().invoke] = s_ValidateLocationInVehicle()
   self.Pck_invoke_c[s_TradeUpdate().invoke] = s_TradeUpdate()
   self.Pck_invoke_c[s_TradePressOwnOk().invoke] = s_TradePressOwnOk()
   self.Pck_invoke_c[s_MagicSkillLaunched().invoke] = s_MagicSkillLaunched()
   self.Pck_invoke_c[s_FriendAddRequestResult().invoke] = s_FriendAddRequestResult()
   self.Pck_invoke_c[s_FriendAdd().invoke] = s_FriendAdd()
   self.Pck_invoke_c[s_FriendRemove().invoke] = s_FriendRemove()
   self.Pck_invoke_c[s_FriendList().invoke] = s_FriendList()
   self.Pck_invoke_c[s_FriendStatus().invoke] = s_FriendStatus()
   self.Pck_invoke_c[s_TradePressOtherOk().invoke] = s_TradePressOtherOk()
   self.Pck_invoke_c[s_FriendAddRequest().invoke] = s_FriendAddRequest()
   self.Pck_invoke_c[s_LogOutOk().invoke] = s_LogOutOk()
   self.Pck_invoke_c[s_MagicEffectIcons().invoke] = s_MagicEffectIcons()
   self.Pck_invoke_c[s_QuestList().invoke] = s_QuestList()
   self.Pck_invoke_c[s_EnchantResult().invoke] = s_EnchantResult()
   self.Pck_invoke_c[s_PledgeShowMemberListDeleteAll().invoke] = s_PledgeShowMemberListDeleteAll()
   self.Pck_invoke_c[s_PledgeInfo().invoke] = s_PledgeInfo()
   self.Pck_invoke_c[s_PledgeExtendedInfo().invoke] = s_PledgeExtendedInfo()
   self.Pck_invoke_c[s_SurrenderPersonally().invoke] = s_SurrenderPersonally()
   self.Pck_invoke_c[s_Ride().invoke] = s_Ride()
   self.Pck_invoke_c[s_Dummy().invoke] = s_Dummy()
   self.Pck_invoke_c[s_PledgeShowInfoUpdate().invoke] = s_PledgeShowInfoUpdate()
   self.Pck_invoke_c[s_ClientAction().invoke] = s_ClientAction()
   self.Pck_invoke_c[s_AcquireSkillList().invoke] = s_AcquireSkillList()
   self.Pck_invoke_c[s_AcquireSkillInfo().invoke] = s_AcquireSkillInfo()
   self.Pck_invoke_c[s_ServerObjectInfo().invoke] = s_ServerObjectInfo()
   self.Pck_invoke_c[s_GMHide().invoke] = s_GMHide()
   self.Pck_invoke_c[s_AcquireSkillDone().invoke] = s_AcquireSkillDone()
   self.Pck_invoke_c[s_GMViewCharacterInfo().invoke] = s_GMViewCharacterInfo()
   self.Pck_invoke_c[s_GMViewPledgeInfo().invoke] = s_GMViewPledgeInfo()
   self.Pck_invoke_c[s_GMViewSkillInfo().invoke] = s_GMViewSkillInfo()
   self.Pck_invoke_c[s_GMViewMagicInfo().invoke] = s_GMViewMagicInfo()
   self.Pck_invoke_c[s_GMViewQuestInfo().invoke] = s_GMViewQuestInfo()
   self.Pck_invoke_c[s_GMViewItemList().invoke] = s_GMViewItemList()
   self.Pck_invoke_c[s_GMViewWarehouseWithdrawList().invoke] = s_GMViewWarehouseWithdrawList()
   self.Pck_invoke_c[s_ListPartyWating().invoke] = s_ListPartyWating()
   self.Pck_invoke_c[s_PartyRoomInfo().invoke] = s_PartyRoomInfo()
   self.Pck_invoke_c[s_PlaySound().invoke] = s_PlaySound()
   self.Pck_invoke_c[s_StaticObject().invoke] = s_StaticObject()
   self.Pck_invoke_c[s_PrivateStoreManageList().invoke] = s_PrivateStoreManageList()
   self.Pck_invoke_c[s_PrivateStoreList().invoke] = s_PrivateStoreList()
   self.Pck_invoke_c[s_PrivateStoreMsg().invoke] = s_PrivateStoreMsg()
   self.Pck_invoke_c[s_ShowMinimap().invoke] = s_ShowMinimap()
   self.Pck_invoke_c[s_ReviveRequest().invoke] = s_ReviveRequest()
   self.Pck_invoke_c[s_AbnormalVisualEffect().invoke] = s_AbnormalVisualEffect()
   self.Pck_invoke_c[s_TutorialShowHtml().invoke] = s_TutorialShowHtml()
   self.Pck_invoke_c[s_TutorialShowQuestionMark().invoke] = s_TutorialShowQuestionMark()
   self.Pck_invoke_c[s_TutorialEnableClientEvent().invoke] = s_TutorialEnableClientEvent()
   self.Pck_invoke_c[s_TutorialCloseHtml().invoke] = s_TutorialCloseHtml()
   self.Pck_invoke_c[s_ShowRadar().invoke] = s_ShowRadar()
   self.Pck_invoke_c[s_DeleteRadar().invoke] = s_DeleteRadar()
   self.Pck_invoke_c[s_MyTargetSelected().invoke] = s_MyTargetSelected()
   self.Pck_invoke_c[s_PartyMemberPosition().invoke] = s_PartyMemberPosition()
   self.Pck_invoke_c[s_AskJoinAlliance().invoke] = s_AskJoinAlliance()
   self.Pck_invoke_c[s_JoinAlliance().invoke] = s_JoinAlliance()
   self.Pck_invoke_c[s_WithdrawAlliance().invoke] = s_WithdrawAlliance()
   self.Pck_invoke_c[s_OustAllianceMemberPledge().invoke] = s_OustAllianceMemberPledge()
   self.Pck_invoke_c[s_DismissAlliance().invoke] = s_DismissAlliance()
   self.Pck_invoke_c[s_SetAllianceCrest().invoke] = s_SetAllianceCrest()
   self.Pck_invoke_c[s_AllianceCrest().invoke] = s_AllianceCrest()
   self.Pck_invoke_c[s_ServerCloseSocket().invoke] = s_ServerCloseSocket()
   self.Pck_invoke_c[s_PetStatusShow().invoke] = s_PetStatusShow()
   self.Pck_invoke_c[s_PetInfo().invoke] = s_PetInfo()
   self.Pck_invoke_c[s_PetItemList().invoke] = s_PetItemList()
   self.Pck_invoke_c[s_PetInventoryUpdate().invoke] = s_PetInventoryUpdate()
   self.Pck_invoke_c[s_AllianceInfo().invoke] = s_AllianceInfo()
   self.Pck_invoke_c[s_PetStatusUpdate().invoke] = s_PetStatusUpdate()
   self.Pck_invoke_c[s_PetDelete().invoke] = s_PetDelete()
   self.Pck_invoke_c[s_PrivateStoreBuyManageList().invoke] = s_PrivateStoreBuyManageList()
   self.Pck_invoke_c[s_PrivateBuyListBuy().invoke] = s_PrivateBuyListBuy()
   self.Pck_invoke_c[s_PrivateStoreMsgBuy().invoke] = s_PrivateStoreMsgBuy()
   self.Pck_invoke_c[s_VehicleStart().invoke] = s_VehicleStart()
   self.Pck_invoke_c[s_RequestTimeCheck().invoke] = s_RequestTimeCheck()
   self.Pck_invoke_c[s_StartAllianceWar().invoke] = s_StartAllianceWar()
   self.Pck_invoke_c[s_ReplyStartAllianceWar().invoke] = s_ReplyStartAllianceWar()
   self.Pck_invoke_c[s_StopAllianceWar().invoke] = s_StopAllianceWar()
   self.Pck_invoke_c[s_ReplyStopAllianceWar().invoke] = s_ReplyStopAllianceWar()
   self.Pck_invoke_c[s_SurrenderAllianceWar().invoke] = s_SurrenderAllianceWar()
   self.Pck_invoke_c[s_SkillCoolTime().invoke] = s_SkillCoolTime()
   self.Pck_invoke_c[s_PackageToList().invoke] = s_PackageToList()
   self.Pck_invoke_c[s_PackageSendableList().invoke] = s_PackageSendableList()
   self.Pck_invoke_c[s_EarthQuake().invoke] = s_EarthQuake()
   self.Pck_invoke_c[s_FlyToLoaction().invoke] = s_FlyToLoaction()
   self.Pck_invoke_c[s_BlockList().invoke] = s_BlockList()
   self.Pck_invoke_c[s_SpecialCamera().invoke] = s_SpecialCamera()
   self.Pck_invoke_c[s_NormalCamera().invoke] = s_NormalCamera()
   self.Pck_invoke_c[s_CastleSiegeInfo().invoke] = s_CastleSiegeInfo()
   self.Pck_invoke_c[s_CastleSiegeAttackerList().invoke] = s_CastleSiegeAttackerList()
   self.Pck_invoke_c[s_CastleSiegeDefenderList().invoke] = s_CastleSiegeDefenderList()
   self.Pck_invoke_c[s_NickNameChanged().invoke] = s_NickNameChanged()
   self.Pck_invoke_c[s_PledgeStatusChanged().invoke] = s_PledgeStatusChanged()
   self.Pck_invoke_c[s_RelationChanged().invoke] = s_RelationChanged()
   self.Pck_invoke_c[s_EventTrigger().invoke] = s_EventTrigger()
   self.Pck_invoke_c[s_MultiSellList_().invoke] = s_MultiSellList_()
   self.Pck_invoke_c[s_SetSummonRemainTime().invoke] = s_SetSummonRemainTime()
   self.Pck_invoke_c[s_SkillRemainSec().invoke] = s_SkillRemainSec()
   self.Pck_invoke_c[s_NetPing().invoke] = s_NetPing()
   self.Pck_invoke_c[s_Dice().invoke] = s_Dice()
   self.Pck_invoke_c[s_Snoop().invoke] = s_Snoop()
   self.Pck_invoke_c[s_RecipeBookItemList().invoke] = s_RecipeBookItemList()
   self.Pck_invoke_c[s_RecipeItemMakeInfo().invoke] = s_RecipeItemMakeInfo()
   self.Pck_invoke_c[s_RecipeShopManageList().invoke] = s_RecipeShopManageList()
   self.Pck_invoke_c[s_RecipeShopSellList().invoke] = s_RecipeShopSellList()
   self.Pck_invoke_c[s_RecipeShopItemInfo().invoke] = s_RecipeShopItemInfo()
   self.Pck_invoke_c[s_RecipeShopMsg().invoke] = s_RecipeShopMsg()
   self.Pck_invoke_c[s_ShowCalculator().invoke] = s_ShowCalculator()
   self.Pck_invoke_c[s_MonRaceInfo().invoke] = s_MonRaceInfo()
   self.Pck_invoke_c[s_ShowTownMap().invoke] = s_ShowTownMap()
   self.Pck_invoke_c[s_ObservationMode().invoke] = s_ObservationMode()
   self.Pck_invoke_c[s_ObservationReturn().invoke] = s_ObservationReturn()
   self.Pck_invoke_c[s_ChairSit().invoke] = s_ChairSit()
   self.Pck_invoke_c[s_HennaEquipList().invoke] = s_HennaEquipList()
   self.Pck_invoke_c[s_HennaItemInfo().invoke] = s_HennaItemInfo()
   self.Pck_invoke_c[s_HennaInfo().invoke] = s_HennaInfo()
   self.Pck_invoke_c[s_HennaUnequipList().invoke] = s_HennaUnequipList()
   self.Pck_invoke_c[s_HennaUnequipInfo().invoke] = s_HennaUnequipInfo()
   self.Pck_invoke_c[s_SendMacroList().invoke] = s_SendMacroList()
   self.Pck_invoke_c[s_BuyListSeed().invoke] = s_BuyListSeed()
   self.Pck_invoke_c[s_SellListProcure().invoke] = s_SellListProcure()
   self.Pck_invoke_c[s_GMHennaInfo().invoke] = s_GMHennaInfo()
   self.Pck_invoke_c[s_RadarControl().invoke] = s_RadarControl()
   self.Pck_invoke_c[s_ClientSetTime().invoke] = s_ClientSetTime()
   self.Pck_invoke_c[s_ConfirmDlg().invoke] = s_ConfirmDlg()
   self.Pck_invoke_c[s_PartySpelled().invoke] = s_PartySpelled()
   self.Pck_invoke_c[s_ShopPreviewList().invoke] = s_ShopPreviewList()
   self.Pck_invoke_c[s_ShopPreviewInfo().invoke] = s_ShopPreviewInfo()
   self.Pck_invoke_c[s_CameraMode().invoke] = s_CameraMode()
   self.Pck_invoke_c[s_ShowXMasSeal().invoke] = s_ShowXMasSeal()
   self.Pck_invoke_c[s_EtcStatusUpdate().invoke] = s_EtcStatusUpdate()
   self.Pck_invoke_c[s_ShortBuffStatusUpdate().invoke] = s_ShortBuffStatusUpdate()
   self.Pck_invoke_c[s_SSQStatus_().invoke] = s_SSQStatus_()
   self.Pck_invoke_c[s_PetitionVote().invoke] = s_PetitionVote()
   self.Pck_invoke_c[s_AgitDecoInfo().invoke] = s_AgitDecoInfo()
   self.Pck_invoke_c[s_SSQInfo().invoke] = s_SSQInfo()
   self.Pck_invoke_c[s_GameGuardQuery().invoke] = s_GameGuardQuery()
   self.Pck_invoke_c[s_FriendList().invoke] = s_FriendList()
   self.Pck_invoke_c[s_Friend().invoke] = s_Friend()
   self.Pck_invoke_c[s_FriendStatus().invoke] = s_FriendStatus()
   self.Pck_invoke_c[s_FriendSay().invoke] = s_FriendSay()
   self.Pck_invoke_c[s_ExAutoSoulShot().invoke] = s_ExAutoSoulShot()
   self.Pck_invoke_c[s_ExFishingStart().invoke] = s_ExFishingStart()
   self.Pck_invoke_c[s_ExFishingEnd().invoke] = s_ExFishingEnd()
   self.Pck_invoke_c[s_ExFishingStartCombat().invoke] = s_ExFishingStartCombat()
   self.Pck_invoke_c[s_ExFishingHpRegen().invoke] = s_ExFishingHpRegen()
   self.Pck_invoke_c[s_ExEnchantSkillList().invoke] = s_ExEnchantSkillList()
   self.Pck_invoke_c[s_ExEnchantSkillInfo().invoke] = s_ExEnchantSkillInfo()
   self.Pck_invoke_c[s_ExQuestInfo().invoke] = s_ExQuestInfo()
   self.Pck_invoke_c[s_ExSendManorList().invoke] = s_ExSendManorList()
   self.Pck_invoke_c[s_ManorList1().invoke] = s_ManorList1()
   self.Pck_invoke_c[s_ManorList2().invoke] = s_ManorList2()
   self.Pck_invoke_c[s_ExHeroList().invoke] = s_ExHeroList()
   self.Pck_invoke_c[s_ExPledgeCrestLarge().invoke] = s_ExPledgeCrestLarge()
   self.Pck_invoke_c[s_ExOlympiadUserInfo().invoke] = s_ExOlympiadUserInfo()
   self.Pck_invoke_c[s_ExOlympiadSpelledInfo().invoke] = s_ExOlympiadSpelledInfo()
   self.Pck_invoke_c[s_ExOlympiadMode().invoke] = s_ExOlympiadMode()
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
   self.Pck_invoke_c[s_ExOrcMove().invoke] = s_ExOrcMove()
   self.Pck_invoke_c[s_ExCursedWeaponList().invoke] = s_ExCursedWeaponList()
   self.Pck_invoke_c[s_ExCursedWeaponLocation().invoke] = s_ExCursedWeaponLocation()
   self.Pck_invoke_c[s_ExRestartClient().invoke] = s_ExRestartClient()
   return self.Pck_invoke_c
