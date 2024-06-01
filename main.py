class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def completed_tasks(self):
        if self.completed:
            return "Выполнено"
        else:
            return "Не выполнено"

    def __str__(self):
        status = self.completed_tasks()
        return f"Описание: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Некорректный индекс задачи")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def display_tasks(self):
        if not self.tasks:
            print("Нет задач")
        for index, task in enumerate(self.tasks):
            print(f"Задача {index + 1}: {task}")

    def display_pending_tasks(self):
        pending_tasks = self.get_pending_tasks()
        if not pending_tasks:
            print("Все задачи выполнены")
        for index, task in enumerate(pending_tasks):
            print(f"Задача {index + 1}: {task}")


if __name__ == "__main__":
    task_manager = TaskManager()


    task_manager.add_task("Купить продукты", "2024-06-01")
    task_manager.add_task("Закончить проект", "2024-06-05")


    print("Все задачи:")
    task_manager.display_tasks()


    task_manager.mark_task_as_completed(0)

    
    print("\nТекущие задачи:")
    task_manager.display_pending_tasks()