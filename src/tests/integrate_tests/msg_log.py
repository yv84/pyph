import sys
import os

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
print("!"*80, SCRIPT_DIR)
p = sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
print("!"*80, p)

#from mypackage.mymodule import as_int



from proxy.repr_to_bytes import repr_bytes_to_bytes_gen


class Message():
    def __init__(self, side, log=None, side_log=None):
        self.side = side
        self.msg = b''
        self.pin_pong = self.pin_pong_f(log, side_log)

    def pin_pong_f(self, _log, _side_log):
        log = {'client' : [], 'server' : [], }
        last_string = b''
        last_side = 'client'
        for i in range(len(_log)):
            if i == 0:
                last_string = _log[i]
                last_side = 'client'
            elif i in _side_log[last_side]:
                last_string = b''.join([last_string, _log[i]])
            elif i not in _side_log[last_side]:
                log[last_side].append(last_string)
                last_string = _log[i]
                last_side = 'server' if last_side == 'client' else 'client'
        _pin_pong = {}
        if self.side == 'client':
            _pin_pong.update({b'':log['client'].pop(0)})
            while log['client'] and log['server']:
                _pin_pong.update({log['server'].pop(0):log['client'].pop(0)})
        elif self.side == 'server':
            while log['client'] and log['server']:
                _pin_pong.update({log['client'].pop(0):log['server'].pop(0)})
        return _pin_pong

    def __call__(self, msg=b''):
        self.msg = b''.join([self.msg, msg])
        if self.msg in self.pin_pong:
            yield self.pin_pong[self.msg]
            self.msg = b''

    @staticmethod
    def game_log_from_import(log):
        _log = []
        _side_log = {'client': [], 'server': []}
        i = 0
        while log:
            if log and log[0].get('C') != None:
                _side_log['client'].append(i)
                _log.append(log.pop(0)['C'])
            elif log and log[0].get('S') != None:
                _side_log['server'].append(i)
                _log.append(log.pop(0)['S'])
            else:
                raise Exception("S/C key wrong")
            i += 1
        return (_log, _side_log,)

    @staticmethod
    def get_log_from_file(f, pattern):
        log = []
        with open(f, 'rb') as f:
            for line in f:
                line = b''.join(repr_bytes_to_bytes_gen(line))
                if line[0:len(pattern['c'])] == pattern['c']:
                    log.append({"C": line[pattern['start']:pattern['end']]})
                elif line[0:len(pattern['s'])] == pattern['s']:
                    log.append({"S": line[pattern['start']:pattern['end']]})
        return log
