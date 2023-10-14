row1 = ['0', '0', '0']
row2 = ['0', '0', '0']
row3 = ['0', '0', '0']

map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = input('Where do you want to put the treasure? ').strip().split(' ')

column = int(position[0]) - 1
line = int(position[1]) - 1

map[line][column] = 'x'

print(f'{row1}\n{row2}\n{row3}')


