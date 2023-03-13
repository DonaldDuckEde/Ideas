class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
x = input("x: ")
y = input("y: ")

p = Point(x, y)

print(p.x)
print(p.y)