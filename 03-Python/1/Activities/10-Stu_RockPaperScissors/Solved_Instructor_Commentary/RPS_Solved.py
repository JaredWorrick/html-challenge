# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals

# Print output showing the choices regardless of win/lose/etc. 
# Since i can customize it here using formatted strings, no need to repeat it 
# 100 times in each condition. 
print("You chose {}. The computer chose {}.".format(user_choice, computer_choice))


# Pseudocode: "invalid" -> "not one of 'r','p','s'" -> soo... just not in that list we defined up there ^?
# Start with the invalid so we don't have to do any checks
if user_choice not in options:
    print('Sorry {} was not one of the available options'.format(user_choice))
# Pseudocode: "if win"
# Aka: "If win with paper OR win with rock OR win with scissors"
elif (user_choice == "p" and computer_choice == "r") or (user_choice == "r" and computer_choice == "s") or (user_choice == "s" and computer_choice == "p"):
    print('You won!')
# Psuedocode: "if tie" -> "tie happens when we pick the same thing"-> 
elif user_choice == computer_choice:
    print('A TIE!')
else: 
    # If this is triggered (chained conditional), none of the previous conditions were
    # so user didn't pick an invalid choice (Cond 1)
    # user didn't win (Cond 2)
    # user didn't tie (Cond 3)
    # only thing left is ...
    print('hahhaha u lose')
