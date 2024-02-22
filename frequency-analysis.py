# imports
import sys

filename = sys.argv[1]
# read file
with open(filename, 'r') as f:
    text = f.read()

# init frequency counter
frequency = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
}

# loop through text and count occurences
for char in text:
    frequency[char.upper()] += 1

# sort from largest
frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

print('Frequency analysis results: ')
print(frequency)

# substitute
english_letter_frequency = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']

substitution = {}
i = 0
# for key in frequency:
#     substitution[key] = english_letter_frequency[i]
#     i += 1
#     if i >= 5:
#         break

substitution['E'] = 'E'
substitution['H'] = 'T'
substitution['Z'] = 'H'
substitution['Y'] = 'A'
substitution['F'] = 'N'
substitution['C'] = 'D'
substitution['N'] = 'V'
substitution['U'] = 'U'
substitution['W'] = 'L'
substitution['M'] = 'Y'
substitution['A'] = 'S'
substitution['O'] = 'G'
substitution['B'] = 'R'
substitution['X'] = 'C'
substitution['V'] = 'P'
substitution['R'] = 'O'
substitution['L'] = 'I'
substitution['G'] = 'F'
substitution['P'] = 'M'
substitution['T'] = 'W'
substitution['D'] = 'X'
substitution['K'] = 'B'
substitution['Q'] = 'Q'
substitution['I'] = 'K'
substitution['S'] = 'Z'
substitution['J'] = 'J'

plaintext = ''
for char in text:
    try:
        plaintext += substitution[char]
    except:
        plaintext += '_'

print('Plaintext: ')
print(plaintext)

linewidth = 100
with open('output/result.txt', 'w') as f:
    f.write(plaintext)