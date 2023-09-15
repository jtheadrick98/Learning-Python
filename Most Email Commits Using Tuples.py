#This program also tells the user who has the most sent emails in a mbox file.
#However, this time we will use tuples to do so.

fname = input("Enter a mbox file: ")
try:
  fhand = open(fname)
except:
  print("Please enter a valid mbox file.")
  exit()

#Create dictionary of email address and counts.
emaildict = dict()
for line in fhand:
  if not line.startswith("From "): continue
  words = line.split()
  email = words[1]
  emaildict[email] = emaildict.get(email, 0) + 1

#Create list of tuples to sort by count not email.
emaillist = list()
for email, count in list(emaildict.items()):
  emaillist.append((count, email))

emaillist.sort(reverse = True)

#Prints out email address with most commits.
for count, email in emaillist[0:1]:
    print(email, count)
