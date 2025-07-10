import re

#Check if the string contains what's in the text:

query = input()

txt = open(r"C:\Users\IT\Documents\Codes\text.txt", "r")
x = re.search(query, txt.read())

if x:
  print("YES! We have a match!")
else:
  print("No match")