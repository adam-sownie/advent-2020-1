import re

f = open('input.txt', 'r')
passes = f.readlines()

passed = 0
for password in passes:
    constraint = re.compile('\d+\-\d+').match(password)
    first = int(constraint.group().split('-')[0])
    second = int(constraint.group().split('-')[1])

    password = password[(constraint.end() + 1):]
    letter = password[0]
    password = password[3:]

    if password[first-1] == letter:
        passed += 1
        if password[second-1] == letter:
            passed -= 1

    if password[second-1] == letter:
        passed += 1
        if password[first-1] == letter:
            passed -= 1

print(passed)
