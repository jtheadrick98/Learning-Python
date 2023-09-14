#This program takes a file and stores each word as a key in a dictionary.

worddict = dict()
fname = input("Enter a file name: ")
try:
  fhand = open(fname)
except:
  print("Invalid file name.")
  exit()

count = 0
for line in fhand:
  line.rstrip()
  words = line.split()
  for word in words:
    count = count + 1
    worddict[word] = count
print(worddict)
