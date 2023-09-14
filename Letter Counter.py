#This program counts how many times a letter appears in a word.

w = input("Enter a word: ")
l = input("Enter a letter: ")
def count(word, letter):
  c = 0
  for letter in word:
    if l == letter:
      c = c + 1
  print(c)

count(w, l)
