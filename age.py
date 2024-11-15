class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class Person:
    def __init__(self, name):
        self.name = name
        self.age = None

    def set_age(self, age):
        if age < 0 or age > 120:
            raise InvalidAgeError(f"Неправильний вік для {self.name}: {age}.")
        self.age = age

    def __str__(self):
        return f"{self.name}, вік: {self.age}"


people_age = (
    ("Матвій", 12),
    ("Микита", -1),
    ("Олександр", 120000),
)

for name, age in people_age:
    person = Person(name)
    try:
        person.set_age(age)
        print(person)
    except InvalidAgeError as e:
        print(f"Помилка: {e}")




