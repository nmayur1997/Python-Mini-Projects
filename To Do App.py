#!/usr/bin/env python
# coding: utf-8

# In[4]:


def task():
    tasks = []
    print('---WELCOME TO THE TASK MANAGEMENT APP---')
    
    total_task = int(input('Enter how many tasks you want to add: '))
    for i in range(total_task):
        task_name = input(f'Enter task {i + 1}: ')
        tasks.append(task_name)
    print(f"Today's tasks are\n{tasks}")
    
    while True:
        operation = int(input('Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n'))
        if operation == 1:
            add = input('Enter task you want to add: ')
            tasks.append(add)
            print(f'Task "{add}" has been added successfully.')
        elif operation == 2:
            updated_val = input('Enter the task name you want to update: ')
            if updated_val in tasks:
                up = input('Enter new task: ')
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f'Task "{updated_val}" has been updated to "{up}".')
            else:
                print(f'Task "{updated_val}" not found.')
        elif operation == 3:
            del_val = input('Enter the task name you want to delete: ')
            if del_val in tasks:
                tasks.remove(del_val)
                print(f'Task "{del_val}" has been deleted successfully.')
            else:
                print(f'Task "{del_val}" not found.')
        elif operation == 4:
            print(f"Current tasks are:\n{tasks}")
        elif operation == 5:
            print("Exiting the Task Management App.")
            break
        else:
            print("Invalid operation. Please try again.")

# Running the task management function
task()


# In[ ]:




