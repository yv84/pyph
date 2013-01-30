import numpy
import gs_f_pck_factory

class Me():
  def __init__(self, parent):
    self.pck_f = parent
    self.name = ''
    self.ObjectID = 0
    self.ClanID = 0
    self.AllyID = 0
    self.CurrentCP = 0
    self.CurrentHP = 0
    self.CurrentMP = 0
    self.MaxCP = 0
    self.MaxHP = 0
    self.MaxMP = 0
    self.X = 0
    self.Y = 0
    self.Z = 0
    self.destX = 0
    self.destY = 0
    self.destZ = 0
    self.alive = 0
    self.Race = 0
    self.ClassIDGetClassID = 0
    self.Exp = 0
    self.Level = 0
    self.TargetID = 0
    self.FollowTargetID = 0
    self.FollowDistance = 0
    self.isRunning = 0
    self.isInCombat = 0
    self.AbnormalEffect = 0
    self.Degree = 0
    self.Side = 0
  def s_Die(self, np_arr):
    self.alive = 0
  def s_Revive(self, np_arr):
    self.alive = 1
  def s_CharSelected(self, np_arr):
    self.name       = self.pck_f.l2ByteToStringNp(np_arr['Name'])
    self.CharID     = np_arr['CharID']
    self.ClanID     = np_arr['ClanID']
    self.CurrentHP  = np_arr['CurrentHP']
    self.CurrentMP  = np_arr['CurrentMP']
    self.X          = np_arr['X']
    self.Y          = np_arr['Y']
    self.Z          = np_arr['Z']
    self.Race       = np_arr['Race']
    self.Exp        = np_arr['Exp']
    self.Level      = np_arr['Level']
  def s_StatusUpdate(self, np_arr): pass
  def s_TargetSelected(self, np_arr):
    self.ObjectID = np_arr['ObjectID']
    self.TargetID = np_arr['TargetID']
    self.X = np_arr['X']
    self.Y = np_arr['Y']
    self.Z = np_arr['Z']
  def s_TargetUnselected(self, np_arr):
    self.TargetID = np_arr['TargetID']
    self.X = np_arr['X']
    self.Y = np_arr['Y']
    self.Z = np_arr['Z']
  def s_MoveToLocation(self, np_arr):
    self.CharID = np_arr['CharID']
    self.destX = np_arr['ToX']
    self.destY = np_arr['ToY']
    self.destZ = np_arr['ToZ']
    self.X = np_arr['OriginX']
    self.Y = np_arr['OriginY']
    self.Z = np_arr['OriginZ']
  def s_CharInfo(self, np_arr):
    self.ObjectID = np_arr['ObjectID']
    self.X = np_arr['X']
    self.Y = np_arr['Y']
    self.Z = np_arr['Z']
    self.Name = self.pck_f.l2ByteToStringNp(np_arr['Name'])
    self.ClassIDGetClassID = np_arr['ClassIDGetClassID']
    self.ClanID = np_arr['ClanID']
    self.isRunning = np_arr['isRunning']
    self.isInCombat = np_arr['isInCombat']
    self.AbnormalEffect = np_arr['AbnormalEffect']
  def s_MoveToPawn(self, np_arr):
    self.CharID = np_arr['CreatureObjId']
    self.FollowTargetID = np_arr['TargetObjID']
    self.FollowDistance = np_arr['Distance']
    self.destX = np_arr['CreatureX']
    self.destY = np_arr['CreatureY']
    self.destZ = np_arr['CreatureZ']
    self.X = np_arr['TargetX']
    self.Y = np_arr['TargetY']
    self.Z = np_arr['TargetZ']
  def s_ValidateLocation(self, np_arr):
    self.CharID = np_arr['CharID']
    self.X = np_arr['X']
    self.Y = np_arr['Y']
    self.Z = np_arr['Z']
  def s_StartRotation(self, np_arr):
    self.CharId = np_arr['CharId']
    self.Degree = np_arr['Degree']
    self.Side = np_arr['Side']
  def s_MyTargetSelected(self, np_arr):
    self.TargetID = np_arr['ObjectID']
  def s_ExBrExtraUserInfo(self, np_arr): pass
    
    

class Party():
  def __init__(self, parent):
    self.ObjectID = 0
    self.ClanID = 0
    self.CurrentCP = 0
    self.CurrentHP = 0
    self.CurrentMP = 0
    self.MaxCP = 0
    self.MaxHP = 0
    self.MaxMP = 0
    self.X = 0
    self.Y = 0
    self.Z = 0
    self.alive = 0
    self.Level = 0
    self.TargetID = 0
    self.NpcTypeIdGetNpcId = 0
    self.IsAttackable = 0
    self.isRunning = 0
    self.isInCombat = 0
  def s_PartySmallWindowAll(self, np_arr): pass
  def s_PartySmallWindowAdd(self, np_arr): pass
  def s_PartySmallWindowDeleteAll(self, np_arr): pass
  def s_PartySmallWindowDelete(self, np_arr): pass
  def s_PartySmallWindowUpdate(self, np_arr): pass
  

class User():
  def __init__(self, parent):
    self.ObjectID = 0
    self.ClanID = 0
    self.AllyID = 0
    self.CurrentCP = 0
    self.CurrentHP = 0
    self.CurrentMP = 0
    self.MaxCP = 0
    self.MaxHP = 0
    self.MaxMP = 0
    self.X = 0
    self.Y = 0
    self.Z = 0
    self.alive = 0
    self.Level = 0
    self.TargetID = 0
    self.IsAttackable = 0
    self.isRunning = 0
    self.isInCombat = 0
    self.ClassIDGetClassID = 0
    self.PvPFlag = 0
    self.AbnormalEffect = 0
    self.CurrentLoad = 0
    self.MaxLoad = 0
    self.WeaponEquipment = 0
  def s_UserInfo(self, np_arr):
    self.ObjectID = np_arr['ObjectID']
    self.X = np_arr['X']
    self.Y = np_arr['Y']
    self.Z = np_arr['Z']
    self.Name = self.pck_f.l2ByteToStringNp(np_arr['Name'])
    self.ClassIDGetClassID = np_arr['ClassIDGetClassID']
    self.ClanID = np_arr['ClanID']
    self.AllyID = np_arr['AllyID']
    self.PvPFlag = np_arr['self.PvPFlag = ']
    self.MaxHP = np_arr['MaxHP']
    self.CurrentHP = np_arr['CurrentHP']
    self.MaxHP = np_arr['MaxMP']
    self.CurrentHP = np_arr['CurrentMP']  
    self.isRunning = np_arr['isRunning']
    self.AbnormalEffect = np_arr['AbnormalEffect']
    self.CurrentLoad = np_arr['CurrentLoad']
    self.MaxLoad = np_arr['MaxLoad']
    self.WeaponEquipment = np_arr['WeaponEquipment']

class ObfNpc():
  def __init__(self, parent):
    self.ObfObjectID = 0
  def s_NpcInfo(self, np_arr):
    self.ObjectID   =  np_arr['ObjectID']
    self.NpcTypeIdGetNpcId = np_arr['NpcTypeIdGetNpcId']
    self.IsAttackable = np_arr['IsAttackable']
    self.X          = np_arr['X']
    self.Y          = np_arr['Y']
    self.Z          = np_arr['Z']
    self.isRunning  = np_arr['isRunning']
    self.isInCombat = np_arr['isInCombat']

class Npc():
  def __init__(self, parent):
    self.ObfObjectID = 0
    self.ObjectID = 0
    self.ClanID = 0
    self.CurrentCP = 0
    self.CurrentHP = 0
    self.CurrentMP = 0
    self.MaxCP = 0
    self.MaxHP = 0
    self.MaxMP = 0
    self.X = 0
    self.Y = 0
    self.Z = 0
    self.alive = 0
    self.Level = 0
    self.TargetID = 0
    self.NpcTypeIdGetNpcId = 0
    self.IsAttackable = 0
    self.isRunning = 0
    self.isInCombat = 0
  def s_DeleteObject(self, np_arr): pass
  def s_NpcInfo(self, np_arr):
    self.ObjectID   =  np_arr['ObjectID']
    self.NpcTypeIdGetNpcId = np_arr['NpcTypeIdGetNpcId']
    self.IsAttackable = np_arr['IsAttackable']
    self.X          = np_arr['X']
    self.Y          = np_arr['Y']
    self.Z          = np_arr['Z']
    self.isRunning  = np_arr['isRunning']
    self.isInCombat = np_arr['isInCombat']
  def s_StatusUpdate(self, np_arr): pass

class Item():
  def __init__(self, parent):
    self.ObjectID = 0
    self.DroppedBy = 0
    self.X = 0
    self.Y = 0
    self.Z = 0
    self.Stackable = 0
    self.Count = 0
  def s_SpawnItem(self, np_arr): pass
  def s_DeleteObject(self, np_arr): pass
  def s_DropItem(self, np_arr):
    self.ObjectID = np_arr['ObjectID']
    self.DroppedBy = np_arr['PlayerID']
    self.X = np_arr['X']
    self.Y = np_arr['Y']
    self.Z = np_arr['Z']
    self.Stackable = np_arr['Stackable']
    self.Count = np_arr['Count']
  def s_GetItem(self, np_arr): pass


class Inventory():
  def __init__(self, parent):
    self.ItemTypeID = 0
    self.ObjectID = 0
    self.LocationSlot = 0
    self.Amount = 0
    self.isEquipped = 0
    self.BodyPart = 0
    self.ItemIDGetFunc01 = 0
  def s_ItemList(self, np_arr):
    self.ItemTypeID = np_arr['ItemTypeID']
    self.ObjectID = np_arr['ObjectID']
    self.LocationSlot = np_arr['LocationSlot']
    self.Amount = np_arr['Amount']
    self.isEquipped = np_arr['isEquipped']
    self.BodyPart = np_arr['BodyPart']
  def s_InventoryUpdate(self, np_arr):
    self.ItemTypeID = np_arr['ItemType1']
    self.ObjectID = np_arr['ObjectID']
    self.LocationSlot = np_arr['LocationSlot']
    self.Amount = np_arr['Quantity']
    self.Equipped = np_arr['Equipped']
    self.BodyPart = np_arr['BodyPart']
  def s_ChooseInventoryItem(self, np_arr):
    self.ItemIDGetFunc01 = np_arr['ItemIDGetFunc01']


class Effecttime():
  def __init__(self, parent):
    self.ID = 0
    self.Level = 0
    self.Duration = 0
    self.name = ''

class Skill():
  def __init__(self, parent):
    self.ID = 0
    self.isPassive = 0
    self.level = 0
    self.name = ''
class Abnormal():
  def __init__(self, parent):
    self.skillIDGetSkill = 0
    self.SkillLevel = 0
    self.Duration = 0
  def s_AbnormalStatusUpdate(self, np_arr):
    self.skillIDGetSkill = np_arr['skillIDGetSkill']
    self.SkillLevel = np_arr['SkillLevel']
    self.Duration = np_arr['Duration']


class SkillUser():
  def s_MagicSkillUse(self, np_arr):
    self.CharID = np_arr['CharID']
    self.TargetID = np_arr['TargetID']
    self.skillIDGetSkill = np_arr['skillIDGetSkill']
    self.SkillLevel = np_arr['SkillLevel']
    self.ReuseDelay = np_arr['ReuseDelay']
    self.X = np_arr['X']
    self.Y = np_arr['Y']
    self.Z = np_arr['Z']
    self.destX = np_arr['TargetX']
    self.destY = np_arr['TargetY']
    self.destZ = np_arr['TargetZ']
  def s_MagicSkillLaunched(self, np_arr): pass
  def s_SkillCoolTime(self, np_arr): pass

class pet():
  def __init__(self, parent): pass
  def s_PetInfo(self, np_arr): pass
  def s_PetItemList(self, np_arr): pass
  def s_PetInventoryUpdate(self, np_arr): pass
  def s_PetStatusUpdate(self, np_arr): pass
  def s_PetDelete(self, np_arr): pass









































