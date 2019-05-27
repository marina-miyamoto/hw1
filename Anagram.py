import requests
from bs4 import BeautifulSoup

characters = input("Type in the words: ")
characters = characters.replace(' ', '')
#characters = characters.split()
sorted_input = sorted(characters)
print("The letters entered were: " + str(sorted_input))

response = requests.get("https://icanhazwordz.appspot.com/dictionary.words")
bs = BeautifulSoup(response.content, "lxml")
dictionary = bs.select('p')[0].text
b = dictionary.lower().split('\n')

dictionary_words = []
anagram_words = []
for i in b:
    d = sorted(i)
    dictionary_words.append(d)

#a is the words that was typed in
#d is the each characters that are in the dictionary 
for x in range(len(dictionary_words)):
        sorted_input = sorted(characters)
        for y in range(len(dictionary_words[x])):
                if dictionary_words[x][y] in sorted_input:
                        #removing a letter to avoid words with same two letters
                        sorted_input.remove(dictionary_words[x][y])
                        flag = True
                        
                else:
                        flag = False
                        break
                
        if flag == True:
                anagram_words.append(b[x])
                

for z in range(len(anagram_words)):
        M = max(anagram_words, key = len)
print(M)


