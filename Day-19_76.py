import zlib
X = "hello world!hello world!hello world!hello world!"
Y = bytes(X, 'utf-8')
#TypeError: a bytes-like object is required, not 'str'
x = zlib.compress(Y)
print(x)
print(zlib.decompress(x))