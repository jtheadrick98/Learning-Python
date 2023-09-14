#This program takes a mbox file and creates a counter.
#The counter shows the frequency of messages sent on days of the week.

daydict = dict()
fname = input("Enter a mbox file: ")
try:
  fhand = open(fname)
except:
  print("File does not exist.")
  exit()

for line in fhand:
  line.rstrip()
  if not line.startswith("From "): continue
  words = line.split()
  day = words[2]
  daydict[day] = daydict.get(day, 0) + 1
print(daydict)
