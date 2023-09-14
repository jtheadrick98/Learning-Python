#This program shows the email address that sends the most emails in a mbox file.

emaildict = dict()
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
  emaildict[email] = emaildict.get(email, 0) + 1
largest = None
for address in emaildict:
  count = emaildict.get(address, 0)
  if largest is None or count > largest:
    largest = count
    mostemails = address
print(mostemails, largest)
