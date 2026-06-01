#Nato Alphabet Game

import pandas

file = './Day26/nato_phonetic_alphabet.csv'
data = pandas.read_csv(file)

nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}

word = input("Enter a word: ").upper()
output = [nato_dict[letter] for letter in word]
print(output)
