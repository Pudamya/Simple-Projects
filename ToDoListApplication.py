#Variable initiaization

title=""
due_date=""
description=""
choice=""

#Defining a class called Task
class Task:
    def __init__(self, title, description, due_date):
        "To represent the task with title, description and due_date"
        self.title = title
        self.description = description
        self.due_date = due_date

#Defining a class called TodoList
class TodoList:
    def __init__(self):
        "To represent the tasks"
        self.tasks = []

    def add_task(self, task):
        "To add the tasks"
        self.tasks.append(task)

    def delete_task(self, task_title):
        "To delete the taks"
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def list_tasks(self):
        "To present the list of tasks"
        for task in self.tasks:
            print(f"Title: {task.title}\nDescription: {task.description}\nDue Date: {task.due_date}\n")

#Defining a function called main.
def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task\n2. Delete Task\n3. List Tasks\n4. Exit")
        #Get the choice of the user as a input.
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            title = input("Enter task title to delete: ")
            todo_list.delete_task(title)
            print("Task deleted successfully!")

        elif choice == "3":
            print("Tasks:")
            todo_list.list_tasks()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


print("**********To Do List Application**********")

if __name__ == "__main__":
    main()
