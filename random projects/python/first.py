class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def testDef():    
    try:    
        x = int(input("x: "))
        y = int(input("y: "))

        p = Point(x, y)

        print(p.x)
        print(p.y)
    
    except ValueError():
        print("Please check your input")
        testDef()
    
    except:
        print("I have no idea what went wrong")
        
testDef()