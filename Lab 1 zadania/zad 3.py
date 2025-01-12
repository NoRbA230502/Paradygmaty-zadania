from functools import reduce


class Task:
    def __init__(self, id, time, reward):
        self.id = id
        self.time = time
        self.reward = reward

    def __repr__(self):
        return f"Task(id={self.id}, time={self.time}, reward={self.reward})"


def optimize_tasks_procedural(tasks):

    for i in range(len(tasks)):
        for j in range(len(tasks) - i - 1):
            if (tasks[j].time > tasks[j + 1].time or
                (tasks[j].time == tasks[j + 1].time and tasks[j].reward < tasks[j + 1].reward)):
                tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]

    total_waiting_time = 0
    waiting_time = 0
    for task in tasks:
        total_waiting_time += waiting_time
        waiting_time += task.time

    return tasks, total_waiting_time


def optimize_tasks_functional(tasks):

    sorted_tasks = sorted(tasks, key=lambda task: (task.time, -task.reward))
    total_waiting_time = reduce(lambda acc, task: (acc[0] + acc[1], acc[1] + task.time), sorted_tasks, (0, 0))[0]
    return sorted_tasks, total_waiting_time


if __name__ == "__main__":
    tasks = [
        Task(1, 3, 50),
        Task(2, 1, 60),
        Task(3, 2, 20),
        Task(4, 2, 70)
    ]


    procedural_result, procedural_time = optimize_tasks_procedural(tasks.copy())
    print("Proceduralne podejście:")
    print("Optymalna kolejność zadań:", procedural_result)
    print("Całkowity czas oczekiwania:", procedural_time)

    functional_result, functional_time = optimize_tasks_functional(tasks.copy())
    print("Funkcyjne podejście:")
    print("Optymalna kolejność zadań:", functional_result)
    print("Całkowity czas oczekiwania:", functional_time)
