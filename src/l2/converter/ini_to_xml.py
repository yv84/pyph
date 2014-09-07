import re


class IniToXml():
    def convert(self, line_in):
        xml_out = b''
        if line_in == b"""00=Logout:""":
            xml_out = b"""<pck_struct name="c_Logout" side="client" type="00" />"""
        return xml_out
