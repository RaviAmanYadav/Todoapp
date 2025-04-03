import json


def load_task():
    try:
        with open("task.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("task.txt", "w") as file:
        json.dump(tasks, file)


def add_task(tasks):
    name = input("Enter your task => ")
    tasks.append({"name": name})
    save_tasks(tasks)
    print("Your task has been added")


def list_all_task(tasks):
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']}")


def update_task(tasks):
    list_all_task(tasks)
    index = int(input("Enter the task number to be updated => "))
    if 1 <= index <= len(tasks):
        name = input("Enter new task => ")
        tasks[index - 1] = {"name": name}
        save_tasks(tasks)
        print("Your task has been updated")
    else:
        print("Invalid index selected")


def delete_task(tasks):
    list_all_task(tasks)
    index = int(input("Enter the task number to be deleted => "))
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        save_tasks(tasks)
        print("Your task has been deleted")
    else:
        print("Invalid number you have choosen")


def completed_task(tasks):
    list_all_task(tasks)
    index = int(input("Enter the task number that has been completed => "))
    if 1 <= index <= len(tasks):
        print(f"Your task {tasks[index-1]['name']} has been completed")
        del tasks[index - 1]
        save_tasks(tasks)


def main():
    tasks = load_task()
    while True:
        print("To Do App")
        print("1. Add task")
        print("2. List all the task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Completed Task")
        print("6. Exit")
        choice = input("Enter your choice => ")
        match choice:
            case "1":
                add_task(tasks)

            case "2":
                list_all_task(tasks)

            case "3":
                update_task(tasks)

            case "4":
                delete_task(tasks)
            case "5":
                completed_task(tasks)
            case "6":
                break
            case _:
                print("Invalid! Option is not there")


if __name__ == "__main__":
    main()
