import random
from tabulate import tabulate

def roll_dice():
    return random.randint(1, 6)

def monte_carlo_simulation(num_simulations):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_simulations):
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        results[total] += 1

    probabilities = {key: value / num_simulations for key, value in results.items()}
    return probabilities

def analytical_calculation():
    probabilities = {}
    for i in range(2, 13):
        if i <= 7:
            probabilities[i] = (i - 1) / 36
        else:
            probabilities[i] = (13 - i) / 36
    return probabilities

def main():
    num_simulations_list = [1000, 10000, 100000]
    all_probabilities = []

    for num_simulations in num_simulations_list:
        probabilities = monte_carlo_simulation(num_simulations)
        all_probabilities.append(probabilities)

    analytical_probs = analytical_calculation()

    headers = ["Sum", "Analytical", "1000 Simulations", "10000 Simulations", "100000 Simulations"]
    table_data = []

    for sum_value in range(2, 13):
        row = [sum_value]
        row.append(analytical_probs[sum_value])
        for probabilities in all_probabilities:
            row.append(probabilities.get(sum_value, 0))
        table_data.append(row)

    print(tabulate(table_data, headers=headers, floatfmt=".4f", tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()