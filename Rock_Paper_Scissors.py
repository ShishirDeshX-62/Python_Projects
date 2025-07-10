import random

print("Instructions :\n0 for Rock\n1 for paper \n2 for scissors\n-1 to Quit\nAll the Best")
game = ("Rock", "Paper", "Scissors")

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

while True:
    user_input = int(input("choose your Move=\n"))

    if user_input == -1:
        print("Thanks for playing! See you next time.")
        break

    no = random.randint(0, 2)

    if user_input == 0:
        print(rock)
    elif user_input == 1:
        print(paper)
    elif user_input == 2:
        print(scissors)
    else:
        print("Invalid Choice\nComputer Wins")
        continue  # skip rest and ask again

    if no == 0:
        print(rock)
    elif no == 1:
        print(paper)
    elif no == 2:
        print(scissors)

    if user_input == no:
        print("It's a Tie")
    elif no == 0:
        if user_input == 1:
            print("Paper VS Rock\n You Win!!!")
        elif user_input == 2:
            print("Scissor VS Rock \n You Lost!!!")
    elif no == 1:
        if user_input == 0:
            print("Rock VS Paper\n You Lost!!!")
        elif user_input == 2:
            print("Scissors VS Paper \n You Win!!!")
    elif no == 2:
        if user_input == 0:
            print("Rock VS Scissors\n You Win!!!")
        elif user_input == 1:
            print("Paper VS Scissor \n You Lost!!!")
