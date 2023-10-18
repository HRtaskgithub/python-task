class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully!')

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print(f'Task "{old_task}" updated to "{new_task}" successfully!')
        else:
            print(f'Task "{old_task}" not found.')
            
    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" deleted successfully!')
        else:
            print(f'Task "{task}" not found.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for i, task in enumerate(self.tasks, 1):
                print(f'{i}. {task}')

def main():
    todo_list = TodoList()

    while True:
        print('\n ~~~~~~~~ To-Do List Menu ~~~~~~~~ ')
        print('1. Add Task ')
        print('2. Update Task ')
        print('3. Delete Task ')
        print('4. View Tasks ')
        print('5. Exit ')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
            
        elif choice == '2':
            old_task = input('Enter the task to update: ')
            new_task = input('Enter the new task: ')
            todo_list.update_task(old_task, new_task)
            
        elif choice == '3':
            task = input('Enter the task to delete: ')
            todo_list.delete_task(task)
        
        elif choice == '4':
            todo_list.view_tasks()
            
        elif choice == '5':
            print('Exiting the To-Do List application. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == '__main__':
    main()
