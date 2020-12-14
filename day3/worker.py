import re

def treeFind (r, d):
    f = open('input.txt', 'r')
    lines = f.readlines()

    x = 0;
    trees = 0
    y  = 0;

    for line in lines:
        if (y % d) == 0:
            print(str(y) + ' ' + str(d) + ' ' + str(y%d))
            if line[x] == '#':
                trees += 1

        length = len(line) - 1

        x += r
        x = x % length
        y += 1


    return trees

if __name__ == "__main__":
    print(treeFind(1, 1) * treeFind(3, 1) * treeFind(5, 1)
        * treeFind(7, 1) * treeFind(1, 2))
