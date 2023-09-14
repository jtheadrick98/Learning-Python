#this program takes a number from a string and converts it to float

str = "X-DSPAM-Confidence:0.8475"

colpos = str.find(":")
number = float(str[colpos+1:])
print(number)
