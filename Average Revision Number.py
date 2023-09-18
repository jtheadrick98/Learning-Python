#This program takes a mbox file to compute an average new revision number.
#It uses regex to look for lines of the form: "New Revision: 39772"

import re
name = input("Enter a file name: ")
try:
    hand = open(name)
except:
    print("Invalid file name.")
    exit()
count = 0
total = 0
for line in hand:
    line = line.rstrip()
    num = re.findall("^New Revision: ([0-9]+)", line)
    if len(num) > 0:
        count = count + 1
        total = total + int(num[0])
avg = total/count
print(int(avg))
