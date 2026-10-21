import pandas

data = pandas.read_csv("4-nato-alphabet/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

result = [nato_dict[letter] for letter in word]
print(result)