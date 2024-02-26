# imports
import sys

filename = sys.argv[1]

# read file
with open(filename, 'r') as f:
    text = f.read()

plaintext = ''

substitution = {}
# THELW
substitution['HE'] = 'TH'
substitution['EH'] = 'HT'
substitution['EL'] = 'HE'
substitution['LE'] = 'EH'
substitution['HL'] = 'TE'
substitution['LH'] = 'ET'
substitution['WL'] = 'LE'
substitution['LW'] = 'EL'
substitution['WE'] = 'LH'
substitution['EW'] = 'HL'
substitution['WH'] = 'LT'
substitution['HW'] = 'TL'
substitution['WT'] = 'LW'
substitution['TW'] = 'WL'
substitution['QX'] = 'IN'
substitution['MH'] = 'RE'
substitution['HM'] = 'ER'
substitution['TM'] = 'EV'
substitution['MT'] = 'VE'
substitution['KH'] = 'YW'
substitution['HK'] = 'WY'
substitution['LR'] = 'H_'
substitution['RL'] = '_H'
# substitution['LD'] = 'AT'
# substitution['MH'] = 'NT'

for i in range(0, len(text), 2):
    try:
        bigram = text[i] + text[i+1]
        try:
            plaintext += substitution[bigram]
        except:
            plaintext += '__'
    except:
        pass

linewidth = 100
with open('output/playfair-subs.txt', 'w') as f:
    for i in range (0, len(plaintext), linewidth):
        f.write(text[i:i+linewidth])
        f.write('\n')
        f.write(plaintext[i:i+linewidth])
        f.write('\n\n')