some_bytes = b'\xC3\xA9'

with open ('myFile.txt', 'wb') as binary_file:

    binary_file.write(some_bytes)
#Alternatively, open() and close() can be called explicitly as shown below. However, this method requires you to perform error handling yourself, that is, ensure that the file is always closed, even if there is an error during writing. So, using the “with” statement is better in this regard as it will automatically close the file when the block ends.