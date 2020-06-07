import random
import time

#pick game path & run game:
def play_game():
    print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Welcome to Oregon Trail~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



                     The goal of this game is to travel the Oregon Trail all the way to Oregon City!



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~You are at the General Store~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                     Here are your Supplies Package options. You have $500.

                     Option A: Complete Survival Package ~ includes Food,Water, Tools, Clothing, Oxen, First Aid. Cost: $500

                     Option B: Medium Survival Package ~ includes Food, Water, Oxen, First Aid. Cost: $250

                     Option C: Minimalist Package ~ includes Food, Water,Oxen. Cost: $100""")
    choice = input("Type A, B, or C for your choice:> ")
    if choice.upper() == "A":
        supply = "A"
        start()
        game_path(supply)
    elif choice.upper() == "B":
        supply = "B"
        start()
        game_path(supply)
    elif choice.upper() == "C":
        supply = "C"
        start()
        game_path(supply)
    else:
        invalid_choice()
        play_game()

#game_paths

def game_path(supply):
    ran_events = [" Snake Bite!", " Bandits!", " You have to cross a river!", " You have dysentary!", " Aliens!"]
    time.sleep(3)
    new_event = random.choice(ran_events)
    print("Oh no!" + new_event)
    add_spaces()
# snake bite
    if new_event == " Snake Bite!":
        time_space()
        if supply == "A":
            first_aid()
            time.sleep(3)
            continue_path(supply)
        elif supply == "B":
            time.sleep(3)
            input("You can choose 1.) First Aid Kit or 2.) Wait it out ? Type 1 or 2 > ")
            random_death(supply)
        elif supply == "C":
            time_space()
            no_first_aid()
            random_death(supply)
        else:
            return
#river
    elif new_event == " You have to cross a river!":
        time.sleep(3)
        if supply == "A":
            print("You do not have enough travel money to hire a ferry. You have to ford the river...")
            time_space()
            random_death(supply)
        elif supply == "B":
            river_b = input("You can choose 1.) hire a ferry or 2.) ford the river? Type 1 or 2 > ")
            if river_b == "1":
                continue_path(supply)
            else:
                random_death(supply)
        elif supply == "C":
            print("You have enough money to hire a ferry and are able to continue on the trail")
            continue_path(supply)
        else:
            return
#dysentary
    elif new_event == " You have dysentary!":
        time.sleep(3)
        if supply == "A":
            first_aid()
            time_space()
            continue_path(supply)
        elif supply == "B":
            first_aid()
            time.sleep(3)
            continue_path(supply)
        elif supply == "C":
            no_first_aid()
            time_space()
            random_death(supply)
        else:
            return
 #aliens
    elif new_event == " Aliens!":
        if supply == "A":
            no_money()
            time_space()
            random_death(supply)
        elif supply == "B":
            mod_band_choice = input("You can try to 1.) pay off the Aliens or 2.) Ask if they accept a trade of your supplies. Type 1 or 2 for your choice.")
            if mod_band_choice == "1":
                time_space()
                print("It worked!")
                continue_path(supply)
            elif mod_band_choice == "2":
                random_death(supply)
            elif mod_band_choice == "teleport":
                time_space()
                print("Amazing! You teleported safetly to Oregon City! You have finally beat Oregon Trail Lite!")
            else:
                invalid_choice()
                return game_path(supply)
        elif supply == "C":
            time_space()
            print("You have enough money to pay off the Aliens. You are allowed to continue on....")
            continue_path(supply)
        else:
            return
   
#bandits
    elif new_event == " Bandits!":
        time.sleep(3)
        if supply == "A":
            no_money()
            time_space()
            random_death(supply)
        elif supply == "B":
            mod_band_choice = input("You can try to 1.) pay off the Bandits or 2.) Ask if they accept a trade of your supplies. Type 1 or 2 for your choice.")
            if mod_band_choice == "1":
                time_space()
                print("It worked!")
                continue_path(supply)
            elif mod_band_choice == "2":
                random_death(supply)
            elif mod_band_choice == "teleport":
                time_space()
                print("Amazing! You teleported safetly to Oregon City! You have finally beat Oregon Trail Lite!")
            else:
                invalid_choice()
                return game_path()
        elif supply == "C":
            time_space()
            print("You have enough money to pay off the Bandits. You are allowed to continue on....")
            continue_path(supply)
    else:
        return
       
def continue_path(supply):
    checkpoints = iter([" Chimney Rock", " Fort Laramie", " Independence Rock", " Soda Springs", " The Dalles", "Oregon City!"])
    check = next(checkpoints)
    print("You have made it to ", check)
    if check != "Oregon City!":
        prompt = input("Would you like to continue? Type Y / N ")
        time.sleep(3)
        add_spaces
        if prompt.upper() == "Y":
            game_path(supply)
        elif prompt.upper() == "N":
            vol_end()
        else:
            invalid_choice()
            continue_path(supply)
    else:
        win_game()
        
def random_death(supply):
    life = "You have survived! You can continue on the trail..."
    death = "Sorry! It didn't work! You were not able to complete Oregon Trail Lite. Please try again!"
    life_death =  [life, death]
    if random.choice(life_death) == life:
        if supply == 'A':
            print(life)
            continue_path(supply)
        elif supply == 'B':
            print(life)
            continue_path(supply) 
        elif supply == 'C': 
            print(life)
            continue_path(supply)
        else:
            return
    else: 
        print(death)

#helper functions:

#invalid function
def invalid_choice():
    print("That is not a valid choice. Please try again.")
#end of game function
    #vol_end
def vol_end():
    print("Thanks for playing! Try again next time!")

def win_game():
    print("Oregon City! Hurray!! You have finally beat Oregon Trail Lite. Congrats!")
#time and space function
def time_space():
    add_spaces()
    time.sleep(3)
#first aid kit
def first_aid():
    print("Luckily, you have a First Aid Kit and can treat this ailment. Your health is restored! You may continue on the trail....")
    time_space()
#no_first aid
def no_first_aid():
    print("Unfortunately, you did not purchase a First Aid Kit with your supplies. You will have to wait to see if your health will be restored!")
    time_space()
#no money
def no_money():
    time_space()
    print("They are demanding money, but you do not have any left after buying supplies. Instead, you hope they will accept some of your vaulable belongings.")
    time_space()
# spacing function
def add_spaces():
    print()
    print("...")
    print(".....")
    print(".........")
    print("......................")
    print("......................................................................")
#game starts:
def start():
    print("                                      Good choice! Let's hit the trail...")
    add_spaces()
    print("Welcome! You are leaving from Independence, Missouri! Good Luck!")
    time_space()

play_game()
