class Task:
    def __init__(self, name, arrival_time, completion_time, deadline, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.completion_time = completion_time
        self.deadline = deadline
        self.priority = priority

class List_Of_Tasks():
    def __init__(self, task):
        self.task = task

    def order_by_priority(self, task):
        n = len(task)
        if n <= 1:
            return task
        m = n // 2
        left = task[0:m]
        right = task[m:n]

        left = self.order_by_priority(left)
        right = self.order_by_priority(right)
        return self.sort(left, right)

    @staticmethod
    def sort(left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i].priority < right[j].priority:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

def compare_deadline_and_finish_time(deadline, finishtime):
    if finishtime > deadline:
        print("we failed a task")
        return 1
        
    else:
        print("We succedded")
        return 0

def leifes_extremely_complex_pruning_algorithm(ordered_tasks, current_time):
    current_time = 0
#pruning algorithm 
    for current_task in ordered_tasks:
        task_name = current_task.name
        arrival_time = current_task.arrival_time
        completion_time = current_task.completion_time
        if current_time < arrival_time:
            current_time = completion_time + current_time + arrival_time 
        else:
            current_time = completion_time + current_time
        deadline = current_task.deadline
        completion_time = current_task.completion_time
        print("current task is", current_task.name)
        value = compare_deadline_and_finish_time(deadline, current_time)
        if value != 0:
            print("My loop is broken")
            print("Deadline is ", deadline, "Finish time is :", current_time)
            break

task = [Task("task1", 4, 2, 7, 1),    
        Task("task2", 1, 1, 5, 2),    
        Task("task3", 1, 2, 6, 3),    
        Task("task4", 0, 2, 6, 4),    
       ]

my_task_list = List_Of_Tasks(task)
ordered_tasks = my_task_list.order_by_priority(my_task_list.task)

#pruning algorithm 
print("leifes_extremely_complex_pruning_algorithm")
current_time = 0
leifes_extremely_complex_pruning_algorithm(ordered_tasks, current_time)

