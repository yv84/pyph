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
        return b''.join(re.findall(b"[\w'=:().-]+", ini_string))

    @staticmethod
    def xml_string_trim (xml_string):
        return b''.join(re.findall(b"<.+?>", xml_string))

    def setUp(self):
        self.ini_to_xml = IniToXml()

    def tearDown(self):
        pass

    def testEasy1(self):
        ini_string = b"""
          00=Logout:
        """
        xml_string = b"""
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct name="c_Logout" side="client" type="00"/>
          </root>
        """
        self.ini_to_xml.side = b"client"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )

    def testMiddle1(self):
        ini_string = b"""
          01=AttackRequest:d(ObjectID)d(OrigX)d(OrigY)d(OrigZ)c(AttackClick)
        """
        xml_string = b"""
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
          <la2:pck_struct name="c_AttackRequest" side="client" type="01">
            <la2:primitive name="ObjectID" type="i4"/>
            <la2:primitive name="OrigX" type="i4"/>
            <la2:primitive name="OrigY" type="i4"/>
            <la2:primitive name="OrigZ" type="i4"/>
            <la2:primitive name="AttackClick" type="i1"/>
          </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"client"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )

    def testMiddle2(self):
        ini_string = b"""
          03=ReqStartPledgeWar:s(PledgeName)
        """
        xml_string = b"""
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct name="c_ReqStartPledgeWar" side="client" type="03">
              <la2:primitive name="PledgeName" type="S"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"client"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )

    def testMiddle4(self):
        ini_string = b"""
          FEA3=ExDominionWarStart:
            h(subID)d(objID)d(1)d(terrID)
            d(isDisguised)d(isDisgTerrID)
        """
        xml_string = b"""
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct name="s_ExDominionWarStart" side="server" type="FEA3">
              <la2:primitive name="subID" type="i2"/>
              <la2:primitive name="objID" type="i4"/>
              <la2:primitive name="1" type="i4"/>
              <la2:primitive name="terrID" type="i4"/>
              <la2:primitive name="isDisguised" type="i4"/>
              <la2:primitive name="isDisgTerrID" type="i4"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"server"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )

    def testMiddle5(self):
        ini_string = b"""
          0B=RequestGiveNickName:s(Target)s(Title)
        """
        xml_string = b"""
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct name="c_RequestGiveNickName" side="client" type="0B">
              <la2:primitive name="Target" type="S"/>
              <la2:primitive name="Title" type="S"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"client"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )

    def testMiddle6(self):
        ini_string = b"""
          FECE=ExBrBroadcastEventState:
            h(subID)d(eventID)d(eventState)
            d(:)d(:)d(:)d(:)d(:)s(:)s(:)
        """
        xml_string = b"""
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct name="s_ExBrBroadcastEventState" side="server" type="FECE">
              <la2:primitive name="subID" type="i2"/>
              <la2:primitive name="eventID" type="i4"/>
              <la2:primitive name="eventState" type="i4"/>
              <la2:primitive name="U" type="i4"/>
              <la2:primitive name="U" type="i4"/>
              <la2:primitive name="U" type="i4"/>
              <la2:primitive name="U" type="i4"/>
              <la2:primitive name="U" type="i4"/>
              <la2:primitive name="U" type="S"/>
              <la2:primitive name="U" type="S"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"server"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )

    def testHard1(self):
        ini_string = b"""
          31=SetPrivateStoreListSell:d(isPackage)
            d(count:Loop.01.0003)d(ObjectID)q(Count)q(Price)
        """
        xml_string = b"""
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct name="c_SetPrivateStoreListSell" side="client" type="31">
              <la2:primitive name="isPackage" type="i4"/>
              <la2:loop loop="3" name="count" skip="0" type="i4">
                <la2:primitive name="ObjectID" type="i4"/>
                <la2:primitive name="Count" type="i8"/>
                <la2:primitive name="Price" type="i8"/>
              </la2:loop>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"client"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )

    def testHard2(self):
        ini_string = b"""
          D066=RequestSendPost:h(subID)s(receiver)d(isCod)
            s(subj)s(text)d(attachCount:Loop.01.0002)
            d(ObjID)q(count)q(reqAdena)
        """
        xml_string = b"""
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct name="c_RequestSendPost" side="client" type="D066">
              <la2:primitive name="subID" type="i2"/>
              <la2:primitive name="receiver" type="S"/>
              <la2:primitive name="isCod" type="i4"/>
              <la2:primitive name="subj" type="S"/>
              <la2:primitive name="text" type="S"/>
              <la2:loop loop="2" name="attachCount" skip="0" type="i4">
                <la2:primitive name="ObjID" type="i4"/>
                <la2:primitive name="count" type="i8"/>
              </la2:loop>
              <la2:primitive name="reqAdena" type="i8"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"client"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )

    def testHard3(self):
        ini_string = b"""
          FE16=ExShowAgitInfo:
            h(subID)
            d(ClanHallsSize:Loop.01.0004)d(ClanHallID)
            s(HallName)s(LeaderName)d(Grade)
        """
        xml_string = b"""
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct name="s_ExShowAgitInfo" side="server" type="FE16">
              <la2:primitive name="subID" type="i2"/>
              <la2:loop loop="4" name="ClanHallsSize" skip="0" type="i4">
                <la2:primitive name="ClanHallID" type="i4"/>
                <la2:primitive name="HallName" type="S"/>
                <la2:primitive name="LeaderName" type="S"/>
                <la2:primitive name="Grade" type="i4"/>
              </la2:loop>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"server"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )

    def testHard4(self):
        ini_string = b"""
          D022=RequestSaveKeyMapping:
            h(subID)d(:)d(:)
            d(count:Loop.01.0010)
            c(cmd1sz:Loop.01.0001)c(cmdID)
            c(cmd2sz:Loop.01.0001)c(cmdID)
            d(cmdSz:Loop.01.0005)d(cmd)d(key)d(tgK1)d(tgK2)d(show)
            d(:)d(:)
        """
        xml_string = b"""
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct name="c_RequestSaveKeyMapping" side="client" type="D022">
              <la2:primitive name="subID" type="i2"/>
              <la2:primitive name="U" type="i4"/>
              <la2:primitive name="U" type="i4"/>
              <la2:loop loop="10" name="count" skip="0" type="i4">
                <la2:loop loop="1" name="cmd1sz" skip="0" type="i1">
                  <la2:primitive name="cmdID" type="i1"/>
                </la2:loop>
                <la2:loop loop="1" name="cmd2sz" skip="0" type="i1">
                  <la2:primitive name="cmdID" type="i1"/>
                </la2:loop>
                <la2:loop loop="5" name="cmdSz" skip="0" type="i4">
                  <la2:primitive name="cmd" type="i4"/>
                  <la2:primitive name="key" type="i4"/>
                  <la2:primitive name="tgK1" type="i4"/>
                  <la2:primitive name="tgK2" type="i4"/>
                  <la2:primitive name="show" type="i4"/>
                </la2:loop>
              </la2:loop>
              <la2:primitive name="U" type="i4"/>
              <la2:primitive name="U" type="i4"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"client"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )

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
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct name="s_ItemList" side="server" type="11">
              <la2:primitive name="ShowWindow" type="i2"/>
              <la2:loop loop="24" name="count" skip="0" type="i2">
                <la2:primitive name="ObjectID" type="i4"/>
                <la2:primitive name="ItemID:Get.F0" type="i4"/>
                <la2:primitive name="LocationSlot" type="i4"/>
                <la2:primitive name="Count" type="i8"/>
                <la2:primitive name="ItemType2" type="i2"/>
                <la2:primitive name="CustomType1" type="i2"/>
                <la2:primitive name="isEquipped" type="i2"/>
                <la2:primitive name="BodyPart" type="i4"/>
                <la2:primitive name="EnchantLevel" type="i2"/>
                <la2:primitive name="CustType2" type="i2"/>
                <la2:primitive name="AugmentID:Get.F1" type="i4"/>
                <la2:primitive name="Mana" type="i4"/>
                <la2:primitive name="remainTime" type="i4"/>
                <la2:primitive name="AttackElem" type="i2"/>
                <la2:primitive name="AttackElemVal" type="i2"/>
                <la2:primitive name="DefAttrFire" type="i2"/>
                <la2:primitive name="DefAttrWater" type="i2"/>
                <la2:primitive name="DefAttrWind" type="i2"/>
                <la2:primitive name="DefAttrEarth" type="i2"/>
                <la2:primitive name="DefAttrHoly" type="i2"/>
                <la2:primitive name="DefAttrUnholy" type="i2"/>
                <la2:primitive name="EnchEff1" type="i2"/>
                <la2:primitive name="enchEff2" type="i2"/>
                <la2:primitive name="enchEff3" type="i2"/>
              </la2:loop>
              <la2:loop loop="1" name="blockedItems" skip="1" type="i2">
                <la2:primitive name="blockItem" type="i4"/>
              </la2:loop>
              <la2:primitive name="blockMode" type="i1"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"server"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )

    def testHard6(self):
        ini_string = b"""
          FE70=ExUISetting:h(subID)d(bufsize)d(categories)
            d(count:Loop.01.0010)
            c(catList1:Loop.01.0001)c(cmd)
            c(catList2:Loop.01.0001)c(cmd)
            d(keyList:Loop.01.0005)d(cmdID)d(keyID)
              d(toogleKey1)d(toogleKey2)d(showStatus)
            d(11)d(10)
        """
        xml_string = b"""
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct name="s_ExUISetting" side="server" type="FE70">
              <la2:primitive name="subID" type="i2"/>
              <la2:primitive name="bufsize" type="i4"/>
              <la2:primitive name="categories" type="i4"/>
              <la2:loop loop="10" name="count" skip="0" type="i4">
                <la2:loop loop="1" name="catList1" skip="0" type="i1">
                  <la2:primitive name="cmd" type="i1"/>
                </la2:loop>
                <la2:loop loop="1" name="catList2" skip="0" type="i1">
                  <la2:primitive name="cmd" type="i1"/>
                </la2:loop>
                <la2:loop loop="5" name="keyList" skip="0" type="i4">
                  <la2:primitive name="cmdID" type="i4"/>
                  <la2:primitive name="keyID" type="i4"/>
                  <la2:primitive name="toogleKey1" type="i4"/>
                  <la2:primitive name="toogleKey2" type="i4"/>
                  <la2:primitive name="showStatus" type="i4"/>
                </la2:loop>
              </la2:loop>
              <la2:primitive name="11" type="i4"/>
              <la2:primitive name="10" type="i4"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"server"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )

    def testHard7(self):
        ini_string = b"""
          FE970000=ExCubeGameTeamList:
            h(subID)d(sub2ID)d(roomNumber)d(-1)
            d(bluePlayersCount:Loop.01.0002)d(playerObjID)d(name)
            d(redPlayersCount:Loop.01.0002)d(playerObjID)d(name)
        """
        xml_string = b"""
          <?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct name="s_ExCubeGameTeamList" side="server" type="FE970000">
              <la2:primitive name="subID" type="i2"/>
              <la2:primitive name="sub2ID" type="i4"/>
              <la2:primitive name="roomNumber" type="i4"/>
              <la2:primitive name="-1" type="i4"/>
              <la2:loop loop="2" name="bluePlayersCount" skip="0" type="i4">
                <la2:primitive name="playerObjID" type="i4"/>
                <la2:primitive name="name" type="i4"/>
              </la2:loop>
              <la2:loop loop="2" name="redPlayersCount" skip="0" type="i4">
                <la2:primitive name="playerObjID" type="i4"/>
                <la2:primitive name="name" type="i4"/>
              </la2:loop>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"server"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert(self.ini_string_trim(ini_string))),
            self.xml_string_trim(xml_string),
        )


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner().run(suite)
    #unittest.main()
