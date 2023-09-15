#This program creates a "histogram" of the hours when emails are sent in a mbox file.

fname = input("Enter a mbox file name: ")
try:
  fhand = open(fname)
except:
  print("Invalid file name.")
  exit()

#Create dictionary of hours and the frequency of hours that emails were sent.
hourdict = dict()
for line in fhand:
  if not line.startswith("From "): continue
  words = line.split()
  time = words[5]
  colpos = time.find(":")
  hour = time[:colpos]
  hourdict[hour] = hourdict.get(hour, 0) + 1

#Creates list of tuples of hours and counts and sorts them.
hourlist = list(hourdict.items())
hourlist.sort()

for hour, count in hourlist:
    print(hour, count)
  
