#This program takes a file and capitializes every letter.

fname = input("Enter a file name: ")
try:
  fhand = open(fname)
except:
  print("Invalid file name:",fname)
  exit()
for line in fhand:
  line = line.upper()
  print(line)
