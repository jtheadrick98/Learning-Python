#This program takes user input of numbers and puts them in a list.
#Then, it tells the user the max and min numbers of the list.

numlist = list()
while True:
  try:
    x = input("Enter a number or done when finished: ")
    if x == "done": break
    x = float(x)
    numlist.append(x)
  except:
    print("Invalid input. Enter a number.")
    continue
print("Maximum:", max(numlist))
print("Minimum:", min(numlist))
