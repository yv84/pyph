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
