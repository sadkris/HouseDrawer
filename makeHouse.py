def drawHouse(size):
    drawRoof(size)
    drawBase(size)

def drawRoof(size):
    size -= 1
    for i in range(size, -1, -1):
        print((i*" ")+"/"+(" "*(2*(size-i)))+"\\")

def drawBase(size):
    print(size*2*"-")
    print("|"+((size*2-2)*" ")+"|")

drawHouse(1)