f = open('input.txt', 'r')
costs = f.readlines()

for cost in costs:
    for s_cost in costs:
        if (int(cost) + int(s_cost)) == 2020:
            print(int(cost) * int(s_cost))
            exit()
