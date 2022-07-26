# Create bytearray 
# (sequence of values in 
# the range 0-255 in binary form)
  
# ASCII for A,B,C,D
byte_arr = [65,66,67,68] 
some_bytes = bytearray(byte_arr)
  
# Bytearray allows modification
# ASCII for exclamation mark
some_bytes.append(33)
  
# Bytearray can be cast to bytes
immutable_bytes = bytes(some_bytes)
  
# Write bytes to file
with open("my_file.txt", "wb") as binary_file:
    binary_file.write(immutable_bytes)