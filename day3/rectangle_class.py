class Rectangle:
    """Rectangle.

    Args:
        width
        height
    Both width an height should be positive numbers
    """
    def __init__(self, width, height):
        if width <= 0:
            raise ValueError('Width has to be positive.')
        if height <= 0:
            raise ValueError('Height has to be positive')
        self.width = width
        self.height = height

    def area(self):
        """computes the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def draw(self):
        pass

rect = Rectangle(100, 20)
print('Wysokość: ', rect.height)
print('Szerokość: ', rect.width)
print('Pole wynosi: ', rect.area())
print('Obówd wynosi: ', rect.perimeter())
Rectangle(-1, 2)