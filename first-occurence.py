# imports
import sys

filename = sys.argv[1]
search = sys.argv[2]

# read file
with open(filename, 'r') as f:
    text = f.read()

for i in range(0, len(text)):
    try:
        if (text[i] == sys.argv[2][0] and text[i+1] == sys.argv[2][1] and text[i+2] == sys.argv[2][2]):
            print('First occurence at index: ', i)
            print('Column: ', i%12)
            break
    except:
        pass