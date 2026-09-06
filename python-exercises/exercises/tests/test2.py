class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def squared(self):
        result = self.width * self.height
        return result

box = Rectangle(10,10)

print (box.squared())