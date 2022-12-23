caloriesPerElve = []

with open('input.txt', encoding='utf-8') as f:
    
    calories = 0

    for line in f:
        if line == '\n':
            caloriesPerElve.append(calories)
            calories = 0
        else:
            calories += int(line)

caloriesPerElve.sort()


print("Part 1: ")
print(caloriesPerElve[-1])


topThreeCalorieElves = caloriesPerElve[-1] + caloriesPerElve[-2] + caloriesPerElve[-3]

print("Part 2: ")
print(topThreeCalorieElves)