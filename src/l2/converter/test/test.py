# /usr/bin/python3

import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import sys
import os
import time
import io
import re
import random
import struct
import binascii
from itertools import chain
import string

import numpy


PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from converter.ini_to_xml import IniToXml, PacketCompileException
from converter.xml_to_py import XmlToPy


class TestCase(unittest.TestCase):

    @staticmethod
    def ini_string_trim (ini_string):
        return b''.join(re.findall(b"[\w'=:().-]+", ini_string))

    @staticmethod
    def xml_string_trim (xml_string):
        return b''.join(re.findall(b"<.+?>", xml_string))

    @staticmethod
    def random_i(np_type, count):
        c_type = {b"i1": b"b", b"i2": b"h", b"i4": b"i", b"i8": b"q",}
        signed_value_min = {b"i1": -128, b"i2": -32767,
            b"i4": -2147483648, b"i8": -9223372036854775808}
        signed_value = {b"i1": 0xff, b"i2": 0xffff,
            b"i4": 0xffffffff, b"i8": 0xffffffffffffffff}
        return (lambda count: [(lambda x: \
            [struct.pack(c_type[np_type], x), x]) \
            (int(signed_value[np_type]*random.random())+\
                  signed_value_min[np_type]) \
            for i in range(count)])(count)

    @staticmethod
    def random_f(np_type, count):
        c_type = {b"f4": b"f", b"f8": b"d",}
        return (lambda count: [(lambda x: \
            [struct.pack(c_type[np_type], x), x]) \
            (random.random()) \
            for i in range(count)])(count)

    @staticmethod
    def random_string_fixed_length(np_type, count):
        return (lambda count: [(lambda x: \
            [x, x]) \
            (os.urandom(int(np_type[2:]))) \
            for i in range(count)])(count)

    @staticmethod
    def random_string(count):
        MIN_STRING = 1
        MAX_STRING = 16
        return (lambda count: [(lambda x: \
            [b''.join([x, '\x00'.encode('UTF-16LE')]), x[:-1] ]) \
            (''.join([random.choice(string.ascii_letters+string.digits) \
                for i in range(
                    int(random.random()*(MAX_STRING-MIN_STRING)+MIN_STRING))
            ]).encode('UTF-16LE')) \
            for i in range(count)])(count)

    @staticmethod
    def random_loop(np_type, list_loop, skip=[]):
        MIN_LOOP = 0
        MAX_LOOP = 5
        c_type = {b"i1": b"b", b"i2": b"h", b"i4": b"i", b"i8": b"q",}
        signed_value_min = {b"i1": -128, b"i2": -32767,
            b"i4": -2147483648, b"i8": -9223372036854775808}
        signed_value = {b"i1": 0xff, b"i2": 0xffff,
            b"i4": 0xffffffff, b"i8": 0xffffffffffffffff}
        return (lambda loop: list(chain(
                  (loop,), (skip), list(chain.from_iterable(loop[1]*list_loop)), 
               )))(\
            (lambda x: \
                [struct.pack(c_type[np_type], x), x])( \
                int(random.random()*(MAX_LOOP+1-MIN_LOOP)+MIN_LOOP))
                  )


    def setUp(self):
        self.ini_to_xml = IniToXml()
        self.xml_to_py = XmlToPy()

    def tearDown(self):
        pass



    def testEasy1(self):
        # PacketsHighFive.ini
        ini_string = b"""
          00=Logout:
        """
        ini_string1 = b"""
          00=Logout
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="simple" name="pck_type" opt_code="00" pck_name="c_Logout" side="client" type="i1"/>
          </root>
        """
        py_string = """
class c_Logout():
    @classmethod
    def dtype(cls, data):
        dtype = [('pck_type', 'i1')]
        return dtype

pck_client[b'\\x00'] = c_Logout"""
        self.ini_to_xml.side = b"client"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
            self.xml_string_trim(xml_string),
        )
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string1),])),
            self.xml_string_trim(xml_string),
        )
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\x00", 0),],
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute
        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])



    def testMiddle1(self):
        # PacketsHighFive.ini
        ini_string = b"""
          01=AttackRequest:d(ObjectID)d(OrigX)d(OrigY)d(OrigZ)c(AttackClick)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
          <la2:pck_struct complexity="simple" name="pck_type" opt_code="01" pck_name="c_AttackRequest" side="client" type="i1">
            <la2:primitive name="ObjectID" type="i4"/>
            <la2:primitive name="OrigX" type="i4"/>
            <la2:primitive name="OrigY" type="i4"/>
            <la2:primitive name="OrigZ" type="i4"/>
            <la2:primitive name="AttackClick" type="i1"/>
          </la2:pck_struct>
          </root>
        """
        py_string = """
class c_AttackRequest():
    @classmethod
    def dtype(cls, data):
        dtype = [('pck_type', 'i1'), ('ObjectID', 'i4'), ('OrigX', 'i4'), ('OrigY', 'i4'), ('OrigZ', 'i4'), ('AttackClick', 'i1')]
        return dtype

pck_client[b'\\x01'] = c_AttackRequest"""
        self.ini_to_xml.side = b"client"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
            self.xml_string_trim(xml_string),
        )
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\x01", 1),],
                self.random_i(b"i4", 4),
                self.random_i(b"i1", 1),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute
        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['ObjectID'].item(),
            unpack_value[1])
        self.assertEqual(pck_np_array['OrigX'].item(),
            unpack_value[2])
        self.assertEqual(pck_np_array['OrigY'].item(),
            unpack_value[3])
        self.assertEqual(pck_np_array['OrigZ'].item(),
            unpack_value[4])
        self.assertEqual(pck_np_array['AttackClick'].item(),
            unpack_value[5])



    def testMiddle2(self):
        # PacketsHighFive.ini
        ini_string = b"""
          03=ReqStartPledgeWar:s(PledgeName)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="complex" name="pck_type" opt_code="03" pck_name="c_ReqStartPledgeWar" side="client" type="i1">
              <la2:primitive name="PledgeName" type="|S"/>
            </la2:pck_struct>
          </root>
        """
        py_string = """
class c_ReqStartPledgeWar():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('PledgeName', '|S')])
        return dtype

pck_client[b'\\x03'] = c_ReqStartPledgeWar"""
        py_execute = b"".join([b"\x03", ('test_string\x00').encode('UTF-16LE')])
        self.ini_to_xml.side = b"client"
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
            self.xml_string_trim(xml_string),
        )
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\x03", 3),],
                self.random_string(1),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute
        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['PledgeName'].item(),
            unpack_value[1])



    def testMiddle4(self):
        ini_string = b"""
          FEA3=ExDominionWarStart:
            h(subID)d(objID)d(1)d(terrID)
            d(isDisguised)d(isDisgTerrID)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="simple" name="pck_type" opt_code="FEA3" pck_name="s_ExDominionWarStart" side="server" type="i1">
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
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
            self.xml_string_trim(xml_string),
        )
        py_string = """
class s_ExDominionWarStart():
    @classmethod
    def dtype(cls, data):
        dtype = [('pck_type', 'i1'), ('subID', 'i2'), ('objID', 'i4'), ('1', 'i4'), ('terrID', 'i4'), ('isDisguised', 'i4'), ('isDisgTerrID', 'i4')]
        return dtype

pck_server[b'\\xfe\\xa3'] = s_ExDominionWarStart"""
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
            self.xml_string_trim(xml_string),
        )
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\xfe", -2),],
                [(b"\xa3\x00", 0x00a3),],
                self.random_i(b"i4", 5),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute
        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['subID'].item(),
            unpack_value[1])
        self.assertEqual(pck_np_array['objID'].item(),
            unpack_value[2])
        self.assertEqual(pck_np_array['1'].item(),
            unpack_value[3])
        self.assertEqual(pck_np_array['terrID'].item(),
            unpack_value[4])
        self.assertEqual(pck_np_array['isDisguised'].item(),
            unpack_value[5])
        self.assertEqual(pck_np_array['isDisgTerrID'].item(),
            unpack_value[6])


    def testMiddle5(self):
        # PacketsHighFive.ini
        ini_string = b"""
          0B=RequestGiveNickName:s(Target)s(Title)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="complex" name="pck_type" opt_code="0B" pck_name="c_RequestGiveNickName" side="client" type="i1">
              <la2:primitive name="Target" type="|S"/>
              <la2:primitive name="Title" type="|S"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"client"

        py_string = """
class c_RequestGiveNickName():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('Target', '|S'), ('Title', '|S')])
        return dtype

pck_client[b'\\x0b'] = c_RequestGiveNickName"""
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
            self.xml_string_trim(xml_string),
        )
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\x0b", 0x0b),],
                self.random_string(2),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute
        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['Target'].item(),
            unpack_value[1])
        self.assertEqual(pck_np_array['Title'].item(),
            unpack_value[2])



    def testMiddle6(self):
        # PacketsHighFive.ini
        ini_string = b"""
          FECE=ExBrBroadcastEventState:
            h(subID)d(eventID)d(eventState)
            d(:)d(:)d(:)d(:)d(:)s(:)s(:)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="complex" name="pck_type" opt_code="FECE" pck_name="s_ExBrBroadcastEventState" side="server" type="i1">
              <la2:primitive name="subID" type="i2"/>
              <la2:primitive name="eventID" type="i4"/>
              <la2:primitive name="eventState" type="i4"/>
              <la2:primitive name="U" type="i4"/>
              <la2:primitive name="U_" type="i4"/>
              <la2:primitive name="U__" type="i4"/>
              <la2:primitive name="U___" type="i4"/>
              <la2:primitive name="U____" type="i4"/>
              <la2:primitive name="U_____" type="|S"/>
              <la2:primitive name="U______" type="|S"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"server"
        py_string = """
class s_ExBrBroadcastEventState():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('subID', 'i2'), ('eventID', 'i4'), ('eventState', 'i4'), ('U', 'i4'), ('U_', 'i4'), ('U__', 'i4'), ('U___', 'i4'), ('U____', 'i4'), ('U_____', '|S'), ('U______', '|S')])
        return dtype

pck_server[b'\\xfe\\xce'] = s_ExBrBroadcastEventState"""
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
            self.xml_string_trim(xml_string),
        )
        self.maxDiff = None
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\xfe", -2),],
                [(b"\xce\x00", 0x00CE),],
                self.random_i(b"i4", 7),
                self.random_string(2),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute
        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['subID'].item(),
            unpack_value[1])
        self.assertEqual(pck_np_array['eventID'].item(),
            unpack_value[2])
        self.assertEqual(pck_np_array['eventState'].item(),
            unpack_value[3])
        self.assertEqual(pck_np_array['U'].item(),
            unpack_value[4])
        self.assertEqual(pck_np_array['U_'].item(),
            unpack_value[5])
        self.assertEqual(pck_np_array['U__'].item(),
            unpack_value[6])
        self.assertEqual(pck_np_array['U___'].item(),
            unpack_value[7])
        self.assertEqual(pck_np_array['U____'].item(),
            unpack_value[8])
        self.assertEqual(pck_np_array['U_____'].item(),
            unpack_value[9])
        self.assertEqual(pck_np_array['U______'].item(),
            unpack_value[10])




    def testMiddle7(self):
        # PacketsHighFive.ini
        ini_string = b"""
          D05101=RequestSaveBookMarkSlot:h(subID)s(name)d(icon)s(tag)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="complex" name="pck_type" opt_code="D05101" pck_name="c_RequestSaveBookMarkSlot" side="client" type="i1">
              <la2:primitive name="subID" type="i2"/>
              <la2:primitive name="name" type="|S"/>
              <la2:primitive name="icon" type="i4"/>
              <la2:primitive name="tag" type="|S"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"client"
        py_string = """
class c_RequestSaveBookMarkSlot():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('subID', 'i2'), ('name', '|S'), ('icon', 'i4'), ('tag', '|S')])
        return dtype

pck_client[b'\\xd0Q\\x01'] = c_RequestSaveBookMarkSlot"""
        self.maxDiff = None
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\xd0", -48),],
                [(b"\x51\x01", 0x0151),],
                self.random_string(1),
                self.random_i(b"i4", 1),
                self.random_string(1),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute

        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['subID'].item(),
            unpack_value[1])
        self.assertEqual(pck_np_array['name'].item(),
            unpack_value[2])
        self.assertEqual(pck_np_array['icon'].item(),
            unpack_value[3])
        self.assertEqual(pck_np_array['tag'].item(),
            unpack_value[4])




    def testHard1(self):
        # PacketsHighFive.ini
        ini_string = b"""
          31=SetPrivateStoreListSell:d(isPackage)
            d(count:Loop.01.0003)d(ObjectID)q(Count)q(Price)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="complex" name="pck_type" opt_code="31" pck_name="c_SetPrivateStoreListSell" side="client" type="i1">
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
        py_string = """
class c_SetPrivateStoreListSell():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('isPackage', 'i4'), ('count', 'value', 'i4'), ('count', 'loop', [('ObjectID', 'i4'), ('Count', 'i8'), ('Price', 'i8')])])
        return dtype

pck_client[b'1'] = c_SetPrivateStoreListSell"""
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
            self.xml_string_trim(xml_string),
        )
        self.maxDiff = None
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\x31", 49),],
                self.random_i(b"i4", 1),
                self.random_loop(b"i4",
                    (
                        self.random_i(b"i4", 1),
                        self.random_i(b"i8", 2),
                    )
                ),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute

        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['isPackage'].item(),
            unpack_value[1])
        self.assertEqual(pck_np_array['count'].item(),
            unpack_value[2])
        loop_count, unpack_value_count = 0, 2
        while loop_count < pck_np_array['count']:
            loop_count += 1
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['ObjectID'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['Count'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['Price'].item(),
                unpack_value[unpack_value_count])




    def testHard2(self):
        # PacketsHighFive.ini
        ini_string = b"""
          D066=RequestSendPost:h(subID)s(receiver)d(isCod)
            s(subj)s(text)d(attachCount:Loop.01.0002)
            d(ObjID)q(count)q(reqAdena)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="complex" name="pck_type" opt_code="D066" pck_name="c_RequestSendPost" side="client" type="i1">
              <la2:primitive name="subID" type="i2"/>
              <la2:primitive name="receiver" type="|S"/>
              <la2:primitive name="isCod" type="i4"/>
              <la2:primitive name="subj" type="|S"/>
              <la2:primitive name="text" type="|S"/>
              <la2:loop loop="2" name="attachCount" skip="0" type="i4">
                <la2:primitive name="ObjID" type="i4"/>
                <la2:primitive name="count" type="i8"/>
              </la2:loop>
              <la2:primitive name="reqAdena" type="i8"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"client"
        py_string = """
class c_RequestSendPost():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('subID', 'i2'), ('receiver', '|S'), ('isCod', 'i4'), ('subj', '|S'), ('text', '|S'), ('attachCount', 'value', 'i4'), ('attachCount', 'loop', [('ObjID', 'i4'), ('count', 'i8')]), ('reqAdena', 'i8')])
        return dtype

pck_client[b'\\xd0f'] = c_RequestSendPost"""
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
            self.xml_string_trim(xml_string),
        )
        self.maxDiff = None
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\xd0", -48),],
                [(b"\x66\x00", 0x0066),],
                self.random_string(1),
                self.random_i(b"i4", 1),
                self.random_string(2),
                self.random_loop(b"i4",
                    (
                        self.random_i(b"i4", 1),
                        self.random_i(b"i8", 1),
                    )
                ),
                self.random_i(b"i8", 1),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute

        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['subID'].item(),
            unpack_value[1])
        self.assertEqual(pck_np_array['receiver'].item(),
            unpack_value[2])
        self.assertEqual(pck_np_array['isCod'].item(),
            unpack_value[3])
        self.assertEqual(pck_np_array['subj'].item(),
            unpack_value[4])
        self.assertEqual(pck_np_array['text'].item(),
            unpack_value[5])
        self.assertEqual(pck_np_array['attachCount'].item(),
            unpack_value[6])
        loop_count, unpack_value_count = 0, 6
        while loop_count < pck_np_array['attachCount']:
            loop_count += 1
            unpack_value_count += 1
            self.assertEqual(pck_np_array['attachCount'+str(loop_count)]['ObjID'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['attachCount'+str(loop_count)]['count'].item(),
                unpack_value[unpack_value_count])
        unpack_value_count += 1
        self.assertEqual(pck_np_array['reqAdena'].item(),
            unpack_value[unpack_value_count])




    def testHard3(self):
        # PacketsHighFive.ini
        ini_string = b"""
          FE16=ExShowAgitInfo:
            h(subID)
            d(ClanHallsSize:Loop.01.0004)d(ClanHallID)
            s(HallName)s(LeaderName)d(Grade)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="complex" name="pck_type" opt_code="FE16" pck_name="s_ExShowAgitInfo" side="server" type="i1">
              <la2:primitive name="subID" type="i2"/>
              <la2:loop loop="4" name="ClanHallsSize" skip="0" type="i4">
                <la2:primitive name="ClanHallID" type="i4"/>
                <la2:primitive name="HallName" type="|S"/>
                <la2:primitive name="LeaderName" type="|S"/>
                <la2:primitive name="Grade" type="i4"/>
              </la2:loop>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"server"
        py_string = """
class s_ExShowAgitInfo():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('subID', 'i2'), ('ClanHallsSize', 'value', 'i4'), ('ClanHallsSize', 'loop', [('ClanHallID', 'i4'), ('HallName', '|S'), ('LeaderName', '|S'), ('Grade', 'i4')])])
        return dtype

pck_server[b'\\xfe\\x16'] = s_ExShowAgitInfo"""
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
            self.xml_string_trim(xml_string),
        )
        self.maxDiff = None
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\xfe", -2),],
                [(b"\x16\x00", 0x0016),],
                self.random_loop(b"i4",
                    (
                        self.random_i(b"i4", 1),
                        self.random_string(2),
                        self.random_i(b"i4", 1),
                    )
                ),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute

        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['subID'].item(),
            unpack_value[1])
        self.assertEqual(pck_np_array['ClanHallsSize'].item(),
            unpack_value[2])
        loop_count, unpack_value_count = 0, 2
        while loop_count < pck_np_array['ClanHallsSize']:
            loop_count += 1
            unpack_value_count += 1
            self.assertEqual(pck_np_array['ClanHallsSize'+str(loop_count)]['ClanHallID'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['ClanHallsSize'+str(loop_count)]['HallName'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['ClanHallsSize'+str(loop_count)]['LeaderName'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['ClanHallsSize'+str(loop_count)]['Grade'].item(),
                unpack_value[unpack_value_count])




    def testHard4(self):
        # PacketsHighFive.ini
        ini_string = b"""
          D022=RequestSaveKeyMapping:
            h(subID)d(:)d(:)
            d(count:Loop.01.0010)
            c(cmd1sz:Loop.01.0001)c(cmdID)
            c(cmd2sz:Loop.01.0001)c(cmdID)
            d(cmdSz:Loop.01.0005)d(cmd)d(key)d(tgK1)d(tgK2)d(show)
            d(:)d(:)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="complex" name="pck_type" opt_code="D022" pck_name="c_RequestSaveKeyMapping" side="client" type="i1">
              <la2:primitive name="subID" type="i2"/>
              <la2:primitive name="U" type="i4"/>
              <la2:primitive name="U_" type="i4"/>
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
              <la2:primitive name="U__" type="i4"/>
              <la2:primitive name="U___" type="i4"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"client"
        py_string = """
class c_RequestSaveKeyMapping():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('subID', 'i2'), ('U', 'i4'), ('U_', 'i4'), ('count', 'value', 'i4'), ('count', 'loop', [('cmd1sz', 'value', 'i1'), ('cmd1sz', 'loop', [('cmdID', 'i1')]), ('cmd2sz', 'value', 'i1'), ('cmd2sz', 'loop', [('cmdID', 'i1')]), ('cmdSz', 'value', 'i4'), ('cmdSz', 'loop', [('cmd', 'i4'), ('key', 'i4'), ('tgK1', 'i4'), ('tgK2', 'i4'), ('show', 'i4')])]), ('U__', 'i4'), ('U___', 'i4')])
        return dtype

pck_client[b'\\xd0"'] = c_RequestSaveKeyMapping"""
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
            self.xml_string_trim(xml_string),
        )
        self.maxDiff = None
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\xd0", -48),],
                [(b"\x22\x00", 0x0022),],
                self.random_i(b"i4", 2),
                self.random_loop(b"i4",
                    (
                        self.random_loop(b"i1",
                            (
                                self.random_i(b"i1", 1),
                            )
                        ),
                        self.random_loop(b"i1",
                            (
                                self.random_i(b"i1", 1),
                            )
                        ),
                        self.random_loop(b"i4",
                            (
                                self.random_i(b"i4", 5),
                            )
                        ),
                    )
                ),
                self.random_i(b"i4", 2),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute

        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['subID'].item(),
            unpack_value[1])
        self.assertEqual(pck_np_array['U'].item(),
            unpack_value[2])
        self.assertEqual(pck_np_array['U_'].item(),
            unpack_value[3])
        self.assertEqual(pck_np_array['count'].item(),
            unpack_value[4])
        loop_count, unpack_value_count = 0, 4
        while loop_count < pck_np_array['count'].item():
            loop_count += 1
            unpack_value_count += 1

            self.assertEqual(pck_np_array['count'+str(loop_count)]['cmd1sz'].item(),
                unpack_value[unpack_value_count])
            loop_count1, unpack_value_count = 0, unpack_value_count
            while loop_count1 < pck_np_array['count'+str(loop_count)]['cmd1sz'].item():
                loop_count1 += 1
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['cmd1sz'+str(loop_count1)]['cmdID'].item(),
                    unpack_value[unpack_value_count])

            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['cmd2sz'].item(),
                unpack_value[unpack_value_count])
            loop_count1, unpack_value_count = 0, unpack_value_count
            while loop_count1 < pck_np_array['count'+str(loop_count)]['cmd2sz'].item():
                loop_count1 += 1
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['cmd2sz'+str(loop_count1)]['cmdID'].item(),
                    unpack_value[unpack_value_count])

            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['cmdSz'].item(),
                unpack_value[unpack_value_count])
            loop_count1, unpack_value_count = 0, unpack_value_count
            while loop_count1 < pck_np_array['count'+str(loop_count)]['cmdSz'].item():
                loop_count1 += 1
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['cmdSz'+str(loop_count1)]['cmd'].item(),
                    unpack_value[unpack_value_count])
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['cmdSz'+str(loop_count1)]['key'].item(),
                    unpack_value[unpack_value_count])
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['cmdSz'+str(loop_count1)]['tgK1'].item(),
                    unpack_value[unpack_value_count])
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['cmdSz'+str(loop_count1)]['tgK2'].item(),
                    unpack_value[unpack_value_count])
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['cmdSz'+str(loop_count1)]['show'].item(),
                    unpack_value[unpack_value_count])
        unpack_value_count += 1
        self.assertEqual(pck_np_array['U__'].item(),
            unpack_value[unpack_value_count])
        unpack_value_count += 1
        self.assertEqual(pck_np_array['U___'].item(),
            unpack_value[unpack_value_count])



    def testHard5(self):
        # PacketsHighFive.ini
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
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="complex" name="pck_type" opt_code="11" pck_name="s_ItemList" side="server" type="i1">
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
                <la2:skip>
                  <la2:primitive name="blockMode" type="i1"/>
                </la2:skip>
                <la2:loop>
                    <la2:primitive name="blockItem" type="i4"/>
                </la2:loop>
              </la2:loop>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"server"
        py_string = """
class s_ItemList():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('ShowWindow', 'i2'), ('count', 'value', 'i2'), ('count', 'loop', [('ObjectID', 'i4'), ('ItemID:Get.F0', 'i4'), ('LocationSlot', 'i4'), ('Count', 'i8'), ('ItemType2', 'i2'), ('CustomType1', 'i2'), ('isEquipped', 'i2'), ('BodyPart', 'i4'), ('EnchantLevel', 'i2'), ('CustType2', 'i2'), ('AugmentID:Get.F1', 'i4'), ('Mana', 'i4'), ('remainTime', 'i4'), ('AttackElem', 'i2'), ('AttackElemVal', 'i2'), ('DefAttrFire', 'i2'), ('DefAttrWater', 'i2'), ('DefAttrWind', 'i2'), ('DefAttrEarth', 'i2'), ('DefAttrHoly', 'i2'), ('DefAttrUnholy', 'i2'), ('EnchEff1', 'i2'), ('enchEff2', 'i2'), ('enchEff3', 'i2')]), ('blockedItems', 'value', 'i2'), ('blockMode', 'i1'), ('blockedItems', 'loop', [('blockItem', 'i4')])])
        return dtype

pck_server[b'\\x11'] = s_ItemList"""
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
                self.xml_string_trim(xml_string),
        )
        self.maxDiff = None
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\x11", 17),],
                self.random_i(b"i2", 1),
                self.random_loop(b"i2",
                    (
                        self.random_i(b"i4", 3),
                        self.random_i(b"i8", 1),
                        self.random_i(b"i2", 3),
                        self.random_i(b"i4", 1),
                        self.random_i(b"i2", 2),
                        self.random_i(b"i4", 3),
                        self.random_i(b"i2", 11),
                    )
                ),
                self.random_loop(b"i2",
                    (
                        self.random_i(b"i4", 1),
                    ),
                    skip=self.random_i(b"i1", 1),
                ),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute

        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['ShowWindow'].item(),
            unpack_value[1])
        self.assertEqual(pck_np_array['count'].item(),
            unpack_value[2])
        loop_count, unpack_value_count = 0, 2
        while loop_count < pck_np_array['count'].item():
            loop_count += 1

            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['ObjectID'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['ItemID:Get.F0'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['LocationSlot'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['Count'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['ItemType2'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['CustomType1'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['isEquipped'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['BodyPart'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['EnchantLevel'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['CustType2'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['AugmentID:Get.F1'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['Mana'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['remainTime'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['AttackElem'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['AttackElemVal'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['DefAttrFire'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['DefAttrWater'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['DefAttrWind'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['DefAttrEarth'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['DefAttrHoly'].item(),
                unpack_value[unpack_value_count])           
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['DefAttrUnholy'].item(),
                unpack_value[unpack_value_count])            
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['EnchEff1'].item(),
                unpack_value[unpack_value_count])            
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['enchEff2'].item(),
                unpack_value[unpack_value_count])            
            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['enchEff3'].item(),
                unpack_value[unpack_value_count])            

        unpack_value_count += 1
        self.assertEqual(pck_np_array['blockedItems'].item(),
            unpack_value[unpack_value_count])
        unpack_value_count += 1
        self.assertEqual(pck_np_array['blockMode'].item(),
            unpack_value[unpack_value_count])
        loop_count = 0
        while loop_count < pck_np_array['blockedItems'].item():
            loop_count += 1

            unpack_value_count += 1
            self.assertEqual(pck_np_array['blockedItems'+str(loop_count)]['blockItem'].item(),
                unpack_value[unpack_value_count])   



    def testHard6(self):
        # PacketsHighFive.ini
        ini_string = b"""
          FE70=ExUISetting:h(subID)d(bufsize)d(categories)
            d(count:Loop.01.0010)
            c(catList1:Loop.01.0001)c(cmd)
            c(catList2:Loop.01.0001)c(cmd)
            d(keyList:Loop.01.0005)d(cmdID)d(keyID)
              d(toogleKey1)d(toogleKey2)d(showStatus)
            d(11)d(10)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="complex" name="pck_type" opt_code="FE70" pck_name="s_ExUISetting" side="server" type="i1">
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
        py_string = """
class s_ExUISetting():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('subID', 'i2'), ('bufsize', 'i4'), ('categories', 'i4'), ('count', 'value', 'i4'), ('count', 'loop', [('catList1', 'value', 'i1'), ('catList1', 'loop', [('cmd', 'i1')]), ('catList2', 'value', 'i1'), ('catList2', 'loop', [('cmd', 'i1')]), ('keyList', 'value', 'i4'), ('keyList', 'loop', [('cmdID', 'i4'), ('keyID', 'i4'), ('toogleKey1', 'i4'), ('toogleKey2', 'i4'), ('showStatus', 'i4')])]), ('11', 'i4'), ('10', 'i4')])
        return dtype

pck_server[b'\\xfep'] = s_ExUISetting"""
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
                self.xml_string_trim(xml_string),
        )
        self.maxDiff = None
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\xfe", -2),],
                [(b"\x70\x00", 0x0070),],
                self.random_i(b"i4", 2),
                self.random_loop(b"i4",
                    (
                        self.random_loop(b"i1",
                            (
                                self.random_i(b"i1", 1),
                            )
                        ),
                        self.random_loop(b"i1",
                            (
                                self.random_i(b"i1", 1),
                            )
                        ),
                        self.random_loop(b"i4",
                            (
                                self.random_i(b"i4", 5),
                            )
                        ),
                    )
                ),
                self.random_i(b"i4", 2),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute

        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['subID'].item(),
            unpack_value[1])
        self.assertEqual(pck_np_array['bufsize'].item(),
            unpack_value[2])
        self.assertEqual(pck_np_array['categories'].item(),
            unpack_value[3])
        self.assertEqual(pck_np_array['count'].item(),
            unpack_value[4])
        loop_count, unpack_value_count = 0, 4
        while loop_count < pck_np_array['count'].item():
            loop_count += 1
            unpack_value_count += 1

            self.assertEqual(pck_np_array['count'+str(loop_count)]['catList1'].item(),
                unpack_value[unpack_value_count])
            loop_count1, unpack_value_count = 0, unpack_value_count
            while loop_count1 < pck_np_array['count'+str(loop_count)]['catList1'].item():
                loop_count1 += 1
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['catList1'+str(loop_count1)]['cmd'].item(),
                    unpack_value[unpack_value_count])

            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['catList2'].item(),
                unpack_value[unpack_value_count])
            loop_count1, unpack_value_count = 0, unpack_value_count
            while loop_count1 < pck_np_array['count'+str(loop_count)]['catList2'].item():
                loop_count1 += 1
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['catList2'+str(loop_count1)]['cmd'].item(),
                    unpack_value[unpack_value_count])

            unpack_value_count += 1
            self.assertEqual(pck_np_array['count'+str(loop_count)]['keyList'].item(),
                unpack_value[unpack_value_count])
            loop_count1, unpack_value_count = 0, unpack_value_count
            while loop_count1 < pck_np_array['count'+str(loop_count)]['keyList'].item():
                loop_count1 += 1
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['keyList'+str(loop_count1)]['cmdID'].item(),
                    unpack_value[unpack_value_count])
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['keyList'+str(loop_count1)]['keyID'].item(),
                    unpack_value[unpack_value_count])
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['keyList'+str(loop_count1)]['toogleKey1'].item(),
                    unpack_value[unpack_value_count])
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['keyList'+str(loop_count1)]['toogleKey2'].item(),
                    unpack_value[unpack_value_count])
                unpack_value_count += 1
                self.assertEqual(pck_np_array['count'+str(loop_count)]['keyList'+str(loop_count1)]['showStatus'].item(),
                    unpack_value[unpack_value_count])
        unpack_value_count += 1
        self.assertEqual(pck_np_array['11'].item(),
            unpack_value[unpack_value_count])
        unpack_value_count += 1
        self.assertEqual(pck_np_array['10'].item(),
            unpack_value[unpack_value_count])   





    def testHard7(self):
        # PacketsHighFive.ini
        ini_string = b"""
          FE970000=ExCubeGameTeamList:
            h(subID)d(sub2ID)d(roomNumber)d(-1)
            d(bluePlayersCount:Loop.01.0002)d(playerObjID)d(name)
            d(redPlayersCount:Loop.01.0002)d(playerObjID)d(name)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="complex" name="pck_type" opt_code="FE970000" pck_name="s_ExCubeGameTeamList" side="server" type="i1">
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
        py_string = """
class s_ExCubeGameTeamList():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('subID', 'i2'), ('sub2ID', 'i4'), ('roomNumber', 'i4'), ('-1', 'i4'), ('bluePlayersCount', 'value', 'i4'), ('bluePlayersCount', 'loop', [('playerObjID', 'i4'), ('name', 'i4')]), ('redPlayersCount', 'value', 'i4'), ('redPlayersCount', 'loop', [('playerObjID', 'i4'), ('name', 'i4')])])
        return dtype

pck_server[b'\\xfe\\x97\\x00\\x00'] = s_ExCubeGameTeamList"""
        self.maxDiff = None
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\xfe", -2),],
                [(b"\x97\x00", 0x0097),],
                [(b"\x00\x00\x00\x00", 0x00000000),],
                self.random_i(b"i4", 2),
                self.random_loop(b"i4",
                    (
                        self.random_i(b"i4", 2),
                    )
                ),
                self.random_loop(b"i4",
                    (
                        self.random_i(b"i4", 2),
                    )
                ),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute

        self.assertEqual(pck_np_array['pck_type'].item(),
            unpack_value[0])
        self.assertEqual(pck_np_array['subID'].item(),
            unpack_value[1])
        self.assertEqual(pck_np_array['sub2ID'].item(),
            unpack_value[2])
        self.assertEqual(pck_np_array['roomNumber'].item(),
            unpack_value[3])
        self.assertEqual(pck_np_array['-1'].item(),
            unpack_value[4])
        self.assertEqual(pck_np_array['bluePlayersCount'].item(),
            unpack_value[5])
        loop_count, unpack_value_count = 0, 5
        while loop_count < pck_np_array['bluePlayersCount'].item():
            loop_count += 1

            unpack_value_count += 1
            self.assertEqual(pck_np_array['bluePlayersCount'+str(loop_count)]['playerObjID'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['bluePlayersCount'+str(loop_count)]['name'].item(),
                unpack_value[unpack_value_count])

        unpack_value_count += 1
        self.assertEqual(pck_np_array['redPlayersCount'].item(),
            unpack_value[unpack_value_count])
        loop_count = 0
        while loop_count < pck_np_array['redPlayersCount'].item():
            loop_count += 1

            unpack_value_count += 1
            self.assertEqual(pck_np_array['redPlayersCount'+str(loop_count)]['playerObjID'].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1
            self.assertEqual(pck_np_array['redPlayersCount'+str(loop_count)]['name'].item(),
                unpack_value[unpack_value_count])


    def testX1(self):
        # PacketsGraciaFinal.ini
        ini_string = b"""
        0B=CharSelected:
          s(Name)d(CharID)s(Title)d(SessionID)d(ClanID)
          d(0)d(Sex)d(Race)d(ClassID:Get.ClassID)d(1)
          d(X)d(Y)d(Z)f(CurrentHP)f(CurrentMP)
          d(SP)q(Exp)d(Level)d(Karma)d(PkKills)
          d(INT)d(STR)d(CON)d(MEN)d(DEX)
          d(WIT)d(GameTime)d(0)d(ClassID:Get.ClassID)d(0)
          d(0)d(0)d(0)-(64)d(0)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
          <root xmlns:la2="la2">
            <la2:pck_struct complexity="complex" name="pck_type" opt_code="0B" pck_name="s_CharSelected" side="server" type="i1">
              <la2:primitive name="Name" type="|S"/>
              <la2:primitive name="CharID" type="i4"/>
              <la2:primitive name="Title" type="|S"/>
              <la2:primitive name="SessionID" type="i4"/>
              <la2:primitive name="ClanID" type="i4"/>
              <la2:primitive name="0" type="i4"/>
              <la2:primitive name="Sex" type="i4"/>
              <la2:primitive name="Race" type="i4"/>
              <la2:primitive name="ClassID:Get.ClassID" type="i4"/>
              <la2:primitive name="1" type="i4"/>
              <la2:primitive name="X" type="i4"/>
              <la2:primitive name="Y" type="i4"/>
              <la2:primitive name="Z" type="i4"/>
              <la2:primitive name="CurrentHP" type="f8"/>
              <la2:primitive name="CurrentMP" type="f8"/>
              <la2:primitive name="SP" type="i4"/>
              <la2:primitive name="Exp" type="i8"/>
              <la2:primitive name="Level" type="i4"/>
              <la2:primitive name="Karma" type="i4"/>
              <la2:primitive name="PkKills" type="i4"/>
              <la2:primitive name="INT" type="i4"/>
              <la2:primitive name="STR" type="i4"/>
              <la2:primitive name="CON" type="i4"/>
              <la2:primitive name="MEN" type="i4"/>
              <la2:primitive name="DEX" type="i4"/>
              <la2:primitive name="WIT" type="i4"/>
              <la2:primitive name="GameTime" type="i4"/>
              <la2:primitive name="0_" type="i4"/>
              <la2:primitive name="ClassID:Get.ClassID_" type="i4"/>
              <la2:primitive name="0__" type="i4"/>
              <la2:primitive name="0___" type="i4"/>
              <la2:primitive name="0____" type="i4"/>
              <la2:primitive name="0_____" type="i4"/>
              <la2:primitive name="64" type="|S64"/>
              <la2:primitive name="0______" type="i4"/>
            </la2:pck_struct>
          </root>
        """
        self.ini_to_xml.side = b"server"
        py_string = """
class s_CharSelected():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('Name', '|S'), ('CharID', 'i4'), ('Title', '|S'), ('SessionID', 'i4'), ('ClanID', 'i4'), ('0', 'i4'), ('Sex', 'i4'), ('Race', 'i4'), ('ClassID:Get.ClassID', 'i4'), ('1', 'i4'), ('X', 'i4'), ('Y', 'i4'), ('Z', 'i4'), ('CurrentHP', 'f8'), ('CurrentMP', 'f8'), ('SP', 'i4'), ('Exp', 'i8'), ('Level', 'i4'), ('Karma', 'i4'), ('PkKills', 'i4'), ('INT', 'i4'), ('STR', 'i4'), ('CON', 'i4'), ('MEN', 'i4'), ('DEX', 'i4'), ('WIT', 'i4'), ('GameTime', 'i4'), ('0_', 'i4'), ('ClassID:Get.ClassID_', 'i4'), ('0__', 'i4'), ('0___', 'i4'), ('0____', 'i4'), ('0_____', 'i4'), ('64', '|S64'), ('0______', 'i4')])
        return dtype

pck_server[b'\\x0b'] = s_CharSelected"""
        self.assertEqual(
            self.xml_string_trim(
                self.ini_to_xml.convert([self.ini_string_trim(ini_string),])),
                self.xml_string_trim(xml_string),
        )
        self.maxDiff = None
        self.assertEqual(
            list(self.xml_to_py.convert(xml_string))[0],
            py_string,
        )
        pck = self.xml_to_py.execute(py_string)
        pack_value, unpack_value = [], []
        [(pack_value.append(i[0]), unpack_value.append(i[1])) \
            for i in chain(
                [(b"\x0b", 11),],
                self.random_string(1),
                self.random_i(b"i4", 1),
                self.random_string(1),
                self.random_i(b"i4", 10),
                self.random_f(b"f8", 2),
                self.random_i(b"i4", 1),
                self.random_i(b"i8", 1),
                self.random_i(b"i4", 16),
                self.random_string_fixed_length(b"|S64", 1),
                self.random_i(b"i4", 1),
            )
        ]
        py_execute = b"".join(pack_value)
        dtype = pck.dtype(self.ini_to_xml.side, py_execute)
        pck_np_array = numpy.zeros(1,dtype)
        pck_np_array[:] = py_execute

        unpack_value_count = 0
        for name in ("pck_type", 'Name', 'CharID', 'Title', 'SessionID',
    'ClanID', '0', 'Sex', 'Race', 'ClassID:Get.ClassID', '1', 'X', 'Y', 'Z',
    'CurrentHP', 'CurrentMP', 'SP', 'Exp', 'Level', 'Karma', 'PkKills', 'INT',
    'STR', 'CON', 'MEN', 'DEX', 'WIT', 'GameTime', '0_',
    'ClassID:Get.ClassID_', '0__', '0___', '0____', '0_____', '64', '0______'):
            self.assertEqual(pck_np_array[name].item(),
                unpack_value[unpack_value_count])
            unpack_value_count += 1

        


    def testX2(self):
        # PacketsGraciaFinal.ini
        ini_string = b"""
        09=CharSelectionInfo:
          d(ListSize:Loop.03.0066)
            d(a7_)c(a01_)
            s(Name1)d(CharID_)s(LoginName_)d(SessionID_)d(ClanID_)
            d(ab02)d(Sex_)d(Race_)d(ClassID1:Get.ClassID1)d(az1)
            d(X)d(Y)d(Z)f(CurrentHP)f(CurrentMP)
            d(SP)q(Exp)d(Level)d(Karma)d(PkKills)
            d(0_1)d(a0_2)d(a0_3)d(a0_4)d(a0_5)
            d(a0_6)d(a0_7)d(a0_8)d(Unknown_1)d(RightEarring)
            d(LeftEarring)d(Necklace)d(RightRing)d(LeftRing)d(Head)
            d(RightHand)d(LeftHand)d(Gloves)d(Chest)d(Legs)
            d(Boots)d(Unknown1)d(Unknown2)d(Hair)d(Face)
            d(Unknown3)d(Unknown4)d(0_a1)d(0_a2)d(0_a3)
            d(0_a4)d(0_a5)d(0_a6)d(HairStyle)d(HairColor)
            d(Face)f(MaxHP)f(MaxMP)d(DeleteDays)d(ClassID2:Get.ClassID2)
            d(ActiveID)c(EnchantEffect)d(AugmentID:Get.AugmentID)d(TransformID)d(aa1?)
        """
        xml_string = b"""<?xml version=\'1.0\' encoding=\'ASCII\'?>
<root xmlns:la2="la2">
  <la2:pck_struct complexity="complex" name="pck_type" opt_code="09" pck_name="s_CharSelectionInfo" side="server" type="i1">
    <la2:loop loop="66" name="ListSize" skip="2" type="i4">
      <la2:skip>
        <la2:primitive name="a7_" type="i4"/>
        <la2:primitive name="a01_" type="i1"/>
      </la2:skip>
      <la2:loop>
        <la2:primitive name="Name1" type="|S"/>
        <la2:primitive name="CharID_" type="i4"/>
        <la2:primitive name="LoginName_" type="|S"/>
        <la2:primitive name="SessionID_" type="i4"/>
        <la2:primitive name="ClanID_" type="i4"/>
        <la2:primitive name="ab02" type="i4"/>
        <la2:primitive name="Sex_" type="i4"/>
        <la2:primitive name="Race_" type="i4"/>
        <la2:primitive name="ClassID1:Get.ClassID1" type="i4"/>
        <la2:primitive name="az1" type="i4"/>
        <la2:primitive name="X" type="i4"/>
        <la2:primitive name="Y" type="i4"/>
        <la2:primitive name="Z" type="i4"/>
        <la2:primitive name="CurrentHP" type="f8"/>
        <la2:primitive name="CurrentMP" type="f8"/>
        <la2:primitive name="SP" type="i4"/>
        <la2:primitive name="Exp" type="i8"/>
        <la2:primitive name="Level" type="i4"/>
        <la2:primitive name="Karma" type="i4"/>
        <la2:primitive name="PkKills" type="i4"/>
        <la2:primitive name="0_1" type="i4"/>
        <la2:primitive name="a0_2" type="i4"/>
        <la2:primitive name="a0_3" type="i4"/>
        <la2:primitive name="a0_4" type="i4"/>
        <la2:primitive name="a0_5" type="i4"/>
        <la2:primitive name="a0_6" type="i4"/>
        <la2:primitive name="a0_7" type="i4"/>
        <la2:primitive name="a0_8" type="i4"/>
        <la2:primitive name="Unknown_1" type="i4"/>
        <la2:primitive name="RightEarring" type="i4"/>
        <la2:primitive name="LeftEarring" type="i4"/>
        <la2:primitive name="Necklace" type="i4"/>
        <la2:primitive name="RightRing" type="i4"/>
        <la2:primitive name="LeftRing" type="i4"/>
        <la2:primitive name="Head" type="i4"/>
        <la2:primitive name="RightHand" type="i4"/>
        <la2:primitive name="LeftHand" type="i4"/>
        <la2:primitive name="Gloves" type="i4"/>
        <la2:primitive name="Chest" type="i4"/>
        <la2:primitive name="Legs" type="i4"/>
        <la2:primitive name="Boots" type="i4"/>
        <la2:primitive name="Unknown1" type="i4"/>
        <la2:primitive name="Unknown2" type="i4"/>
        <la2:primitive name="Hair" type="i4"/>
        <la2:primitive name="Face" type="i4"/>
        <la2:primitive name="Unknown3" type="i4"/>
        <la2:primitive name="Unknown4" type="i4"/>
        <la2:primitive name="0_a1" type="i4"/>
        <la2:primitive name="0_a2" type="i4"/>
        <la2:primitive name="0_a3" type="i4"/>
        <la2:primitive name="0_a4" type="i4"/>
        <la2:primitive name="0_a5" type="i4"/>
        <la2:primitive name="0_a6" type="i4"/>
        <la2:primitive name="HairStyle" type="i4"/>
        <la2:primitive name="HairColor" type="i4"/>
        <la2:primitive name="Face_" type="i4"/>
        <la2:primitive name="MaxHP" type="f8"/>
        <la2:primitive name="MaxMP" type="f8"/>
        <la2:primitive name="DeleteDays" type="i4"/>
        <la2:primitive name="ClassID2:Get.ClassID2" type="i4"/>
        <la2:primitive name="ActiveID" type="i4"/>
        <la2:primitive name="EnchantEffect" type="i1"/>
        <la2:primitive name="AugmentID:Get.AugmentID" type="i4"/>
        <la2:primitive name="TransformID" type="i4"/>
        <la2:primitive name="aa1" type="i4"/>
      </la2:loop>
    </la2:loop>
  </la2:pck_struct>
</root>

        """
        self.ini_to_xml.side = b"server"
        py_string = """
class s_CharSelectionInfo():
    @classmethod
    def dtype(cls, data):
        pos = GetPosition(data)
        dtype = pos.get_dtype([('pck_type', 'i1'), ('ListSize', 'value', 'i4'), ('a7_', 'i4'), ('a01_', 'i1'), ('ListSize', 'loop', [('Name1', '|S'), ('CharID_', 'i4'), ('LoginName_', '|S'), ('SessionID_', 'i4'), ('ClanID_', 'i4'), ('ab02', 'i4'), ('Sex_', 'i4'), ('Race_', 'i4'), ('ClassID1:Get.ClassID1', 'i4'), ('az1', 'i4'), ('X', 'i4'), ('Y', 'i4'), ('Z', 'i4'), ('CurrentHP', 'f8'), ('CurrentMP', 'f8'), ('SP', 'i4'), ('Exp', 'i8'), ('Level', 'i4'), ('Karma', 'i4'), ('PkKills', 'i4'), ('0_1', 'i4'), ('a0_2', 'i4'), ('a0_3', 'i4'), ('a0_4', 'i4'), ('a0_5', 'i4'), ('a0_6', 'i4'), ('a0_7', 'i4'), ('a0_8', 'i4'), ('Unknown_1', 'i4'), ('RightEarring', 'i4'), ('LeftEarring', 'i4'), ('Necklace', 'i4'), ('RightRing', 'i4'), ('LeftRing', 'i4'), ('Head', 'i4'), ('RightHand', 'i4'), ('LeftHand', 'i4'), ('Gloves', 'i4'), ('Chest', 'i4'), ('Legs', 'i4'), ('Boots', 'i4'), ('Unknown1', 'i4'), ('Unknown2', 'i4'), ('Hair', 'i4'), ('Face', 'i4'), ('Unknown3', 'i4'), ('Unknown4', 'i4'), ('0_a1', 'i4'), ('0_a2', 'i4'), ('0_a3', 'i4'), ('0_a4', 'i4'), ('0_a5', 'i4'), ('0_a6', 'i4'), ('HairStyle', 'i4'), ('HairColor', 'i4'), ('Face_', 'i4'), ('MaxHP', 'f8'), ('MaxMP', 'f8'), ('DeleteDays', 'i4'), ('ClassID2:Get.ClassID2', 'i4'), ('ActiveID', 'i4'), ('EnchantEffect', 'i1'), ('AugmentID:Get.AugmentID', 'i4'), ('TransformID', 'i4'), ('aa1', 'i4')])])
        return dtype

pck_server[b'\\t'] = s_CharSelectionInfo"""

        with self.assertRaisesRegex(PacketCompileException, "wrong ini body.*"):
            self.ini_to_xml.convert([self.ini_string_trim(ini_string),])





if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner().run(suite)
    #unittest.main()
