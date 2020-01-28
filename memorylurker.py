in_file = open("memory5.bin", "rb")
data = in_file.read()
in_file.close()
startingaddress = 0x22C85A8
structlength = 0

while True:
    while True:
        yes = data.find(startingaddress.to_bytes(4, 'little'))
        if yes != -1:
            break
        startingaddress-=4
        structlength+=4
    print("Needed to rewind to %s" % hex(startingaddress))
    print("The value is at position %s" % hex(yes + 0x2000000))
    print("The value is at struct's position %d " % structlength)
    if yes<0x200000:
        break
    startingaddress = yes + 0x2000000
    structlength = 0

