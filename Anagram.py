characters = input("Type in the words: ")
characters = characters.replace(' ', '')

with open("sample1.csv", "r") as f:
    dictionary = f.readlines()
b = dictionary[0].lower().split(',')

'''
with open("dictionary.words", "r") as f:
        dictionary = [w.lower().strip("\n") for w in f.readlines()]
'''

dictionary_words = []
anagram_words = []
for i in b:
    d = sorted(i)
    dictionary_words.append(d)


scores = []
two_points = ['c', 'f', 'h', 'l', 'm', 'p', 'v','w', 'y']
three_points = ['j', 'k', 'q', 'x', 'z']


for word in dictionary_words:
        sorted_input = sorted(characters)
        for char in word:
                if char in sorted_input:
                        #removing a letter to avoid words with same two letters
                        sorted_input.remove(char)
                        flag = True
                
                else:
                        flag = False
                        break
                
        if flag == True:
                i = dictionary_words.index(word)
                anagram_words.append(b[i])


scored_anagram = []
for anagram_word in anagram_words:
        score = 0
        for x in anagram_word:
                if x in two_points:
                        score += 2
                elif x in three_points:
                        score+= 3
                else:
                        score += 1
        scored_anagram.append((anagram_word, score))

highest_score = max(scored_anagram, key = lambda v: v[1])[0]
print("Highest Scoring Anagram: " + highest_score)
                
