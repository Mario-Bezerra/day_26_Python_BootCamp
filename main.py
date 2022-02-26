import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}
message = str(input("Type the message : ")).upper()
nato_message = [nato_dict[letter] for letter in message]
print(nato_message)


