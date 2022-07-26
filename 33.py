x = 1

def funkcja():
    global x
    x = 2
    y = 3
    print ('funkcja x =', x, "y = ", y)
    return

print (x)
funkcja()
print (x)    