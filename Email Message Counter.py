#This program counts how many messages come from each email address in a mbox file.

fname = input("Enter a mbox file: ")
emaildict = dict()
try:
  fhand = open(fname)
except:
  print("Invalid file name.")
  exit()
for line in fhand:
  line.rstrip()
  if not line.startswith("From "): continue
  words = line.split()
  email = words[1]
  emaildict[email] = emaildict.get(email, 0) + 1
print(emaildict)
