#This program reads a file.
#It takes that file and creates a letter counter in decreasing order of frequency.

import string
fname = input("Enter a file: ")
try:
  fhand = open(fname)
except:
  print("Invalid file name.")
  exit()

#Create a dictionary of letters and respective counts.
letterdict = dict()
for line in fhand:
  line.rstrip()
  #deletes puncutation
  line = line.translate(str.maketrans("","", string.punctuation)) 
  #deletes numbers
  line = line.translate(str.maketrans("","","0123456789"))
  line = line.lower()
  words = line.split()
  for word in words:
    letters = list(word)
    for letter in letters:
      letterdict[letter] = letterdict.get(letter, 0) + 1

#Creates letter list to put counts as the "key" in the tuples.
letterlist = list()
for letter, count in list(letterdict.items()):
  letterlist.append((count, letter))

#Allows us to sort letter list by count in descending order.
letterlist.sort(reverse = True)
for count, letter in letterlist:
  print(letter, count)
