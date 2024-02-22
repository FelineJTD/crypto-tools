# imports
import sys
import math

filename = sys.argv[1]
search = sys.argv[2]
# read file
with open(filename, 'r') as f:
    text = f.read()

frequency = {}
cur = 0
arr_of_steps = []
for i in range(0, len(text)):
    try:
        if (text[i] == sys.argv[2][0] and text[i+1] == sys.argv[2][1] and text[i+2] == sys.argv[2][2]):
            if cur != 0:
                arr_of_steps.append(i-cur)
            cur = i
    except:
        pass

print('Array of steps: ')
print(arr_of_steps)

print('Possible array of steps (by GCD): ')
print(math.gcd(*arr_of_steps))