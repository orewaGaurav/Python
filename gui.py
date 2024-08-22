import random
user_choice  = input("Choose your choice : 'Rock' , 'Paper' , 'scissor'\n")
print("your choice is :",user_choice)
system = ["Rock","Paper","scissor"]
system_choice = random.choice(system)
print("System choice is :",system_choice)
if user_choice == system_choice:
    print("Nobody wins its a clear TIE !")
elif user_choice == "Rock" and system_choice == "Scissor":
    print("You Win the game!")
elif user_choice == "Paper" and system_choice == "Rock":
    print("You win the game!")
elif user_choice == "Scissor" and system_choice == "Paper":
    print("You win the game!")
else:
    print("System wins !")