import re

f = open('input.txt', 'r')
passes = f.readlines()

passed = 0
for password in passes:
    constraint = re.compile('\d+\-\d+').match(password)
    min = int(constraint.group().split('-')[0])
    max = int(constraint.group().split('-')[1])

    password = password[(constraint.end() + 1):]
    letter = password[0]
    password = password[3:]

    characterCount = 0

    for character in password:
        if character == letter:
            characterCount += 1

    if characterCount <= max and characterCount >= min:
        passed += 1

print(passed)
