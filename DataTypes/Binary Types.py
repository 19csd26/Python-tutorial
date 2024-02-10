#7.Binary Types:
#I.bytes: Represents a sequence of bytes, immutable.
binary_data = b'hello'

#II.bytearray: Mutable version of bytes.
mutable_binary_data = bytearray(b'hello')

#III.memoryview: Provides a memory view of a sequence of bytes.
mv = memoryview(b'hello')
