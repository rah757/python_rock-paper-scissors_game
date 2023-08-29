import random
import time
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]
choice_name = ["rock", "paper", "scissors"]

best_of = int(input("Enter the amount of points needed to win - (3, 5 etc): "))

human_points = 0
computer_points = 0

while human_points < best_of and computer_points < best_of:
  
  human = int(input("\nSelect rock, paper or scissors. \n(rock - 0) ~ (paper - 1) ~ (scissors - 2)\n\nOption: "))

  if human == 0 or human == 1 or human == 2:
    pc = random.randint(0,2)

    print(f"\nyou chose {choice_name[human]} \n {choice[human]}\n")

    print(f"the computer chose {choice_name[pc]} \n {choice[pc]}\n")

    if(human == 0 and pc == 0 or human == 1 and pc == 1 or human == 2 and pc == 2):
      print("That's a tie! You both got 0 extra points. \n")
    elif(human == 0 and pc == 1 or human == 1 and pc == 2 or human == 2 and pc == 0):
      print("The computer won this round, computer gets a point! \n")
      computer_points += 1
    elif(pc == 0 and human == 1 or pc == 1 and human == 2 or pc == 2 and human == 0):
      print("You won this round, you got a point!")
      human_points += 1 

    print(f"The current score is {human_points} - {computer_points}")

  else: 
    print("\nwrong choice, choose again:")

if human_points > computer_points:
  print("\nCongrats human, you won the game! ♡⸜(˶˃ ᵕ ˂˶)⸝♡ ")
else:
  print("\nThe computer won the game ˙◠˙ , better luck next time!")

time.sleep(5)
