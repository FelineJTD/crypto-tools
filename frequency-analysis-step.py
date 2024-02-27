# imports
import sys

filename = sys.argv[1]
step = int(sys.argv[2])
# read file
with open(filename, 'r') as f:
    text = f.read()

# init frequency counter
frequency = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
}

# loop through text and count occurences
for i in range(0, len(text), step):
    frequency[text[i].upper()] += 1

# sort from largest
frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

print('Frequency analysis results: ')
print(frequency)