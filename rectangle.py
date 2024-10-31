class Rectangle:
  def __init__(self, weight, height):
     self.weight = weight
     self.height = height

  def calculate_area(self):
    return self.weight * self.height

  def calculate_perimeter(self):
    return (self.weight+self.height)*2

  def rectangle_info(self):
    print(f"Ширина: {self.weight}")
    print(f"Висота: {self.height}")
    print(f"Площа: {self.calculate_area()}")
    print(f"Периметр: {self.calculate_perimeter()}")



rectangle = Rectangle(20, 40)
rectangle.rectangle_info()



