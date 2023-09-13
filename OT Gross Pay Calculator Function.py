#This is yet another OT gross pay calculator. 
#This time let's use a function.

def computepay(hours, rate):
  if hours > 40:
    pay = (40 * rate) + (1.5 * rate * (hours-40))
    return pay
  else:
    pay = hours * rate
    return pay

try:
  h = float(input("Enter Hours: "))
  r = float(input("Enter Rate: "))
  p = computepay(h, r)
  print("Pay:", p)
except:
  print("Please enter a numeric input.")
