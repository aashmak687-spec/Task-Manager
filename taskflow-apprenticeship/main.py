class Task:
    def __init__(self,id,title,priority):
        allowed_priorities =["Low","Medium","High"]
        if priority not in allowed_priorities:
            raise ValueError("Invalid priority!")
        self.id = id
        self.title = title
        self.priority = priority
        self.is_completed = False
    def rename(self,new_title):
        print("Before:",self.title)
        print("New title:",new_title)
        self.title = new_title
        print("After:",self.title)
    def mark_completed(self):
        self.is_completed = True
    def get_details(self):
       if self.is_completed == False:
           return f"ID: {self.id} | Title: {self.title} | Status: Pending | Priority: {self.priority}"
       else:
           return f"ID: {self.id} | Title: {self.title} | Status: Completed | Priority: {self.priority}"
class TaskManager:
    def __init__(self):
        self.tasks =[]
    def add_task(self,task):
        self.tasks.append(task)
        print("Task added successfully!")
    def find_task(self,task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    def delete_tasks(self,task_id):
        task = self.find_task(task_id)
        if task is not None:
            self.tasks.remove(task)
            return True
        return False  
    def filter_tasks(self,is_completed):
        filtered_tasks =[]
        for task in self.tasks:
            if task.is_completed == is_completed:
                filtered_tasks.append(task)
        return filtered_tasks
    def filter_by_priority(self,priority):
        priority_tasks =[]
        for task in self.tasks:
            if task.priority == priority:
                priority_tasks.append(task)
        return priority_tasks
    def get_all_tasks(self):
        return self.tasks
    def count_completed(self):
        count = 0
        for task in self.tasks:
            if task.is_completed == True:
                 count +=1
        print(f"Completed task: {count}")
manager = TaskManager()

task1 = Task(1,"Learn Python OOP","High")
task2 = Task(2,"Practise Git","Medium")
task3 = Task(3,"Build a FastAPI project","Low")
task4 = Task(4,"Tutor the kids","Medium")

manager.add_task(task1)
manager.add_task(task2)
manager.add_task(task3)
manager.add_task(task4)

task2.mark_completed()
task3.mark_completed()

task4.rename("Tutor the childrens")

result = task1.get_details()
print("Retured value:",result)

x = manager.find_task(1)
print(x.get_details())

print(manager.find_task(99))

print(manager.delete_tasks(4))

for task in manager.get_all_tasks():
    print(task.get_details())

manager.count_completed()

print("Pending tasks:")
for task in manager.filter_tasks(False):
    print(task.get_details())

print("Completed tasks:")
for task in manager.filter_tasks(True):
    print(task.get_details())

print("High Priority Tasks")
for task in manager.filter_by_priority("High"):
    print(task.get_details())

print("Medium Priority Tasks")
for task in manager.filter_by_priority("Medium"):
    print(task.get_details())

print("Low Priority Tasks")
for task in manager.filter_by_priority("Low"):
    print(task.get_details())