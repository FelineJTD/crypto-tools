# imports
import sys

filename = sys.argv[1]

# read file
with open(filename, 'r') as f:
    text = f.read()

plaintext = ''

substitution = {}
substitution['HE'] = 'TH'
substitution['EH'] = 'HT'
substitution['HL'] = 'TE'
substitution['LH'] = 'ET'
substitution['HA'] = 'TL'
substitution['AH'] = 'LT'
substitution['HT'] = 'TA'
substitution['TH'] = 'AT'
substitution['HT'] = 'TA'
substitution['EL'] = 'HE'
substitution['LE'] = 'EH'
substitution['EA'] = 'HL'
substitution['AE'] = 'LH'
substitution['ET'] = 'HA'
substitution['TE'] = 'AH'
substitution['LA'] = 'EL'
substitution['AL'] = 'LE'
substitution['LT'] = 'EA'
substitution['TL'] = 'AE'
substitution['AT'] = 'LA'
substitution['TA'] = 'AL'
substitution['AV'] = 'T_'
substitution['VA'] = '_T'
substitution['AR'] = 'H_'
substitution['RA'] = '_H'
substitution['AM'] = 'E_'
substitution['MA'] = '_E'
substitution['QX'] = 'IN'
substitution['XQ'] = 'NI'
substitution['IN'] = 'QX'
substitution['MH'] = 'RE'
substitution['HM'] = 'ER'
substitution['ER'] = 'HM'
substitution['RE'] = 'MH'
substitution['HV'] = 'TR'
substitution['VH'] = 'RT'
substitution['TR'] = 'HV'
substitution['RT'] = 'VH'
substitution['EV'] = 'TM'
substitution['VE'] = 'MT'
substitution['TM'] = 'EV'
substitution['MT'] = 'VE'
substitution['LV'] = 'T_'
substitution['VL'] = '_T'
substitution['LM'] = 'E_'
substitution['ML'] = '_E'
substitution['KH'] = 'YW'
substitution['HK'] = 'WY'
substitution['LR'] = 'H_'
substitution['RL'] = '_H'
substitution['KN'] = '_W'
substitution['NK'] = 'W_'
substitution['VA'] = 'ST'
substitution['AV'] = 'TS'
substitution['BL'] = '_T'
substitution['LB'] = 'T_'
substitution['BE'] = '_T'
substitution['EB'] = 'T_'
# substitution['LD'] = 'AT'
# substitution['MH'] = 'NT'

more_subs = {}

# propagate substitutions
for key in substitution:
    # balikan
    more_subs[key[1] + key[0]] = substitution[key][1] + substitution[key][0]
    # square
    if (key[0] != key[1]) and (key[1] != substitution[key][0]) and (key[1] != substitution[key][1]) and (substitution[key][0] != substitution[key][1]) and (key[0] != substitution[key][0]) and (key[0] != substitution[key][1]) and (substitution[key][0] != '_') and (substitution[key][1] != '_'):
        more_subs[substitution[key][0] + substitution[key][1]] = key[0] + key[1]
        more_subs[substitution[key][1] + substitution[key][0]] = key[1] + key[0]


for i in range(0, len(text), 2):
    try:
        bigram = text[i] + text[i+1]
        try:
            plaintext += substitution[bigram]
        except:
            plaintext += '__'
            # try:
            #     plaintext += more_subs[bigram]
            # except:
            #     plaintext += '__'
    except:
        pass

print(plaintext)

linewidth = 100
with open('output/playfair-subs.txt', 'w') as f:
    for i in range (0, len(plaintext), linewidth):
        f.write(text[i:i+linewidth])
        f.write('\n')
        f.write(plaintext[i:i+linewidth])
        f.write('\n\n')