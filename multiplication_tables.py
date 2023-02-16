# The Multiplication Tables Program
# lets you pull up endless tables of any multiples. You can also practice your multiplication skills. Try it out!

# Creator: Zane Palino
# Date: 2/15/2023 11:58 AM

#______________________________________________________________________________________________________________________
start_mode = True

import random
import sys

def tab(amount):
    return "\t"*amount

def hearts_count(amount):
    lost = 3 - amount
    print("Hearts remaining: " + "♥ "*amount + "♡ "*lost)
    print("")

# ak means Accepted Keywords
view_tables_ak = ["view tables", "view table", "vt", "v", "vi", "view", "tables", "table"]
quiz_ak = ["quiz", "qu", "qui", "quiz time"]
quiz_mode1_ak = ["mode1", "mode 1", "mod1", "mo1", "1", "m1", "md1", "first mode", "first", "1st"]
quiz_mode2_ak = ["mode2", "mode 2", "mod2", "mo2", "2", "m2", "md2", "second mode", "second", "2nd"]
yes_ak = ["y", "yes", "yea", "yay", "okay", "ok", "yeah", "yep", "mhm", "ya", "yah"]
no_ak = ["n", "no", "nah", "nay", "nope", "noo", "nooo", "nein", "non", "no way"]

print("\n\nWelcome to The Multiplication Tables Program")

while start_mode == True:
    view_tables = False
    quiz = False
    answer_mode = True
    mode = input(f"\n{tab(5)}      Available Modes:\n{tab(6)}\033[1mVIEW TABLES\033[0m\n{tab(6)}   \033[1mQUIZ\033[0m\n\nChoose a mode:  ")
    if mode.lower() == 'q':
        sys.exit("You have ended the program.")
    else:
        for word in view_tables_ak:
            if word == mode.lower():
                view_tables = True
                break
        for word in quiz_ak:
            if word == mode.lower():
                quiz = True
                break
        if view_tables == False and quiz == False:
            print("Invalid input. Choose from the following available modes.")
            continue 
#_____________________________________________________________________________________________________________________
    if view_tables == True:
        print("View tables mode selected. Enter 'q' to exit anytime.")
    # View Tables Mode
    while view_tables == True:
        multiplier = input("\n\nWhat times table do you want to practice?  ")
        if multiplier.lower() == 'q':
            break
        while multiplier.isnumeric() == False:
            print("Please enter a number.")
            multiplier = input("\n\nWhat times table do you want to practice?  ")
        multiplier = int(multiplier)
        multiplicand = input("\nHow many rows do you want to see?  ")
        if multiplicand.lower() == 'q':
            break
        while multiplicand.isnumeric() == False:
            print("Please enter a number.")
            multiplicand = input("\nHow many rows do you want to see?  ")
        multiplicand = int(multiplicand)
        print("")
        for i in range(1, multiplicand+1):
            product = multiplier * i
            print(f"{multiplier} x {i} = {product}")
        status = input("\nHit enter to create a new table. Press 'q' to exit view tables mode.  ")
        if status.lower() == "q":
            break
        else:
            continue
            
    if quiz == True:
        print("You have selected study mode.\nEnter 'q' to quit anytime.")
        print("\nSelect from the following modes:")
        print("\033[1mMode 1\033[0m: The multiplier remains the same for each question. \nOnly the multiplicand changes for each question.")
        print("\n\033[1mMode 2\033[0m: Both the multiplier and the multiplicand can change for each question (harder mode!)")

    # Quiz Mode
    while quiz == True:
        quiz_mode1 = False
        quiz_mode2 = False
        score = 0
        streak = 0
        hearts = 3

        quiz_mode = input(f"\n{tab(5)}      Available Modes:\n{tab(6)}   \033[1mMODE 1\033[0m\n{tab(6)}   \033[1mMODE 2\033[0m\n\nChoose a mode:  ")
        if quiz_mode.lower() == 'q':
            break
        else:
            for word in quiz_mode1_ak:
                if word == quiz_mode.lower():
                    quiz_mode1 = True
                    break
            for word in quiz_mode2_ak:
                if word == quiz_mode.lower():
                    quiz_mode2 = True
                    break
            if quiz_mode1 == False and quiz_mode2 == False:
                print("Invalid input. Choose from the following available modes.")
                continue

        if quiz_mode1 == True:
            print("You have selected Quiz Mode 1. You will only receive questions containing the multiplier that you select.")
            hearts_on = input("Would you like to turn on hearts? (y/n)  ")
            if hearts_on.lower() == 'y':
                hearts_on = True
            elif hearts_on.lower() == "n":
                hearts_on = False
            else:
                continue 
        # Quiz Mode 1
        while quiz_mode1 == True: 
            multiplier = input("\n\nWhat number do you want to multiply by?  ")
            while multiplier.isnumeric() == False:
                if multiplier.lower() == 'q':
                    break
                print("Please enter a number.")
                multiplier = input("\n\nWhat number do you want to multiply by?  ")
            if multiplier.lower() == 'q':
                    break
            multiplier = int(multiplier)

            multiplicand = input("\nWhat is the max number you want to multiply by?  ")
            while multiplicand.isnumeric() == False:
                if multiplicand.lower() == 'q':
                    break
                print("Please enter a number.")
                multiplicand = input("\nWhat is the max number you want to multiply by?  ")
            if multiplicand.lower() == 'q':
                break
            multiplicand = int(multiplicand)

            while answer_mode == True:
                temporary_multiplicand = random.randint(1, multiplicand)
                product = multiplier * temporary_multiplicand
                answer = (input(f"{multiplier} x {temporary_multiplicand} = "))
                if answer == "q":
                    hearts = 3
                    score = 0
                    streak = 0
                    break
                elif answer == str(product):
                    print("Correct! ✓\n\n")
                    score += 1
                    streak += 1
                    print(f"Score: {score}")
                    print(f"Streak: {streak}")
                    if hearts_on == True:
                        hearts_count(hearts)
                else:
                    print(f"Wrong. ❌\nAnswer: {product}\n")
                    streak = 0
                    print(f"Score: {score}")
                    print(f"Streak: {streak}")
                    if hearts_on == True:
                        hearts -= 1
                        hearts_count(hearts)
                        if hearts == 0:
                            hearts = 3
                            status = input("Quiz over. Restart? (y/n)  ")
                            if status.lower() == "y":
                                continue
                            else:
                                break
                            
        if quiz_mode2 == True:
            print("You have selected Quiz Mode 2. You will receive questions with numbers in the range that you select.")
            hearts_on = input("Would you like to turn on hearts? (y/n)  ")
            if hearts_on.lower() == 'y':
                hearts_on = True
            elif hearts_on.lower() == "n":
                hearts_on = False
            else:
                continue 
        # Quiz Mode 2
        while quiz_mode2 == True: 
            multiplier = input("\n\nSelect range for the first number:  ")
            while multiplier.isnumeric() == False:
                if multiplier.lower() == 'q':
                    break
                print("Please enter a number.")
                multiplier = input("\n\nSelect range for the first number:  ")
            if multiplier.lower() == 'q':
                    break
            multiplier = int(multiplier)

            multiplicand = input("\nSelect range for the second number:  ")
            while multiplicand.isnumeric() == False:
                if multiplicand.lower() == 'q':
                    break
                print("Please enter a number.")
                multiplicand = input("\nSelect range for the second number:  ")
            if multiplicand.lower() == 'q':
                break
            multiplicand = int(multiplicand)

            while answer_mode == True:
                temporary_multiplier = random.randint(1, multiplier)
                temporary_multiplicand = random.randint(1, multiplicand)
                product = temporary_multiplier * temporary_multiplicand
                answer = (input(f"{temporary_multiplier} x {temporary_multiplicand} = "))
                if answer == "q":
                    hearts = 3
                    score = 0
                    streak = 0
                    break
                elif answer == str(product):
                    print("Correct! ✓\n\n")
                    score += 1
                    streak += 1
                    print(f"Score: {score}")
                    print(f"Streak: {streak}")
                    if hearts_on == True:
                        hearts_count(hearts)
                else:
                    print(f"Wrong. ❌\nAnswer: {product}\n")
                    streak = 0
                    print(f"Score: {score}")
                    print(f"Streak: {streak}")
                    if hearts_on == True:
                        hearts -= 1
                        hearts_count(hearts)
                        if hearts == 0:
                            hearts = 3
                            status = input("Quiz over. Restart? (y/n)  ")
                            if status.lower() == "y":
                                continue
                            else:
                                break
            quiz = False