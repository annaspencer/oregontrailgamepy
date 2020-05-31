import random
import time
import sys
#variables:
global life
global death

life = "You have survived! You can continue on the trail..."
death = "Sorry! It didn't work! You were not able to complete Oregon Trail Lite. Please try again!"

#random events list:
ran_events = [" Snake Bite!", " You have to cross a river!", " You have dysentary!", " Aliens!", " Bandits!"]

#checkpoints list:

checkpoints = iter([" Chimney Rock", " Fort Laramie", " Independence Rock", " Soda Springs", " The Dalles", "Oregon City!"])

#life/death list:
life_death =  [life, death]

#continue function
def continue_game_a():
    check = next(checkpoints)
    print("You have made it to ", check)
    if check != "Oregon City!":
        prompt = input("Would you like to continue? Type Y / N ")
        if prompt.upper() == "Y":
                
            time_space()
            events_a()
        elif prompt.upper() == "N":
            vol_end()
        else:
            invalid_choice()
            continue_game_a()
    else:
        win_game()
        sys.exit
def continue_game_b():
    check = next(checkpoints)
    print("You have made it to ", check)
    if check != "Oregon City!":
        prompt = input("Would you like to continue? Type Y / N ")
        if prompt.upper() == "Y":
                
            time.sleep(3)
            add_spaces
            events_b()
        elif prompt.upper() == "N":
            vol_end()
        else:
            invalid_choice()
            continue_game_b()
    else:
        win_game()
        sys.exit
def continue_game_c():
    check = next(checkpoints)
    print("You have made it to ", check)
    if check != "Oregon City!":
        prompt = input("Would you like to continue? Type Y / N ")
        if prompt.upper() == "Y":
                
            time.sleep(3)
            add_spaces
            events_c()
        elif prompt.upper() == "N":
            vol_end()
        else:
            invalid_choice()
            continue_game_c()
    else:
        win_game()
        sys.exit
#random death
def random_death_a():
    if random.choice(life_death) == life:
        print(life)
        continue_game_a()
    else: 
        print(death)

def random_death_b():
    if random.choice(life_death) == life:
        print(life)
        continue_game_b()
    else: 
        print(death)

def random_death_c():
    if random.choice(life_death) == life: 
        print(life)
        continue_game_c()
    else: 
        print(death)


# packages function:
def sup_choices():
    choice = input("Type A, B, or C for your choice:> ")
    if choice.upper() == "A":
        start()
        events_a()
    elif choice.upper() == "B":
        start()
        events_b()
    elif choice.upper() == "C":
        start()
        events_c()
    else:
        invalid_choice()
        sup_choices()
   
#random event function:
def events_a():
    new_event = random.choice(ran_events)
    print("Oh no!" + new_event)
    add_spaces()
    if new_event == " Snake Bite!":
        time_space()
        first_aid()
        time.sleep(3)
        return continue_game_a()
    elif new_event == " You have to cross a river!":
        time.sleep(3)
        print("You do not have enough travel money to hire a ferry. You have to ford the river...")
        time_space()
        return random_death_a()
    elif new_event == " You have dysentary!":
        first_aid()
        time_space()
        return continue_game_a()
    elif new_event == " Aliens!":
        no_money()
        time_space()
        return random_death_a()
    elif new_event == " Bandits!":
        no_money()
        time_space()
        random_death_a()
    else:
        win_game()


#events functions:
def events_b():
    new_event = random.choice(ran_events)
    print("Oh no!" + new_event)
    if new_event == " Snake Bite!":
        time.sleep(3)
        input("You can choose 1.) First Aid Kit or 2.) Wait it out ? Type 1 or 2 > ")
        random_death_b()
    elif new_event == " You have to cross a river!":
        time.sleep(3)
        input("You can choose 1.) Hire a Ferry or 2.) Ford the river ? Type 1 or 2 > ")
        random_death_b()
    elif new_event == " You have dysentary!":
        first_aid()
        time.sleep(3)
        continue_game_b()
    elif new_event == " Aliens!":
        time.sleep(3)
        mod_aliens()
    elif new_event == " Bandits!":
        time.sleep(3)
        bandits_b()
    else:
        win_game()

def events_c():
    new_event = random.choice(ran_events)
    print("Oh no!" + new_event)
    if new_event == " Snake Bite!" :
        time_space()
        no_first_aid()
        random_death_c()
    elif new_event == " You have to cross a river!" :
        time_space()
        print("You have enough money to hire a ferry and are able to continue on the trail")
        continue_game_c()
    elif new_event == " You have dysentary!" :
       no_first_aid()
       time_space()
       random_death_c()
        
    elif new_event == " Aliens!" :
        time_space()
        print("You have enough money to pay off the Aliens. You are allowed to continue on....")
        continue_game_c()
    elif new_event == " Bandits!":
        time_space()
        print("You have enough money to pay off the Bandits. You are allowed to continue on....")
        continue_game_c()
    else:
        win_game()
#Choice B functions:
def mod_aliens():
        mod_alien = input("You can try to 1.) pay off the Aliens or 2.) Ask if they accept a trade of your supplies. Type 1 or 2 for your choice.")
        if mod_alien == "1":
            time_space()
            print("It worked!")
            return continue_game_b()
        elif mod_alien == "2":
            return random_death_b()
        else:
            invalid_choice()
            return mod_aliens()
        
def bandits_b():
    mod_band_choice = input("You can try to 1.) pay off the Bandits or 2.) Ask if they accept a trade of your supplies. Type 1 or 2 for your choice.")
    if mod_band_choice == "1":
        time_space()
        print("It worked!")
        continue_game_b()
    elif mod_band_choice == "2":
        random_death_b()
    elif mod_band_choice == "teleport":
        time_space()
        print("Amazing! You teleported safetly to Oregon City! You have finally beat Oregon Trail Lite!")


    else:
        invalid_choice()
        return bandits_b()
#invalid function
def invalid_choice():
    print("That is not a valid choice. Please try again.")
#end of game function
    
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
#no money
def no_money():
    time_space()
    print("They are demanding money, but you do not have any left after buying supplies. Instead, you hope they will accept some of your vaulable belongings.")
# spacing function
def add_spaces():
    print()
    print("...")
    print(".....")
    print(".........")
    print("......................")
    print("......................................................................")
def start():
    print("                                      Good choice! Let's hit the trail...")
    add_spaces()
    print("Welcome! You are leaving from Independence, Missouri! Good Luck!")
    time_space()

#Game Introduction:
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Welcome to Oregon Trail~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Explain briefly the goal of the game.
print()
print()
print()
print("                     The goal of this game is to travel the Oregon Trail all the way to Oregon City!")
print()
print()
print()
#General Store:
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~You are at the General Store~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("                     Here are your Supplies Package options. You have $500.")
print()
print("                     Option A: Complete Survival Package ~ includes Food,Water, Tools, Clothing, Oxen, First Aid. Cost: $500")
print()
print("                     Option B: Medium Survival Package ~ includes Food, Water, Oxen, First Aid. Cost: $250")
print()
print("                     Option C: Minimalist Package ~ includes Food, Water,Oxen. Cost: $100")
print()
sup_choices()
print()





#Game Introduction:
  
    #Explain briefly the goal of the game.
#General Store:
    #User is assigned a dollar amount.
    #User is presented with surivial gear options.
    #Options are:    
       # Most prepared = highest cost, leaving user with less travel money
       # Moderately prepared = middle cost, leaving user with some travel money
       # Least prepared = lowest cost, most highest amount of travel money.
    #User picks level of preparedness.
    #The level of preparedness is assigned to User throughout the game.
#Journey:
    #There are 6 checkpoints/locations throughout the trail.
   # At the first 5 checkpoints a random event occurs.
    #The 6th checkpoint is Oregon City/end of game. 
    #1. Chimney Rock
   # 2. Fort Laramie
   # 3. Independence Rock
    #4. Soda Springs
    #5. Dalles
    #6. Oregon City
   # Random Events are:
   # 1. Snake Bite
       # options for Most Prepared
           # First Aid and continue
        #options for Moderately Prepared
           # First Aid 
           # Wait it out
           # both options return randomly picked continue or die.
        #options for least Prepared
           # Wait it out and return randomly picked continue or die
    #2. Cross a river
        #options for Most Prepared
           # Ford the river and return randomly picked continue or tip the wagon over and game ends.
        #options for Moderately Prepared
           # Ford the river
            #Hire a Ferry
            #both options return randomly picked continue or tip the wagon over and game ends.
        #options for least Prepared
           # Hire Ferry and continue
   # 3. Dysentary 
        #options for Most Prepared
           # First Aid and continue
       # options for Moderately Prepared
           # First Aid 
            #Wait it out
            #both options return randomly picked continue or die.
        #options for least Prepared
           # Wait it out and return randomly picked continue or die
    #4. Alien Invasion
        #options for Most Prepared
            # Trade supplies return randomly picked continue or abduction/end of game.
        #options for Moderately Prepared
            #Pay them off and continue
            #Trade Supplies and return randomly picked continue or die.
        #options for least Prepared
           # Pay them off and continue
    #5. Bandits
      # options for Most Prepared
            # Trade supplies return randomly picked continue or end of game.
        #options for Moderately Prepared
           # Pay them off and continue
            #Trade Supplies and return randomly picked continue or die.
        #options for least Prepared
            #Pay them off and continue

    #If the game ends at a certain check point then a message declares that the game ended and the User made it as far as the checkpoint

    #If the game ends at Oregon City a message declares that the User has made it to their destination and won the game.
    

#Nice to haves:
   # -picture between checkpoints
   # -cheat code
###



#Game Introduction:
    #Have user enter name.
    #Explain briefly the goal of the game.
#General Store:
    #User is assigned a dollar amount.
    #User is presented with surivial gear options.
    #Options are:    
       # Most prepared = highest cost, leaving user with less travel money
       # Moderately prepared = middle cost, leaving user with some travel money
       # Least prepared = lowest cost, most highest amount of travel money.
    #User picks level of preparedness.
    #The level of preparedness is assigned to User throughout the game.
#Journey:
    #There are 6 checkpoints/locations throughout the trail.
   # At the first 5 checkpoints a random event occurs.
    #The 6th checkpoint is Oregon City/end of game. 
    #1. Chimney Rock
   # 2. Fort Laramie
   # 3. Independence Rock
    #4. Soda Springs
    #5. Dalles
    #6. Oregon City
   # Random Events are:
   # 1. Snake Bite
       # options for Most Prepared
           # First Aid and continue
        #options for Moderately Prepared
           # First Aid 
           # Wait it out
           # both options return randomly picked continue or die.
        #options for least Prepared
           # Wait it out and return randomly picked continue or die
    #2. Cross a river
        #options for Most Prepared
           # Ford the river and return randomly picked continue or tip the wagon over and game ends.
        #options for Moderately Prepared
           # Ford the river
            #Hire a Ferry
            #both options return randomly picked continue or tip the wagon over and game ends.
        #options for least Prepared
           # Hire Ferry and continue
   # 3. Dysentary 
        #options for Most Prepared
           # First Aid and continue
       # options for Moderately Prepared
           # First Aid 
            #Wait it out
            #both options return randomly picked continue or die.
        #options for least Prepared
           # Wait it out and return randomly picked continue or die
    #4. Alien Invasion
        #options for Most Prepared
            # Trade supplies return randomly picked continue or abduction/end of game.
        #options for Moderately Prepared
            #Pay them off and continue
            #Trade Supplies and return randomly picked continue or die.
        #options for least Prepared
           # Pay them off and continue
    #5. Bandits
      # options for Most Prepared
            # Trade supplies return randomly picked continue or end of game.
        #options for Moderately Prepared
           # Pay them off and continue
            #Trade Supplies and return randomly picked continue or die.
        #options for least Prepared
            #Pay them off and continue

    #If the game ends at a certain check point then a message declares that the game ended and the User made it as far as the checkpoint

    #If the game ends at Oregon City a message declares that the User has made it to their destination and won the game.
    

#Nice to haves:
   # -picture between checkpoints
   # -cheat code
###