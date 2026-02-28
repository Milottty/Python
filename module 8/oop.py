

class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width
    def calculate_perimeter(self):
        return 2*(self.height * self.width)

new_rectangle = Rectangle(5, 4)

area = new_rectangle.calculate_area()
perimeter = new_rectangle.calculate_perimeter()
print(area)
print(perimeter)
