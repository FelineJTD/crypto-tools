# imports
import sys

filename = sys.argv[1]
key = sys.argv[2]

# read file
with open(filename, 'r') as f:
    text = f.read()

plaintext = ''

for i in range(len(text)):
    if key[i % len(key)] != '_':
        try:
            plaintext += chr(((ord(text[i]) - ord(key[i % len(key)])) % 26) + 65)
        except:
            pass
    else:
        plaintext += '_'

linewidth = 100
with open('output/vig-subs.txt', 'w') as f:
    for i in range (0, len(plaintext), linewidth):
        f.write(text[i:i+linewidth])
        f.write('\n')
        f.write(plaintext[i:i+linewidth])
        f.write('\n\n')