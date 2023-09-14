#This program finds all unique words in a file.
#It then sorts it to be in alphabetical order.

fname = input("Enter a file name: ")
try:
  fhand = open(fname)
except:
  print("Invalid file name.")
  exit()
wordlist = list()
for line in fhand:
  line.rstrip()
  words = line.split()
  for word in words:
    word = word.lower()
    if word in wordlist: continue
    wordlist.append(word)
wordlist.sort()
print(wordlist)
