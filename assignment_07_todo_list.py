def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')

def view_tasks(tasks):
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("Your Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def delete_task(tasks):
    if len(tasks) == 0:
