import pandas

alpha = pandas.read_csv("nato_phonetic_alphabet.csv")
nalpha = pandas.DataFrame(alpha)

for (index, row) in nalpha.iterrows():
  new_dict = {row['letter']:row["code"] for (index,row) in nalpha.iterrows()}

print(new_dict['A'])

name = input("Name: ").upper()
name_letters = list(name)
alpha_list = [new_dict[letter] for letter in name_letters]
print(alpha_list)



