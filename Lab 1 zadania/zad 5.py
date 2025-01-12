from functools import lru_cache, reduce

class Task:
    def __init__(self, id, start, end, reward):
        self.id = id
        self.start = start
        self.end = end
        self.reward = reward

    def __repr__(self):
        return f"Task(id={self.id}, start={self.start}, end={self.end}, reward={self.reward})"


def schedule_tasks_procedural(tasks):
    tasks.sort(key=lambda task: task.end)
    selected_tasks = []
    last_end_time = 0
    total_reward = 0

    for task in tasks:
        if task.start >= last_end_time:
            selected_tasks.append(task)
            last_end_time = task.end
            total_reward += task.reward
    return total_reward, selected_tasks


def schedule_tasks_functional(tasks):

    sorted_tasks = sorted(tasks, key=lambda task: task.end)
    def reducer(acc, task):
        last_end_time, selected, total_reward = acc
        if task.start >= last_end_time:
            return task.end, selected + [task], total_reward + task.reward
        return last_end_time, selected, total_reward
    _, selected_tasks, total_reward = reduce(reducer, sorted_tasks, (0, [], 0))
    return total_reward, selected_tasks


if __name__ == "__main__":
    tasks = [
        Task(1, 1, 3, 50),
        Task(2, 2, 5, 20),
        Task(3, 4, 6, 70),
        Task(4, 6, 7, 60),
        Task(5, 5, 8, 30)
    ]


    procedural_reward, procedural_schedule = schedule_tasks_procedural(tasks.copy())
    print("Proceduralne podejście:")
    print("Maksymalna nagroda:", procedural_reward)
    print("Wybrane zadania:", procedural_schedule)


    functional_reward, functional_schedule = schedule_tasks_functional(tasks.copy())
    print("Funkcyjne podejście:")
    print("Maksymalna nagroda:", functional_reward)
    print("Wybrane zadania:", functional_schedule)
