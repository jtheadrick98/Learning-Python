#This program searches through a file to see how many lines have a desired substring.
#This program allows a user to input a desired regular expression.

import re
name = input("Enter a file name: ")
try:
    hand = open(name)
except:
    print("Invalid file name.")
    exit()
regex = input("Enter a regular expression: ")
count = 0
for line in hand:
    line = line.rstrip()
    x = re.findall(regex, line)
    if len(x) > 0:
        count = count + 1
print(name, "had", count, "lines that matched", regex)
