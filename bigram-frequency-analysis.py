# imports
import sys

filename = sys.argv[1]
# read file
with open(filename, 'r') as f:
    text = f.read()

frequency = {}
for i in range(0, len(text), 2):
    try:
        bigram = text[i] + text[i+1]
        try:
            frequency[bigram] += 1
        except:
            frequency[bigram] = 1
    except:
        pass

print(dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True)))