import struct
import types


class LenPackets():

    def pck_in(self, data: types.GeneratorType) -> types.GeneratorType:
        _data =  b''.join(data)
        if _data:
            yield _data

    def pck_out(self, value: types.GeneratorType) -> types.GeneratorType :
        yield from value
