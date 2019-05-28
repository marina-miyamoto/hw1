import requests
from bs4 import BeautifulSoup

characters = input("Type in the words: ")
characters = characters.replace(' ', '')
sorted_input = sorted(characters)
print("The letters entered were: " + str(sorted_input))


with open("sample1.csv", "r") as f:
    dictionary = f.readlines()
b = dictionary[0].lower().split(',')


dictionary_words = []
anagram_words = []
for i in b:
    d = sorted(i)
    dictionary_words.append(d)


scores = []
two_points = ['c', 'f', 'h', 'l', 'm', 'p', 'v','w', 'y']
three_points = ['j', 'k', 'q', 'x', 'z']


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

for x in range(len(anagram_words)):
        score = 0
        for y in range(len(anagram_words[x])):
                if anagram_words[x][y] in two_points:
                        score += 2
                elif anagram_words[x][y] in three_points:
                        score += 3
                else: score += 1
        scores.append(score)
                                
                
longest_anagram = max(anagram_words, key = len)
anagram_index = anagram_words.index(longest_anagram)
highest_score = scores.index(max(scores))

if scores[anagram_index] >= scores[highest_score]:
        print('Highest Score: ' + str((scores[anagram_index]+1)**2))
        print(anagram_words[anagram_index])
else:
        print('Highest Score: ' + str((scores[highest_score]+1)**2))
        print(highest_score)