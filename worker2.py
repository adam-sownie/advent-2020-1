f = open('input.txt', 'r')
costs = f.readlines()

for cost in costs:
    for s_cost in costs:
        for t_cost in costs:
            if (int(cost) + int(s_cost) + int(t_cost)) == 2020:
                print(int(cost) * int(s_cost) * int(t_cost))
                exit()
