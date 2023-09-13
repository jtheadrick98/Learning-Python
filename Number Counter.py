#This program takes a running list of numbers.
#It displays the final total, count, and average.

count = 0
total = 0
while True:
  try:
    n = input("Enter a number or type done when finished: ")
    if n == "done": break
    fn = float(n)
    count = count + 1
    total = total + fn
  except:
    print("Invalid input.")
    continue
average = total/count
print(total, count, average)
