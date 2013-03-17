#===============================================================================
# Vladimir Yudintsev 2012
#===============================================================================
#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
# -*- coding: utf-8 -*-


import time
import numpy
from .import l2_class


class event():

 #структура if/.../elif не эффективна, нужно исправить на обращение к элементу Dict
 def act_s(self, pck, Pck_invoke):
   if pck[:1] == b'\xFE':
     if pck[:3] == b'\xFE01':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_Eself.last_packetRegMaself.last_packet: ", self.last_packet)
     elif pck[:3] == b'\xFE0C':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_Eself.last_packetAutoSoulShot: ", self.last_packet)
     elif pck[:3] == b'\xFE12':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_Eself.last_packetOpenMPCC: ", self.last_packet)
     elif pck[:3] == b'\xFE13':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_Eself.last_packetCloseMPCC: ", self.last_packet)
     elif pck[:3] == b'\xFE16':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_Eself.last_packetShowAgitInfo: ", self.last_packet)
     elif pck[:3] == b'\xFE1A':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_Eself.last_packetAskJoinMPCC: ", self.last_packet)
     elif pck[:3] == b'\xFE2E':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_Eself.last_packetMailArrived: ", self.last_packet)
     elif pck[:3] == b'\xFE41':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_Eself.last_packetRedSky: ", self.last_packet)
     elif pck[:3] == b'\xFE48':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_Eself.last_packetRestartClient: ", self.last_packet)
     elif pck[:3] == b'\xFE5F':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_Eself.last_packetBasicActionList: ", self.last_packet)
     elif pck[:3] == b'\xFE84':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_Eself.last_packetGetBookMarkInfoPacket: ", self.last_packet)
     elif pck[:3] == b'\xFEAA':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_UnknownFEAA: ", self.last_packet)
     elif pck[:3] == b'\xFEAC':
       self.last_packet=self.unpack(pck, Pck_invoke, 'S')
       print("s_Eself.last_packetBrEself.last_packettraUserInfo: ", self.last_packet)









   elif pck[:1] == b'\x00':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_Die: ", self.last_packet)
   elif pck[:1] == b'\x01':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_Revive: ", self.last_packet)
   elif pck[:1] == b'\x05':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_SpawnItem: ", self.last_packet)
   elif pck[:1] == b'\x06':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_SellList: ", self.last_packet)
   elif pck[:1] == b'\x07':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_BuyList: ", self.last_packet)
   elif pck[:1] == b'\x08':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_DeleteObject: ", self.last_packet)
   elif pck[:1] == b'\x09':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_CharSelectionInfo: ", self.last_packet)
   elif pck[:1] == b'\x0A':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_LoginFail: ", self.last_packet)
   elif pck[:1] == b'\x0B':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      self.me.s_CharSelected(self.last_packet)
      #print("s_CharSelected: ", self.l2ByteToStringNp(self.last_packet['Name']))
      print("s_CharSelected: ", self.last_packet)
      print("s_CharSelected: ", self.me.name)
      

   elif pck[:1] == b'\x0C':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_NpcInfo: ", self.last_packet)
   elif pck[:1] == b'\x11':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_ItemList: ", self.last_packet)
   elif pck[:1] == b'\x12':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_SunRise: ", self.last_packet)
   elif pck[:1] == b'\x13':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_SunSet: ", self.last_packet)
   elif pck[:1] == b'\x14':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_TradeStart: ", self.last_packet)
   elif pck[:1] == b'\x16':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_DropItem: ", self.last_packet)
   elif pck[:1] == b'\x17':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_GetItem: ", self.last_packet)
   elif pck[:1] == b'\x18':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_StatusUpdate: ", self.last_packet)
   elif pck[:1] == b'\x19':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_NpcHtmlMessage: ", self.last_packet)
   elif pck[:1] == b'\x1A':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_TradeOwnAdd: ", self.last_packet)
   elif pck[:1] == b'\x1B':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_TradeOtherAdd: ", self.last_packet)
   elif pck[:1] == b'\x1C':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_TradeDone: ", self.last_packet)
   elif pck[:1] == b'\x1F':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_ActionFailed: ", self.last_packet)
   elif pck[:1] == b'\x20':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_ServerClose: ", self.last_packet)
   elif pck[:1] == b'\x21':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_InventoryUpdate: ", self.last_packet)
   elif pck[:1] == b'\x22':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_TeleportToLocation: ", self.last_packet)
   elif pck[:1] == b'\x23':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_TargetSelected: ", self.last_packet)
   elif pck[:1] == b'\x24':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_TargetUnselected: ", self.last_packet)
   elif pck[:1] == b'\x25':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_AutoAttackStart: ", self.last_packet)
   elif pck[:1] == b'\x26':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_AutoAttackStop: ", self.last_packet)
   elif pck[:1] == b'\x27':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_SocialAction: ", self.last_packet)
   elif pck[:1] == b'\x28':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_ChangeMoveType: ", self.last_packet)
   elif pck[:1] == b'\x29':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_ChangeWaitType: ", self.last_packet)
   elif pck[:1] == b'\x2E':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_KeyPacket: ", self.last_packet)
   elif pck[:1] == b'\x2F':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_MoveToLocation: ", self.last_packet)
   elif pck[:1] == b'\x31':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_CharInfo: ", self.last_packet)
   elif pck[:1] == b'\x32':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_UserInfo: ", self.last_packet)
   elif pck[:1] == b'\x33':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_Attack: ", self.last_packet)
   elif pck[:1] == b'\x39':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_AskJoinParty: ", self.last_packet)
   elif pck[:1] == b'\x3A':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_JoinParty: ", self.last_packet)
   elif pck[:1] == b'\x41':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_WareHouseDepositList: ", self.last_packet)
   elif pck[:1] == b'\x42':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_WareHouseWithdrawList: ", self.last_packet)
   elif pck[:1] == b'\x47':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_StopMove: ", self.last_packet)
   elif pck[:1] == b'\x48':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_MagicSkillUse: ", self.last_packet)
   elif pck[:1] == b'\x49':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_MagicSkillCanceled: ", self.last_packet)
   elif pck[:1] == b'\x4A':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_CreatureSay: ", self.last_packet)
   elif pck[:1] == b'\x4B':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_EquipUpdate: ", self.last_packet)
   elif pck[:1] == b'\x4C':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_DoorInfo: ", self.last_packet)
   elif pck[:1] == b'\x4D':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_DoorStatusUpdate: ", self.last_packet)
   elif pck[:1] == b'\x54':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_MagicSkillLaunched: ", self.last_packet)
   elif pck[:1] == b'\x5F':
      self.l2_d['my_skills']=self.unpack(pck, Pck_invoke, 'S')
      print("self.l2_d['my_skills']: ", self.l2_d['my_skills'])
   elif pck[:1] == b'\x61':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_StopRotation: ", self.last_packet)
   elif pck[:1] == b'\x6B':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_SetupGauge: ", self.last_packet)
   elif pck[:1] == b'\x70':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_SendTradeRequest: ", self.last_packet)
   elif pck[:1] == b'\x71':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_RestartResponse: ", self.last_packet)
   elif pck[:1] == b'\x72':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_MoveToPawn: ", self.last_packet)
   elif pck[:1] == b'\x73':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_SSQInfo: ", self.last_packet)
   elif pck[:1] == b'\x74':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_GameGuardQuery: ", self.last_packet)
   elif pck[:1] == b'\x79':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_ValidateLocation: ", self.last_packet)
   elif pck[:1] == b'\x7A':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_StartRotation: ", self.last_packet)
   elif pck[:1] == b'\x7C':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_ChooseInventoryItem: ", self.last_packet)
   elif pck[:1] == b'\x84':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_LeaveWorld: ", self.last_packet)
   elif pck[:1] == b'\x85':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_AbnormalStatusUpdate: ", self.last_packet)
   elif pck[:1] == b'\x86':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_QuestList: ", self.last_packet)
   elif pck[:1] == b'\x90':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_AcquireSkillList: ", self.last_packet)
   elif pck[:1] == b'\x91':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_AcquireSkillInfo: ", self.last_packet)
   elif pck[:1] == b'\x95':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_GMViewCharacterInfo: ", self.last_packet)
   elif pck[:1] == b'\x9F':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_StaticObject: ", self.last_packet)
   elif pck[:1] == b'\xA0':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_PrivateStoreManageListSell: ", self.last_packet)
   elif pck[:1] == b'\xA1':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_PrivateStoreListSell: ", self.last_packet)
   elif pck[:1] == b'\xA2':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_PrivateStoreMsgSell: ", self.last_packet)
   elif pck[:1] == b'\xA6':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_TutorialShowHtml: ", self.last_packet)
   elif pck[:1] == b'\xB1':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_PetStatusShow: ", self.last_packet)
   elif pck[:1] == b'\xB2':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_PetInfo: ", self.last_packet)
   elif pck[:1] == b'\xB3':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_PetItemList: ", self.last_packet)
   elif pck[:1] == b'\xB4':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_PetInventoryUpdate: ", self.last_packet)
   elif pck[:1] == b'\xB6':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_PetStatusUpdate: ", self.last_packet)
   elif pck[:1] == b'\xB9':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_MyTargetSelected: ", self.last_packet)
   elif pck[:1] == b'\xBE':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_PrivateStoreListBuy: ", self.last_packet)
   elif pck[:1] == b'\xC7':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_SkillCoolTime: ", self.last_packet)
   elif pck[:1] == b'\xC8':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_PackageToList: ", self.last_packet)
   elif pck[:1] == b'\xCE':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_RelationChanged: ", self.last_packet)
   elif pck[:1] == b'\xD1':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_SetSummonRemainTime: ", self.last_packet)
   elif pck[:1] == b'\xD2':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_PackageSendableList: ", self.last_packet)
   elif pck[:1] == b'\xD9':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_NetPing: ", self.last_packet)
   elif pck[:1] == b'\xDA':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_Dice: ", self.last_packet)
   elif pck[:1] == b'\xDB':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_Snoop: ", self.last_packet)
   elif pck[:1] == b'\xE4':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_HennaItemInfo: ", self.last_packet)
   elif pck[:1] == b'\xE5':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_HennaInfo: ", self.last_packet)
   elif pck[:1] == b'\xED':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_ChairSit: ", self.last_packet)
   elif pck[:1] == b'\xEE':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_HennaEquipList: ", self.last_packet)
   elif pck[:1] == b'\xF0':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_GMHennaInfo: ", self.last_packet)
   elif pck[:1] == b'\xF1':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_RadarControl: ", self.last_packet)
   elif pck[:1] == b'\xF3':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_ConfirmDlg: ", self.last_packet)
   elif pck[:1] == b'\xF4':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_PartySpelled: ", self.last_packet)
   elif pck[:1] == b'\xF9':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_EtcStatusUpdate: ", self.last_packet)
   elif pck[:1] == b'\xFA':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_ShortBuffStatusUpdate: ", self.last_packet)
   elif pck[:1] == b'\xFB':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_SSQStatus: ", self.last_packet)
   elif pck[:1] == b'\xFD':
      self.last_packet=self.unpack(pck, Pck_invoke, 'S')
      print("s_AgitDecoInfo: ", self.last_packet)







 
 def act_c(self, pck, Pck_invoke):
   
   if pck[:1] == b'\xD0':
     if pck[:3] == b'\xD009':
       self.last_packet=self.unpack(pck, Pck_invoke, 'C')
       print("c_RequestOustFromPartyRoom: ", self.last_packet)
     elif pck[:3] == b'\xD00A':
       self.last_packet=self.unpack(pck, Pck_invoke, 'C')
       print("c_RequestDismissPartyRoom: ", self.last_packet)
     elif pck[:3] == b'\xD00B':
       self.last_packet=self.unpack(pck, Pck_invoke, 'C')
       print("c_RequestWithdrawPartyRoom: ", self.last_packet)
     elif pck[:3] == b'\xD00C':
       self.last_packet=self.unpack(pck, Pck_invoke, 'C')
       print("c_RequestChangePartyLeader: ", self.last_packet)
     elif pck[:3] == b'\xD00D':
       self.last_packet=self.unpack(pck, Pck_invoke, 'C')
       print("c_RequestAutoSoulShot: ", self.last_packet)
     elif pck[:3] == b'\xD021':
       self.last_packet=self.unpack(pck, Pck_invoke, 'C')
       print("c_RequestKeyMapping: ", self.last_packet)
     elif pck[:3] == b'\xD024':
       self.last_packet=self.unpack(pck, Pck_invoke, 'C')
       print("c_RequestSaveInventoryOrder: ", self.last_packet)
     elif pck[:3] == b'\xD047':
       self.last_packet=self.unpack(pck, Pck_invoke, 'C')
       print("c_RequestEself.last_packetMagicSkillUseGround: ", self.last_packet)
     elif pck[:3] == b'\xD049':
       self.last_packet=self.unpack(pck, Pck_invoke, 'C')
       print("c_RequestEself.last_packetEnchantSkillInfoDetail: ", self.last_packet)
     elif pck[:3] == b'\xD04E':
       self.last_packet=self.unpack(pck, Pck_invoke, 'C')
       print("c_RequestEself.last_packetCancelAbnormalState: ", self.last_packet)





   elif pck[:1] == b'\x00':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_Logout: ", self.last_packet)
   elif pck[:1] == b'\x01':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_AttackRequest: ", self.last_packet)
   elif pck[:1] == b'\x11':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_Enter World: ", self.last_packet)
   elif pck[:1] == b'\x0F':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_MoveBackwardToLocation: ", self.last_packet)
   elif pck[:1] == b'\x12':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_CharacterSelect: ", self.last_packet)
   elif pck[:1] == b'\x14':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestItemList: ", self.last_packet)
   elif pck[:1] == b'\x16':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestUnEquipItem: ", self.last_packet)
   elif pck[:1] == b'\x17':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestDropItem: ", self.last_packet)      
   elif pck[:1] == b'\x19':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_UseItem: ", self.last_packet)      
   elif pck[:1] == b'\x1A':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_TradeRequest: ", self.last_packet)      
   elif pck[:1] == b'\x1B':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_AddTradeItem: ", self.last_packet)      
   elif pck[:1] == b'\x1C':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_TradeDone: ", self.last_packet)      
   elif pck[:1] == b'\x1F':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_Action: ", self.last_packet)      
   elif pck[:1] == b'\x2B':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_AuthLogin: ", self.last_packet)
   elif pck[:1] == b'\x34':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestSocialAction: ", self.last_packet)
   elif pck[:1] == b'\x39':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestMagicSkillUse: ", self.last_packet)
   elif pck[:1] == b'\x42':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestJoinParty: ", self.last_packet)
   elif pck[:1] == b'\x43':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestAnswerJoinParty: ", self.last_packet)
   elif pck[:1] == b'\x44':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestWithDrawalParty: ", self.last_packet)
   elif pck[:1] == b'\x45':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestOustPartyMember: ", self.last_packet)
   elif pck[:1] == b'\x48':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestTargetCanceld: ", self.last_packet)
   elif pck[:1] == b'\x49':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_Say2: ", self.last_packet)
   elif pck[:1] == b'\x50':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestSkillList: ", self.last_packet)
   elif pck[:1] == b'\x52':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_MoveWithDelta: ", self.last_packet)
   elif pck[:1] == b'\x55':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_AnswerTradeRequest: ", self.last_packet)
   elif pck[:1] == b'\x56':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestActionUse: ", self.last_packet)
   elif pck[:1] == b'\x57':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestRestart: ", self.last_packet)
   elif pck[:1] == b'\x59':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_ValidatePosition: ", self.last_packet)
   elif pck[:1] == b'\x6F':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestHennaEquip: ", self.last_packet)
   elif pck[:1] == b'\x73':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestAcquireSkillInfo: ", self.last_packet)
   elif pck[:1] == b'\x7C':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestAcquireSkill: ", self.last_packet)
   elif pck[:1] == b'\x83':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestPrivateStoreBuy: ", self.last_packet)
   elif pck[:1] == b'\x85':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestTutorialLinkHtml: ", self.last_packet)
   elif pck[:1] == b'\x86':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestTutorialPassCmdToServer: ", self.last_packet)
   elif pck[:1] == b'\x87':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestTutorialQuestionMark: ", self.last_packet)
   elif pck[:1] == b'\x88':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestTutorialClientEvent: ", self.last_packet)
   elif pck[:1] == b'\x96':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestPrivateStoreQuitSell: ", self.last_packet)
   elif pck[:1] == b'\x97':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_SetPrivateStoreMsgSell: ", self.last_packet)
   elif pck[:1] == b'\xA6':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestSkillCoolTime: ", self.last_packet)
   elif pck[:1] == b'\xB1':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_NetPing: ", self.last_packet)
   elif pck[:1] == b'\xC3':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestHennaList: ", self.last_packet)
   elif pck[:1] == b'\xC4':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_RequestHennaItemInfo: ", self.last_packet)
   elif pck[:1] == b'\xC6':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_DlgAnswer: ", self.last_packet)
   elif pck[:1] == b'\xCB':
      self.last_packet=self.unpack(pck, Pck_invoke, 'C')
      print("c_GameGuardReply: ", self.last_packet)





















































      
