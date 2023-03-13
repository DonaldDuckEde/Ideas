def testDef():    
    try:    
        x = int(input("x: "))
        y = int(input("y: "))

        p = Point(x, y)

        print(p.x)
        print(p.y)
    
    except:
        print("Please check your input")
        testDef()