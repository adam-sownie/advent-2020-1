import re

f = open('input.txt', 'r')
lines = f.readlines()

def getNumber (r):
    return int(r[1:])

if __name__ == "__main__":
    dir = 'E'
    N = 0
    S = 0
    E = 0
    W = 0
    for line in lines:
        if line[0] == 'N':
            amt = getNumber(line)
            N += amt
        if line[0] == 'S':
            amt = getNumber(line)
            S += amt
        if line[0] == 'E':
            amt = getNumber(line)
            E += amt
        if line[0] == 'W':
            amt = getNumber(line)
            W += amt
        if line[0] == 'L':
            amt = getNumber(line)
            while amt != 0:
                amt -= 90
                if dir == 'N':
                    dir = 'W'
                elif dir == 'W':
                    dir = 'S'
                elif dir == 'S':
                    dir = 'E'
                elif dir == 'E':
                    dir = 'N'
        if line[0] == 'R':
            amt = getNumber(line)
            while amt != 0:
                amt -= 90
                if dir == 'N':
                    dir = 'E'
                elif dir == 'E':
                    dir = 'S'
                elif dir == 'S':
                    dir = 'W'
                elif dir == 'W':
                    dir = 'N'
        if line[0] == 'F':
            amt = getNumber(line)
            if dir == 'N':
                N += amt
            if dir == 'S':
                S += amt
            if dir == 'E':
                E += amt
            if dir == 'W':
                W += amt

    print('W:' + str(W) + ' N:' + str(N) + ' S:' + str(S) + ' E:' + str(E))
    if W > E:
        W = W - E
    else:
        W = E - W
    if N > S:
        N = N - S
    else:
        N = S - N

    print(N + W)
