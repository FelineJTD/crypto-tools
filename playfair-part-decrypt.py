# imports
import sys

filename = sys.argv[1]

# read file
with open(filename, 'r') as f:
    text = f.read()

plaintext = ''

substitution = {}
substitution['OE'] = 'D_'
substitution['EO'] = '_D'
substitution['KE'] = 'D_'
substitution['EK'] = '_D'
substitution['AR'] = 'H_'
substitution['RA'] = '_H'
substitution['AM'] = 'E_'
substitution['MA'] = '_E'
substitution['LV'] = 'T_'
substitution['VL'] = '_T'
substitution['LM'] = 'E_'
substitution['ML'] = '_E'
substitution['LR'] = 'H_'
substitution['RL'] = '_H'
substitution['KN'] = '_W'
substitution['NK'] = 'W_'
substitution['BL'] = '_T'
substitution['LB'] = 'T_'
substitution['BE'] = '_T'
substitution['EB'] = 'T_'
substitution['SL'] = '_A'
substitution['LS'] = 'A_'

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
substitution['QX'] = 'IN'
substitution['XQ'] = 'NI'
substitution['IN'] = 'QX'
substitution['NI'] = 'XQ'
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

substitution['KH'] = 'YW'
substitution['HK'] = 'WY'

substitution['VA'] = 'ST'
substitution['AV'] = 'TS'

substitution['ST'] = 'VA'
substitution['TS'] = 'AV'
substitution['VA'] = 'ST'
substitution['AV'] = 'TS'

substitution['SH'] = 'RA'
substitution['HS'] = 'AR'
substitution['RA'] = 'SH'
substitution['AR'] = 'HS'

substitution['SE'] = 'MA'
substitution['ES'] = 'AM'
substitution['MA'] = 'SE'
substitution['AM'] = 'ES'

substitution['AU'] = 'L_'
substitution['CX'] = '_B'

substitution['TH'] = 'AT'
substitution['HT'] = 'TA'
substitution['TE'] = 'AH'
substitution['ET'] = 'HA'
substitution['TL'] = 'AE'
substitution['LT'] = 'EA'
substitution['TA'] = 'AL'
substitution['AT'] = 'LA'
substitution['HE'] = 'TH'
substitution['EH'] = 'HT'
substitution['HL'] = 'TE'
substitution['LH'] = 'ET'
substitution['HA'] = 'TL'
substitution['AH'] = 'LT'
substitution['EL'] = 'HE'
substitution['LE'] = 'EH'
substitution['EA'] = 'HL'
substitution['AE'] = 'LH'
substitution['LA'] = 'EL'
substitution['AL'] = 'LE'
substitution['VR'] = 'SV'
substitution['RV'] = 'VS'
substitution['VM'] = 'SR'
substitution['MV'] = 'RS'
substitution['V_'] = 'SM'
substitution['_V'] = 'MS'
substitution['VS'] = 'S_'
substitution['SV'] = '_S'
substitution['RM'] = 'VR'
substitution['MR'] = 'RV'
substitution['R_'] = 'VM'
substitution['_R'] = 'MV'
substitution['RS'] = 'V_'
substitution['SR'] = '_V'
substitution['M_'] = 'RM'
substitution['_M'] = 'MR'
substitution['MS'] = 'R_'
substitution['SM'] = '_R'
substitution['_S'] = 'M_'
substitution['S_'] = '_M'
substitution['TR'] = 'HV'
substitution['VH'] = 'RT'
substitution['HV'] = 'TR'
substitution['RT'] = 'VH'
substitution['TM'] = 'EV'
substitution['VE'] = 'MT'
substitution['EV'] = 'TM'
substitution['MT'] = 'VE'
substitution['T_'] = 'LV'
substitution['VL'] = '_T'
substitution['LV'] = 'T_'
substitution['_T'] = 'VL'
substitution['TS'] = 'AV'
substitution['VA'] = 'ST'
substitution['AV'] = 'TS'
substitution['ST'] = 'VA'
substitution['HM'] = 'ER'
substitution['RE'] = 'MH'
substitution['ER'] = 'HM'
substitution['MH'] = 'RE'
substitution['H_'] = 'LR'
substitution['RL'] = '_H'
substitution['LR'] = 'H_'
substitution['_H'] = 'RL'
substitution['HS'] = 'AR'
substitution['RA'] = 'SH'
substitution['AR'] = 'HS'
substitution['SH'] = 'RA'
substitution['E_'] = 'LM'
substitution['ML'] = '_E'
substitution['LM'] = 'E_'
substitution['_E'] = 'ML'
substitution['ES'] = 'AM'
substitution['MA'] = 'SE'
substitution['AM'] = 'ES'
substitution['SE'] = 'MA'
substitution['LS'] = 'A_'
substitution['_A'] = 'SL'
substitution['A_'] = 'LS'
substitution['SL'] = '_A'
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