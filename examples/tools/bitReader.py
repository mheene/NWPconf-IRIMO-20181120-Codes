import sys



#print ("Size of bytearry {0:08d}".format(size))

f = open(sys.argv[1], "rb")

counter = 0

try:
    byte = f.read(1)

    print ""

    while byte != "":
        # Do stuff with byte.
        byte = ord(byte)
        # now convert to string of 1s and 0s
        byte = bin(byte)[2:].rjust(8, '0')
        # now byte contains a string with 0s and 1s
        for bit in byte:
            #print bit
            sys.stdout.write(bit)
            sys.stdout.flush()

        counter = counter + 1
        if ( counter % 8 == 0 ):
            print "|  : %d" % (counter)
            print ""

#        if (counter % 8):
        sys.stdout.write('|')
        sys.stdout.flush()
        
        byte = f.read(1)

    print ""

finally:
    f.close()

#print ("counter %d " %counter )

