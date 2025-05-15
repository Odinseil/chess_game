def plateau():
    x = 0
    y = 0
    print(x,y)
    for i in range(8):
        for i in range(7):
            x = x + 1
            print(x,y)
        x = 0
        y = y + 1
        print(x,y)

plateau()
