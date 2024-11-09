

# try:
#     a = int(input())
#     b = 0
#     c = a/b
# except ZeroDivisionError:
#     print("На 0 делить нельзя")

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def multiplication(self):
#         if self.length <= 0 or self.width <= 0:
#             return "Ошибка! Одна из сторон равна 0 или меньше 0"
#         return self.length * self.width
#
#
# rectangle = Rectangle(10, 0)
# print(rectangle.multiplication())
#
# rectangle = Rectangle(10, 4)
# print(rectangle.multiplication())

# class StringIterator:
#     def __init__(self, strings):
#         self.strings = strings
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.strings):
#             result = self.strings[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration
#
#
# strings = ["green", "blue","yellow", "violet"]
# iterator = StringIterator(strings)
#
# for string in iterator:
#     print(string)

def my_generator():
    for i in range(1, 7):
        yield i


gen = my_generator()


print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))









