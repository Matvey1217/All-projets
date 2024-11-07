

class Task:
    def __init__(self, title, description, deadline, completed=False):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = completed


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Завдання '{task.title}' додано.")

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Завдання '{task.title}' видалено.")
        else:
            print(f"Завдання '{task.title}' не знайдено.")

    def list_tasks(self):
        if not self.tasks:
            print("Завдань немає.")
        else:
            for task in self.tasks:
                status = "Виконано" if task.completed else "Не виконано"
                print(f"{task.title} - {task.deadline} - {status}")



task1 = Task("Купити одяг", "Купити шкільну форму", "2024-09-01")
task2 = Task("Виконати домашні завдання", "Математика, англійська мова, історія", "2024-11-15")
task3 = Task("Пройти комп'ютерну гру", "Gta 5", "2024-12-30")


manager = TaskManager()
manager.add_task(task1)
manager.add_task(task2)
manager.add_task(task3)


print("Список завдань:")
manager.list_tasks()


manager.delete_task(task1)
manager.delete_task(task2)


print("\nСписок завдань після видалення:")
manager.list_tasks()




