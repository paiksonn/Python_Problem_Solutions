## Задание 4

### Описание

Реализовать менеджер задач.
Покрыть тестами TaskManager класс. Например, что подзадачи, ведет к тому, что и из соответствующей ComplexTask удаляется эта подзадача. 


<details><summary>Исходный код</summary><blockquote>

````
class Task:
    def __init__(self, id, name, description, ):
        self.__id = id
        self.__name = name
        self.__description = description
        
    def get_id(self):
        return self.__id
        
    def get_name(self):
        return self.__name
class Subtask(Task):
    # have comlex task id
    def __init__(self):
        self.parent_id = 
    
class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self):
        self.subtasks = []  
  
class TaskManager:
    
    id_series = 0
    
    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
    
    
    def __get_and_increment_id(self):
        next_id_value = TaskManager.id_series
        TaskManager.id_series += 1 
        return next_id_value
        
    
    def create_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_task = Task(current_id, name, description)
        self.tasks[current_id] = new_task
        return new_task
    
    
    def create_subtask(self, subtask):
        pass
    
    def create_complex_task(self, complex_task):
        pass
    
    def get_tasks(self):
        pass
    
    def get_subtasks(self):
        pass
    
    def get_complex_tasks(self):
        pass
    
    def get_tasks_by_id(self, id):
        pass
    
    def get_subtasks_by_id(self, id):
        pass
    
    def get_complex_tasks_by_id(self, id):
        pass
    
    def remove_tasks(self):
        pass
    
    def remove_subtasks(self):
        pass
    
    def remove_complex_tasks(self):
        pass
    
    def remove_task_by_id(self, id):
        pass
    
    def remove_subtask_by_id(self, id):
        pass
    
    def remove_complex_task_by_id(self, id):
        pass
    
    def update_status(self, task):
        pass
````

</blockquote></details>

