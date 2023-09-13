#This program calculates a grade.

score = float(input("Enter a grade between 0.0 and 1.0: "))
try:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
except:
    print("Bad score.")
