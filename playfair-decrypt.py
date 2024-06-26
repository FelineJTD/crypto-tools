# imports
import sys

filename = sys.argv[1]

# read file
with open(filename, 'r') as f:
    text = f.read()

key = [
    ['T', 'H', 'E', 'L', 'A'],
    ['Z', 'Y', 'Q', 'U', 'I'],
    ['C', 'K', 'D', 'O', 'G'],
    ['V', 'R', 'M', 'P', 'S'],
    ['B', 'W', 'N', 'F', 'X']
]

substitution = {}
substitution['UR'] = '_P'
substitution['RU'] = 'P_'
substitution['AZ'] = '_I'
substitution['ZA'] = 'I_'
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
substitution['BL'] = 'FT'
substitution['LB'] = 'TF'
substitution['BE'] = '_T'
substitution['EB'] = 'T_'
substitution['SL'] = '_A'
substitution['LS'] = 'A_'
substitution['IH'] = '_A'
substitution['HI'] = 'A_'
substitution['SI'] = 'G_'
substitution['VW'] = 'R_'
substitution['WV'] = '_R'

substitution['IX'] = 'AS'
substitution['XI'] = 'SA'
substitution['DF'] = 'ON'
substitution['FD'] = 'NO'
substitution['ON'] = 'DF'
substitution['NO'] = 'FD'

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

substitution['AI'] = 'XA'
substitution['IA'] = 'AX'
substitution['AG'] = 'XI'
substitution['GA'] = 'IX'
substitution['AS'] = 'XG'
substitution['SA'] = 'GX'
substitution['AX'] = 'XS'
substitution['XA'] = 'SX'
substitution['IG'] = 'AI'
substitution['GI'] = 'IA'
substitution['IS'] = 'AG'
substitution['SI'] = 'GA'
substitution['IX'] = 'AS'
substitution['XI'] = 'SA'
substitution['GS'] = 'IG'
substitution['SG'] = 'GI'
substitution['GX'] = 'IS'
substitution['XG'] = 'SI'
substitution['SX'] = 'GS'
substitution['XS'] = 'SG'

substitution['BE'] = 'NT'
substitution['EB'] = 'TN'
substitution['OM'] = 'D_'
substitution['MO'] = '_D'

substitution['QE'] = 'YH'
substitution['EQ'] = 'HY'
substitution['LP'] = 'FO'
substitution['PL'] = 'OF'
substitution['AQ'] = 'LY'
substitution['QA'] = 'YL'

plaintext = ''

unkeyed = {}
for i in range(0, len(text), 2):
    try:
        a = text[i]
        b = text[i+1]
        a_row, a_col = -99, -99
        b_row, b_col = -99, -99
        for row in range(5):
            for col in range(5):
                if key[row][col] == a:
                    a_row, a_col = row, col
                if key[row][col] == b:
                    b_row, b_col = row, col
        if a_row == b_row:
            plaintext += key[a_row][(a_col-1+5) % 5]
            plaintext += key[b_row][(b_col-1+5) % 5]
        elif a_col == b_col:
            plaintext += key[(a_row-1+5) % 5][a_col]
            plaintext += key[(b_row-1+5) % 5][b_col]
        else:
            plaintext += key[a_row][b_col]
            plaintext += key[b_row][a_col]
    except:
        bigram = text[i] + text[i+1]
        try:
            plaintext += substitution[bigram]
            unkeyed[bigram] = substitution[bigram]
        except:
            plaintext += '__'

print(unkeyed)

linewidth = 100
with open('output/playfair-final.txt', 'w') as f:
    f.write(plaintext)
    # for i in range (0, len(plaintext), linewidth):
    #     f.write(text[i:i+linewidth])
    #     f.write('\n')
    #     f.write(plaintext[i:i+linewidth])
    #     f.write('\n\n')