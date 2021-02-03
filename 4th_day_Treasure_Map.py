row1 = ['_', '_', '_']
row2 = ['_', '_', '_']
row3 = ['_', '_', '_']
map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = input('Where do you want to put the treasure? ')

vertical = int(position[1])
horisontal = int(position[0])

map[vertical - 1][horisontal - 1] = 'X'

# pos_list = []
# for i in range(len(position)):
#     pos_list.append(int(position[i]))
# if pos_list[1] == 1:
#     row1[pos_list[0] - 1] = "X"
# elif pos_list[1] == 2:
#     row2[pos_list[0] - 1] = "X"
# elif pos_list[1] == 3:
#     row3[pos_list[0] - 1] = "X"


print(f'{row1}\n{row2}\n{row3}')
