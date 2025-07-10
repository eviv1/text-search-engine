import re

#Check if the string contains what's in the text:

search_query = input()

txt = "The quick brown fox jumps over the lazy dog"
x = re.search(search_query, txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")