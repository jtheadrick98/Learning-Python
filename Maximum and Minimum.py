#This program takes a user-created list of numbers.
#It will spit out the min and max values using loops.

smallest = None
largest = None
while True:
  try:
    n = input("Enter a number or done when finished: ")
    if n == "done": break
    n = float(n)
    if smallest is None or n < smallest:
      smallest = n
    elif: largest is None or n > largest:
      largest = n
  except:
    print("Invalid input.")
    continue
print(largest, smallest)
