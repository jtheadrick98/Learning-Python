#This program takes a mbox file and creates a dictionary.
#The dictionary contains all domains found in senders' email addresses.

domaindict = dict()
fname = input("Enter a mbox file name: ")
try:
  fhand = open(fname)
except:
  print("Invalid mbox file name.")
  exit()

for line in fhand:
  if not line.startswith("From "): continue
  words = line.split()
  email = words[1]
  atpos = email.find("@")
  domain = email[atpos+1:]
  domaindict[domain] = domaindict.get(domain, 0) + 1
print(domaindict)
