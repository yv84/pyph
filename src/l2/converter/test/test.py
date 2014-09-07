# /usr/bin/python3

import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import sys
import os
import time
import io
import re


PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from converter.ini_to_xml import IniToXml


class TestCase(unittest.TestCase):

    @staticmethod
    def ini_string_trim (ini_string):
        return b''.join(re.findall(b"[\w'=:().]+", ini_string))

    @staticmethod
    def xml_string_trim (xml_string):
        return b''.join(re.findall(b"<[\w\"\'=_ ]+(?:>|/>)", xml_string))

    def setUp(self):
        self.ini_to_xml = IniToXml()

    def tearDown(self):
        pass

    def testSmoke(self):
        self.assertEqual(1, 2)


    def testEasy1(self):
        ini_string = b"""
          00=Logout:
        """
        xml_string = b"""
          <pck_struct name="c_Logout" side="client" type="00" />
        """

        self.assertEqual(
            self.ini_to_xml.convert(self.ini_string_trim(ini_string)),
            self.xml_string_trim(xml_string),
        )




    def testMiddle1(self):
        ini_string = b"""
          01=AttackRequest:d(ObjectID)d(OrigX)d(OrigY)d(OrigZ)c(AttackClick)
        """
        xml_string = b"""
          <pck_struct name="c_AttackRequest" side="client" type="01" >
            <primitive name="ObjectID" type="i4" />
            <primitive name="OrigX" type="i4" />
            <primitive name="OrigY" type="i4" />
            <primitive name="OrigZ" type="i4" />
            <primitive name="AttackClick" type="i1" />
          </pck_struct>
        """

    def testMiddle2(self):
        ini_string = b"""
          03=ReqStartPledgeWar:s(PledgeName)
        """
        xml_string = b"""
          <pck_struct pck_name="c_ReqStartPledgeWar" pck_type="03">
            <S.PledgeName/>
          </pck_struct>
        """


    def testMiddle4(self):
        ini_string = b"""
          FEA3=ExDominionWarStart:
            h(subID)d(objID)d(1)d(terrID)
            d(isDisguised)d(isDisgTerrID)
        """
        xml_string = b"""
          <pck_struct pck_name="s_ExDominionWarStart" pck_type="FEA3">
            <i2.subID/>
            <i4.objID/>
            <i4.1/>
            <i4.terrID/>
            <i4.isDisguised/>
            <i4.isDisgTerrID/>
          </pck_struct>
        """


    def testMiddle5(self):
        ini_string = b"""
          0B=RequestGiveNickName:s(Target)s(Title)
        """
        xml_string = b"""
          <pck_struct pck_name="c_RequestGiveNickName" pck_type="0B">
            <S.Target/>
            <S.Title/>
          </pck_struct>
        """

    def testMiddle6(self):
        ini_string = b"""
          FECE=ExBrBroadcastEventState:
            h(subID)d(eventID)d(eventState)
            d(:)d(:)d(:)d(:)d(:)s(:)s(:)
        """
        xml_string = b"""
          <pck_struct pck_name="s_ExBrBroadcastEventState" pck_type="FECE">
            <i2.subID/>
            <i4.eventID/>
            <i4.eventState/>
            <i4.U/>
            <i4.U/>
            <i4.U/>
            <i4.U/>
            <i4.U/>
            <S.U/>
            <S.U/>
          </pck_struct>
        """

    def testHard1(self):
        ini_string = b"""
          31=SetPrivateStoreListSell:d(isPackage)
            d(count:Loop.01.0003)d(ObjectID)q(Count)q(Price)
        """
        xml_string = b"""
          <pck_struct pck_name="c_SetPrivateStoreListSell" pck_type="31">
            <i4.isPackage/>
            <i4.countValue loop="3" skip="0">
              <i4.ObjectID/>
              <i8.Count/>
              <i8.Price/>
            </i4.countValue>
          </pck_struct>
        """


    def testHard2(self):
        ini_string = b"""
          D066=RequestSendPost:h(subID)s(receiver)d(isCod)
            s(subj)s(text)d(attachCount:Loop.01.0002)
            d(ObjID)q(count)q(reqAdena)
        """
        xml_string = b"""
          <pck_struct pck_name="c_RequestSendPost" pck_type="D066">
            <i2.subID/>
            <S.receiver/>
            <i4.isCod/>
            <S.subj/>
            <S.text/>
            <i4.attachCountValue loop="2" skip="0">
              <i4.ObjID/>
              <i8.count/>
            </i4.attachCountValue>
            <i8.reqAdena/>
          </pck_struct>
        """

    def testHard3(self):
        ini_string = b"""
          FE16=ExShowAgitInfo:
            h(subID)
            d(ClanHallsSize:Loop.01.0004)d(ClanHallID)
            s(HallName)s(LeaderName)d(Grade)
        """
        xml_string = b"""
          <pck_struct pck_name="s_ExShowAgitInfo" pck_type="FE16">
            <i2.subID/>
            <i4.ClanHallsSizeValue loop="4" skip="0">
              <i4.ClanHallID/>
              <S.HallName/>
              <S.LeaderName/>
              <i4.Grade/>
            </i4.ClanHallsSizeValue>
          </pck_struct>
        """


    def testHard4(self):
        ini_string = b"""
          D022=RequestSaveKeyMapping:
            h(subID)d(:)d(:)d(count:Loop.01.0010)c(cmd1sz:Loop.01.0001)
            c(cmdID)c(cmd2sz:Loop.01.0001)c(cmdID)d(cmdSz:Loop.01.0005)
            d(cmd)d(key)d(tgK1)d(tgK2)d(show)d(:)d(:)
        """


        xml_string = b"""<?xml version="1.0" encoding="utf-16"?>
          <pck_struct pck_name="c_RequestSaveKeyMapping" side="c" pck_type="D022">
            <subID type="i2" />
            <U type="i4" />
            <U type="i4" />
            <countValue type="i4" loop="10" skip="0">
              <cmd1szValue type="i1" loop="1" skip="0">
                <cmdID type="i1" />
                <cmd2szValue type="i1" loop="1" skip="0">
                  <cmdID type="i1" />
                  <cmdSzValue type="i4" loop="5" skip="0">
                    <cmd type="i4" />
                    <key type="i4" />
                    <tgK1 type="i4" />
                    <tgK2 type="i4" />
                    <show type="i4" />
                    <U type="i4" />
                    <U type="i4" />
                  </cmdSzValue>
                </cmd2szValue>
              </cmd1szValue>
            </countValue>
          </pck_struct>"""





    def testHard5(self):
        ini_string = b"""
          11=ItemList:
            h(ShowWindow)h(count:Loop.01.0024)d(ObjectID)
            d(ItemID:Get.F0)d(LocationSlot)q(Count)
            h(ItemType2)h(CustomType1)h(isEquipped)
            d(BodyPart)h(EnchantLevel)h(CustType2)
            d(AugmentID:Get.F1)d(Mana)d(remainTime)
            h(AttackElem)h(AttackElemVal)h(DefAttrFire)
            h(DefAttrWater)h(DefAttrWind)h(DefAttrEarth)
            h(DefAttrHoly)h(DefAttrUnholy)h(EnchEff1)
            h(enchEff2)h(enchEff3)h(blockedItems:Loop.02.0001)
            c(blockMode)d(blockItem)
        """
        xml_string = b"""
          <pck_struct pck_name="s_ItemList" pck_type="11">
            <i2.ShowWindow/>
            <i2.countValue loop="24" skip="0">
              <i4.ObjectID/>
              <i4.ItemID/>
              <i4.LocationSlot/>
              <i8.Count/>
              <i2.ItemType2/>
              <i2.CustomType1/>
              <i2.isEquipped/>
              <i4.BodyPart/>
              <i2.EnchantLevel/>
              <i2.CustType2/>
              <i4.AugmentID/>
              <i4.Mana/>
              <i4.remainTime/>
              <i2.AttackElem/>
              <i2.AttackElemVal/>
              <i2.DefAttrFire/>
              <i2.DefAttrWater/>
              <i2.DefAttrWind/>
              <i2.DefAttrEarth/>
              <i2.DefAttrHoly/>
              <i2.DefAttrUnholy/>
              <i2.EnchEff1/>
              <i2.enchEff2/>
              <i2.enchEff3/>
            </i2.countValue>
            <i2.blockedItemsValue loop="1" skip="1">
              <i4.blockItem/>
            </i2.blockedItemsValue>
            <i1.blockMode/>
          </pck_struct>
        """



    def testHard6(self):
        ini_string = b"""
          FE70=ExUISetting:h(subID)d(bufsize)d(categories)
            d(count:Loop.01.0010)c(catList1:Loop.01.0001)c(cmd)
            c(catList2:Loop.01.0001)c(cmd)d(keyList:Loop.01.0005)
            d(cmdID)d(keyID)d(toogleKey1)d(toogleKey2)
            d(showStatus)d(11)d(10)
        """
        xml_string = b"""
          <pck_struct pck_name="s_ExUISetting" pck_type="FE70">
            <i2.subID/>
            <i4.bufsize/>
            <i4.categories/>
            <i4.countValue loop="10" skip="0">
              <i1.catList1Value loop="1" skip="0">
                <i1.cmd/>
                <i1.catList2Value loop="1" skip="0">
                  <i1.cmd/>
                  <i4.keyListValue loop="5" skip="0">
                    <i4.cmdID/>
                    <i4.keyID/>
                    <i4.toogleKey1/>
                    <i4.toogleKey2/>
                    <i4.showStatus/>
                    <i4.11/>
                    <i4.10/>
                  </i4.keyListValue>
                </i1.catList2Value>
              </i1.catList1Value>
            </i4.countValue>
          </pck_struct>
        """


    def testHard7(self):
        ini_string = b"""
          FE970000=ExCubeGameTeamList:
            h(subID)d(sub2ID)d(roomNumber)d(-1)
            d(bluePlayersCount:Loop.01.0002)d(playerObjID)
            d(name)d(redPlayersCount:Loop.01.0002)
            d(playerObjID)d(name)
        """
        xml_string = b"""
          <pck_struct pck_name="s_ExCubeGameTeamList" pck_type="FE970000">
            <i2.subID/>
            <i4.sub2ID/>
            <i4.roomNumber/>
            <i4.1/>
            <i4.bluePlayersCountValue loop="2" skip="0">
              <i4.playerObjID/>
              <i4.name/>
            </i4.bluePlayersCountValue>
            <i4.redPlayersCountValue loop="2" skip="0">
              <i4.playerObjID/>
              <i4.name/>
            </i4.redPlayersCountValue>
          </pck_struct>
        """




if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner().run(suite)
    #unittest.main()
