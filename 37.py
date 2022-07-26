x = 1

def funkcja():
    global x
    global y
    x = 2
    y = 3
    print ('funkcja x =', x, "y = ", y)
    return

print (x)
funkcja()
print ('x = ', x, 'y = ', y)    