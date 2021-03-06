import binascii
from types import GeneratorType

int_to_bytes = lambda i: binascii.a2b_hex( ('%x'%i if i>15 else ''.join(['0', '%x'%i])).encode('latin-1') )


def repr_bytes_to_bytes_gen(s: bytes) -> GeneratorType:
    simvol = { 116: b'\x09', 110: b'\x0a', 114: b'\x0d', 0x5c: b'\x5c', 0x22: b'\x22',  0x27: b'\x27'} # \t \n \r \ ' \"
    i = 0
    while i < len(s):
        if (i+3<len(s)) and s[i:i+2]==b'\\x':
            if not isinstance(binascii.a2b_hex(s[i+2:i+4]), bytes):
                print(binascii.a2b_hex(s[i+2:i+4]))
            yield binascii.a2b_hex(s[i+2:i+4])
            i += 4
        elif (i+1<len(s)) and s[i]==0x5c:
            if not isinstance(simvol[s[i+1]], bytes):
                print(simvol[s[i+1]])
            yield simvol[s[i+1]]
            i += 2
        else:
            if not isinstance(s[i:i+1], bytes):
                print(s[i:i+1])
            yield s[i:i+1]
            i += 1

def from_str_to_repr_bytes(s: str) -> bytes:
    return b''.join(repr_bytes_to_bytes_gen(s.encode('latin-1')))


def test_from_str_to_repr_bytes(i):
    assert(i == len(from_str_to_repr_bytes(''.join([chr(i) for i in range(i)]))))

def test_repr_bytes_to_bytes_gen(s: bytes):
    assert(s == b''.join(repr_bytes_to_bytes_gen(s.__repr__()[2:-1].encode('latin-1'))))

test_repr_bytes_to_bytes_gen(b'123\\ \t \n \t \n\x0c\x00\xff)')
test_repr_bytes_to_bytes_gen(b''.join([int_to_bytes(i) for i in range(256)]))
test_from_str_to_repr_bytes(90)



