def print_result(func):
    def wrapper():
        result = func()
        print(f"Результат: {result}")
    return wrapper


class MyIterator:
    def __init__(self, n):
        self.n = n


    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.current
            self.current += 1
            return result
        raise StopIteration


    def count_down(self):
        for i in range(self.n, -1, -1):
            yield i


    def multiplier(self, m):
        return lambda x: x * m


iterator = MyIterator(5)


print("Ітератор:")
for num in iterator:
    print(num)
print("Результат: None")


print("Генератор:")
for num in iterator.count_down():
    print(num)
print("Результат: None")


print("Замикання:")
multiply_by_2 = iterator.multiplier(2)
result = multiply_by_2(3)
print(result)





