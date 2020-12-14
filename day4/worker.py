import re

f = open('input.txt', 'r')
lines = f.readlines()

valid = 0
fullLine = ''
for line in lines:
    if line != '\n':
        fullLine += line
    else:
        if (fullLine.find('byr:') != -1 and
            fullLine.find('iyr:') != -1 and
            fullLine.find('eyr:') != -1 and
            fullLine.find('hgt:') != -1 and
            fullLine.find('hcl:') != -1 and
            fullLine.find('ecl:') != -1 and
            fullLine.find('pid:') != -1):
            valid += 1
        fullLine = ''
print(valid)
