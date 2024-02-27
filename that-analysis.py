# imports
import sys

filename = sys.argv[1]
# read file
with open(filename, 'r') as f:
    text = f.read()

frequency = {}
freq_one = {}
for i in range(0, len(text)):
    if text[i] == 'H' and text[i+1] == 'E':
        try:
            bigram = text[i+2] + text[i+3]
            try:
                frequency[bigram] += 1
                freq_one[text[i+3]] += 1
            except:
                frequency[bigram] = 1
                freq_one[text[i+3]] = 1
        except:
            pass

print(dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True)))
# print(dict(sorted(freq_one.items(), key=lambda item: item[1], reverse=True)))