class Task :
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.complete = False
class TaskManager:
    def __init__(self) :
        self.tasks = []
    
    def add_task(self, name, deadline):
        task = Task(name, deadline)
        self.tasks.append(task)
    def mark_as_complete(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.complete = True
    def display_task(self):
        if not self.tasks :
            print("tidak ada tugas")
        else:
            for task in self.tasks :
                status = 'selesai' if task.complete else 'belum selesai'
                print(f"{task.name} - Deadline : {task.deadline} - status : {status}")
#contoh penggunaan aplikasi tak manager
task_manager = TaskManager()
task_manager.add_task("menyelesaikan project python", "10 November 2023")
task_manager.add_task("mengikuti pertemuan tim", "5 November 2023")
task_manager.mark_as_complete("menyelesaikan project python")
task_manager.display_task()