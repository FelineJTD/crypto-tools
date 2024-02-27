# imports
import sys

filename = sys.argv[1]
# read file
with open(filename, 'r') as f:
    text = f.read()

frequency = {}
for i in range(0, len(text)):
    try:
        trigram = text[i] + text[i+1] + text[i+2]
        try:
            frequency[trigram] += 1
        except:
            frequency[trigram] = 1
    except:
        pass

print(dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True)))