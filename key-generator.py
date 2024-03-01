# THELA
# VRMUS

# key_matrix = [['T', 'H', 'E', 'L', 'A'], ['V', 'R', 'M', '_', 'S']]
# AISDX
key_matrix = [['A', 'I', 'D', 'X', 'S']]

print('Possible subsitution keys: ')

# row
for h in range(0, len(key_matrix)):
  for i in range(0, 5):
    for j in range(i+1, 5):
      print(f'substitution[\'{key_matrix[h][(i)%5]}{key_matrix[h][(j)%5]}\'] = \'{key_matrix[h][(i+4)%5]}{key_matrix[h][(j+4)%5]}\'')
      print(f'substitution[\'{key_matrix[h][(j)%5]}{key_matrix[h][(i)%5]}\'] = \'{key_matrix[h][(j+4)%5]}{key_matrix[h][(i+4)%5]}\'')

# # box
# for i in range(0, 5):
#   for j in range(i+1, 5):
#     print(f'substitution[\'{key_matrix[0][i%5]}{key_matrix[1][j%5]}\'] = \'{key_matrix[0][j%5]}{key_matrix[1][i%5]}\'')
#     print(f'substitution[\'{key_matrix[1][i%5]}{key_matrix[0][j%5]}\'] = \'{key_matrix[1][j%5]}{key_matrix[0][i%5]}\'')
#     print(f'substitution[\'{key_matrix[0][j%5]}{key_matrix[1][i%5]}\'] = \'{key_matrix[0][i%5]}{key_matrix[1][j%5]}\'')
#     print(f'substitution[\'{key_matrix[1][j%5]}{key_matrix[0][i%5]}\'] = \'{key_matrix[1][i%5]}{key_matrix[0][j%5]}\'')