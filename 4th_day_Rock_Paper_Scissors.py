import random

choice = int(input('Type 0 for Rock, 1 for Paper and 2 for Scissors. '))
com_choice = ['Rock', 'Paper', 'Scissors']
if choice == 0:
  print("Your choice is Rock")
elif choice == 1:
  print("Your choice is Paper")
elif choice == 2:
  print("Your choice is Scissors")
comp = random.choice(com_choice)
print(f'Computer choice is {comp}')
if (comp == 'Rock' and choice == 0) or (comp == 'Paper' and choice == 1) or (comp == 'Scissors' and choice == 2):
  print("It's a draw!")
elif (comp == 'Rock' and choice == 1) or (comp == 'Paper' and choice == 2) or (comp == 'Scissors' and choice == 1):
  print("You won!")
else:
  print('You lose!') 




user_choice =  int(input('Type 0 for Rock, 1 for Paper and 2 for Scissors. '))
computer_choice = random.randint(0, 2)
print(f'Your choice is {com_choice[user_choice]}')
print(f'Computer choice is {com_choice[computer_choice]}')
if user_choice  == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice > user_choice:
  print("You lose")
elif computer_choice == user_choice:
  print("It's a draw!")
elif user_choice == 2 and computer_choice == 0:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
