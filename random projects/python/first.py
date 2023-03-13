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
    
    except:
        print("Please check your input")
        testDef()
        
testDef()
    