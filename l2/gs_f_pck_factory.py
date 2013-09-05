import numpy
import rpgClubEmpire.l2_class

def f_packet_R(Rules, status):
    class pck_f(type):
         
        def __new__(meta, classname, supers, classdict):
            if (Rules.get('chronicles') in ('rpg-club_empire')):
                if status == 0: from rpgClubEmpire import l2_func
                else:           reload(rpgClubEmpire.l2_func)
                for i in l2_func.l2_func.__dict__:
                    if type(lambda : 0) == type(l2_func.l2_func.__dict__[i]): classdict[i] = l2_func.l2_func.__dict__[i] #slovar' classa sosctit iz mnogix znacheniu', vibiraem tol'ko func
                if status == 0: from rpgClubEmpire import event
                else:           reload(rpgClubEmpire.event)
                if (Rules.get('dest') == 'C'): classdict['act_c'] = event.event.act_c
                if (Rules.get('dest') == 'S'): classdict['act_s'] = event.event.act_s
                if status == 0: from rpgClubEmpire import gs_l2_packet
                else:           reload(rpgClubEmpire.gs_l2_packet)
                if (Rules.get('dest') == 'C'): classdict['init_Pck_invoke_dict_c'] = gs_l2_packet.gs_l2_packet.init_Pck_invoke_dict_c
                if (Rules.get('dest') == 'S'): classdict['init_Pck_invoke_dict_s'] = gs_l2_packet.gs_l2_packet.init_Pck_invoke_dict_s
                classdict['pack'] = gs_l2_packet.gs_l2_packet.pack
                classdict['unpack'] = gs_l2_packet.gs_l2_packet.unpack
                if status == 0: from rpgClubEmpire import l2_class
                else:           reload(rpgClubEmpire.l2_class)
            if Rules.get('xor') in ('native', 'rpg-club_empire'):
                if status == 0: from rpgClubEmpire import xor
                else:           reload(rpgClubEmpire.xor)
                classdict['set_new_key'] = xor.xor.set_new_key
                classdict['set_key']     = xor.xor.set_key
                classdict['Decode']      = xor.xor.Decode
                classdict['Code']        = xor.xor.Code
            if (Rules.get('server') in ('rpg-club_empire')):
                if (Rules.get('dest') == 'C'):
                    if status == 0: from rpgClubEmpire import mod_pck_c
                    else:           reload(rpgClubEmpire.mod_pck_c)
                    classdict['ChangePck_in'] = mod_pck_c.mod_pck_c.ChangePck_in
                    classdict['ChangePck_out'] = mod_pck_c.mod_pck_c.ChangePck_out
                if (Rules.get('dest') == 'S'):
                    if status == 0: from rpgClubEmpire import mod_pck_s
                    else:           reload(rpgClubEmpire.mod_pck_s)
                    classdict['ChangePck_in'] = mod_pck_s.mod_pck_s.ChangePck_in
                    classdict['ChangePck_out'] = mod_pck_s.mod_pck_s.ChangePck_out
        
            return type.__new__(meta, classname, supers, classdict)
    return pck_f


def f_pck_factory(Rules,status):    #cherez obraschenie k funcii class budet sozdan, daje esli ranshe ego uje ispolzovali
    class pck_factory(metaclass=f_packet_R(Rules,status)):
        def __init__(self, parent):
            self.gs_packet = parent
            self.last_packet = None
            self.last_head = None
            self.l2_d = self.gs_packet.l2_d
            self.me = rpgClubEmpire.l2_class.Me(self)
            self.npc = rpgClubEmpire.l2_class.Npc(self)
            self.l2_d = {
            'me': self.me
            }
    return pck_factory