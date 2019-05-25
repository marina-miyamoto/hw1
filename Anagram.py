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

new_list = []
for i in range(len(b)):
    d = sorted(b[i])
    
    if a == d:
        new_list.append(b[i])


for h in range(len(new_list)):
    print(new_list[h])