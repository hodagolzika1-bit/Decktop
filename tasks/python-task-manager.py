tasks=[]

def min():
    message="""
    1-add tasks to a list
    2-mark task as comblete
    3-view tasks
    4-quit
    """
    while True:
        print(message)
        choice=input("enter choice number please : ")
        if choice=="1":
            add_task()    
        elif choice=="2":
            mark_task()
        elif choice=="3":
            view_tasks()
        elif choice=="4":
            print("quit good bye ")
            break    


def add_task():
    task=input("enter your task :")
    task_info={"task":task ,"completed":False} 
    tasks.append(task_info)   
    print("task added")
def mark_task():
    incomplete_tasks=[task for task in tasks if task["completed"]==False]
    if not incomplete_tasks:print(" no tasks to complete!");return
    for i,task in enumerate(incomplete_tasks):
        print(f"{i+1}- {task['task']}")
    print("-"*30)
    try:
        
        task_number=int(input("choose the task is complete : "))
        if 1 <= task_number <= len(incomplete_tasks):
            incomplete_tasks[task_number-1]["completed"]=True
            print(" task is marked as completed!")
        else:
            print(" invalid task number!")
    except ValueError:
        print(" please enter a valid number.")            
def view_tasks():
    if not tasks: print("no tasks yet");return
    else:
        for val,key in enumerate(tasks):
            stats="✔"if key["completed"] else "✖"
            print(f"{val+1}:{key['task']} {stats}")
min()