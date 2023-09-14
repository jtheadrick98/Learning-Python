#This program takes a user's word and prints out the letters backwards one by one.


word = input("Enter a word: ")
index = len(word)
while index > 0:
  letter = word[index-1]
  index = index -1
  print(letter)
  
