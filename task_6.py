def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item_name, item_info in sorted_items:
        if total_cost + item_info['cost'] <= budget:
            total_cost += item_info['cost']
            total_calories += item_info['calories']
            chosen_items.append(item_name)

    return chosen_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i, (_, item_info) in enumerate(items.items(), 1):
        for j in range(1, budget + 1):
            if item_info['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_info['cost']] + item_info['calories'])
            else:
                dp[i][j] = dp[i - 1][j]

    # Reconstruction of chosen items
    chosen_items = []
    i = n
    j = budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            chosen_items.append(list(items.keys())[i - 1])
            j -= items[chosen_items[-1]]['cost']
        i -= 1

    return chosen_items, dp[n][budget]

# Given items
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Greedy Algorithm
chosen_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Chosen items:", chosen_items_greedy)
print("Total cost:", total_cost_greedy)
print("Total calories:", total_calories_greedy)

# Dynamic Programming Algorithm
chosen_items_dp, total_calories_dp = dynamic_programming(items, budget)
total_cost_dp = sum(items[item]['cost'] for item in chosen_items_dp)
print("\nDynamic Programming:")
print("Chosen items:", chosen_items_dp)
print("Total cost:", total_cost_dp)
print("Total calories:", total_calories_dp)