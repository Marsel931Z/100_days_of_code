import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ,'m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
simbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print('Welcome to the PyPassword generator!')
nr_letters = int(input('How many letters do you want? '))
nr_numbers = int(input('How many numbers do you want? '))
nr_simbols = int(input('How many simbols do you want? '))
pass_list = []
while nr_letters != 0:
  pass_list.append(letters[random.randint(0,len(letters) - 1)])
  nr_letters -= 1
while nr_numbers != 0:
  pass_list.append(numbers[random.randint(0,len(numbers) - 1)])
  nr_numbers -= 1
while nr_simbols != 0:
  pass_list.append(simbols[random.randint(0,len(simbols) - 1)])
  nr_simbols -= 1
random.shuffle(pass_list)
print(''.join(pass_list))
