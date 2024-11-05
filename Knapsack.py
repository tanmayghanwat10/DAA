def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    ratio = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]

    ratio.sort(reverse=True)

    total_value = 0
    knapsack = [0] * n

    for i in range(n):
        if ratio[i][1] <= capacity:
            knapsack[i] = 1
            total_value += ratio[i][2]
            capacity -= ratio[i][1]
        else:
            knapsack[i] = capacity / ratio[i][1]
            total_value += knapsack[i] * ratio[i][2]
            break

    return total_value, knapsack

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

result, selected_items = fractional_knapsack(weights, values, capacity)
print(f"Maximum value in Knapsack: {result}")
print("Selected items (fraction):", selected_items)
