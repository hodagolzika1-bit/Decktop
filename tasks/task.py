task=[]
print("---welcome to the to-list app---")

while True:     
   print("-"*30)
   print("choose an option")
   print("1: add task")
   print("2: view task")
   print("3: delete task")
   print("4: exit")
   print("-------------------")
   choise=input("enter your choise (1-4) =>:")
   if choise=="1":
       value=input("enter a task :")
       task.append(value)
       print("task added : ")
   elif choise =="2":
       if not task:
           print("no tasks yet ")
       else:    
        for vla,key in enumerate(task):
           print(f"{vla+1}:{key}")   
   elif choise=="3":
        if not task:
            print("no tasks to dalete")
        else:
            print(task)
            task_number=int(input("enter task number to delate"))
            
            if task_number>=1 and task_number<=len(task):
                delete=task.pop(task_number-1)
                print(f"deleted task is: {delete}")
            else:
                print("invield value")
   elif choise=="4":
        print("good bye")
        break
   else:
        print("invield choise try again (1-4)")                           