class Item:
    def __init__(self, weight, value, index):
        self.weight = weight
        self.value = value
        self.index = index
        self.ratio = value / weight

def knapsack_branch_and_bound(weights, values, capacity):
    n = len(weights)
    items = [Item(weights[i], values[i], i) for i in range(n)]
    items.sort(key=lambda x: x.ratio, reverse=True)

    max_value = 0
    selected_items = [0] * n

    def bound(i, weight, value):
        while i < n and weight + items[i].weight <= capacity:
            weight += items[i].weight
            value += items[i].value
            i += 1

        if i < n:
            value += (capacity - weight) * items[i].ratio

        return value

    def knapsack_recursive(i, weight, value):
        nonlocal max_value
        if weight <= capacity and value > max_value:
            max_value = value
            selected_items.clear()
            selected_items.extend([0] * n)
            for j in range(i):
                selected_items[items[j].index] = 1

        if i < n and bound(i, weight, value) > max_value:
            knapsack_recursive(i + 1, weight + items[i].weight, value + items[i].value)
            knapsack_recursive(i + 1, weight, value)

    knapsack_recursive(0, 0, 0)

    return max_value, selected_items

# Taking user input
n = int(input("Enter the number of items: "))
weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter the weight of item {i+1}: "))
    value = int(input(f"Enter the value of item {i+1}: "))
    weights.append(weight)
    values.append(value)

capacity = int(input("Enter the capacity of the knapsack: "))

result, selected_items = knapsack_branch_and_bound(weights, values, capacity)
print(f"Maximum value in 0-1 Knapsack using Branch and Bound: {result}")
print("Selected items:", selected_items)
