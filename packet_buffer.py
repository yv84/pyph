from l2.key_init import KeyInit, Connect
        

class Packet():
    def __init__(self):
        self._data = {'client': b'', 'server': b''} # from side
        self.client = Connect()
        self.server = Connect()
        self.key_init = KeyInit(self)
        self.server.command_stack.append(lambda data: self.key_init.key_packet_initialization(data))

    def update_data(self, side, data):
        if side == 'client':
            self.client._data = b''.join([self.client._data, data])
        elif side == 'server':
            self.server._data = b''.join([self.server._data, data])
        else:
            raise Exception('invalid side')

    def run(self):
        to_c_data, to_s_data = self.client._data, self.server._data
        self.client._data, self.server._data = b'', b''

        for stack, to_data in zip([self.client.command_stack, self.server.command_stack],
                    [to_s_data, to_c_data]):
            gen = to_data
            for cmd in stack:
                gen = cmd(gen)
            to_data = gen

        print(to_c_data, to_s_data)
        return to_c_data, to_s_data # to side
