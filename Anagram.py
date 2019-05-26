words = input("Type in the words: ")
words = words.replace(' ', '')
words.split()
a = sorted(words)
print(a)

import requests
from bs4 import BeautifulSoup

response = requests.get("https://icanhazwordz.appspot.com/dictionary.words")
bs = BeautifulSoup(response.content, "lxml")
dictionary = bs.select('p')[0].text
b = dictionary.lower().split('\n')

list = []
new_list = []
for i in range(len(b)):
    d = sorted(b[i])
    list.append(d)

#a is the words that was typed in
#d is the each words that are in the dictionary 
for x in range(len(list)):
        a = sorted(words)
        for y in range(len(list[x])):
                if list[x][y] in a:
                        a.remove(list[x][y])
                        flag = True
                        
                else:
                        flag = False
                        break
        if flag == True:
                new_list.append(b[x])

for z in range(len(new_list)):
        M = max(new_list, key = len)
print(M)
