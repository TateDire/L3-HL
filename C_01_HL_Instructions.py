# checks users enter yes (y) or no (n)

def yes_no(question):
    ### Checks user response to a question is yes / no (y/n), returns 'yes' or 'no'

    while True:

        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print('''
    **** Instructions ****

To begin, choose the number of rounds and either customise
the game parameters or go with the default game (where the
secret number will be generated will be between 1 and 100)

Then choose how many rounds you'd like to play <enter> for
infinite mode.

Your goal is to try to guess the secret number without
running out of guesses.

Good luck.

    ''')


# Main routine
print()
print("⬆️⬆️⬆️ Welcome to the Higher Lower Game 🔻🔻🔻")
print()

# looping for testing purposes

want_instructions = yes_no("Do you want to see the instructions? ")

# Checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print()
print("program continues")
