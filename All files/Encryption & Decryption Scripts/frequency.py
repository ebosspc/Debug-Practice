#   a212_frequency.py
#   Counts letters in a given string

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

phrase = input("Enter the string to analyze: ")
count_letters = char_frequency(phrase)

for keys, values in count_letters.items():
  print(keys, ":", values)
