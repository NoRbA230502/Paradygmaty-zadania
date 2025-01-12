from functools import lru_cache


class Item:
    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"Item(id={self.id}, weight={self.weight}, value={self.value})"


def knapsack_procedural(items, capacity):

    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]


    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if items[i - 1].weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1].weight] + items[i - 1].value)
            else:
                dp[i][w] = dp[i - 1][w]


    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1].weight

    return dp[n][capacity], selected_items


@lru_cache(maxsize=None)
def knapsack_functional(index, capacity, items):

    if index == 0 or capacity == 0:
        return 0, []


    if items[index - 1].weight > capacity:
        return knapsack_functional(index - 1, capacity, items)


    value_without, items_without = knapsack_functional(index - 1, capacity, items)
    value_with, items_with = knapsack_functional(index - 1, capacity - items[index - 1].weight, items)
    value_with += items[index - 1].value


    if value_with > value_without:
        return value_with, items_with + [items[index - 1]]
    else:
        return value_without, items_without


if __name__ == "__main__":
    items = [
        Item(1, 2, 3),
        Item(2, 3, 4),
        Item(3, 4, 5),
        Item(4, 5, 6)
    ]
    capacity = 5


    procedural_result, procedural_items = knapsack_procedural(items, capacity)
    print("Proceduralne podejście:")
    print("Maksymalna wartość:", procedural_result)
    print("Wybrane przedmioty:", procedural_items)


    functional_result, functional_items = knapsack_functional(len(items), capacity, tuple(items))
    print("Funkcyjne podejście:")
    print("Maksymalna wartość:", functional_result)
    print("Wybrane przedmioty:", functional_items)
