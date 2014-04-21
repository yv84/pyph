# Ну писал же пару страниц назад и в репозиторий заливал.
# XX XX DD 03 DATA
# Где DATA - запакованные данные. Первые 2 байта распакованных данных опкод. Остальное пакет.

# XX XX DD 04 PC PC DATA
# Где PC - два байта - количество пакетов в контейнере.
# DATA - запакованные данные. Подряд лежащие пакеты опкод-тело.

# Алгоритм сжатия Deflate.




# inflate / deflate algoritm based on http://pastebin.com/wEVGmaWZ

import zlib
import base64
 
def decode_base64_and_inflate( b64string ):
    decoded_data = base64.b64decode( b64string )
    return zlib.decompress( decoded_data , -15)
 
def deflate_and_base64_encode( string_val ):
    zlibbed_str = zlib.compress( string_val )
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode( compressed_string )
       
# uncompressed_string.encode('zlib')[2:-4]
# or
# zlib.compress(uncompressed_string)[2:-4]
# Throws away 2-byte zlib header and the 4-byte checksum.
# Version using encode vanishes in Python 3.x.
       
# import zlib
 
def deflate(data, compresslevel=9):
    compress = zlib.compressobj(
            compresslevel,        # level: 0-9
            zlib.DEFLATED,        # method: must be DEFLATED
            -zlib.MAX_WBITS,      # window size in bits:
                                  #   -15..-8: negate, suppress header
                                  #   8..15: normal
                                  #   16..30: subtract 16, gzip header
            zlib.DEF_MEM_LEVEL,   # mem level: 1..8/9
            0                     # strategy:
                                  #   0 = Z_DEFAULT_STRATEGY
                                  #   1 = Z_FILTERED
                                  #   2 = Z_HUFFMAN_ONLY
                                  #   3 = Z_RLE
                                  #   4 = Z_FIXED
    )
    deflated = compress.compress(data)
    deflated += compress.flush()
    return deflated
 
def inflate(data):
    decompress = zlib.decompressobj(
            -zlib.MAX_WBITS  # see above
    )
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated