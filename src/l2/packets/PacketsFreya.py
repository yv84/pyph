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
              , ('AttackClick', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#03
class c_ReqStartPledgeWar():
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
class c_ReqReplyStartPledgeWar():
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
class c_ReqStopPledgeWar():
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
class c_ReqReplyStopPledgeWar():
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
class c_ReqSurrenderPledgeWar():
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
class c_ReqReplySurrenderPledgeWar():
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
class c_ReqSetPledgeCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x09'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CrestData', 'i1')
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
              , ('0256fixed', 'i4')
              , ('U', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#0F
class c_MoveBackwardToLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('targetX', 'i4')
              , ('targetY', 'i4')
              , ('targetZ', 'i4')
              , ('originX', 'i4')
              , ('originY', 'i4')
              , ('originZ', 'i4')
              , ('moveByMouse', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#11
class c_EnterWorld():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x11'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('0032_0', 'i4')
              , ('0016', 'i4')
              , ('0032_1', 'i4')
              , ('d', 'i4')
              , ('Trace0', 'i4')
              , ('Trace1', 'i4')
              , ('Trace2', 'i4')
              , ('Trace3', 'i4')
              , ('Trace4', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#12
class c_CharSelected():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x12'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharSlot', 'i4')
              , ('U_0', 'i2')
              , ('U_1', 'i4')
              , ('U_2', 'i4')
              , ('U_3', 'i4')
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
              , ('Count', 'i8')
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
              , ('ctrlPressed', 'i4')
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
              , ('Count', 'i8')
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
#--------------------------------------------------------------------------#22
class c_RequestLinkHtml():
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
              , ('link', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#23
class c_ReqBypassToServer():
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
class c_ReqBBSwrite():
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
#--------------------------------------------------------------------------#26
class c_ReqJoinPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x26'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Target', 'i4')
              , ('PledgeType', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#27
class c_ReqAnswerJoinPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x27'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Answer', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#28
class c_ReqWithdrawalPledge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x28'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#29
class c_ReqOustPledgeMember():
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
class c_ReqAuthLogin():
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
              , ('U', 'i4')
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
class c_ReqGetItemFromPet():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Amount', 'i8')
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2E
class c_ReqAllyInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#2F
class c_ReqCrystallizeItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Count', 'i8')
                  ]
    return dtype
#--------------------------------------------------------------------------#30
class c_ReqPrivateStoreManageSell():
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
              , ('isPackage', 'i4')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Count', 'i8')
              , ('Price', 'i8')
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
#--------------------------------------------------------------------------#32
class c_AttackRequest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x32'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('OrigX', 'i4')
              , ('OrigY', 'i4')
              , ('OrigZ', 'i4')
              , ('AttackClick', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#34
class c_RequestSocialAction():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x34'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Action', 'i4')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Count', 'i8')
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
#--------------------------------------------------------------------------#39
class c_RequestMagicSkillUse():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x39'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('skillID', 'i4')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Count', 'i8')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Count', 'i8')
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
#--------------------------------------------------------------------------#3D
class c_RequestShortCutReg():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x3D'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Type', 'i4')
              , ('Slot', 'i4')
              , ('ID', 'i4')
              , ('U', 'i4')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ItemID', 'i4')
              , ('Count', 'i8')
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
class c_RequestTargetCancel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x48'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('unselect', 'i2')
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
              , ('Response', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#56
class c_RequestActionUse():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x56'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Action', 'i4')
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
#--------------------------------------------------------------------------#5B
class c_StartRotating():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('degree', 'i4')
              , ('side', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#5C
class c_FinishRotating():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x5C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('degree', 'i4')
              , ('U', 'i4')
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
              , ('supportID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#60
class c_RequestDestroyItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x60'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('Count', 'i8')
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
#--------------------------------------------------------------------------#70
class c_RequestHennaRemoveList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x70'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('symbolID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#71
class c_RequestHennaItemRemoveInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x71'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('symbolID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#72
class c_RequestHennaRemove():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x72'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('symbolID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#73
class c_RequestAcquireSkillInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x73'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('skillID', 'i4')
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
class c_ReqMoveToLocationInVehicle():
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
              , ('skillID', 'i4')
              , ('Level', 'i4')
              , ('Type', 'i4')
              , ('subtype', 'i4')
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
              , ('roomID', 'i4')
              , ('membMax', 'i4')
              , ('lvlMin', 'i4')
              , ('lvlMax', 'i4')
              , ('loot', 'i4')
              , ('roomTitle', '|S'+str(self.It.__next__()) )
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
              , ('roomID', 'i4')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Count', 'i8')
              , ('Price', 'i8')
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
              , ('0', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#8B
class c_RequestGMList():
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
              , ('_ID', 'i4')
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
              , ('CrestAlly', 'i1')
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
              , ('Amount', 'i8')
                  ]
    return dtype
#--------------------------------------------------------------------------#96
class c_ReqPrivateStoreQuitSell():
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
class c_ReqPrivateStoreManageBuy():
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ItemID', 'i4')
              , ('U_0', 'i4')
              , ('Count', 'i8')
              , ('Price', 'i8')
              , ('U_1', 'i4')
              , ('U_2', 'i4')
              , ('U_3', 'i4')
              , ('U_4', 'i4')
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
#--------------------------------------------------------------------------#9C
class c_ReqPrivateStoreQuitBuy():
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('0_0', 'i2')
              , ('0_1', 'i2')
              , ('Count', 'i8')
              , ('Price', 'i8')
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
#--------------------------------------------------------------------------#A6
class c_RequestSkillCoolTime():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#A7
class c_ReqPackageSendableItemList():
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('_ID', 'i4')
              , ('Count', 'i8')
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
#--------------------------------------------------------------------------#AA
class c_RequestSiegeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAA'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
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
class c_ReqConfirmSiegeWaitingList():
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
              , ('Amount', 'i8')
                  ]
    return dtype
#--------------------------------------------------------------------------#B1
class c_NetPing():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xB1'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('kID', 'i4')
              , ('PING', 'i4')
              , ('dta', 'i4')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('RecipeID', 'i4')
              , ('Cost', 'i8')
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
              , ('count', 'i8')
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
              , ('0', 'i4')
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
               ('ItemID', 'i4')
              , ('Count', 'i8')
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
#--------------------------------------------------------------------------#C6
class c_DlgAnswer():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('MessageID', 'i4')
              , ('Answer', 'i4')
              , ('requesterId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#C7
class c_RequestPreviewItem():
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
              , ('U', 'i4')
              , ('ListID', 'i4')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ItemID', 'i4')
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
              , ('d_0', 'i4')
              , ('d_1', 'i4')
              , ('d_2', 'i4')
              , ('d_3', 'i4')
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
              , ('ItemID', 'i4')
              , ('Count', 'i8')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('ManorID', 'i4')
              , ('Count', 'i8')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ItemID', 'i4')
              , ('Sales', 'i8')
              , ('Price', 'i8')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ItemID', 'i4')
              , ('Sales', 'i8')
              , ('Price', 'i8')
              , ('Type', 'i1')
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
              , ('roomID', 'i4')
              , ('Data', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D00B
class c_RequestWithdrawPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x0B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('roomID', 'i4')
              , ('Data', 'i4')
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
              , ('ItemID', 'i4')
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
              , ('skillID', 'i4')
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
              , ('skillID', 'i4')
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
class c_ReqExSetPledgeCrestLarge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x11\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Crest', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#D012
class c_ReqPledgeSetAcademyMaster():
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
class c_ReqPledgePowerGradeList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x13\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D014
class c_ReqPledgeMemberPowerInfo():
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
              , ('U', 'i4')
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
class c_ReqPledgeSetMemberPowerGrade():
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
              , ('U', 'i4')
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
              , ('U', 'i4')
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
              , ('str', '|S'+str(self.It.__next__()) )
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
              , ('U', 'i4')
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
#--------------------------------------------------------------------------#D020
class c_MoveToLocationInAirShip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x20\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('shipID', 'i4')
              , ('x', 'i4')
              , ('y', 'i4')
              , ('z', 'i4')
              , ('origX', 'i4')
              , ('origY', 'i4')
              , ('origZ', 'i4')
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
#--------------------------------------------------------------------------#D022
class c_RequestSaveKeyMapping():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x22\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('U_0', 'i4')
              , ('U_1', 'i4')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('cmd1szValue', 'i1')
                  ]+ list(self.f_cmd1sz()) +[
                  ])
      yield dtype 
  def f_cmd1sz(self):
    for i in range(self.It.__next__()):
      dtype = ('cmd1sz_' + str(i) , [
               ('cmdID', 'i1')
              , ('cmd2szValue', 'i1')
                  ]+ list(self.f_cmd2sz()) +[
                  ])
      yield dtype 
  def f_cmd2sz(self):
    for i in range(self.It.__next__()):
      dtype = ('cmd2sz_' + str(i) , [
               ('cmdID', 'i1')
              , ('cmdSzValue', 'i4')
                  ]+ list(self.f_cmdSz()) +[
                  ])
      yield dtype 
  def f_cmdSz(self):
    for i in range(self.It.__next__()):
      dtype = ('cmdSz_' + str(i) , [
               ('cmd', 'i4')
              , ('key', 'i4')
              , ('tgK1', 'i4')
              , ('tgK2', 'i4')
              , ('show', 'i4')
              , ('U_0', 'i4')
              , ('U_1', 'i4')
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
      count = self.lst[i]
      if count > 100: raise Exception('PacketError')
      yield count
#--------------------------------------------------------------------------#D023
class c_ReqExRemoveItemAttribute():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x23\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ObjID', 'i4')
              , ('element', 'i4')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#D025
class c_ReqExitPartyMatchingWaitingRoom():
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
              , ('GemStoneCount', 'i8')
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
class c_ReqPledgeReorganizeMember():
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
              , ('isSelected', 'i4')
              , ('memberName', '|S'+str(self.It.__next__()) )
              , ('PledgeType', 'i4')
              , ('selectedMember', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D02D
class c_ReqExMPCCShowPartyMembersInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x2D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('partyLeaderID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D02E
class c_RequestOlympiadMatchList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x2E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D02F
class c_RequestAskJoinPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x2F\x00'
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
#--------------------------------------------------------------------------#D030
class c_AnswerJoinPartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x30\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('requesterID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D031
class c_ReqListPartyMatchingWaitingRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x31\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('page', 'i4')
              , ('minlvl', 'i4')
              , ('maxlvl', 'i4')
              , ('mode', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D032
class c_ReqExEnchantSkillSafe():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x32\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('skillID', 'i4')
              , ('SkillLvl', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D033
class c_ReqExEnchantSkillUntrain():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x33\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('skillID', 'i4')
              , ('SkillLvl', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D034
class c_ReqExEnchantSkillRouteChange():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x34\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('skillID', 'i4')
              , ('SkillLvl', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D035
class c_ReqExEnchantItemAttribute():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x35\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ObjID', 'i4')
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
#--------------------------------------------------------------------------#D038
class c_MoveToLocationAirShip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x38\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('command', 'i4')
              , ('param1', 'i4')
              , ('param2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D039
class c_RequestBidItemAuction():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x39\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('instanceID', 'i4')
              , ('bid', 'i8')
                  ]
    return dtype
#--------------------------------------------------------------------------#D03A
class c_RequestInfoItemAuction():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x3A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('instanceID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D03B
class c_RequestExChangeName():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x3B\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('type', 'i4')
              , ('newName', '|S'+str(self.It.__next__()) )
              , ('charSlot', 'i4')
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
#--------------------------------------------------------------------------#D03C
class c_RequestAllCastleInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x3C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D03D
class c_RequestAllFortressInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x3D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D03E
class c_RequestAllAgitInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x3E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D03F
class c_ReqFortressSiegeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x3F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D040
class c_RequestGetBossRecord():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x40\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('BossID', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D041
class c_RequestRefine():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x41\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('TargetItemOID', 'i4')
              , ('RefinerItemOID', 'i4')
              , ('GemStoneItemOID', 'i4')
              , ('GemStoneCount', 'i8')
                  ]
    return dtype
#--------------------------------------------------------------------------#D042
class c_ReqConfirmCancelItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x42\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ObjID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D043
class c_RequestRefineCancel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x43\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('TargetItemOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D044
class c_ReqExMagicSkillUseGround():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x44\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('skillID', 'i4')
              , ('CtrlPressed', 'i4')
              , ('ShiftPressed', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#D045
class c_RequestDuelSurrender():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x45\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D046
class c_ReqExEnchantSkillInfoDetail():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x46\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Type', 'i4')
              , ('skillID', 'i4')
              , ('SkillLvl', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D047
class c_ReqExMagicSkillUseGround():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x47\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('skillID', 'i4')
              , ('CtrlPressed', 'i4')
              , ('ShiftPressed', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#D048
class c_RequestFortressMapInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x48\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('fortressID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D049
class c_RequestPVPMatchRecord():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x49\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D04A
class c_SetPrivateStoreWholeMsg():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x4A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Msg', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D04B
class c_RequestDispel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x4B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('PlayerOID', 'i4')
              , ('skillID', 'i4')
              , ('SkillLvl', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D04C
class c_ReqExTryToPutEnchantTargetItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x4C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ObjID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D04D
class c_ReqExTryToPutEnchantSupportItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x4D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('supportOID', 'i4')
              , ('enchantOID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D04E
class c_ReqExCancelEnchantItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x4E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D04F
class c_ReqChangeNicknameColor():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x4F\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('colorNum', 'i4')
              , ('title', '|S'+str(self.It.__next__()) )
              , ('itemOID', 'i4')
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
#--------------------------------------------------------------------------#D050
class c_ReqResetNickname():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x50\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D051
class c_RequestExCancelEnchantItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x51\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D052
class c_ReqWithDrawPremiumItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x52\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('itemNum', 'i4')
              , ('charID', 'i4')
              , ('itemCount', 'i8')
                  ]
    return dtype
#--------------------------------------------------------------------------#D053
class c_RequestResetNickname():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x53\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D057
class c_ReqJoinDominionWar():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x57\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('territoryID', 'i4')
              , ('isClan', 'i4')
              , ('isJoining', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D058
class c_ReqDominionInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x58\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D05A
class c_ReqExCubeGameChangeTeam():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x5A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('arena', 'i4')
              , ('team', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D05B
class c_EndScenePlayer():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x5B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('movieID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D05C
class c_ReqExCubeGameReadyAnswer():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x5C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('arena', 'i4')
              , ('answer', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D063
class c_RequestSeedPhase():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x63\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D065
class c_RequestPostItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x65\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D066
class c_RequestSendPost():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x66\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('receiver', '|S'+str(self.It.__next__()) )
              , ('isCod', 'i4')
              , ('subj', '|S'+str(self.It.__next__()) )
              , ('text', '|S'+str(self.It.__next__()) )
              , ('attachCountValue', 'i4')
                  ]+ list(self.f_attachCount()) +[
               ('reqAdena', 'i8')
                  ]
    return dtype
  def f_attachCount(self):
    for i in range(self.It.__next__()):
      dtype = ('attachCount_' + str(i) , [
               ('ObjID', 'i4')
              , ('count', 'i8')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
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
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 2
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#D067
class c_ReqReceivedPostList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x67\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D068
class c_ReqDeleteReceivedPost():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x68\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('msgID', 'i4')
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
#--------------------------------------------------------------------------#D069
class c_RequestReceivedPost():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x69\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('msgID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D06A
class c_RequestPostAttachment():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x6A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('msgID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D06B
class c_ReqRejectPostAttachment():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x6B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('msgID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D06C
class c_RequestSentPostList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x6C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D06D
class c_RequestDeleteSentPost():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x6D\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('msgID', 'i4')
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
#--------------------------------------------------------------------------#D06E
class c_RequestSentPost():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x6E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('msgID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D06F
class c_RequestCancelPost():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x6F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('msgID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D075
class c_RequestRefundItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x75\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('listID', 'i4')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('items', 'i4')
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
#--------------------------------------------------------------------------#D076
class c_RequestBuySellUIClose():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x76\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D078
class c_ReqPartyLootModification():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x78\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('mode', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D079
class c_AnswerPartyLootModification():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x79\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('answer', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D07A
class c_AnswerCoupleAction():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x7A\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('actionID', 'i4')
              , ('answer', 'i4')
              , ('objID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D07B
class c_BrEventRankerList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x7B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('eventID', 'i4')
              , ('day', 'i4')
              , ('ranking', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D07C
class c_AskMembership():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x7C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D07D
class c_ReqAddExpandQuestAlarm():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x7D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D07E
class c_RequestVoteNew():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x7E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D07F
class c_RequestBRGamePoint():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x7F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D080
class c_RequestBRProductList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x80\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D081
class c_RequestBRProductInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x81\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D082
class c_RequestBRBuyProduct():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x82\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D083
class c_RequestBRRecentProductList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x83\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D084
class c_BrMinigameLoadScores():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x84\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D085
class c_BrMinigameInsertScore():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x85\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D086
class c_BrLectureMark():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xD0\x86\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D05100
class c_RequestBookMarkSlotInfo():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D05101
class c_RequestSaveBookMarkSlot():
  def __init__(self):
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
              , ('icon', 'i4')
              , ('tag', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 4
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 2
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#D05102
class c_RequestModifyBookMarkSlot():
  def __init__(self):
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('markID', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('icon', 'i4')
              , ('tag', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#D05103
class c_RequestDeleteBookMarkSlot():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('markID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D05104
class c_RequestTeleportBookMark():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('markID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#D05105
class c_RequestChangeBookMarkSlot():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#D05A00
class c_ReqExCubeGameChangeTeam():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('team', 'i4')
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
              , ('ItemID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Stackable', 'i4')
              , ('Count', 'i8')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
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
              , ('Money', 'i8')
              , ('Lease', 'i4')
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ItemType1', 'i2')
              , ('ObjID', 'i4')
              , ('ItemID', 'i4')
              , ('Count', 'i8')
              , ('ItemType2', 'i2')
              , ('0_0', 'i2')
              , ('ItemBodyPart', 'i4')
              , ('enchLvl', 'i2')
              , ('0_1', 'i2')
              , ('custType2', 'i2')
              , ('ReferencePrice2', 'i8')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('EnchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
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
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
              , ('money', 'i8')
              , ('buyListID', 'i4')
              , ('buyListSizeValue', 'i2')
                  ]+ list(self.f_buyListSize()) +[
                  ]
    return dtype
  def f_buyListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('buyListSize_' + str(i) , [
               ('itemID_0', 'i4')
              , ('itemID_1', 'i4')
              , ('0', 'i4')
              , ('curCount', 'i8')
              , ('type2', 'i2')
              , ('type1', 'i2')
              , ('isEquip', 'i2')
              , ('bodyPart', 'i4')
              , ('enchLvl', 'i2')
              , ('custType', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('ElementType', 'i2')
              , ('ElementPower', 'i2')
              , ('Fire', 'i2')
              , ('Water', 'i2')
              , ('Wind', 'i2')
              , ('Earth', 'i2')
              , ('Holy', 'i2')
              , ('Unholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('pricetaxRate', 'i8')
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
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
class s_CharSelectInfo():
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
              , ('CountValue', 'i4')
              , ('07', 'i4')
              , ('0', 'i1')
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
              , ('0_0', 'i4')
              , ('Sex', 'i4')
              , ('Race', 'i4')
              , ('ClassID_0', 'i4')
              , ('active', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('curHP', 'f8')
              , ('curMP', 'f8')
              , ('SP', 'i4')
              , ('Exp', 'i8')
              , ('Level', 'i4')
              , ('karma', 'i4')
              , ('pkKills', 'i4')
              , ('pvpKills', 'i4')
              , ('0028d7', 'i4')
              , ('Unde', 'i4')
              , ('REar', 'i4')
              , ('LEar', 'i4')
              , ('Neck', 'i4')
              , ('RRing', 'i4')
              , ('LRing', 'i4')
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
              , ('Hair2', 'i4')
              , ('RBrace', 'i4')
              , ('LBrace', 'i4')
              , ('DEC1', 'i4')
              , ('DEC2', 'i4')
              , ('DEC3', 'i4')
              , ('DEC4', 'i4')
              , ('DEC5', 'i4')
              , ('DEC6', 'i4')
              , ('Belt', 'i4')
              , ('HairStyle', 'i4')
              , ('HairColor', 'i4')
              , ('Face', 'i4')
              , ('max_HP', 'f8')
              , ('max_MP', 'f8')
              , ('DELDays', 'i4')
              , ('ClassID_1', 'i4')
              , ('autoSel', 'i4')
              , ('EnchantEffect', 'i1')
              , ('Augm', 'i4')
              , ('Transform', 'i4')
              , ('tameNpc', 'i4')
              , ('lvl', 'i4')
              , ('0_1', 'i4')
              , ('food', 'i4')
              , ('maxHp', 'f8')
              , ('curHp', 'f8')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
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
      i += 273
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
              , ('reason', 'i4')
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
              , ('ClassID_0', 'i4')
              , ('active', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('curHP', 'f8')
              , ('curMP', 'f8')
              , ('SP', 'i4')
              , ('EXP', 'i8')
              , ('Level', 'i4')
              , ('karma', 'i4')
              , ('pkKills', 'i4')
              , ('INT', 'i4')
              , ('STR', 'i4')
              , ('CON', 'i4')
              , ('MEN', 'i4')
              , ('DEX', 'i4')
              , ('WIT', 'i4')
              , ('gameTime', 'i4')
              , ('0_1', 'i4')
              , ('ClassID_1', 'i4')
              , ('0016', 'i4')
              , ('0064', 'i4')
              , ('0_2', 'i4')
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
              , ('ObjID', 'i4')
              , ('NpcId', 'i4')
              , ('IsAttackable', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('0_0', 'i4')
              , ('CastSpd', 'i4')
              , ('AtkSpd', 'i4')
              , ('RunSpd', 'i4')
              , ('WalkSpd', 'i4')
              , ('SwimRunSpd', 'i4')
              , ('SwimWalkSpd', 'i4')
              , ('FlRunSpd', 'i4')
              , ('FlWalkSpd', 'i4')
              , ('FlyRunSpd', 'i4')
              , ('FlyWalkSpd', 'i4')
              , ('MoveMult', 'f8')
              , ('ASpdMult', 'f8')
              , ('CollisionRadius_0', 'f8')
              , ('CollisionHeight_0', 'f8')
              , ('RHand', 'i4')
              , ('Chest', 'i4')
              , ('LHand', 'i4')
              , ('nameabove', 'i1')
              , ('isRunning', 'i1')
              , ('isInCombat', 'i1')
              , ('isALikeDead', 'i1')
              , ('isSummoned', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('TitleColor', 'i4')
              , ('pvpFlag', 'i4')
              , ('Karma', 'i4')
              , ('AbnormalEffect', 'i4')
              , ('clanID', 'i4')
              , ('crestID', 'i4')
              , ('allyID', 'i4')
              , ('allyCrest', 'i4')
              , ('isFlying_0', 'i1')
              , ('Team', 'i1')
              , ('CollisionRadius_1', 'f8')
              , ('CollisionHeight_1', 'f8')
              , ('enchEffects', 'i4')
              , ('isFlying_1', 'i4')
              , ('0_1', 'i4')
              , ('form', 'i4')
              , ('isShowName_0', 'i1')
              , ('isShowName_1', 'i1')
              , ('SpecEffects', 'i4')
              , ('dispEffect', 'i4')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('Race', 'i4')
              , ('ClassID', 'i4')
              , ('46_0', 'i4')
              , ('BaseSTR', 'i4')
              , ('0a_0', 'i4')
              , ('46_1', 'i4')
              , ('BaseDEX', 'i4')
              , ('0a_1', 'i4')
              , ('46_2', 'i4')
              , ('BaseCON', 'i4')
              , ('0a_2', 'i4')
              , ('46_3', 'i4')
              , ('BaseINT', 'i4')
              , ('0a_3', 'i4')
              , ('46_4', 'i4')
              , ('BaseWIT', 'i4')
              , ('0a_4', 'i4')
              , ('46_5', 'i4')
              , ('BaseMEN', 'i4')
              , ('0a_5', 'i4')
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
#--------------------------------------------------------------------------#0F
class s_CharCreateOk():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x0F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('01', 'i4')
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
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
               ('blockedItemsValue', 'i2')
              , ('blockMode', 'i1')
                  ]+ list(self.f_blockedItems()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('LocationSlot', 'i4')
              , ('Count', 'i8')
              , ('ItemType2', 'i2')
              , ('CustomType1', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('CustType2', 'i2')
              , ('AugmentID', 'i4')
              , ('Mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemVal', 'i2')
              , ('DefAttrFire', 'i2')
              , ('DefAttrWater', 'i2')
              , ('DefAttrWind', 'i2')
              , ('DefAttrEarth', 'i2')
              , ('DefAttrHoly', 'i2')
              , ('DefAttrUnholy', 'i2')
              , ('EnchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
                  ])
      yield dtype 
  def f_blockedItems(self):
    for i in range(self.It.__next__()):
      dtype = ('blockedItems_' + str(i) , [
               ('blockItem', 'i4')
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
      i += 68
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
      i += 24
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
              , ('ObjID', 'i4')
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquip', 'i2')
              , ('BodyPart', 'i4')
              , ('enchantLvl', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
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
#--------------------------------------------------------------------------#16
class s_DropItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x16'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('PlayerID', 'i4')
              , ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Stackable', 'i4')
              , ('Count', 'i8')
              , ('U', 'i4')
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
              , ('objID', 'i4')
              , ('HTML', '|S'+str(self.It.__next__()) )
              , ('itemID', 'i4')
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
               ('ItemType1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Count', 'i8')
              , ('ItemType2', 'i2')
              , ('custType1', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('0', 'i2')
              , ('custType2', 'i2')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('EnchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
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
#--------------------------------------------------------------------------#1B
class s_TradeOtherAdd():
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
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ItemType1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Count', 'i8')
              , ('ItemType2', 'i2')
              , ('custType1', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('0', 'i2')
              , ('custType2', 'i2')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('EnchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
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
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('1add2mod3remove', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count', 'i8')
              , ('ItemType2', 'i2')
              , ('CustomType1', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('CustType2', 'i2')
              , ('AugmID', 'i4')
              , ('Mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemVal', 'i2')
              , ('DefAttrFire', 'i2')
              , ('DefAttrWater', 'i2')
              , ('DefAttrWind', 'i2')
              , ('DefAttrEarth', 'i2')
              , ('DefAttrHoly', 'i2')
              , ('DefAttrUnholy', 'i2')
              , ('EnchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
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
class s_TeleportToLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x22'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('TargetID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('0', 'i4')
              , ('heading', 'i4')
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
              , ('PlayerID', 'i4')
              , ('Action', 'i4')
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
              , ('U_0', 'i4')
              , ('U_1', 'i4')
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
              , ('subPledgeName_0', '|S'+str(self.It.__next__()) )
              , ('pledgeType', 'i4')
              , ('subPledgeName_1', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 4
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 4
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 2
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
class s_KeyInit():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2E'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('isOk', 'i1')
              , ('KeyL', 'i8')
              , ('KeyH', 'i8')
              , ('c', 'i1')
              , ('seed', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#2F
class s_MoveToLocation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x2F'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('DestX', 'i4')
              , ('DestY', 'i4')
              , ('DestZ', 'i4')
              , ('CurX', 'i4')
              , ('CurY', 'i4')
              , ('CurZ', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#30
class s_NpcSay():
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
              , ('textType', 'i4')
              , ('NpcID', 'i4')
              , ('msgType', 'i4')
              , ('Msg', '|S'+str(self.It.__next__()) )
              , ('pMsg', '|S'+str(self.It.__next__()) )
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
   i += 4
   s_len = len(self.lst[i])
   yield s_len
   i += 1
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
              , ('ClassID', 'i4')
              , ('Under', 'i4')
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
              , ('Hair2', 'i4')
              , ('RBrace', 'i4')
              , ('LBrace', 'i4')
              , ('DEC1', 'i4')
              , ('DEC2', 'i4')
              , ('DEC3', 'i4')
              , ('DEC4', 'i4')
              , ('DEC5', 'i4')
              , ('DEC6', 'i4')
              , ('Belt', 'i4')
              , ('AUnder', 'i4')
              , ('AHead', 'i4')
              , ('ARHand', 'i4')
              , ('ALHand', 'i4')
              , ('AGloves', 'i4')
              , ('AChest', 'i4')
              , ('ALegs', 'i4')
              , ('AFeet', 'i4')
              , ('ABack', 'i4')
              , ('ALRHand', 'i4')
              , ('AHair', 'i4')
              , ('AHair2', 'i4')
              , ('ARBrace', 'i4')
              , ('ALBrace', 'i4')
              , ('ADEC1', 'i4')
              , ('ADEC2', 'i4')
              , ('ADEC3', 'i4')
              , ('ADEC4', 'i4')
              , ('ADEC5', 'i4')
              , ('ADEC6', 'i4')
              , ('ABelt', 'i4')
              , ('0_0', 'i4')
              , ('1', 'i4')
              , ('pvpFlag', 'i4')
              , ('karma', 'i4')
              , ('CastSpd', 'i4')
              , ('AtkSpd', 'i4')
              , ('0_1', 'i4')
              , ('runSpd', 'i4')
              , ('walkSpd', 'i4')
              , ('swimRSpd', 'i4')
              , ('swimWSpd', 'i4')
              , ('flRunSpd', 'i4')
              , ('flWalkSpd', 'i4')
              , ('flyRunSpd', 'i4')
              , ('flyWalkSpd', 'i4')
              , ('SpdMult', 'f8')
              , ('ASpdMult', 'f8')
              , ('collisRadius', 'f8')
              , ('collisHeight', 'f8')
              , ('HairStyle', 'i4')
              , ('HairColor', 'i4')
              , ('Face', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('clanID', 'i4')
              , ('clanCrestID', 'i4')
              , ('allyID', 'i4')
              , ('allyCrestID', 'i4')
              , ('isStand', 'i1')
              , ('isRun', 'i1')
              , ('isInFight', 'i1')
              , ('isAlikeDead', 'i1')
              , ('Invis', 'i1')
              , ('mountType', 'i1')
              , ('isShop', 'i1')
              , ('cubicsValue', 'i2')
                  ]+ list(self.f_cubics()) +[
               ('findparty', 'i1')
              , ('abnEffects', 'i4')
              , ('isFlying', 'i1')
              , ('RecomHave', 'i2')
              , ('MountNpcID', 'i4')
              , ('classID', 'i4')
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
              , ('heading', 'i4')
              , ('PledgeClass', 'i4')
              , ('PledgeType', 'i4')
              , ('TitleColor', 'i4')
              , ('CursedItem', 'i4')
              , ('ClanRep', 'i4')
              , ('TransformID', 'i4')
              , ('AgathionID', 'i4')
              , ('Fame', 'i4')
              , ('specEffects', 'i4')
              , ('0_2', 'i4')
              , ('0_3', 'i4')
              , ('0_4', 'i4')
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
   i += 284
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 23
   p = self.pck[i:i+2]
   count = struct.unpack('h', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 68
   s_len = len(self.lst[i])
   yield s_len
   i += 12
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
              , ('ClassID_0', 'i4')
              , ('Level', 'i4')
              , ('Exp', 'i8')
              , ('Str', 'i4')
              , ('Dex', 'i4')
              , ('Con', 'i4')
              , ('Int', 'i4')
              , ('Wit', 'i4')
              , ('Men', 'i4')
              , ('MaxHP', 'i4')
              , ('CurHP', 'i4')
              , ('MaxMP', 'i4')
              , ('CurMP', 'i4')
              , ('Sp', 'i4')
              , ('CurLoad', 'i4')
              , ('MaxLoad', 'i4')
              , ('isWeapEquip40yes', 'i4')
              , ('Under_0', 'i4')
              , ('REar_0', 'i4')
              , ('LEar_0', 'i4')
              , ('Neck_0', 'i4')
              , ('RRing_0', 'i4')
              , ('LRing_0', 'i4')
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
              , ('Hair2_0', 'i4')
              , ('RBrace_0', 'i4')
              , ('LBrace_0', 'i4')
              , ('DEC1_0', 'i4')
              , ('DEC2_0', 'i4')
              , ('DEC3_0', 'i4')
              , ('DEC4_0', 'i4')
              , ('DEC5_0', 'i4')
              , ('DEC6_0', 'i4')
              , ('Belt_0', 'i4')
              , ('Under_1', 'i4')
              , ('REar_1', 'i4')
              , ('LEar_1', 'i4')
              , ('Neck_1', 'i4')
              , ('RRing_1', 'i4')
              , ('LRing_1', 'i4')
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
              , ('Hair2_1', 'i4')
              , ('RBrace_1', 'i4')
              , ('LBrace_1', 'i4')
              , ('DEC1_1', 'i4')
              , ('DEC2_1', 'i4')
              , ('DEC3_1', 'i4')
              , ('DEC4_1', 'i4')
              , ('DEC5_1', 'i4')
              , ('DEC6_1', 'i4')
              , ('Belt_1', 'i4')
              , ('AUnder', 'i4')
              , ('AREar', 'i4')
              , ('ALEar', 'i4')
              , ('ANeck', 'i4')
              , ('ARRing', 'i4')
              , ('ALRing', 'i4')
              , ('AHead', 'i4')
              , ('ARHand', 'i4')
              , ('ALHand', 'i4')
              , ('AGloves', 'i4')
              , ('AChest', 'i4')
              , ('ALegs', 'i4')
              , ('AFeet', 'i4')
              , ('ABack', 'i4')
              , ('ALRHand', 'i4')
              , ('AHair', 'i4')
              , ('AHair2', 'i4')
              , ('ARBrace', 'i4')
              , ('ALBrace', 'i4')
              , ('ADEC1', 'i4')
              , ('ADEC2', 'i4')
              , ('ADEC3', 'i4')
              , ('ADEC4', 'i4')
              , ('ADEC5', 'i4')
              , ('ADEC6', 'i4')
              , ('ABelt', 'i4')
              , ('talismanSlots', 'i4')
              , ('cloakStatus', 'i4')
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
              , ('mountType', 'i1')
              , ('privateStoreType', 'i1')
              , ('isDwarvenCraft', 'i1')
              , ('pkKills', 'i4')
              , ('pvpKills', 'i4')
              , ('cubicsSizeValue', 'i2')
                  ]+ list(self.f_cubicsSize()) +[
               ('findParty', 'i1')
              , ('abnormalEffect', 'i4')
              , ('isFlyingMounted', 'i1')
              , ('clanPrivs', 'i4')
              , ('recomLeft', 'i2')
              , ('recomHave', 'i2')
              , ('mountNpcID', 'i4')
              , ('inventoryLimit', 'i2')
              , ('ClassID_1', 'i4')
              , ('specEffects_0', 'i4')
              , ('MaxCP', 'i4')
              , ('CurCP', 'i4')
              , ('isMounted', 'i1')
              , ('Team', 'i1')
              , ('clanCrestLargeID', 'i4')
              , ('isNoble', 'i1')
              , ('isHero', 'i1')
              , ('isFishing', 'i1')
              , ('fishX', 'i4')
              , ('fishY', 'i4')
              , ('fishZ', 'i4')
              , ('nameColor', 'i4')
              , ('isRunning', 'i1')
              , ('PledgeClass', 'i4')
              , ('PledgeType', 'i4')
              , ('titleColor', 'i4')
              , ('cursedWeap', 'i4')
              , ('Transformation', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('AgathionId', 'i4')
              , ('Fame', 'i4')
              , ('mmapAllowed', 'i4')
              , ('Vitality', 'i4')
              , ('specEffects_1', 'i4')
                  ]
    return dtype
  def f_cubicsSize(self):
    for i in range(self.It.__next__()):
      dtype = ('cubicsSize_' + str(i) , [
               ('cubicID', 'i2')
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
   if count > 100: raise Exception('PacketError')
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
   if count > 100: raise Exception('PacketError')
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
              , ('AttackerObjID', 'i4')
              , ('TargetObjID', 'i4')
              , ('Damage', 'i4')
              , ('Flags', 'i1')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('HitsLengthValue', 'i2')
                  ]+ list(self.f_HitsLength()) +[
               ('TargetX', 'i4')
              , ('TargetY', 'i4')
              , ('TargetZ', 'i4')
                  ]
    return dtype
  def f_HitsLength(self):
    for i in range(self.It.__next__()):
      dtype = ('HitsLength_' + str(i) , [
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 7
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
              , ('Response', 'i4')
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
              , ('PlayerAdena', 'i8')
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquip', 'i2')
              , ('BodyPart', 'i4')
              , ('enchantLvl', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('ObjId', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 10
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
              , ('WhType', 'i2')
              , ('PlayerAdena', 'i8')
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquip', 'i2')
              , ('BodyPart', 'i4')
              , ('enchantLvl', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('ObjId', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 10
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
              , ('charID', 'i4')
              , ('targetID', 'i4')
              , ('skillID', 'i4')
              , ('skillLvl', 'i4')
              , ('hitTime', 'i4')
              , ('reuseDelay', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('U', 'i4')
              , ('tx', 'i4')
              , ('ty', 'i4')
              , ('tz', 'i4')
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
              , ('CurrentHP', 'i4')
              , ('MaxHP', 'i4')
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
              , ('LeaderOID', 'i4')
              , ('LootDistribution', 'i4')
              , ('memberCountValue', 'i4')
                  ]+ list(self.f_memberCount()) +[
                  ]
    return dtype
  def f_memberCount(self):
    for i in range(self.It.__next__()):
      dtype = ('memberCount_' + str(i) , [
               ('MemberObjId', 'i4')
              , ('MemberName', '|S'+str(self.It.__next__()) )
              , ('CurCP', 'i4')
              , ('MaxCP', 'i4')
              , ('CurHP', 'i4')
              , ('MaxHP', 'i4')
              , ('CurMP', 'i4')
              , ('MaxMP', 'i4')
              , ('Level', 'i4')
              , ('ClassID', 'i4')
              , ('0_0', 'i4')
              , ('Race', 'i4')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
              , ('PetOID', 'i4')
              , ('PetID', 'i4')
              , ('summonType', 'i4')
              , ('PetName', '|S'+str(self.It.__next__()) )
              , ('curHP', 'i4')
              , ('maxHP', 'i4')
              , ('curMP', 'i4')
              , ('maxMP', 'i4')
              , ('lvl', 'i4')
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
      i += 60
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 20
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
      i += 16
      s_len = len(self.lst[i])
      yield s_len
      i += 6
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
              , ('leaderID', 'i4')
              , ('distrib', 'i4')
              , ('memberOID', 'i4')
              , ('memberName', '|S'+str(self.It.__next__()) )
              , ('CurCP', 'i4')
              , ('MaxCP', 'i4')
              , ('CurHP', 'i4')
              , ('MaxHP', 'i4')
              , ('CurMP', 'i4')
              , ('MaxMP', 'i4')
              , ('Level', 'i4')
              , ('ClassID', 'i4')
              , ('U_0', 'i4')
              , ('U_1', 'i4')
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
              , ('ClassID', 'i4')
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
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjectID', 'i4')
              , ('SkillID', 'i4')
              , ('SkillLevel', 'i4')
              , ('HitTimesValue', 'i4')
                  ]+ list(self.f_HitTimes()) +[
               ('SingleTargetID', 'i4')
                  ]
    return dtype
  def f_HitTimes(self):
    for i in range(self.It.__next__()):
      dtype = ('HitTimes_' + str(i) , [
               ('TargetID', 'i4')
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
              , ('hasFortress', 'i4')
              , ('Rank', 'i4')
              , ('ReputationScore', 'i4')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
              , ('AllyID', 'i4')
              , ('AllyName', '|S'+str(self.It.__next__()) )
              , ('AllyCrestID', 'i4')
              , ('isAtWar', 'i4')
              , ('terraCastleID', 'i4')
              , ('SubPledgeMembersCountValue', 'i4')
                  ]+ list(self.f_SubPledgeMembersCount()) +[
                  ]
    return dtype
  def f_SubPledgeMembersCount(self):
    for i in range(self.It.__next__()):
      dtype = ('SubPledgeMembersCount_' + str(i) , [
               ('MemberName', '|S'+str(self.It.__next__()) )
              , ('MemberLevel', 'i4')
              , ('MemberClassID', 'i4')
              , ('Sex', 'i4')
              , ('Race', 'i4')
              , ('onlineObjId', 'i4')
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
   i += 12
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
   i += 11
   s_len = len(self.lst[i])
   yield s_len
   i += 4
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
              , ('ClassID', 'i4')
              , ('Sex', 'i4')
              , ('Race', 'i4')
              , ('onlineObjID', 'i4')
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
              , ('ClassID', 'i4')
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
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('isPassive', 'i4')
              , ('Level', 'i4')
              , ('SkillID', 'i4')
              , ('isDisabled', 'i1')
              , ('enchanted', 'i1')
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
              , ('speed', 'i4')
              , ('0', 'i1')
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
              , ('CrestData', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#6B
class s_SetupGauge():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x6B'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CharObjID', 'i4')
              , ('Dat1', 'i4')
              , ('Time', 'i4')
              , ('Time2', 'i4')
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
              , ('isOk', 'i4')
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
              , ('charID', 'i4')
              , ('targetId', 'i4')
              , ('distance', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('tX', 'i4')
              , ('tY', 'i4')
              , ('tZ', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#73
class s_SSQInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x73'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Sky', 'i2')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('FriendID', 'i4')
              , ('FriendName', '|S'+str(self.It.__next__()) )
              , ('isOnLine', 'i4')
              , ('onlineObjID', 'i4')
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
#--------------------------------------------------------------------------#76
class s_FriendPacket():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x76'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('action1add3rem', 'i4')
              , ('objID', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('isOnline', 'i4')
              , ('onlineObjID', 'i4')
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
#--------------------------------------------------------------------------#77
class s_FriendStatusPacket():
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
              , ('isOnline', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('objID', 'i4')
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
              , ('speed', 'i4')
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
              , ('show', 'i1')
              , ('bbshome', '|S'+str(self.It.__next__()) )
              , ('bbsgetfav', '|S'+str(self.It.__next__()) )
              , ('bbsloc', '|S'+str(self.It.__next__()) )
              , ('bbsclan', '|S'+str(self.It.__next__()) )
              , ('bbsmemo', '|S'+str(self.It.__next__()) )
              , ('bbsmail', '|S'+str(self.It.__next__()) )
              , ('bbsfriends', '|S'+str(self.It.__next__()) )
              , ('bbs_add_fav', '|S'+str(self.It.__next__()) )
              , ('curPage', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#7C
class s_ChooseInventoryItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x7C'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ItemID', 'i4')
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
              , ('ObjID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#82
class s_TradeOtherDone():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x82'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
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
class s_MagicEffectIcons():
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
              , ('ListCountValue', 'i2')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('skillID', 'i4')
              , ('SkillLevel', 'i2')
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
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
               ('0128', 'i4')
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('QuestId', 'i4')
              , ('Cond', 'i4')
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
#--------------------------------------------------------------------------#87
class s_EnchantResult():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x87'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Result', 'i4')
              , ('crystal', 'i4')
              , ('count', 'i8')
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
              , ('clanID', 'i4')
              , ('crestID', 'i4')
              , ('clanLevel', 'i4')
              , ('hasCastle', 'i4')
              , ('hasHideOut', 'i4')
              , ('hasFort', 'i4')
              , ('Rank', 'i4')
              , ('ReputationScore', 'i4')
              , ('U_0', 'i4')
              , ('U_1', 'i4')
              , ('allyID', 'i4')
              , ('allyName', '|S'+str(self.It.__next__()) )
              , ('allyCrestID', 'i4')
              , ('hasWar', 'i4')
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
              , ('skillID', 'i4')
              , ('Level', 'i4')
              , ('SpCost', 'i4')
              , ('Mode', 'i4')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('Type', 'i4')
              , ('ItemID', 'i4')
              , ('Count', 'i8')
              , ('Requirements', 'i4')
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
#--------------------------------------------------------------------------#92
class s_ServerObjectInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x92'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('charOID', 'i4')
              , ('ID', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('isAttackable', 'i4')
              , ('x', 'i4')
              , ('y', 'i4')
              , ('z', 'i4')
              , ('heading', 'i4')
              , ('moveMult', 'f8')
              , ('ASpdMult', 'f8')
              , ('collisionRad', 'f8')
              , ('collisionHeight', 'f8')
              , ('curHP', 'i4')
              , ('maxHP', 'i4')
              , ('objType', 'i4')
              , ('SpecEffects', 'i4')
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
#--------------------------------------------------------------------------#93
class s_GMHide():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x93'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('mode', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#94
class s_AcquireSkillDone():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\x94'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
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
              , ('ClassID_0', 'i4')
              , ('Level', 'i4')
              , ('Exp', 'i8')
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
              , ('PkKills', 'i4')
              , ('Under_0', 'i4')
              , ('REar_0', 'i4')
              , ('LEar_0', 'i4')
              , ('Neck_0', 'i4')
              , ('RRing_0', 'i4')
              , ('LRing_0', 'i4')
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
              , ('Hair2_0', 'i4')
              , ('RBrace_0', 'i4')
              , ('LBrace_0', 'i4')
              , ('DEC1_0', 'i4')
              , ('DEC2_0', 'i4')
              , ('DEC3_0', 'i4')
              , ('DEC4_0', 'i4')
              , ('DEC5_0', 'i4')
              , ('DEC6_0', 'i4')
              , ('Belt_0', 'i4')
              , ('Under_1', 'i4')
              , ('REar_1', 'i4')
              , ('LEar_1', 'i4')
              , ('Neck_1', 'i4')
              , ('RRing_1', 'i4')
              , ('LRing_1', 'i4')
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
              , ('Hair2_1', 'i4')
              , ('RBrace_1', 'i4')
              , ('LBrace_1', 'i4')
              , ('DEC1_1', 'i4')
              , ('DEC2_1', 'i4')
              , ('DEC3_1', 'i4')
              , ('DEC4_1', 'i4')
              , ('DEC5_1', 'i4')
              , ('DEC6_1', 'i4')
              , ('Belt_1', 'i4')
              , ('AUnder', 'i4')
              , ('AREar', 'i4')
              , ('ALEar', 'i4')
              , ('ANeck', 'i4')
              , ('ARRing', 'i4')
              , ('ALRing', 'i4')
              , ('AHead', 'i4')
              , ('ARHand', 'i4')
              , ('ALHand', 'i4')
              , ('AGloves', 'i4')
              , ('AChest', 'i4')
              , ('ALegs', 'i4')
              , ('AFeet', 'i4')
              , ('ABack', 'i4')
              , ('ALRHand', 'i4')
              , ('AHair', 'i4')
              , ('AHair2', 'i4')
              , ('ARBrace', 'i4')
              , ('ALBrace', 'i4')
              , ('ADEC1', 'i4')
              , ('ADEC2', 'i4')
              , ('ADEC3', 'i4')
              , ('ADEC4', 'i4')
              , ('ADEC5', 'i4')
              , ('ADEC6', 'i4')
              , ('ABelt', 'i4')
              , ('talismanSlots', 'i4')
              , ('cloakStatus', 'i4')
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
              , ('MoveMult', 'f8')
              , ('ASpdMult', 'f8')
              , ('CollisionRadius', 'f8')
              , ('CollisionHeight', 'f8')
              , ('HairStyle', 'i4')
              , ('HairColor', 'i4')
              , ('Face', 'i4')
              , ('isGM', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('ClanID', 'i4')
              , ('ClanCrestID', 'i4')
              , ('AllyID', 'i4')
              , ('MounType', 'i1')
              , ('PrivateStoreType', 'i1')
              , ('isDwarvenCraft', 'i1')
              , ('pkKills', 'i4')
              , ('pvpKills', 'i4')
              , ('RecomLeft', 'i2')
              , ('RecomHave', 'i2')
              , ('ClassID_1', 'i4')
              , ('SpecEffects', 'i4')
              , ('MaxCP', 'i4')
              , ('CurrCP', 'i4')
              , ('isRunning', 'i1')
              , ('321', 'i1')
              , ('PledgeClass', 'i4')
              , ('isNoble', 'i1')
              , ('isHero', 'i1')
              , ('NameColor', 'i4')
              , ('TitleColor', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('Fame', 'i4')
              , ('Vitality', 'i4')
                  ]
    return dtype
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
  def parse_list(self):
   i = 1
   i += 5
   s_len = len(self.lst[i])
   yield s_len
   i += 128
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
              , ('hasFortress', 'i4')
              , ('Rank', 'i4')
              , ('ReputationScore', 'i4')
              , ('0_1', 'i4')
              , ('0_2', 'i4')
              , ('AllyID', 'i4')
              , ('AllyName', '|S'+str(self.It.__next__()) )
              , ('AllyCrestID', 'i4')
              , ('isAtWar', 'i4')
              , ('U', 'i4')
              , ('MembersCountValue', 'i4')
                  ]+ list(self.f_MembersCount()) +[
                  ]
    return dtype
  def f_MembersCount(self):
    for i in range(self.It.__next__()):
      dtype = ('MembersCount_' + str(i) , [
               ('MemberName', '|S'+str(self.It.__next__()) )
              , ('MemberLevel', 'i4')
              , ('ClassID', 'i4')
              , ('Sex', 'i4')
              , ('Race', 'i4')
              , ('onlineObjID', 'i4')
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
   i += 12
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
   i += 4
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('isPassive', 'i4')
              , ('SkillLevel', 'i4')
              , ('skillID', 'i4')
              , ('isDisabled', 'i1')
              , ('isEnchantable', 'i1')
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
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
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
              , ('shown', 'i2')
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('LocationSlot', 'i4')
              , ('Count', 'i8')
              , ('Type2', 'i2')
              , ('CustomType1', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('CustomType2', 'i2')
              , ('AugmentID', 'i4')
              , ('Mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemVal', 'i2')
              , ('DefAttrFire', 'i2')
              , ('DefAttrWater', 'i2')
              , ('DefAttrWind', 'i2')
              , ('DefAttrEarth', 'i2')
              , ('DefAttrHoly', 'i2')
              , ('DefAttrUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
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
              , ('Money', 'i8')
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count', 'i8')
              , ('Type2', 'i2')
              , ('CustomType1', 'i2')
              , ('isEquip', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('custType2', 'i2')
              , ('AugmentID', 'i4')
              , ('Mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemVal', 'i2')
              , ('DefAttrFire', 'i2')
              , ('DefAttrWater', 'i2')
              , ('DefAttrWind', 'i2')
              , ('DefAttrEarth', 'i2')
              , ('DefAttrHoly', 'i2')
              , ('DefAttrUnholy', 'i2')
              , ('EnchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('ObjID', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 8
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
#--------------------------------------------------------------------------#9C
class s_ListPartyWating():
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
              , ('isSize', 'i4')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjID', 'i4')
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('location', 'i4')
              , ('minLvl', 'i4')
              , ('maxLvl', 'i4')
              , ('members', 'i4')
              , ('maxMembers', 'i4')
              , ('ownerName', '|S'+str(self.It.__next__()) )
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
   i += 4
   for _ in range(count):
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 20
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
      i += 6
      s_len = len(self.lst[i])
      yield s_len
      i += 1
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
              , ('roomID', 'i4')
              , ('maxMembers', 'i4')
              , ('minLvl', 'i4')
              , ('maxLvl', 'i4')
              , ('lootType', 'i4')
              , ('location', 'i4')
              , ('roomTitle', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 24
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 6
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
              , ('type_0', 'i4')
              , ('SoundFile', '|S'+str(self.It.__next__()) )
              , ('type_1', 'i4')
              , ('shipID', 'i4')
              , ('x', 'i4')
              , ('y', 'i4')
              , ('z', 'i4')
              , ('U', 'i4')
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
              , ('CurrentHP', 'i4')
              , ('MaxHP', 'i4')
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
              , ('ObjID', 'i4')
              , ('isPackage', 'i4')
              , ('Money', 'i8')
              , ('tradeListValue', 'i4')
                  ]+ list(self.f_tradeList()) +[
               ('sellListValue', 'i4')
                  ]+ list(self.f_sellList()) +[
                  ]
    return dtype
  def f_tradeList(self):
    for i in range(self.It.__next__()):
      dtype = ('tradeList_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquip', 'i2')
              , ('BodyPart', 'i4')
              , ('enchantLvl', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('refPrice', 'i8')
                  ])
      yield dtype 
  def f_sellList(self):
    for i in range(self.It.__next__()):
      dtype = ('sellList_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquip', 'i2')
              , ('BodyPart', 'i4')
              , ('enchantLvl', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('price', 'i8')
              , ('refPrice', 'i8')
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
   i += 4
   for _ in range(count):
      i += 76
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
      i += 25
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
              , ('Money', 'i8')
              , ('ItemsCountValue', 'i4')
                  ]+ list(self.f_ItemsCount()) +[
                  ]
    return dtype
  def f_ItemsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemsCount_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('0', 'i2')
              , ('BodyPart', 'i4')
              , ('enchantLvl', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('price', 'i8')
              , ('refPrice', 'i8')
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
   i += 3
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
              , ('SevenSignsPeriod', 'i1')
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
#--------------------------------------------------------------------------#A7
class s_TutorialShowQuestionMark():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Blink', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A8
class s_TutorialEnableClientEvent():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA8'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('eventId', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#A9
class s_TutorialClose():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xA9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#AF
class s_AllyCrest():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xAF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('CrestID', 'i4')
              , ('CrestAlly', 'i1')
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
              , ('isAttackable', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('0_0', 'i4')
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
              , ('MoveMult', 'f8')
              , ('ASpdMult', 'f8')
              , ('CollisionRadius', 'f8')
              , ('CollisionHeight', 'f8')
              , ('Rhand', 'i4')
              , ('Body', 'i4')
              , ('LHand', 'i4')
              , ('nameAbove', 'i1')
              , ('isRunning', 'i1')
              , ('isInCombat', 'i1')
              , ('isAlikeDead', 'i1')
              , ('isSummoned', 'i1')
              , ('Name', '|S'+str(self.It.__next__()) )
              , ('Title', '|S'+str(self.It.__next__()) )
              , ('1', 'i4')
              , ('PvpFlag', 'i4')
              , ('Karma', 'i4')
              , ('CurrFed', 'i4')
              , ('MaxFed', 'i4')
              , ('CurrHP', 'i4')
              , ('MaxHP', 'i4')
              , ('CurrMP', 'i4')
              , ('MaxMP', 'i4')
              , ('SP', 'i4')
              , ('Level', 'i4')
              , ('Exp', 'i8')
              , ('ExpForThisLevel', 'i8')
              , ('ExpForNextLevel', 'i8')
              , ('CurrLoad', 'i4')
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
              , ('abnormalEffects', 'i4')
              , ('isRide', 'i2')
              , ('0_1', 'i1')
              , ('0_2', 'i2')
              , ('Team', 'i1')
              , ('SoulShotsPerHit', 'i4')
              , ('SpiritShotsPerHit', 'i4')
              , ('form', 'i4')
              , ('specEffect', 'i4')
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
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count', 'i8')
              , ('Type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('Enchant', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
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
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('Change', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count', 'i8')
              , ('Type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('Enchant', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
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
              , ('CountValue', 'i4')
                  ]+ list(self.f_Count()) +[
                  ]
    return dtype
  def f_Count(self):
    for i in range(self.It.__next__()):
      dtype = ('Count_' + str(i) , [
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
#--------------------------------------------------------------------------#BD
class s_PrivateStoreManageListBuy():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xBD'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('ObjID', 'i4')
              , ('Money', 'i8')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
               ('buyListValue', 'i4')
                  ]+ list(self.f_buyList()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquip', 'i2')
              , ('BodyPart', 'i4')
              , ('enchantLvl', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('refPrice', 'i8')
                  ])
      yield dtype 
  def f_buyList(self):
    for i in range(self.It.__next__()):
      dtype = ('buyList_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count_0', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquip', 'i2')
              , ('BodyPart', 'i4')
              , ('enchantLvl', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('price', 'i8')
              , ('refPrice', 'i8')
              , ('Count_1', 'i8')
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
      i += 76
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
      i += 25
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
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
              , ('Money', 'i8')
              , ('ItemsCountValue', 'i4')
                  ]+ list(self.f_ItemsCount()) +[
                  ]
    return dtype
  def f_ItemsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemsCount_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Slot', 'i4')
              , ('Count', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('0', 'i2')
              , ('BodyPart', 'i4')
              , ('enchantLvl', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('objID', 'i4')
              , ('price', 'i8')
              , ('refPrice', 'i8')
              , ('StoreCnt', 'i8')
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
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
#--------------------------------------------------------------------------#C0
class s_VehicleStarted():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xC0'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('ObjectId', 'i4')
              , ('state', 'i4')
                  ]
    return dtype
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
              , ('listSizeValue', 'i4')
                  ]+ list(self.f_listSize()) +[
                  ]
    return dtype
  def f_listSize(self):
    for i in range(self.It.__next__()):
      dtype = ('listSize_' + str(i) , [
               ('skillID', 'i4')
              , ('skillLvl', 'i4')
              , ('reuseDelay', 'i4')
              , ('timeRemain', 'i4')
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
#--------------------------------------------------------------------------#C8
class s_PackageToList():
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjID', 'i4')
              , ('Name', '|S'+str(self.It.__next__()) )
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
      i += 1
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
              , ('Time', 'i4')
              , ('Siege_Time', 'i4')
              , ('numOfChoice', 'i4')
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
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('CastleID', 'i4')
              , ('0_0', 'i4')
              , ('1', 'i4')
              , ('0_1', 'i4')
              , ('count', 'i4')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ClanID', 'i4')
              , ('clanName', '|S'+str(self.It.__next__()) )
              , ('leaderName', '|S'+str(self.It.__next__()) )
              , ('crestID', 'i4')
              , ('0', 'i4')
              , ('allyID', 'i4')
              , ('allyName', '|S'+str(self.It.__next__()) )
              , ('allyLeader', '|S'+str(self.It.__next__()) )
              , ('allyCrestID', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 20
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
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 12
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 4
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
      i += 1
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
      i += 2
#--------------------------------------------------------------------------#CB
class s_SiegeDefenderList():
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
              , ('0_0', 'i4')
              , ('1', 'i4')
              , ('0_1', 'i4')
              , ('count', 'i4')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ClanID', 'i4')
              , ('clanName', '|S'+str(self.It.__next__()) )
              , ('leaderName', '|S'+str(self.It.__next__()) )
              , ('crestID', 'i4')
              , ('signedTime', 'i4')
              , ('SiegeType', 'i4')
              , ('allyID', 'i4')
              , ('allyName', '|S'+str(self.It.__next__()) )
              , ('allyLeader', '|S'+str(self.It.__next__()) )
              , ('allyCrestID', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 20
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
      i += 4
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
      i += 1
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
      i += 2
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
              , ('LeaderID', 'i4')
              , ('ClanID', 'i4')
              , ('CrestID', 'i4')
              , ('AllyID', 'i4')
              , ('AllyCrest', 'i4')
              , ('U_0', 'i4')
              , ('U_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#CE
class s_RelationChanged():
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('Relation', 'i4')
              , ('AutoAttackable', 'i4')
              , ('Karma', 'i4')
              , ('PvpFlag', 'i4')
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
#--------------------------------------------------------------------------#CF
class s_OnEventTrigger():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xCF'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('emitterID', 'i4')
              , ('isClosed', 'i4')
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
              , ('Money', 'i8')
              , ('ItemsCountValue', 'i4')
                  ]+ list(self.f_ItemsCount()) +[
                  ]
    return dtype
  def f_ItemsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ItemsCount_' + str(i) , [
               ('Type1', 'i2')
              , ('ObjectID_0', 'i4')
              , ('ItemID', 'i4')
              , ('Count', 'i8')
              , ('Type2', 'i2')
              , ('CustomType1', 'i2')
              , ('BodyPart', 'i4')
              , ('Enchant', 'i2')
              , ('0', 'i2')
              , ('CustomType2', 'i2')
              , ('ObjectID_1', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
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
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
class s_FlyToLocation():
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
              , ('_id', 'i4')
              , ('Distantion', 'i4')
              , ('Yaw', 'i4')
              , ('Pitch', 'i4')
              , ('Time', 'i4')
              , ('Duration', 'i4')
              , ('turn', 'i4')
              , ('rise', 'i4')
              , ('widescreen', 'i4')
              , ('U', 'i4')
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
              , ('ItemID', 'i4')
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
              , ('num', 'i4')
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
#--------------------------------------------------------------------------#DD
class s_RecipeItemMakeInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xDD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('OID', 'i4')
              , ('isDwarvenRecipe', 'i4')
              , ('CurrentMP', 'i4')
              , ('MaxMP', 'i4')
              , ('isSuccess', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#DE
class s_RecipeShopManageList():
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
              , ('ObjectID', 'i4')
              , ('Money', 'i4')
              , ('IsDwarven', 'i4')
              , ('countValue_0', 'i4')
                  ]+ list(self.f_count()) +[
               ('countValue_1', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('RecipeID', 'i4')
              , ('num', 'i4')
                  ])
      yield dtype 
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('RecipeID', 'i4')
              , ('0', 'i4')
              , ('Cost', 'i8')
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
              , ('CurrMP', 'i4')
              , ('max_MP', 'i4')
              , ('Money', 'i8')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('RecipeID', 'i4')
              , ('0', 'i4')
              , ('Cost', 'i8')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 20
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
              , ('U', 'i4')
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
              , ('U_0', 'i4')
              , ('U_1', 'i4')
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
              , ('0020speeds', 'i4')
              , ('0', 'i4')
              , ('specEffects', 'i4')
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
#--------------------------------------------------------------------------#E4
class s_HennaItemDrawInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE4'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('SymbolID', 'i4')
              , ('ItemDyeID', 'i4')
              , ('DyeRequire', 'i8')
              , ('Price', 'i8')
              , ('Draw', 'i4')
              , ('Adena', 'i8')
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
              , ('slots', 'i4')
              , ('SlotCountValue', 'i4')
                  ]+ list(self.f_SlotCount()) +[
                  ]
    return dtype
  def f_SlotCount(self):
    for i in range(self.It.__next__()):
      dtype = ('SlotCount_' + str(i) , [
               ('SymbolID', 'i4')
              , ('01', 'i4')
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
  def parse_list(self):
   i = 1
   i += 7
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#E6
class s_HennaRemoveList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE6'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('money', 'i8')
              , ('0', 'i4')
              , ('slotsValue', 'i4')
                  ]+ list(self.f_slots()) +[
                  ]
    return dtype
  def f_slots(self):
    for i in range(self.It.__next__()):
      dtype = ('slots_' + str(i) , [
               ('symbolID', 'i4')
              , ('ItemIDdye', 'i4')
              , ('dyeRequired', 'i4')
              , ('0_0', 'i4')
              , ('price', 'i4')
              , ('0_1', 'i4')
              , ('1', 'i4')
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
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#E7
class s_HennaItemRemoveInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xE7'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('symbolID', 'i4')
              , ('ItemIDdye', 'i4')
              , ('dyeRequired', 'i8')
              , ('price', 'i8')
              , ('1', 'i4')
              , ('money', 'i8')
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
              , ('Count', 'i1')
              , ('isCheck', 'i1')
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
               ('Idx', 'i1')
              , ('Type', 'i1')
              , ('subjID', 'i4')
              , ('ShortCutID', 'i1')
              , ('CmdName', '|S'+str(self.It.__next__()) )
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
              , ('Money', 'i8')
              , ('ManorID', 'i4')
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ItemID_0', 'i4')
              , ('ItemID_1', 'i4')
              , ('0', 'i4')
              , ('Count', 'i8')
              , ('custType2', 'i2')
              , ('custType1', 'i2')
              , ('isequip', 'i2')
              , ('bodyPart', 'i4')
              , ('enchantLvl', 'i2')
              , ('custType', 'i2')
              , ('augm', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemPower', 'i2')
              , ('DefFire', 'i2')
              , ('DefWater', 'i2')
              , ('DefWind', 'i2')
              , ('DefEarth', 'i2')
              , ('DefHoly', 'i2')
              , ('DefUnholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('price', 'i8')
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
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
              , ('c0', 'i1')
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
              , ('Money', 'i8')
              , ('Slots', 'i4')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('SymbolID', 'i4')
              , ('ItemDyeID', 'i4')
              , ('DyeRequire', 'i8')
              , ('Price', 'i8')
              , ('isRequire', 'i4')
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
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
              , ('Money', 'i8')
              , ('lease', 'i4')
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ItemType1', 'i2')
              , ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('Count', 'i8')
              , ('ItemType2', 'i2')
              , ('0', 'i2')
              , ('Price', 'i8')
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
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
              , ('slots', 'i4')
              , ('SlotCountValue', 'i4')
                  ]+ list(self.f_SlotCount()) +[
                  ]
    return dtype
  def f_SlotCount(self):
    for i in range(self.It.__next__()):
      dtype = ('SlotCount_' + str(i) , [
               ('SymbolID', 'i4')
              , ('01', 'i4')
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
  def parse_list(self):
   i = 1
   i += 7
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
#--------------------------------------------------------------------------#F2
class s_ClientSetTime():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF2'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('gameTime', 'i4')
              , ('clientSpeed', 'i4')
                  ]
    return dtype
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
               ('skillID', 'i4')
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 2
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
              , ('c0', 'i1')
              , ('13', 'i1')
              , ('0_0', 'i1')
              , ('0_1', 'i1')
              , ('Money', 'i8')
              , ('ListID', 'i4')
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ItemID', 'i4')
              , ('Type2', 'i2')
              , ('BodyPart', 'i2')
              , ('WearPrice', 'i8')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 16
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
#--------------------------------------------------------------------------#F6
class s_ShopPreviewInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF6'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('totalSlot', 'i4')
              , ('Under', 'i4')
              , ('Rear', 'i4')
              , ('Lear', 'i4')
              , ('Neck', 'i4')
              , ('RRing', 'i4')
              , ('LRing', 'i4')
              , ('Head', 'i4')
              , ('RHand', 'i4')
              , ('LHand', 'i4')
              , ('Gloves', 'i4')
              , ('Chest', 'i4')
              , ('Legs', 'i4')
              , ('Boots', 'i4')
              , ('Cloak', 'i4')
              , ('LRHand', 'i4')
              , ('Hair', 'i4')
              , ('Hair2', 'i4')
              , ('RBrace', 'i4')
              , ('LBrace', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#F9
class s_EtcStatusUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xF9'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('Charges', 'i4')
              , ('WeightPenalty', 'i4')
              , ('isChatBanned', 'i4')
              , ('isDangerArea', 'i4')
              , ('ExpertiseWeapPenalty', 'i4')
              , ('ExpertArmorPenalty', 'i4')
              , ('CharmOfCourage', 'i4')
              , ('DeathPenaltyLevel', 'i4')
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
#--------------------------------------------------------------------------#FD
class s_AgitDecoInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFD'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('hallID', 'i4')
              , ('HPrecoverFireplace', 'i1')
              , ('MPrecoverCarpet', 'i1')
              , ('MPrecoverStatue', 'i1')
              , ('hallEXPrecover', 'i1')
              , ('hasTeleport', 'i1')
              , ('Crystal', 'i1')
              , ('Curtain', 'i1')
              , ('ItemCreate', 'i1')
              , ('hasSupport', 'i1')
              , ('hasSuport', 'i1')
              , ('has_platform', 'i1')
              , ('has_itemcreate', 'i1')
              , ('0_0', 'i4')
              , ('0_1', 'i4')
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
#--------------------------------------------------------------------------#FE08
class s_ExPartyRoomMember():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x08\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('mode', 'i4')
              , ('membersValue', 'i4')
                  ]+ list(self.f_members()) +[
                  ]
    return dtype
  def f_members(self):
    for i in range(self.It.__next__()):
      dtype = ('members_' + str(i) , [
               ('objID', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('class', 'i4')
              , ('level', 'i4')
              , ('location', 'i4')
              , ('isOwnerOrInParty', 'i4')
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
   i += 4
   for _ in range(count):
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 16
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
      i += 5
#--------------------------------------------------------------------------#FE09
class s_ExClosePartyRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x09\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE0A
class s_ExManagePartyRoomMember():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x0A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('mode', 'i4')
              , ('objID', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
              , ('class', 'i4')
              , ('level', 'i4')
              , ('location', 'i4')
              , ('isOwnerOrInParty', 'i4')
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
#--------------------------------------------------------------------------#FE0C
class s_ExAutoSoulShot():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x0C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ItemID', 'i4')
              , ('Type', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE0F
class s_ExEventMatchMessage():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x0F\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
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
              , ('listSizeValue', 'i4')
                  ]+ list(self.f_listSize()) +[
                  ]
    return dtype
  def f_listSize(self):
    for i in range(self.It.__next__()):
      dtype = ('listSize_' + str(i) , [
               ('FortID', 'i4')
              , ('OwnerClan', '|S'+str(self.It.__next__()) )
              , ('IsInProgress', 'i4')
              , ('PossessionTime', 'i4')
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
   if count > 100: raise Exception('PacketError')
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
      s_len = len(self.lst[i])
      yield s_len
      i += 2
#--------------------------------------------------------------------------#FE17
class s_ExShowFortressSiegeInfo():
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
              , ('FortID', 'i4')
              , ('sizeValue', 'i4')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('status', 'i4')
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
              , ('Crest', 'i1')
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
              , ('isNightLure_0', 'i1')
              , ('0_0', 'i1')
              , ('isNightLure_1', 'i1')
              , ('0_1', 'i1')
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
              , ('ListCountValue', 'i4')
                  ]+ list(self.f_ListCount()) +[
                  ]
    return dtype
  def f_ListCount(self):
    for i in range(self.It.__next__()):
      dtype = ('ListCount_' + str(i) , [
               ('idx', 'i4')
              , ('Manor', '|S'+str(self.It.__next__()) )
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
              , ('leftToBuy', 'i8')
              , ('StartProduce', 'i8')
              , ('sellPrice', 'i8')
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 4
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
              , ('CropAmount', 'i8')
              , ('StartAmount', 'i8')
              , ('Price', 'i8')
              , ('Reward', 'i1')
              , ('SeedLevelByCrop', 'i4')
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 4
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
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
              , ('SeedLevelByCrop', 'i4')
              , ('SeedBasicPriceByCrop', 'i4')
              , ('CropBasicPrice', 'i4')
              , ('1_0', 'i1')
              , ('RewardItem1', 'i4')
              , ('1_1', 'i1')
              , ('RewardItem2', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 3
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
#--------------------------------------------------------------------------#FE26
class s_ExShowSeedSetting():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x26\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('manorID', 'i4')
              , ('sizeValue', 'i4')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('seedID', 'i4')
              , ('Level', 'i4')
              , ('1', 'i1')
              , ('rewardID1', 'i4')
              , ('2', 'i1')
              , ('rewardID2', 'i4')
              , ('nextSaleLimit', 'i4')
              , ('price', 'i4')
              , ('minSeedPrice', 'i4')
              , ('maxSeedPrice', 'i4')
              , ('todaySales', 'i8')
              , ('todayPrice', 'i8')
              , ('nextSales', 'i8')
              , ('nextPrice', 'i8')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('skillID', 'i4')
              , ('NextLevel', 'i4')
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
              , ('skillID', 'i4')
              , ('Level', 'i4')
              , ('isNotMaxEnchanted', 'i4')
              , ('isEnchanted', 'i4')
              , ('routesSizeValue', 'i4')
                  ]+ list(self.f_routesSize()) +[
                  ]
    return dtype
  def f_routesSize(self):
    for i in range(self.It.__next__()):
      dtype = ('routesSize_' + str(i) , [
               ('lvl', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 18
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 5
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FE2B
class s_ExShowCropSetting():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x2B\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('manorID', 'i4')
              , ('sizeValue', 'i4')
                  ]+ list(self.f_size()) +[
                  ]
    return dtype
  def f_size(self):
    for i in range(self.It.__next__()):
      dtype = ('size_' + str(i) , [
               ('cropID', 'i4')
              , ('seedLevel', 'i4')
              , ('1_0', 'i1')
              , ('rewardID1', 'i4')
              , ('1_1', 'i1')
              , ('rewardID2', 'i4')
              , ('nextSaleLimit', 'i4')
              , ('count', 'i4')
              , ('minCropPrice', 'i4')
              , ('maxCropPrice', 'i4')
              , ('todayBuy', 'i8')
              , ('todayPrice', 'i8')
              , ('todayReward', 'i1')
              , ('nextBuy', 'i8')
              , ('nextPrice', 'i8')
              , ('nextReward', 'i1')
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
#--------------------------------------------------------------------------#FE2C
class s_ExShowSellCropList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x2C\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ManorId', 'i4')
              , ('CropCountValue', 'i4')
                  ]+ list(self.f_CropCount()) +[
                  ]
    return dtype
  def f_CropCount(self):
    for i in range(self.It.__next__()):
      dtype = ('CropCount_' + str(i) , [
               ('ObjectID', 'i4')
              , ('CropID', 'i4')
              , ('cropLevel', 'i4')
              , ('1_0', 'i1')
              , ('RewardItemCrop', 'i4')
              , ('1_1', 'i1')
              , ('RewardItemCrop2', 'i4')
              , ('ManorID', 'i4')
              , ('CroopAmount', 'i8')
              , ('BuyPrice', 'i8')
              , ('reward', 'i1')
              , ('myCropsCount', 'i8')
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
#--------------------------------------------------------------------------#FE2D
class s_ExOlympiadMatchEnd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x2D\x00'
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
              , ('PrivSellStoreLimit', 'i4')
              , ('PrivBuyStoreLimit', 'i4')
              , ('DwarfRecipeLimit', 'i4')
              , ('CommonRecipeLimit', 'i4')
              , ('invExtraSlots', 'i4')
              , ('invQuestItems', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE31
class s_ExMultiPartyCommandChannelInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x31\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('chanOwnerName', '|S'+str(self.It.__next__()) )
              , ('chanLoot', 'i4')
              , ('membCount', 'i4')
              , ('partysSizeValue', 'i4')
                  ]+ list(self.f_partysSize()) +[
                  ]
    return dtype
  def f_partysSize(self):
    for i in range(self.It.__next__()):
      dtype = ('partysSize_' + str(i) , [
               ('leaderName', '|S'+str(self.It.__next__()) )
              , ('leaderOID', 'i4')
              , ('membCount', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 2
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
      i += 8
  def parse_list(self):
   i = 1
   i += 1
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
      i += 3
#--------------------------------------------------------------------------#FE32
class s_ExPCCafePointInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x32\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('numPoints', 'i4')
              , ('pointsInc', 'i4')
              , ('period', 'i1')
              , ('periodHoursLeft', 'i4')
              , ('pointIncColor', 'i1')
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
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('rank', 'i4')
              , ('totalPoints', 'i4')
              , ('ListSizeValue', 'i4')
                  ]+ list(self.f_ListSize()) +[
                  ]
    return dtype
  def f_ListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('ListSize_' + str(i) , [
               ('bossID', 'i4')
              , ('points', 'i4')
              , ('U', 'i4')
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
  def parse_list(self):
   i = 1
   i += 3
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
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
#--------------------------------------------------------------------------#FE36
class s_ExListPartyMatchingWaitingRoom():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x36\x00'
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
              , ('membersSizeValue', 'i4')
                  ]+ list(self.f_membersSize()) +[
                  ]
    return dtype
  def f_membersSize(self):
    for i in range(self.It.__next__()):
      dtype = ('membersSize_' + str(i) , [
               ('name', '|S'+str(self.It.__next__()) )
              , ('class', 'i4')
              , ('level', 'i4')
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
   i += 4
   for _ in range(count):
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 8
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
      s_len = len(self.lst[i])
      yield s_len
      i += 3
#--------------------------------------------------------------------------#FE38
class s_ExShowAdventurerGuideBook():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x38\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE39
class s_ExShowScreenMessage():
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
              , ('type', 'i4')
              , ('sysMessageId', 'i4')
              , ('position', 'i4')
              , ('U_0', 'i4')
              , ('size', 'i4')
              , ('U_1', 'i4')
              , ('U_2', 'i4')
              , ('hasEffect', 'i4')
              , ('time', 'i4')
              , ('U_3', 'i4')
              , ('U_4', 'i4')
              , ('text', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 46
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 12
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#FE3B
class s_PledgeSkillListAdd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x3B\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('skillID', 'i4')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
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
              , ('0064test', 'i4')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('CursedWeaponID', 'i4')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
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
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FE48
class s_ExRestartClient():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x48\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
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
              , ('ItemID', 'i4')
              , ('grpID', 'i4')
              , ('remainTime', 'i4')
              , ('totalTime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE4B
class s_ExMPCCShowPartyMemberInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x4B\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('memberCountValue', 'i4')
                  ]+ list(self.f_memberCount()) +[
                  ]
    return dtype
  def f_memberCount(self):
    for i in range(self.It.__next__()):
      dtype = ('memberCount_' + str(i) , [
               ('name', '|S'+str(self.It.__next__()) )
              , ('objId', 'i4')
              , ('classID', 'i4')
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
      i += 3
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
              , ('U', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE4E
class s_ExDuelStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x4E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('type', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE4F
class s_ExDuelEnd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x4F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('type', 'i4')
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
              , ('ClassID', 'i4')
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
              , ('ItemID', 'i4')
              , ('1', 'i4')
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
              , ('GemStoneCount', 'i8')
              , ('U', 'i4')
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
              , ('ItemID', 'i4')
              , ('GemStoneCount', 'i8')
              , ('U_0', 'i4')
              , ('U_1', 'i4')
              , ('U_2', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE56
class s_ExVariationResult():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x56\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('stat12', 'i4')
              , ('stat34', 'i4')
              , ('U', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE57
class s_ExPutItemResultForVariationCancel():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x57\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ItemObjID', 'i4')
              , ('ItemID', 'i4')
              , ('Aug1', 'i4')
              , ('Aug2', 'i4')
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
              , ('result', 'i4')
              , ('U', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE5B
class s_ExMPCCPartyInfoUpdate():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x5B\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('leaderName', '|S'+str(self.It.__next__()) )
              , ('leaderOID', 'i4')
              , ('membCount', 'i4')
              , ('mode', 'i4')
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
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('type', 'i4')
              , ('skillid', 'i4')
              , ('skillLvl', 'i4')
              , ('SP', 'i4')
              , ('Exp', 'i4')
              , ('requiredItemCountValue', 'i4')
                  ]+ list(self.f_requiredItemCount()) +[
                  ]
    return dtype
  def f_requiredItemCount(self):
    for i in range(self.It.__next__()):
      dtype = ('requiredItemCount_' + str(i) , [
               ('reqItemID', 'i4')
              , ('itemCount', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 22
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ActionID', 'i4')
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
#--------------------------------------------------------------------------#FE60
class s_ExAirShipInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x60\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ObjectID', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('Heading', 'i4')
              , ('OIDWhoControlShip', 'i4')
              , ('MoveSpeed', 'i4')
              , ('RotationSpeed', 'i4')
              , ('helm', 'i4')
              , ('conX', 'i4')
              , ('conY', 'i4')
              , ('conZ', 'i4')
              , ('capX', 'i4')
              , ('capY', 'i4')
              , ('capZ', 'i4')
              , ('CurFuel', 'i4')
              , ('MaxFuel', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE61
class s_ExAttributeEnchantResult():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x61\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('result', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE62
class s_ExChooseInventoryAttributeItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x62\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ItemID', 'i4')
              , ('fire', 'i4')
              , ('water', 'i4')
              , ('wind', 'i4')
              , ('earth', 'i4')
              , ('holy', 'i4')
              , ('unholy', 'i4')
              , ('lvl', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE63
class s_ExGetOnAirShip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x63\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('playerID', 'i4')
              , ('shipID', 'i4')
              , ('x', 'i4')
              , ('y', 'i4')
              , ('z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE64
class s_ExGetOffAirShip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x64\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('playerID', 'i4')
              , ('shipID', 'i4')
              , ('x', 'i4')
              , ('y', 'i4')
              , ('z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE65
class s_ExMoveToLocationAirShip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x65\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('airShipId', 'i4')
              , ('dX', 'i4')
              , ('dY', 'i4')
              , ('dZ', 'i4')
              , ('x', 'i4')
              , ('y', 'i4')
              , ('z', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE66
class s_ExStopMoveAirShip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x66\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('airShipId', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('heading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE67
class s_ExShowTrace():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x67\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('traceSizeValue', 'i2')
                  ]+ list(self.f_traceSize()) +[
                  ]
    return dtype
  def f_traceSize(self):
    for i in range(self.It.__next__()):
      dtype = ('traceSize_' + str(i) , [
               ('x', 'i4')
              , ('y', 'i4')
              , ('d', 'i4')
              , ('time', 'i2')
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
#--------------------------------------------------------------------------#FE68
class s_ExItemAuctionInfoPacket():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x68\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('notRefresh', 'i1')
              , ('instanceID', 'i4')
              , ('highestBid', 'i8')
              , ('remainTime_0', 'i4')
              , ('itemID_0', 'i4')
              , ('itemID_1', 'i4')
              , ('slot_0', 'i4')
              , ('count_0', 'i8')
              , ('type2_0', 'i2')
              , ('custType1_0', 'i2')
              , ('0_0', 'i2')
              , ('bodyPart_0', 'i4')
              , ('enchLvl_0', 'i2')
              , ('custType2_0', 'i2')
              , ('augment_0', 'i4')
              , ('mana_0', 'i4')
              , ('remainTime_1', 'i4')
              , ('ElementType_0', 'i2')
              , ('ElementPower_0', 'i2')
              , ('Fire_0', 'i2')
              , ('Water_0', 'i2')
              , ('Wind_0', 'i2')
              , ('Earth_0', 'i2')
              , ('Holy_0', 'i2')
              , ('Unholy_0', 'i2')
              , ('enchEff1_0', 'i2')
              , ('enchEff2_0', 'i2')
              , ('enchEff3_0', 'i2')
              , ('nextAucInitBid', 'i8')
              , ('nextAucStartTime', 'i4')
              , ('itemID_2', 'i4')
              , ('itemID_3', 'i4')
              , ('slot_1', 'i4')
              , ('count_1', 'i8')
              , ('type2_1', 'i2')
              , ('custType1_1', 'i2')
              , ('0_1', 'i2')
              , ('bodyPart_1', 'i4')
              , ('enchLvl_1', 'i2')
              , ('custType2_1', 'i2')
              , ('augment_1', 'i4')
              , ('mana_1', 'i4')
              , ('remainTime_2', 'i4')
              , ('ElementType_1', 'i2')
              , ('ElementPower_1', 'i2')
              , ('Fire_1', 'i2')
              , ('Water_1', 'i2')
              , ('Wind_1', 'i2')
              , ('Earth_1', 'i2')
              , ('Holy_1', 'i2')
              , ('Unholy_1', 'i2')
              , ('enchEff1_1', 'i2')
              , ('enchEff2_1', 'i2')
              , ('enchEff3_1', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE69
class s_ExNeedToChangeName():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x69\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('type', 'i4')
              , ('subType', 'i4')
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
#--------------------------------------------------------------------------#FE6C
class s_ExRpItemLink():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x6C\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('ObjID', 'i4')
              , ('ItemID', 'i4')
              , ('slot', 'i4')
              , ('count', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('0', 'i2')
              , ('Bodypart', 'i4')
              , ('enchLvl', 'i2')
              , ('custype2', 'i2')
              , ('Augm', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('ElementType', 'i2')
              , ('ElementPower', 'i2')
              , ('Fire', 'i2')
              , ('Water', 'i2')
              , ('Wind', 'i2')
              , ('Earth', 'i2')
              , ('Holy', 'i2')
              , ('Unholy', 'i2')
              , ('enchEffect1', 'i2')
              , ('enchEffect2', 'i2')
              , ('enchEffect3', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE6D
class s_ExMoveToLocationInAirShip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x6D\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('charOID', 'i4')
              , ('airShipId', 'i4')
              , ('destX', 'i4')
              , ('destY', 'i4')
              , ('destZ', 'i4')
              , ('destHeading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE6E
class s_ExStopMoveInAirShip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x6E\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('charOID', 'i4')
              , ('airShipId', 'i4')
              , ('charDestX', 'i4')
              , ('charDestY', 'i4')
              , ('charDestZ', 'i4')
              , ('charDestHeading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE6F
class s_ExValidateLocationInAirShip():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x6F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('charOID', 'i4')
              , ('airShipId', 'i4')
              , ('X', 'i4')
              , ('Y', 'i4')
              , ('Z', 'i4')
              , ('charHeading', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE70
class s_ExUISetting():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x70\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('bufsize', 'i4')
              , ('categories', 'i4')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('catList1Value', 'i1')
                  ]+ list(self.f_catList1()) +[
                  ])
      yield dtype 
  def f_catList1(self):
    for i in range(self.It.__next__()):
      dtype = ('catList1_' + str(i) , [
               ('cmd', 'i1')
              , ('catList2Value', 'i1')
                  ]+ list(self.f_catList2()) +[
                  ])
      yield dtype 
  def f_catList2(self):
    for i in range(self.It.__next__()):
      dtype = ('catList2_' + str(i) , [
               ('cmd', 'i1')
              , ('keyListValue', 'i4')
                  ]+ list(self.f_keyList()) +[
                  ])
      yield dtype 
  def f_keyList(self):
    for i in range(self.It.__next__()):
      dtype = ('keyList_' + str(i) , [
               ('cmdID', 'i4')
              , ('keyID', 'i4')
              , ('toogleKey1', 'i4')
              , ('toogleKey2', 'i4')
              , ('showStatus', 'i4')
              , ('11', 'i4')
              , ('10', 'i4')
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
      count = self.lst[i]
      if count > 100: raise Exception('PacketError')
      yield count
#--------------------------------------------------------------------------#FE74
class s_ExShowBaseAttributeCancelWindow():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x74\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('itemCountValue', 'i4')
                  ]+ list(self.f_itemCount()) +[
                  ]
    return dtype
  def f_itemCount(self):
    for i in range(self.It.__next__()):
      dtype = ('itemCount_' + str(i) , [
               ('objID', 'i4')
              , ('price', 'i8')
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
#--------------------------------------------------------------------------#FE75
class s_ExBaseAttributeCancelResult():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x75\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('result', 'i4')
              , ('objID', 'i4')
              , ('attrib', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE76
class s_ExSubPledgeSkillAdd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x76\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('type', 'i4')
              , ('skillID', 'i4')
              , ('skillLvl', 'i4')
                  ]
    return dtype
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
              , ('CastleCropsSizeValue', 'i4')
                  ]+ list(self.f_CastleCropsSize()) +[
                  ]
    return dtype
  def f_CastleCropsSize(self):
    for i in range(self.It.__next__()):
      dtype = ('CastleCropsSize_' + str(i) , [
               ('ManorID', 'i4')
              , ('CropAmount', 'i8')
              , ('CropPrice', 'i8')
              , ('CropReward', 'i1')
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
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('HeroName', '|S'+str(self.It.__next__()) )
              , ('ClassID', 'i4')
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
#--------------------------------------------------------------------------#FE7A
class s_ExOlympiadUserInfo():
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
              , ('ClassID', 'i4')
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
              , ('PlayerID', 'i4')
              , ('countValue', 'i4')
                  ]+ list(self.f_count()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('skillID', 'i4')
              , ('level', 'i2')
              , ('Duration', 'i4')
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
#--------------------------------------------------------------------------#FE7D
class s_ExShowFortressMapInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x7D\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('fortID', 'i4')
              , ('fortSiegeStat', 'i4')
              , ('fortSizeValue', 'i4')
                  ]+ list(self.f_fortSize()) +[
                  ]
    return dtype
  def f_fortSize(self):
    for i in range(self.It.__next__()):
      dtype = ('fortSize_' + str(i) , [
               ('status', 'i4')
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
  def parse_list(self):
   i = 1
   i += 3
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FE80
class s_ExPrivateStoreSetWholeMsg():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x80\x00'
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
              , ('Msg', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#FE81
class s_ExPutEnchantTargetItemResult():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x81\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Result', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE82
class s_ExPutEnchantSupportItemResult():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x82\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('Result', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE83
class s_ExRequestChangeNicknameColor():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x83\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('objID', 'i4')
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
              , ('bookmarkSlot', 'i4')
              , ('SizeValue', 'i4')
                  ]+ list(self.f_Size()) +[
                  ]
    return dtype
  def f_Size(self):
    for i in range(self.It.__next__()):
      dtype = ('Size_' + str(i) , [
               ('ID', 'i4')
              , ('X', 'i4')
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
   if count > 100: raise Exception('PacketError')
   yield count
   i += 4
   for _ in range(count):
      i += 16
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
      i += 2
      s_len = len(self.lst[i])
      yield s_len
      i += 1
#--------------------------------------------------------------------------#FE85
class s_ExNotifyPremiumItem():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x85\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE86
class s_ExGetPremiumItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x86\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('listSizeValue', 'i4')
                  ]+ list(self.f_listSize()) +[
                  ]
    return dtype
  def f_listSize(self):
    for i in range(self.It.__next__()):
      dtype = ('listSize_' + str(i) , [
               ('num', 'i4')
              , ('objID', 'i4')
              , ('ItemID', 'i4')
              , ('count', 'i8')
              , ('0', 'i4')
              , ('sender', '|S'+str(self.It.__next__()) )
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
      i += 24
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
      i += 5
      s_len = len(self.lst[i])
      yield s_len
      i += 1
#--------------------------------------------------------------------------#FE8D
class s_NpcQuestHtmlMessage():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x8D\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('NpcObjId', 'i4')
              , ('Html', '|S'+str(self.It.__next__()) )
              , ('QuestId', 'i4')
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
#--------------------------------------------------------------------------#FE8E
class s_ExSendUIEvent():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x8E\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('objID', 'i4')
              , ('isHide', 'i4')
              , ('U_0', 'i4')
              , ('U_1', 'i4')
              , ('increase', '|S'+str(self.It.__next__()) )
              , ('timerMinutes', '|S'+str(self.It.__next__()) )
              , ('timerSeconds', '|S'+str(self.It.__next__()) )
              , ('text', '|S'+str(self.It.__next__()) )
              , ('lengthMinutes', '|S'+str(self.It.__next__()) )
              , ('lengthSeconds', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 18
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
   i += 5
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
#--------------------------------------------------------------------------#FE8F
class s_ExBirthdayPopup():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x8F\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE90
class s_ExShowDominionRegistry():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x90\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('territoryID', 'i4')
              , ('ownerClan', '|S'+str(self.It.__next__()) )
              , ('ownerClanLeader', '|S'+str(self.It.__next__()) )
              , ('ownerAlly', '|S'+str(self.It.__next__()) )
              , ('clanReq', 'i4')
              , ('mercReq', 'i4')
              , ('warTime', 'i4')
              , ('currTime', 'i4')
              , ('isClanReg', 'i4')
              , ('isMercReg', 'i4')
              , ('01', 'i4')
              , ('terrCountValue', 'i4')
                  ]+ list(self.f_terrCount()) +[
                  ]
    return dtype
  def f_terrCount(self):
    for i in range(self.It.__next__()):
      dtype = ('terrCount_' + str(i) , [
               ('terrID', 'i4')
              , ('emblemCountValue', 'i4')
                  ]+ list(self.f_emblemCount()) +[
                  ])
      yield dtype 
  def f_emblemCount(self):
    for i in range(self.It.__next__()):
      dtype = ('emblemCount_' + str(i) , [
               ('emblemID', 'i4')
                  ])
      yield dtype 
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
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   i += 28
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
   i += 4
   for _ in range(count):
      i += 4
      p = self.pck[i:i+4]
      count = struct.unpack('i', p)[0]
      if count > 100: raise Exception('PacketError')
      yield count
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
   i += 8
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
      count = self.lst[i]
      if count > 100: raise Exception('PacketError')
      yield count
#--------------------------------------------------------------------------#FE92
class s_ExReplyDominionInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x92\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('terraListSizeValue', 'i4')
                  ]+ list(self.f_terraListSize()) +[
                  ]
    return dtype
  def f_terraListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('terraListSize_' + str(i) , [
               ('terrID', 'i4')
              , ('terrName', '|S'+str(self.It.__next__()) )
              , ('ownerClan', '|S'+str(self.It.__next__()) )
              , ('emblemCountValue', 'i4')
                  ]+ list(self.f_emblemCount()) +[
                  ])
      yield dtype 
  def f_emblemCount(self):
    for i in range(self.It.__next__()):
      dtype = ('emblemCount_' + str(i) , [
               ('emblemID', 'i4')
              , ('warTime', 'i4')
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
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
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
      i += 1
      count = self.lst[i]
      if count > 100: raise Exception('PacketError')
      yield count
#--------------------------------------------------------------------------#FE93
class s_ExShowOwnthingPos():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x93\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('terraWardListValue', 'i4')
                  ]+ list(self.f_terraWardList()) +[
                  ]
    return dtype
  def f_terraWardList(self):
    for i in range(self.It.__next__()):
      dtype = ('terraWardList_' + str(i) , [
               ('terraID', 'i4')
              , ('wardX', 'i4')
              , ('wardY', 'i4')
              , ('wardZ', 'i4')
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
#--------------------------------------------------------------------------#FE99
class s_ExStartScenePlayer():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x99\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('movieID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE9A
class s_ExAirShipTeleportList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\x9A\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('dockID', 'i4')
              , ('teleportsSizeValue', 'i4')
                  ]+ list(self.f_teleportsSize()) +[
                  ]
    return dtype
  def f_teleportsSize(self):
    for i in range(self.It.__next__()):
      dtype = ('teleportsSize_' + str(i) , [
               ('idx', 'i4')
              , ('fuel', 'i4')
              , ('dstX', 'i4')
              , ('dstY', 'i4')
              , ('dstZ', 'i4')
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
#--------------------------------------------------------------------------#FEA0
class s_ExVitalityPointInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xA0\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('vitalityPoints', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEA1
class s_ExShowSeedMapInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xA1\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('seedCountValue', 'i4')
                  ]+ list(self.f_seedCount()) +[
                  ]
    return dtype
  def f_seedCount(self):
    for i in range(self.It.__next__()):
      dtype = ('seedCount_' + str(i) , [
               ('x', 'i4')
              , ('y', 'i4')
              , ('z', 'i4')
              , ('sysMsgID', 'i4')
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
#--------------------------------------------------------------------------#FEA3
class s_ExDominionWarStart():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xA3\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('objID', 'i4')
              , ('1', 'i4')
              , ('terrID', 'i4')
              , ('isDisguised', 'i4')
              , ('isDisgTerrID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEA4
class s_ExDominionWarEnd():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xA4\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEA7
class s_ExEnchantSkillResult():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xA7\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('isEnchanted', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEA9
class s_ExNoticePostArrived():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xA9\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('doShowAnim', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEAA
class s_ExShowReceivedPostList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xAA\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('systemTime', 'i4')
              , ('inboxSizeValue', 'i4')
                  ]+ list(self.f_inboxSize()) +[
                  ]
    return dtype
  def f_inboxSize(self):
    for i in range(self.It.__next__()):
      dtype = ('inboxSize_' + str(i) , [
               ('msgID', 'i4')
              , ('subj', '|S'+str(self.It.__next__()) )
              , ('senderName', '|S'+str(self.It.__next__()) )
              , ('isLocked', 'i4')
              , ('expirateSecond', 'i4')
              , ('isUnread', 'i4')
              , ('01', 'i4')
              , ('hasAttachs', 'i4')
              , ('isFourStars', 'i4')
              , ('isNews', 'i4')
              , ('0', 'i4')
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
   i += 4
   for _ in range(count):
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 32
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 9
#--------------------------------------------------------------------------#FEAB
class s_ExReplyReceivedPost():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xAB\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('msgID', 'i4')
              , ('isLocked', 'i4')
              , ('0', 'i4')
              , ('senderName', '|S'+str(self.It.__next__()) )
              , ('subj', '|S'+str(self.It.__next__()) )
              , ('content', '|S'+str(self.It.__next__()) )
              , ('itemsCountValue', 'i4')
                  ]+ list(self.f_itemsCount()) +[
                  ]
    return dtype
  def f_itemsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('itemsCount_' + str(i) , [
               ('objID', 'i4')
              , ('itemID', 'i4')
              , ('Slot', 'i4')
              , ('count', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquip', 'i2')
              , ('bodyPart', 'i4')
              , ('enchLvl', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('ElementType', 'i2')
              , ('ElementPower', 'i2')
              , ('Fire', 'i2')
              , ('Water', 'i2')
              , ('Wind', 'i2')
              , ('Earth', 'i2')
              , ('Holy', 'i2')
              , ('Unholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('ObjID', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 14
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 4
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FEAC
class s_ExShowSentPostList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xAC\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('systemTime', 'i4')
              , ('outboxSizeValue', 'i4')
                  ]+ list(self.f_outboxSize()) +[
                  ]
    return dtype
  def f_outboxSize(self):
    for i in range(self.It.__next__()):
      dtype = ('outboxSize_' + str(i) , [
               ('msgID', 'i4')
              , ('subj', '|S'+str(self.It.__next__()) )
              , ('receiverName', '|S'+str(self.It.__next__()) )
              , ('isLocked', 'i4')
              , ('expirateSecond', 'i4')
              , ('isUnread', 'i4')
              , ('01', 'i4')
              , ('hasAttachs', 'i4')
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
   i += 4
   for _ in range(count):
      i += 4
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      s_len = f_s_len(self.pck[i:])
      yield s_len
      i += s_len
      i += 20
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
      i += 1
      s_len = len(self.lst[i])
      yield s_len
      i += 6
#--------------------------------------------------------------------------#FEAD
class s_ExReplySentPost():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xAD\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('msgID', 'i4')
              , ('isLocked', 'i4')
              , ('receiverName', '|S'+str(self.It.__next__()) )
              , ('subj', '|S'+str(self.It.__next__()) )
              , ('content', '|S'+str(self.It.__next__()) )
              , ('itemsCountValue', 'i4')
                  ]+ list(self.f_itemsCount()) +[
               ('regAdena', 'i8')
              , ('isFourStars', 'i4')
                  ]
    return dtype
  def f_itemsCount(self):
    for i in range(self.It.__next__()):
      dtype = ('itemsCount_' + str(i) , [
               ('objID_0', 'i4')
              , ('itemID', 'i4')
              , ('Slot', 'i4')
              , ('count', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquip', 'i2')
              , ('bodyPart', 'i4')
              , ('enchLvl', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('ElementType', 'i2')
              , ('ElementPower', 'i2')
              , ('Fire', 'i2')
              , ('Water', 'i2')
              , ('Wind', 'i2')
              , ('Earth', 'i2')
              , ('Holy', 'i2')
              , ('Unholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('objID_1', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 10
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   p = self.pck[i:i+4]
   count = struct.unpack('i', p)[0]
   if count > 100: raise Exception('PacketError')
   yield count
  def parse_list(self):
   i = 1
   i += 3
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FEB2
class s_ExReplyPostItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xB2\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('itemListSizeValue', 'i4')
                  ]+ list(self.f_itemListSize()) +[
                  ]
    return dtype
  def f_itemListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('itemListSize_' + str(i) , [
               ('objID', 'i4')
              , ('itemID', 'i4')
              , ('Slot', 'i4')
              , ('count', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('isEquip', 'i2')
              , ('bodyPart', 'i4')
              , ('enchLvl', 'i2')
              , ('custType2', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('ElementType', 'i2')
              , ('ElementPower', 'i2')
              , ('Fire', 'i2')
              , ('Water', 'i2')
              , ('Wind', 'i2')
              , ('Earth', 'i2')
              , ('Holy', 'i2')
              , ('Unholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
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
#--------------------------------------------------------------------------#FEB3
class s_ExChangePostState():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xB3\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('isReceivedBoard', 'i4')
              , ('msgSizeValue', 'i4')
                  ]+ list(self.f_msgSize()) +[
                  ]
    return dtype
  def f_msgSize(self):
    for i in range(self.It.__next__()):
      dtype = ('msgSize_' + str(i) , [
               ('postID', 'i4')
              , ('changeID', 'i4')
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
#--------------------------------------------------------------------------#FEB4
class s_ExNoticePostSent():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xB4\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('doShowAnim', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEBB
class s_ExAskCoupleAction():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xBB\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('actionID', 'i4')
              , ('objID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEBC
class s_ExBrLoadEventTopRankers():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xBC\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('eventID', 'i4')
              , ('day', 'i4')
              , ('count', 'i4')
              , ('bestScore', 'i4')
              , ('myScore', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEBD
class s_ExChangeNpcState():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xBD\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('objID', 'i4')
              , ('state', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEBE
class s_ExAskModifyPartyLooting():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xBE\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('requestor', '|S'+str(self.It.__next__()) )
              , ('mode', 'i4')
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
#--------------------------------------------------------------------------#FEBF
class s_ExSetPartyLooting():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xBF\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('result', 'i4')
              , ('mode', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEC0
class s_ExRotation():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xC0\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('objID', 'i4')
              , ('degree', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEC5
class s_ExQuestItemList():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xC5\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('countValue', 'i2')
                  ]+ list(self.f_count()) +[
               ('blockedItemsValue', 'i2')
              , ('blockMode', 'i1')
                  ]+ list(self.f_blockedItems()) +[
                  ]
    return dtype
  def f_count(self):
    for i in range(self.It.__next__()):
      dtype = ('count_' + str(i) , [
               ('ObjectID', 'i4')
              , ('ItemID', 'i4')
              , ('LocationSlot', 'i4')
              , ('Count', 'i8')
              , ('ItemType2', 'i2')
              , ('CustomType1', 'i2')
              , ('isEquipped', 'i2')
              , ('BodyPart', 'i4')
              , ('EnchantLevel', 'i2')
              , ('CustType2', 'i2')
              , ('AugmentID', 'i4')
              , ('Mana', 'i4')
              , ('remainTime', 'i4')
              , ('AttackElem', 'i2')
              , ('AttackElemVal', 'i2')
              , ('DefAttrFire', 'i2')
              , ('DefAttrWater', 'i2')
              , ('DefAttrWind', 'i2')
              , ('DefAttrEarth', 'i2')
              , ('DefAttrHoly', 'i2')
              , ('DefAttrUnholy', 'i2')
              , ('EnchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
                  ])
      yield dtype 
  def f_blockedItems(self):
    for i in range(self.It.__next__()):
      dtype = ('blockedItems_' + str(i) , [
               ('blockItem', 'i4')
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
      i += 68
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
      i += 24
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
#--------------------------------------------------------------------------#FEC8
class s_ExVoteSystemInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xC8\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('recomLeft', 'i4')
              , ('recomHave', 'i4')
              , ('bonusTime', 'i4')
              , ('bonusVal', 'i4')
              , ('bonusType', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FECD
class s_ExBrPremiumState():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xCD\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('objID', 'i4')
              , ('state', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FECE
class s_ExBrBroadcastEventState():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xCE\x00'
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('eventID', 'i4')
              , ('eventState', 'i4')
              , ('U_0', 'i4')
              , ('U_1', 'i4')
              , ('U_2', 'i4')
              , ('U_3', 'i4')
              , ('U_4', 'i4')
              , ('U_0', '|S'+str(self.It.__next__()) )
              , ('U_1', '|S'+str(self.It.__next__()) )
                  ]
    return dtype
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 30
   s_len = f_s_len(self.pck[i:])
   yield s_len
   i += s_len
   s_len = f_s_len(self.pck[i:])
   yield s_len
  def parse_list(self):
   i = 1
   i += 8
   s_len = len(self.lst[i])
   yield s_len
   i += 1
   s_len = len(self.lst[i])
   yield s_len
#--------------------------------------------------------------------------#FECF
class s_ExBrExtraUserInfo():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xCF\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('charOID', 'i4')
              , ('val', 'i4')
              , ('eventFlag', 'i1')
                  ]
    return dtype
#--------------------------------------------------------------------------#FED0
class s_ExBrBuffEventState():
  def __init__(self):
    self.lst, self.pck, self.invoke= [], b'', b'\xFE\xD0\x00'
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('type', 'i4')
              , ('value', 'i4')
              , ('state', 'i4')
              , ('endtime', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE970000
class s_ExCubeGameTeamList():
  def __init__(self):
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('sub2ID', 'i4')
              , ('roomNumber', 'i4')
              , ('1', 'i4')
              , ('bluePlayersCountValue', 'i4')
                  ]+ list(self.f_bluePlayersCount()) +[
               ('redPlayersCountValue', 'i4')
                  ]+ list(self.f_redPlayersCount()) +[
                  ]
    return dtype
  def f_bluePlayersCount(self):
    for i in range(self.It.__next__()):
      dtype = ('bluePlayersCount_' + str(i) , [
               ('playerObjID', 'i4')
              , ('name', 'i4')
                  ])
      yield dtype 
  def f_redPlayersCount(self):
    for i in range(self.It.__next__()):
      dtype = ('redPlayersCount_' + str(i) , [
               ('playerObjID', 'i4')
              , ('name', 'i4')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 14
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
   i += 4
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
#--------------------------------------------------------------------------#FE970001
class s_ExCubeGameAddPlayer():
  def __init__(self):
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('sub2ID', 'i4')
              , ('1', 'i4')
              , ('isRedTeam', 'i4')
              , ('ObjID', 'i4')
              , ('name', '|S'+str(self.It.__next__()) )
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
#--------------------------------------------------------------------------#FE970002
class s_ExCubeGameRemovePlayer():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('sub2ID', 'i4')
              , ('1', 'i4')
              , ('isRedTeam', 'i4')
              , ('ObjID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE970003
class s_ExCubeGameChangeTimeToStart():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('sub2ID', 'i4')
              , ('seconds', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE970004
class s_ExCubeGameRequestReady():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('sub2ID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE970005
class s_ExCubeGameChangeTeam():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('sub2ID', 'i4')
              , ('ObjID', 'i4')
              , ('fromRedTeam_0', 'i4')
              , ('fromRedTeam_1', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE9700FF
class s_ExCubeGameCloseUI():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('sub2ID', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE980000
class s_ExCubeGameExtendedChangePoints():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('sub2ID', 'i4')
              , ('timeLeft', 'i4')
              , ('bluePoints', 'i4')
              , ('redPoints', 'i4')
              , ('isRedTeam', 'i4')
              , ('ObjID', 'i4')
              , ('playerPoints', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE980001
class s_ExCubeGameEnd():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('sub2ID', 'i4')
              , ('isRedTeamWin', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FE980002
class s_ExCubeGameChangePoints():
  def __init__(self):
  def dtype(self, act, data):
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('sub2ID', 'i4')
              , ('timeLeft', 'i4')
              , ('bluePoints', 'i4')
              , ('redPoints', 'i4')
                  ]
    return dtype
#--------------------------------------------------------------------------#FEB70000
class s_ExBuyList():
  def __init__(self):
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('sub2ID', 'i4')
              , ('money', 'i8')
              , ('buyListID', 'i4')
              , ('buyListSizeValue', 'i2')
                  ]+ list(self.f_buyListSize()) +[
                  ]
    return dtype
  def f_buyListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('buyListSize_' + str(i) , [
               ('itemID_0', 'i4')
              , ('itemID_1', 'i4')
              , ('0', 'i4')
              , ('curCount', 'i8')
              , ('type2', 'i2')
              , ('type1', 'i2')
              , ('isEquip', 'i2')
              , ('bodyPart', 'i4')
              , ('enchLvl', 'i2')
              , ('custType', 'i2')
              , ('augment', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('ElementType', 'i2')
              , ('ElementPower', 'i2')
              , ('Fire', 'i2')
              , ('Water', 'i2')
              , ('Wind', 'i2')
              , ('Earth', 'i2')
              , ('Holy', 'i2')
              , ('Unholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('pricetaxRate', 'i8')
                  ])
      yield dtype 
  def parse_packet(self):
   i = 1
   f_s_len = (lambda data: (data[::2].find(b'\x00')+1)*2)
   i += 18
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
#--------------------------------------------------------------------------#FEB70001
class s_ExBuySellListPacket():
  def __init__(self):
  def dtype(self, act, data):
    if   act == 1:
      self.It = self.parse_packet()
      self.pck= data
    elif act == 2:
      self.It = self.parse_list()
      self.lst= data
    dtype = [('pck_type', 'i1')
              , ('subID', 'i2')
              , ('sub2ID', 'i4')
              , ('sellListSizeValue', 'i2')
                  ]+ list(self.f_sellListSize()) +[
               ('refundListSizeValue', 'i2')
                  ]+ list(self.f_refundListSize()) +[
               ('isDone', 'i1')
                  ]
    return dtype
  def f_sellListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('sellListSize_' + str(i) , [
               ('objID', 'i4')
              , ('itemID', 'i4')
              , ('slot', 'i4')
              , ('curCount', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('0', 'i2')
              , ('bodyPart', 'i4')
              , ('enchLvl', 'i2')
              , ('custType2', 'i2')
              , ('augm', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('ElementType', 'i2')
              , ('ElementPower', 'i2')
              , ('Fire', 'i2')
              , ('Water', 'i2')
              , ('Wind', 'i2')
              , ('Earth', 'i2')
              , ('Holy', 'i2')
              , ('Unholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('price', 'i8')
                  ])
      yield dtype 
  def f_refundListSize(self):
    for i in range(self.It.__next__()):
      dtype = ('refundListSize_' + str(i) , [
               ('objID', 'i4')
              , ('itemID', 'i4')
              , ('0_0', 'i4')
              , ('curCount', 'i8')
              , ('type2', 'i2')
              , ('custType1', 'i2')
              , ('0_1', 'i2')
              , ('bodyPart', 'i4')
              , ('enchLvl', 'i2')
              , ('custType2', 'i2')
              , ('augm', 'i4')
              , ('mana', 'i4')
              , ('remainTime', 'i4')
              , ('ElementType', 'i2')
              , ('ElementPower', 'i2')
              , ('Fire', 'i2')
              , ('Water', 'i2')
              , ('Wind', 'i2')
              , ('Earth', 'i2')
              , ('Holy', 'i2')
              , ('Unholy', 'i2')
              , ('enchEff1', 'i2')
              , ('enchEff2', 'i2')
              , ('enchEff3', 'i2')
              , ('idx', 'i4')
              , ('price', 'i8')
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
   i += 2
   for _ in range(count):
      i += 76
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
      i += 25
   count = self.lst[i]
   if count > 100: raise Exception('PacketError')
   yield count
class Pck_invoke_dict():
 def __init__(self):
   self.Pck_invoke_s = {}
   self.Pck_invoke_c = {}
 def get_Pck_invoke_c(self):
   self.Pck_invoke_s[c_Logout().invoke] = c_Logout()
   self.Pck_invoke_s[c_AttackRequest().invoke] = c_AttackRequest()
   self.Pck_invoke_s[c_ReqStartPledgeWar().invoke] = c_ReqStartPledgeWar()
   self.Pck_invoke_s[c_ReqReplyStartPledgeWar().invoke] = c_ReqReplyStartPledgeWar()
   self.Pck_invoke_s[c_ReqStopPledgeWar().invoke] = c_ReqStopPledgeWar()
   self.Pck_invoke_s[c_ReqReplyStopPledgeWar().invoke] = c_ReqReplyStopPledgeWar()
   self.Pck_invoke_s[c_ReqSurrenderPledgeWar().invoke] = c_ReqSurrenderPledgeWar()
   self.Pck_invoke_s[c_ReqReplySurrenderPledgeWar().invoke] = c_ReqReplySurrenderPledgeWar()
   self.Pck_invoke_s[c_ReqSetPledgeCrest().invoke] = c_ReqSetPledgeCrest()
   self.Pck_invoke_s[c_RequestGiveNickName().invoke] = c_RequestGiveNickName()
   self.Pck_invoke_s[c_CharacterCreate().invoke] = c_CharacterCreate()
   self.Pck_invoke_s[c_CharacterDelete().invoke] = c_CharacterDelete()
   self.Pck_invoke_s[c_ProtocolVersion().invoke] = c_ProtocolVersion()
   self.Pck_invoke_s[c_MoveBackwardToLocation().invoke] = c_MoveBackwardToLocation()
   self.Pck_invoke_s[c_EnterWorld().invoke] = c_EnterWorld()
   self.Pck_invoke_s[c_CharSelected().invoke] = c_CharSelected()
   self.Pck_invoke_s[c_NewCharacter().invoke] = c_NewCharacter()
   self.Pck_invoke_s[c_RequestItemList().invoke] = c_RequestItemList()
   self.Pck_invoke_s[c_RequestUnEquipItem().invoke] = c_RequestUnEquipItem()
   self.Pck_invoke_s[c_RequestDropItem().invoke] = c_RequestDropItem()
   self.Pck_invoke_s[c_UseItem().invoke] = c_UseItem()
   self.Pck_invoke_s[c_TradeRequest().invoke] = c_TradeRequest()
   self.Pck_invoke_s[c_AddTradeItem().invoke] = c_AddTradeItem()
   self.Pck_invoke_s[c_TradeDone().invoke] = c_TradeDone()
   self.Pck_invoke_s[c_Action().invoke] = c_Action()
   self.Pck_invoke_s[c_RequestLinkHtml().invoke] = c_RequestLinkHtml()
   self.Pck_invoke_s[c_ReqBypassToServer().invoke] = c_ReqBypassToServer()
   self.Pck_invoke_s[c_ReqBBSwrite().invoke] = c_ReqBBSwrite()
   self.Pck_invoke_s[c_ReqJoinPledge().invoke] = c_ReqJoinPledge()
   self.Pck_invoke_s[c_ReqAnswerJoinPledge().invoke] = c_ReqAnswerJoinPledge()
   self.Pck_invoke_s[c_ReqWithdrawalPledge().invoke] = c_ReqWithdrawalPledge()
   self.Pck_invoke_s[c_ReqOustPledgeMember().invoke] = c_ReqOustPledgeMember()
   self.Pck_invoke_s[c_ReqAuthLogin().invoke] = c_ReqAuthLogin()
   self.Pck_invoke_s[c_ReqGetItemFromPet().invoke] = c_ReqGetItemFromPet()
   self.Pck_invoke_s[c_ReqAllyInfo().invoke] = c_ReqAllyInfo()
   self.Pck_invoke_s[c_ReqCrystallizeItem().invoke] = c_ReqCrystallizeItem()
   self.Pck_invoke_s[c_ReqPrivateStoreManageSell().invoke] = c_ReqPrivateStoreManageSell()
   self.Pck_invoke_s[c_SetPrivateStoreListSell().invoke] = c_SetPrivateStoreListSell()
   self.Pck_invoke_s[c_AttackRequest().invoke] = c_AttackRequest()
   self.Pck_invoke_s[c_RequestSocialAction().invoke] = c_RequestSocialAction()
   self.Pck_invoke_s[c_ChangeMoveType2().invoke] = c_ChangeMoveType2()
   self.Pck_invoke_s[c_ChangeWaitType2().invoke] = c_ChangeWaitType2()
   self.Pck_invoke_s[c_RequestSellItem().invoke] = c_RequestSellItem()
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
   self.Pck_invoke_s[c_RequestTargetCancel().invoke] = c_RequestTargetCancel()
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
   self.Pck_invoke_s[c_StartRotating().invoke] = c_StartRotating()
   self.Pck_invoke_s[c_FinishRotating().invoke] = c_FinishRotating()
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
   self.Pck_invoke_s[c_RequestHennaRemoveList().invoke] = c_RequestHennaRemoveList()
   self.Pck_invoke_s[c_RequestHennaItemRemoveInfo().invoke] = c_RequestHennaItemRemoveInfo()
   self.Pck_invoke_s[c_RequestHennaRemove().invoke] = c_RequestHennaRemove()
   self.Pck_invoke_s[c_RequestAcquireSkillInfo().invoke] = c_RequestAcquireSkillInfo()
   self.Pck_invoke_s[c_SendBypassBuildCmd().invoke] = c_SendBypassBuildCmd()
   self.Pck_invoke_s[c_ReqMoveToLocationInVehicle().invoke] = c_ReqMoveToLocationInVehicle()
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
   self.Pck_invoke_s[c_RequestGMList().invoke] = c_RequestGMList()
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
   self.Pck_invoke_s[c_ReqPrivateStoreQuitSell().invoke] = c_ReqPrivateStoreQuitSell()
   self.Pck_invoke_s[c_SetPrivateStoreMsgSell().invoke] = c_SetPrivateStoreMsgSell()
   self.Pck_invoke_s[c_RequestPetGetItem().invoke] = c_RequestPetGetItem()
   self.Pck_invoke_s[c_ReqPrivateStoreManageBuy().invoke] = c_ReqPrivateStoreManageBuy()
   self.Pck_invoke_s[c_SetPrivateStoreListBuy().invoke] = c_SetPrivateStoreListBuy()
   self.Pck_invoke_s[c_ReqPrivateStoreQuitBuy().invoke] = c_ReqPrivateStoreQuitBuy()
   self.Pck_invoke_s[c_SetPrivateStoreMsgBuy().invoke] = c_SetPrivateStoreMsgBuy()
   self.Pck_invoke_s[c_RequestPrivateStoreSell().invoke] = c_RequestPrivateStoreSell()
   self.Pck_invoke_s[c_RequestSkillCoolTime().invoke] = c_RequestSkillCoolTime()
   self.Pck_invoke_s[c_ReqPackageSendableItemList().invoke] = c_ReqPackageSendableItemList()
   self.Pck_invoke_s[c_RequestPackageSend().invoke] = c_RequestPackageSend()
   self.Pck_invoke_s[c_RequestBlock().invoke] = c_RequestBlock()
   self.Pck_invoke_s[c_RequestSiegeInfo().invoke] = c_RequestSiegeInfo()
   self.Pck_invoke_s[c_RequestSiegeAttackerList().invoke] = c_RequestSiegeAttackerList()
   self.Pck_invoke_s[c_RequestSiegeDefenderList().invoke] = c_RequestSiegeDefenderList()
   self.Pck_invoke_s[c_RequestJoinSiege().invoke] = c_RequestJoinSiege()
   self.Pck_invoke_s[c_ReqConfirmSiegeWaitingList().invoke] = c_ReqConfirmSiegeWaitingList()
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
   self.Pck_invoke_s[c_RequestPreviewItem().invoke] = c_RequestPreviewItem()
   self.Pck_invoke_s[c_RequestSSQStatus().invoke] = c_RequestSSQStatus()
   self.Pck_invoke_s[c_GameGuardReply().invoke] = c_GameGuardReply()
   self.Pck_invoke_s[c_RequestPledgePower().invoke] = c_RequestPledgePower()
   self.Pck_invoke_s[c_RequestMakeMacro().invoke] = c_RequestMakeMacro()
   self.Pck_invoke_s[c_RequestDeleteMacro().invoke] = c_RequestDeleteMacro()
   self.Pck_invoke_s[c_RequestBuyProcure().invoke] = c_RequestBuyProcure()
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
   self.Pck_invoke_s[c_ReqExSetPledgeCrestLarge().invoke] = c_ReqExSetPledgeCrestLarge()
   self.Pck_invoke_s[c_ReqPledgeSetAcademyMaster().invoke] = c_ReqPledgeSetAcademyMaster()
   self.Pck_invoke_s[c_ReqPledgePowerGradeList().invoke] = c_ReqPledgePowerGradeList()
   self.Pck_invoke_s[c_ReqPledgeMemberPowerInfo().invoke] = c_ReqPledgeMemberPowerInfo()
   self.Pck_invoke_s[c_ReqPledgeSetMemberPowerGrade().invoke] = c_ReqPledgeSetMemberPowerGrade()
   self.Pck_invoke_s[c_RequestPledgeMemberInfo().invoke] = c_RequestPledgeMemberInfo()
   self.Pck_invoke_s[c_RequestPledgeWarList().invoke] = c_RequestPledgeWarList()
   self.Pck_invoke_s[c_RequestExFishRanking().invoke] = c_RequestExFishRanking()
   self.Pck_invoke_s[c_RequestPCCafeCouponUse().invoke] = c_RequestPCCafeCouponUse()
   self.Pck_invoke_s[c_RequestDuelStart().invoke] = c_RequestDuelStart()
   self.Pck_invoke_s[c_RequestDuelAnswerStart().invoke] = c_RequestDuelAnswerStart()
   self.Pck_invoke_s[c_RequestExRqItemLink().invoke] = c_RequestExRqItemLink()
   self.Pck_invoke_s[c_MoveToLocationInAirShip().invoke] = c_MoveToLocationInAirShip()
   self.Pck_invoke_s[c_RequestKeyMapping().invoke] = c_RequestKeyMapping()
   self.Pck_invoke_s[c_RequestSaveKeyMapping().invoke] = c_RequestSaveKeyMapping()
   self.Pck_invoke_s[c_ReqExRemoveItemAttribute().invoke] = c_ReqExRemoveItemAttribute()
   self.Pck_invoke_s[c_RequestSaveInventoryOrder().invoke] = c_RequestSaveInventoryOrder()
   self.Pck_invoke_s[c_ReqExitPartyMatchingWaitingRoom().invoke] = c_ReqExitPartyMatchingWaitingRoom()
   self.Pck_invoke_s[c_RequestConfirmTargetItem().invoke] = c_RequestConfirmTargetItem()
   self.Pck_invoke_s[c_RequestConfirmRefinerItem().invoke] = c_RequestConfirmRefinerItem()
   self.Pck_invoke_s[c_RequestConfirmGemStone().invoke] = c_RequestConfirmGemStone()
   self.Pck_invoke_s[c_RequestOlympiadObserverEnd().invoke] = c_RequestOlympiadObserverEnd()
   self.Pck_invoke_s[c_RequestCursedWeaponList().invoke] = c_RequestCursedWeaponList()
   self.Pck_invoke_s[c_RequestCursedWeaponLocation().invoke] = c_RequestCursedWeaponLocation()
   self.Pck_invoke_s[c_ReqPledgeReorganizeMember().invoke] = c_ReqPledgeReorganizeMember()
   self.Pck_invoke_s[c_ReqExMPCCShowPartyMembersInfo().invoke] = c_ReqExMPCCShowPartyMembersInfo()
   self.Pck_invoke_s[c_RequestOlympiadMatchList().invoke] = c_RequestOlympiadMatchList()
   self.Pck_invoke_s[c_RequestAskJoinPartyRoom().invoke] = c_RequestAskJoinPartyRoom()
   self.Pck_invoke_s[c_AnswerJoinPartyRoom().invoke] = c_AnswerJoinPartyRoom()
   self.Pck_invoke_s[c_ReqListPartyMatchingWaitingRoom().invoke] = c_ReqListPartyMatchingWaitingRoom()
   self.Pck_invoke_s[c_ReqExEnchantSkillSafe().invoke] = c_ReqExEnchantSkillSafe()
   self.Pck_invoke_s[c_ReqExEnchantSkillUntrain().invoke] = c_ReqExEnchantSkillUntrain()
   self.Pck_invoke_s[c_ReqExEnchantSkillRouteChange().invoke] = c_ReqExEnchantSkillRouteChange()
   self.Pck_invoke_s[c_ReqExEnchantItemAttribute().invoke] = c_ReqExEnchantItemAttribute()
   self.Pck_invoke_s[c_ExGetOnAirShip().invoke] = c_ExGetOnAirShip()
   self.Pck_invoke_s[c_MoveToLocationAirShip().invoke] = c_MoveToLocationAirShip()
   self.Pck_invoke_s[c_RequestBidItemAuction().invoke] = c_RequestBidItemAuction()
   self.Pck_invoke_s[c_RequestInfoItemAuction().invoke] = c_RequestInfoItemAuction()
   self.Pck_invoke_s[c_RequestExChangeName().invoke] = c_RequestExChangeName()
   self.Pck_invoke_s[c_RequestAllCastleInfo().invoke] = c_RequestAllCastleInfo()
   self.Pck_invoke_s[c_RequestAllFortressInfo().invoke] = c_RequestAllFortressInfo()
   self.Pck_invoke_s[c_RequestAllAgitInfo().invoke] = c_RequestAllAgitInfo()
   self.Pck_invoke_s[c_ReqFortressSiegeInfo().invoke] = c_ReqFortressSiegeInfo()
   self.Pck_invoke_s[c_RequestGetBossRecord().invoke] = c_RequestGetBossRecord()
   self.Pck_invoke_s[c_RequestRefine().invoke] = c_RequestRefine()
   self.Pck_invoke_s[c_ReqConfirmCancelItem().invoke] = c_ReqConfirmCancelItem()
   self.Pck_invoke_s[c_RequestRefineCancel().invoke] = c_RequestRefineCancel()
   self.Pck_invoke_s[c_ReqExMagicSkillUseGround().invoke] = c_ReqExMagicSkillUseGround()
   self.Pck_invoke_s[c_RequestDuelSurrender().invoke] = c_RequestDuelSurrender()
   self.Pck_invoke_s[c_ReqExEnchantSkillInfoDetail().invoke] = c_ReqExEnchantSkillInfoDetail()
   self.Pck_invoke_s[c_ReqExMagicSkillUseGround().invoke] = c_ReqExMagicSkillUseGround()
   self.Pck_invoke_s[c_RequestFortressMapInfo().invoke] = c_RequestFortressMapInfo()
   self.Pck_invoke_s[c_RequestPVPMatchRecord().invoke] = c_RequestPVPMatchRecord()
   self.Pck_invoke_s[c_SetPrivateStoreWholeMsg().invoke] = c_SetPrivateStoreWholeMsg()
   self.Pck_invoke_s[c_RequestDispel().invoke] = c_RequestDispel()
   self.Pck_invoke_s[c_ReqExTryToPutEnchantTargetItem().invoke] = c_ReqExTryToPutEnchantTargetItem()
   self.Pck_invoke_s[c_ReqExTryToPutEnchantSupportItem().invoke] = c_ReqExTryToPutEnchantSupportItem()
   self.Pck_invoke_s[c_ReqExCancelEnchantItem().invoke] = c_ReqExCancelEnchantItem()
   self.Pck_invoke_s[c_ReqChangeNicknameColor().invoke] = c_ReqChangeNicknameColor()
   self.Pck_invoke_s[c_ReqResetNickname().invoke] = c_ReqResetNickname()
   self.Pck_invoke_s[c_RequestExCancelEnchantItem().invoke] = c_RequestExCancelEnchantItem()
   self.Pck_invoke_s[c_ReqWithDrawPremiumItem().invoke] = c_ReqWithDrawPremiumItem()
   self.Pck_invoke_s[c_RequestResetNickname().invoke] = c_RequestResetNickname()
   self.Pck_invoke_s[c_ReqJoinDominionWar().invoke] = c_ReqJoinDominionWar()
   self.Pck_invoke_s[c_ReqDominionInfo().invoke] = c_ReqDominionInfo()
   self.Pck_invoke_s[c_ReqExCubeGameChangeTeam().invoke] = c_ReqExCubeGameChangeTeam()
   self.Pck_invoke_s[c_EndScenePlayer().invoke] = c_EndScenePlayer()
   self.Pck_invoke_s[c_ReqExCubeGameReadyAnswer().invoke] = c_ReqExCubeGameReadyAnswer()
   self.Pck_invoke_s[c_RequestSeedPhase().invoke] = c_RequestSeedPhase()
   self.Pck_invoke_s[c_RequestPostItemList().invoke] = c_RequestPostItemList()
   self.Pck_invoke_s[c_RequestSendPost().invoke] = c_RequestSendPost()
   self.Pck_invoke_s[c_ReqReceivedPostList().invoke] = c_ReqReceivedPostList()
   self.Pck_invoke_s[c_ReqDeleteReceivedPost().invoke] = c_ReqDeleteReceivedPost()
   self.Pck_invoke_s[c_RequestReceivedPost().invoke] = c_RequestReceivedPost()
   self.Pck_invoke_s[c_RequestPostAttachment().invoke] = c_RequestPostAttachment()
   self.Pck_invoke_s[c_ReqRejectPostAttachment().invoke] = c_ReqRejectPostAttachment()
   self.Pck_invoke_s[c_RequestSentPostList().invoke] = c_RequestSentPostList()
   self.Pck_invoke_s[c_RequestDeleteSentPost().invoke] = c_RequestDeleteSentPost()
   self.Pck_invoke_s[c_RequestSentPost().invoke] = c_RequestSentPost()
   self.Pck_invoke_s[c_RequestCancelPost().invoke] = c_RequestCancelPost()
   self.Pck_invoke_s[c_RequestRefundItem().invoke] = c_RequestRefundItem()
   self.Pck_invoke_s[c_RequestBuySellUIClose().invoke] = c_RequestBuySellUIClose()
   self.Pck_invoke_s[c_ReqPartyLootModification().invoke] = c_ReqPartyLootModification()
   self.Pck_invoke_s[c_AnswerPartyLootModification().invoke] = c_AnswerPartyLootModification()
   self.Pck_invoke_s[c_AnswerCoupleAction().invoke] = c_AnswerCoupleAction()
   self.Pck_invoke_s[c_BrEventRankerList().invoke] = c_BrEventRankerList()
   self.Pck_invoke_s[c_AskMembership().invoke] = c_AskMembership()
   self.Pck_invoke_s[c_ReqAddExpandQuestAlarm().invoke] = c_ReqAddExpandQuestAlarm()
   self.Pck_invoke_s[c_RequestVoteNew().invoke] = c_RequestVoteNew()
   self.Pck_invoke_s[c_RequestBRGamePoint().invoke] = c_RequestBRGamePoint()
   self.Pck_invoke_s[c_RequestBRProductList().invoke] = c_RequestBRProductList()
   self.Pck_invoke_s[c_RequestBRProductInfo().invoke] = c_RequestBRProductInfo()
   self.Pck_invoke_s[c_RequestBRBuyProduct().invoke] = c_RequestBRBuyProduct()
   self.Pck_invoke_s[c_RequestBRRecentProductList().invoke] = c_RequestBRRecentProductList()
   self.Pck_invoke_s[c_BrMinigameLoadScores().invoke] = c_BrMinigameLoadScores()
   self.Pck_invoke_s[c_BrMinigameInsertScore().invoke] = c_BrMinigameInsertScore()
   self.Pck_invoke_s[c_BrLectureMark().invoke] = c_BrLectureMark()
   self.Pck_invoke_s[c_RequestBookMarkSlotInfo().invoke] = c_RequestBookMarkSlotInfo()
   self.Pck_invoke_s[c_RequestSaveBookMarkSlot().invoke] = c_RequestSaveBookMarkSlot()
   self.Pck_invoke_s[c_RequestModifyBookMarkSlot().invoke] = c_RequestModifyBookMarkSlot()
   self.Pck_invoke_s[c_RequestDeleteBookMarkSlot().invoke] = c_RequestDeleteBookMarkSlot()
   self.Pck_invoke_s[c_RequestTeleportBookMark().invoke] = c_RequestTeleportBookMark()
   self.Pck_invoke_s[c_RequestChangeBookMarkSlot().invoke] = c_RequestChangeBookMarkSlot()
   self.Pck_invoke_s[c_ReqExCubeGameChangeTeam().invoke] = c_ReqExCubeGameChangeTeam()
   return self.Pck_invoke_s
 def get_Pck_invoke_s(self):
   self.Pck_invoke_c[s_Revive().invoke] = s_Revive()
   self.Pck_invoke_c[s_SpawnItem().invoke] = s_SpawnItem()
   self.Pck_invoke_c[s_SellList().invoke] = s_SellList()
   self.Pck_invoke_c[s_BuyList().invoke] = s_BuyList()
   self.Pck_invoke_c[s_DeleteObject().invoke] = s_DeleteObject()
   self.Pck_invoke_c[s_CharSelectInfo().invoke] = s_CharSelectInfo()
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
   self.Pck_invoke_c[s_KeyInit().invoke] = s_KeyInit()
   self.Pck_invoke_c[s_MoveToLocation().invoke] = s_MoveToLocation()
   self.Pck_invoke_c[s_NpcSay().invoke] = s_NpcSay()
   self.Pck_invoke_c[s_CharInfo().invoke] = s_CharInfo()
   self.Pck_invoke_c[s_UserInfo().invoke] = s_UserInfo()
   self.Pck_invoke_c[s_Attack().invoke] = s_Attack()
   self.Pck_invoke_c[s_AskJoinParty().invoke] = s_AskJoinParty()
   self.Pck_invoke_c[s_JoinParty().invoke] = s_JoinParty()
   self.Pck_invoke_c[s_WareHouseDepositList().invoke] = s_WareHouseDepositList()
   self.Pck_invoke_c[s_WareHouseWithdrawList().invoke] = s_WareHouseWithdrawList()
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
   self.Pck_invoke_c[s_FriendPacket().invoke] = s_FriendPacket()
   self.Pck_invoke_c[s_FriendStatusPacket().invoke] = s_FriendStatusPacket()
   self.Pck_invoke_c[s_L2FriendSay().invoke] = s_L2FriendSay()
   self.Pck_invoke_c[s_ValidateLocation().invoke] = s_ValidateLocation()
   self.Pck_invoke_c[s_StartRotation().invoke] = s_StartRotation()
   self.Pck_invoke_c[s_ShowBoard().invoke] = s_ShowBoard()
   self.Pck_invoke_c[s_ChooseInventoryItem().invoke] = s_ChooseInventoryItem()
   self.Pck_invoke_c[s_MoveToLocationInVehicle().invoke] = s_MoveToLocationInVehicle()
   self.Pck_invoke_c[s_StopMoveInVehicle().invoke] = s_StopMoveInVehicle()
   self.Pck_invoke_c[s_ValidateLocationInVehicle().invoke] = s_ValidateLocationInVehicle()
   self.Pck_invoke_c[s_TradeOtherDone().invoke] = s_TradeOtherDone()
   self.Pck_invoke_c[s_FriendAddRequest().invoke] = s_FriendAddRequest()
   self.Pck_invoke_c[s_LeaveWorld().invoke] = s_LeaveWorld()
   self.Pck_invoke_c[s_MagicEffectIcons().invoke] = s_MagicEffectIcons()
   self.Pck_invoke_c[s_QuestList().invoke] = s_QuestList()
   self.Pck_invoke_c[s_EnchantResult().invoke] = s_EnchantResult()
   self.Pck_invoke_c[s_PledgeShowMemberListDeleteAll().invoke] = s_PledgeShowMemberListDeleteAll()
   self.Pck_invoke_c[s_PledgeInfo().invoke] = s_PledgeInfo()
   self.Pck_invoke_c[s_Ride().invoke] = s_Ride()
   self.Pck_invoke_c[s_PledgeShowInfoUpdate().invoke] = s_PledgeShowInfoUpdate()
   self.Pck_invoke_c[s_AcquireSkillInfo().invoke] = s_AcquireSkillInfo()
   self.Pck_invoke_c[s_ServerObjectInfo().invoke] = s_ServerObjectInfo()
   self.Pck_invoke_c[s_GMHide().invoke] = s_GMHide()
   self.Pck_invoke_c[s_AcquireSkillDone().invoke] = s_AcquireSkillDone()
   self.Pck_invoke_c[s_GMViewCharacterInfo().invoke] = s_GMViewCharacterInfo()
   self.Pck_invoke_c[s_GMViewPledgeInfo().invoke] = s_GMViewPledgeInfo()
   self.Pck_invoke_c[s_GMViewSkillInfo().invoke] = s_GMViewSkillInfo()
   self.Pck_invoke_c[s_GMViewQuestInfo().invoke] = s_GMViewQuestInfo()
   self.Pck_invoke_c[s_GMViewItemList().invoke] = s_GMViewItemList()
   self.Pck_invoke_c[s_GMViewWarehouseWithdrawList().invoke] = s_GMViewWarehouseWithdrawList()
   self.Pck_invoke_c[s_ListPartyWating().invoke] = s_ListPartyWating()
   self.Pck_invoke_c[s_PartyMatchDetail().invoke] = s_PartyMatchDetail()
   self.Pck_invoke_c[s_PlaySound().invoke] = s_PlaySound()
   self.Pck_invoke_c[s_StaticObject().invoke] = s_StaticObject()
   self.Pck_invoke_c[s_PrivateStoreManageListSell().invoke] = s_PrivateStoreManageListSell()
   self.Pck_invoke_c[s_PrivateStoreListSell().invoke] = s_PrivateStoreListSell()
   self.Pck_invoke_c[s_PrivateStoreMsgSell().invoke] = s_PrivateStoreMsgSell()
   self.Pck_invoke_c[s_ShowMiniMap().invoke] = s_ShowMiniMap()
   self.Pck_invoke_c[s_TutorialShowHtml().invoke] = s_TutorialShowHtml()
   self.Pck_invoke_c[s_TutorialShowQuestionMark().invoke] = s_TutorialShowQuestionMark()
   self.Pck_invoke_c[s_TutorialEnableClientEvent().invoke] = s_TutorialEnableClientEvent()
   self.Pck_invoke_c[s_TutorialClose().invoke] = s_TutorialClose()
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
   self.Pck_invoke_c[s_PrivateStoreManageListBuy().invoke] = s_PrivateStoreManageListBuy()
   self.Pck_invoke_c[s_PrivateStoreListBuy().invoke] = s_PrivateStoreListBuy()
   self.Pck_invoke_c[s_PrivateStoreMsgBuy().invoke] = s_PrivateStoreMsgBuy()
   self.Pck_invoke_c[s_VehicleStarted().invoke] = s_VehicleStarted()
   self.Pck_invoke_c[s_SkillCoolTime().invoke] = s_SkillCoolTime()
   self.Pck_invoke_c[s_PackageToList().invoke] = s_PackageToList()
   self.Pck_invoke_c[s_SiegeInfo().invoke] = s_SiegeInfo()
   self.Pck_invoke_c[s_SiegeAttackerList().invoke] = s_SiegeAttackerList()
   self.Pck_invoke_c[s_SiegeDefenderList().invoke] = s_SiegeDefenderList()
   self.Pck_invoke_c[s_NicknameChanged().invoke] = s_NicknameChanged()
   self.Pck_invoke_c[s_PledgeStatusChanged().invoke] = s_PledgeStatusChanged()
   self.Pck_invoke_c[s_RelationChanged().invoke] = s_RelationChanged()
   self.Pck_invoke_c[s_OnEventTrigger().invoke] = s_OnEventTrigger()
   self.Pck_invoke_c[s_SetSummonRemainTime().invoke] = s_SetSummonRemainTime()
   self.Pck_invoke_c[s_PackageSendableList().invoke] = s_PackageSendableList()
   self.Pck_invoke_c[s_Earthquake().invoke] = s_Earthquake()
   self.Pck_invoke_c[s_FlyToLocation().invoke] = s_FlyToLocation()
   self.Pck_invoke_c[s_SpecialCamera().invoke] = s_SpecialCamera()
   self.Pck_invoke_c[s_NormalCamera().invoke] = s_NormalCamera()
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
   self.Pck_invoke_c[s_HennaItemDrawInfo().invoke] = s_HennaItemDrawInfo()
   self.Pck_invoke_c[s_HennaInfo().invoke] = s_HennaInfo()
   self.Pck_invoke_c[s_HennaRemoveList().invoke] = s_HennaRemoveList()
   self.Pck_invoke_c[s_HennaItemRemoveInfo().invoke] = s_HennaItemRemoveInfo()
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
   self.Pck_invoke_c[s_ClientSetTime().invoke] = s_ClientSetTime()
   self.Pck_invoke_c[s_PartySpelled().invoke] = s_PartySpelled()
   self.Pck_invoke_c[s_ShopPreviewList().invoke] = s_ShopPreviewList()
   self.Pck_invoke_c[s_ShopPreviewInfo().invoke] = s_ShopPreviewInfo()
   self.Pck_invoke_c[s_EtcStatusUpdate().invoke] = s_EtcStatusUpdate()
   self.Pck_invoke_c[s_ShortBuffStatusUpdate().invoke] = s_ShortBuffStatusUpdate()
   self.Pck_invoke_c[s_AgitDecoInfo().invoke] = s_AgitDecoInfo()
   self.Pck_invoke_c[s_ExRegMax().invoke] = s_ExRegMax()
   self.Pck_invoke_c[s_ExPartyRoomMember().invoke] = s_ExPartyRoomMember()
   self.Pck_invoke_c[s_ExClosePartyRoom().invoke] = s_ExClosePartyRoom()
   self.Pck_invoke_c[s_ExManagePartyRoomMember().invoke] = s_ExManagePartyRoomMember()
   self.Pck_invoke_c[s_ExAutoSoulShot().invoke] = s_ExAutoSoulShot()
   self.Pck_invoke_c[s_ExEventMatchMessage().invoke] = s_ExEventMatchMessage()
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
   self.Pck_invoke_c[s_ExOlympiadMatchEnd().invoke] = s_ExOlympiadMatchEnd()
   self.Pck_invoke_c[s_ExMailArrived().invoke] = s_ExMailArrived()
   self.Pck_invoke_c[s_ExStorageMaxCount().invoke] = s_ExStorageMaxCount()
   self.Pck_invoke_c[s_ExMultiPartyCommandChannelInfo().invoke] = s_ExMultiPartyCommandChannelInfo()
   self.Pck_invoke_c[s_ExPCCafePointInfo().invoke] = s_ExPCCafePointInfo()
   self.Pck_invoke_c[s_ExSetCompassZoneCode().invoke] = s_ExSetCompassZoneCode()
   self.Pck_invoke_c[s_ExGetBossRecord().invoke] = s_ExGetBossRecord()
   self.Pck_invoke_c[s_ExAskJoinPartyRoom().invoke] = s_ExAskJoinPartyRoom()
   self.Pck_invoke_c[s_ExListPartyMatchingWaitingRoom().invoke] = s_ExListPartyMatchingWaitingRoom()
   self.Pck_invoke_c[s_ExShowAdventurerGuideBook().invoke] = s_ExShowAdventurerGuideBook()
   self.Pck_invoke_c[s_ExShowScreenMessage().invoke] = s_ExShowScreenMessage()
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
   self.Pck_invoke_c[s_ExMPCCPartyInfoUpdate().invoke] = s_ExMPCCPartyInfoUpdate()
   self.Pck_invoke_c[s_ExPlayScene().invoke] = s_ExPlayScene()
   self.Pck_invoke_c[s_ExSpawnEmitter().invoke] = s_ExSpawnEmitter()
   self.Pck_invoke_c[s_ExEnchantSkillInfoDetail().invoke] = s_ExEnchantSkillInfoDetail()
   self.Pck_invoke_c[s_ExBasicActionList().invoke] = s_ExBasicActionList()
   self.Pck_invoke_c[s_ExAirShipInfo().invoke] = s_ExAirShipInfo()
   self.Pck_invoke_c[s_ExAttributeEnchantResult().invoke] = s_ExAttributeEnchantResult()
   self.Pck_invoke_c[s_ExChooseInventoryAttributeItem().invoke] = s_ExChooseInventoryAttributeItem()
   self.Pck_invoke_c[s_ExGetOnAirShip().invoke] = s_ExGetOnAirShip()
   self.Pck_invoke_c[s_ExGetOffAirShip().invoke] = s_ExGetOffAirShip()
   self.Pck_invoke_c[s_ExMoveToLocationAirShip().invoke] = s_ExMoveToLocationAirShip()
   self.Pck_invoke_c[s_ExStopMoveAirShip().invoke] = s_ExStopMoveAirShip()
   self.Pck_invoke_c[s_ExShowTrace().invoke] = s_ExShowTrace()
   self.Pck_invoke_c[s_ExItemAuctionInfoPacket().invoke] = s_ExItemAuctionInfoPacket()
   self.Pck_invoke_c[s_ExNeedToChangeName().invoke] = s_ExNeedToChangeName()
   self.Pck_invoke_c[s_ExPartyPetWindowDelete().invoke] = s_ExPartyPetWindowDelete()
   self.Pck_invoke_c[s_ExRpItemLink().invoke] = s_ExRpItemLink()
   self.Pck_invoke_c[s_ExMoveToLocationInAirShip().invoke] = s_ExMoveToLocationInAirShip()
   self.Pck_invoke_c[s_ExStopMoveInAirShip().invoke] = s_ExStopMoveInAirShip()
   self.Pck_invoke_c[s_ExValidateLocationInAirShip().invoke] = s_ExValidateLocationInAirShip()
   self.Pck_invoke_c[s_ExUISetting().invoke] = s_ExUISetting()
   self.Pck_invoke_c[s_ExShowBaseAttributeCancelWindow().invoke] = s_ExShowBaseAttributeCancelWindow()
   self.Pck_invoke_c[s_ExBaseAttributeCancelResult().invoke] = s_ExBaseAttributeCancelResult()
   self.Pck_invoke_c[s_ExSubPledgeSkillAdd().invoke] = s_ExSubPledgeSkillAdd()
   self.Pck_invoke_c[s_ExShowProcureCropDetail().invoke] = s_ExShowProcureCropDetail()
   self.Pck_invoke_c[s_ExHeroList().invoke] = s_ExHeroList()
   self.Pck_invoke_c[s_ExOlympiadUserInfo().invoke] = s_ExOlympiadUserInfo()
   self.Pck_invoke_c[s_ExOlympiadSpelledInfo().invoke] = s_ExOlympiadSpelledInfo()
   self.Pck_invoke_c[s_ExOlympiadMode().invoke] = s_ExOlympiadMode()
   self.Pck_invoke_c[s_ExShowFortressMapInfo().invoke] = s_ExShowFortressMapInfo()
   self.Pck_invoke_c[s_ExPrivateStoreSetWholeMsg().invoke] = s_ExPrivateStoreSetWholeMsg()
   self.Pck_invoke_c[s_ExPutEnchantTargetItemResult().invoke] = s_ExPutEnchantTargetItemResult()
   self.Pck_invoke_c[s_ExPutEnchantSupportItemResult().invoke] = s_ExPutEnchantSupportItemResult()
   self.Pck_invoke_c[s_ExRequestChangeNicknameColor().invoke] = s_ExRequestChangeNicknameColor()
   self.Pck_invoke_c[s_ExGetBookMarkInfoPacket().invoke] = s_ExGetBookMarkInfoPacket()
   self.Pck_invoke_c[s_ExNotifyPremiumItem().invoke] = s_ExNotifyPremiumItem()
   self.Pck_invoke_c[s_ExGetPremiumItemList().invoke] = s_ExGetPremiumItemList()
   self.Pck_invoke_c[s_NpcQuestHtmlMessage().invoke] = s_NpcQuestHtmlMessage()
   self.Pck_invoke_c[s_ExSendUIEvent().invoke] = s_ExSendUIEvent()
   self.Pck_invoke_c[s_ExBirthdayPopup().invoke] = s_ExBirthdayPopup()
   self.Pck_invoke_c[s_ExShowDominionRegistry().invoke] = s_ExShowDominionRegistry()
   self.Pck_invoke_c[s_ExReplyDominionInfo().invoke] = s_ExReplyDominionInfo()
   self.Pck_invoke_c[s_ExShowOwnthingPos().invoke] = s_ExShowOwnthingPos()
   self.Pck_invoke_c[s_ExStartScenePlayer().invoke] = s_ExStartScenePlayer()
   self.Pck_invoke_c[s_ExAirShipTeleportList().invoke] = s_ExAirShipTeleportList()
   self.Pck_invoke_c[s_ExVitalityPointInfo().invoke] = s_ExVitalityPointInfo()
   self.Pck_invoke_c[s_ExShowSeedMapInfo().invoke] = s_ExShowSeedMapInfo()
   self.Pck_invoke_c[s_ExDominionWarStart().invoke] = s_ExDominionWarStart()
   self.Pck_invoke_c[s_ExDominionWarEnd().invoke] = s_ExDominionWarEnd()
   self.Pck_invoke_c[s_ExEnchantSkillResult().invoke] = s_ExEnchantSkillResult()
   self.Pck_invoke_c[s_ExNoticePostArrived().invoke] = s_ExNoticePostArrived()
   self.Pck_invoke_c[s_ExShowReceivedPostList().invoke] = s_ExShowReceivedPostList()
   self.Pck_invoke_c[s_ExReplyReceivedPost().invoke] = s_ExReplyReceivedPost()
   self.Pck_invoke_c[s_ExShowSentPostList().invoke] = s_ExShowSentPostList()
   self.Pck_invoke_c[s_ExReplySentPost().invoke] = s_ExReplySentPost()
   self.Pck_invoke_c[s_ExReplyPostItemList().invoke] = s_ExReplyPostItemList()
   self.Pck_invoke_c[s_ExChangePostState().invoke] = s_ExChangePostState()
   self.Pck_invoke_c[s_ExNoticePostSent().invoke] = s_ExNoticePostSent()
   self.Pck_invoke_c[s_ExAskCoupleAction().invoke] = s_ExAskCoupleAction()
   self.Pck_invoke_c[s_ExBrLoadEventTopRankers().invoke] = s_ExBrLoadEventTopRankers()
   self.Pck_invoke_c[s_ExChangeNpcState().invoke] = s_ExChangeNpcState()
   self.Pck_invoke_c[s_ExAskModifyPartyLooting().invoke] = s_ExAskModifyPartyLooting()
   self.Pck_invoke_c[s_ExSetPartyLooting().invoke] = s_ExSetPartyLooting()
   self.Pck_invoke_c[s_ExRotation().invoke] = s_ExRotation()
   self.Pck_invoke_c[s_ExQuestItemList().invoke] = s_ExQuestItemList()
   self.Pck_invoke_c[s_ExVoteSystemInfo().invoke] = s_ExVoteSystemInfo()
   self.Pck_invoke_c[s_ExBrPremiumState().invoke] = s_ExBrPremiumState()
   self.Pck_invoke_c[s_ExBrBroadcastEventState().invoke] = s_ExBrBroadcastEventState()
   self.Pck_invoke_c[s_ExBrExtraUserInfo().invoke] = s_ExBrExtraUserInfo()
   self.Pck_invoke_c[s_ExBrBuffEventState().invoke] = s_ExBrBuffEventState()
   self.Pck_invoke_c[s_ExCubeGameTeamList().invoke] = s_ExCubeGameTeamList()
   self.Pck_invoke_c[s_ExCubeGameAddPlayer().invoke] = s_ExCubeGameAddPlayer()
   self.Pck_invoke_c[s_ExCubeGameRemovePlayer().invoke] = s_ExCubeGameRemovePlayer()
   self.Pck_invoke_c[s_ExCubeGameChangeTimeToStart().invoke] = s_ExCubeGameChangeTimeToStart()
   self.Pck_invoke_c[s_ExCubeGameRequestReady().invoke] = s_ExCubeGameRequestReady()
   self.Pck_invoke_c[s_ExCubeGameChangeTeam().invoke] = s_ExCubeGameChangeTeam()
   self.Pck_invoke_c[s_ExCubeGameCloseUI().invoke] = s_ExCubeGameCloseUI()
   self.Pck_invoke_c[s_ExCubeGameExtendedChangePoints().invoke] = s_ExCubeGameExtendedChangePoints()
   self.Pck_invoke_c[s_ExCubeGameEnd().invoke] = s_ExCubeGameEnd()
   self.Pck_invoke_c[s_ExCubeGameChangePoints().invoke] = s_ExCubeGameChangePoints()
   self.Pck_invoke_c[s_ExBuyList().invoke] = s_ExBuyList()
   self.Pck_invoke_c[s_ExBuySellListPacket().invoke] = s_ExBuySellListPacket()
   return self.Pck_invoke_c
