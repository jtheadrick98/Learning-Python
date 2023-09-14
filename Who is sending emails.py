#This program takes a mbox file and prints the addresses sending emails.
#As well, it counts how many lines in the file that start with "From ".

fname = input("Enter a mbox file name: ")
try:
  fhand = open(fname)
except:
  print("Invalid file name.")
  quit()

count = 0
for line in fhand:
  line.rstrip()
  if line.notstartswith("From "): continue
  count = count + 1
  words = line.split()
  email = words[1]
  print(email)
print("There were", count, "lines in the file with From as the first word.")
