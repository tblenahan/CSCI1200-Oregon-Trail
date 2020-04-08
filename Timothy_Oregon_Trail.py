#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:14:16 2017

@author: timothylenahan
"""
import trailblazer    #class
import date    #class
import companions    #class
import random    #module for games, etc.


def initial_conditions(player, date, com1, com2, com3, com4):
    """This function asks the player for their name and their companions' names
    and returns these values to be assigned to variables in the main function."""
    name = input("What is your name?: ")    #name of user
    player.set_name(name)    #sets player name in the class for the player
    
    print("Please enter the names of your companions below:")   #rest of the wagon party
    com1_name = input("1 : ")   #each one allows the input of a name and stores it in the classfor companions
    com1.set_name(com1_name)
    com2_name = input("2 : ")
    com2.set_name(com2_name)
    com3_name = input("3 :")
    com3.set_name(com3_name)
    com4_name = input("4 : ")
    com4.set_name(com4_name)
    print()     #space
    
def start_date(date):
    """This function asks the player for when they would like to start the 
    journey and gives them the option of a custom date or the default date and 
    then stores them in the class date"""
    print("Your departure date curently is: ", date.get_year(), "-", date.get_month(), "-", date.get_day())   #prints default date
    change_start = input("Would you like to change it? Y / N ")     #option to change start date
    if change_start == "y" or change_start == "Y":
        print("Remember you can change it to any date between: 1847-03-01 to 1847-05-01")  #acceptable start dates
        date.set_month(0)     #initialize day and month variables
        date.set_day(0)
        while date.get_month() < 3 or date.get_month() > 5:   #takes user input and stores it as new variables in the class date
            new_month = int(input("What month do you want to start on?: "))
            date.set_month(new_month)    #sets month
            new_day = int(input("What day do you want to start on?: "))
            set_date(date, new_day)      #sets day
            if date.get_month() < 3 or date.get_month() > 5:   #date entered outside acceptable range
                print("Invalid date! Please try again")
        print("The final date of departure is: ", date.get_year(), "-", date.get_month(), "-", date.get_day())  #returns chosen departure date for the user to see
        print("You must reach the Oregon City by 1847-11-30")   #goal
        print()     #space
        print("Let's begin the journey!")
        print()     #space
        
            
            
          
def visit_store(player, to_visit, milestone_num):
    """This function asks the player how many oxen, how many pounds of food,
    how many bullets, and what miscellaneous supplies they want to buy. 
    Depending on what they buy it will add what they bought to a variable and
    subtract the money they spent from a variable in the main function."""
    to_visit = input("""You are starting at mile: 0.       
There are 2040 miles that you must travel to reach your destination.
Before the start of your trip, you can visit the store and buy supplies: food, oxen, 
bullets and wagon parts. Would you like to visit the store? Y / N""")   #whether they go to the store initially or not
    if to_visit == "y" or to_visit == "Y":    #if they choose to go to the store
        price_increase = milestone_num * 0.25      #the price of items increases the more miles traveled
        bill = 0.0                            #initialize bill
        print("Welcome to the Store!")   
        if player.get_money() == 0.0:         #if the player has no money, they can't buy anything
            return print("You don't have any money to continue shopping at the store.")
        store = open("/Users/timothylenahan/Documents/Spyder_CODE/store_info.txt", "r")
        for line in store:
            print(line)
        store.close()
        print()     #space
        print("Right now you have: $", player.get_money())
        if player.get_money == 0.0:           #if the player has no money, they can't buy anything
            return print("Sorry, you don't have any money to shop at the store.")
        print("""You must spend between $100 to $200 dollars on oxen. There are 2 oxen in a yoke and the    
price of each yoke is $""", ((price_increase * 40.0) + 40.0), ".")                                        #buying oxen(1 yoke has 2 oxen in it)
        yoke_cost = 0.0                       #amount spent on yokes initially
        while yoke_cost < 100.0 or yoke_cost > 200.0:      #the amount spent on yokes has to be between $100 and $200
            yokes = float(input("How many oxen yokes would you like to purchase?: "))  #user input for num of yokes
            yoke_cost = yokes * 40.0    #one yoke costs $40
            if yoke_cost > 200.0:                                #dollars spents has to be in the range or the user is asked to choose a number of yokes again
                print("You have chosen to spend more than $200 on yokes, please choose again.")
            elif yoke_cost < 100.0:
                print("You have chosen to spend less than $100 on yokes, please choose again.")
            elif yoke_cost > player.get_money():                 #if dollars spent is more than the money they have, they have to choose again
                print("Sorry, you don't have enough money to purchase that many yokes.")
                yoke_cost = 0.0
            else:
                new_money = player.get_money() - yoke_cost                #amount of money after buying oxen
                player.set_money(new_money)                               #sets money status in player class
                add_oxen = player.get_oxen() + (int(yokes) * 2)           #gets number of oxen in player class
                player.set_oxen(add_oxen)                                 #updates number of oxen
                bill = bill + yoke_cost                            #updated bill
        if player.get_money() == 0.0:          #if the player has no money, they can't buy anything
            return print("You don't have any money to continue shopping at the store.")
        print()     #space
        print("Your current bill is: ", bill)                      #prints updated bill
    
    
    print("""I recommend at least 200 lbs. per person at the price of $0.5 per pound. Remember the 
wagon cannot hold more than 1000 lbs. of food.""")               #directions for buying food
    food_cost = 1000000.0    #these two values are to help the loop that ensures that the user can't buy more food than they have money for
    food = 1001
    while food_cost > player.get_money() and food > 1000:      #when the player has the option to buy a quantity of food
        food = float(input("How many pounds of food do you wish to purchase?: "))
        food_cost = (0.5 * price_increase) * food                    #food costs 50 cents/pound
        if food_cost > player.get_money():
            print("Sorry, you don't have enough money to purchase that many pounds of food. Pick a different amount.")
        else:                                                #this part of the loop is for updating values
            add_food = player.get_food() + int(food)           #gets the value for amount of food they have
            player.set_food(add_food)                          #updates the amount of food they have
            new_money = player.get_money() - food_cost         #gets amount of money they have minus the money spent on food
            player.set_money(new_money)                        #updates amount of money left
            bill = bill + food_cost                            #updates bill
    print()     #space
    print("Your current bill is: ", bill)            #prints updated bill
            #ask how many lbs. the user wants to buy
            #50cents/lb.
            #recommended 200 lbs/person
            #bill = bill + (food * 0.5)
            #calculate bill(oxen + food)
    print("A box of 20 bullets costs $2.0.")                       #directions for buying bullets
    bullet_cost = 1000000.0       #ensures that loop works when the user has no more money
    while bullet_cost > player.get_money():
        bullets = float(input("How many boxes do you wish to purchase?: "))     #option for user to buy a quantity of bullets
        bullet_cost = bullets * (2.0 * price_increase)               #bullets cost $2
        if bullet_cost > player.get_money():
            print("Sorry, you don't have enough money to purchase that many boxes of bullets. Pick a different amount.")
        else:                                               #part of the loop that updates values
            add_ammo = player.get_ammo() + (20 * int(bullets))  #gets amount of ammo plus the ammo that was just bought
            player.set_ammo(add_ammo)                           #updates amount of ammo
            new_money = player.get_money() - bullet_cost        #gets amount of money they have minus the money spent on bullets                        
            player.set_money(new_money)                         #updates amount of money left
            bill = bill + bullet_cost                           #updates bill
    print()     #space
    print("Your current bill is: ", bill)            #prints updated bill
    if player.get_money() == 0.0:          #if the player has no money, they can't buy anything
        return print("You don't have any money to continue shopping at the store.")                
            #ask how many boxes the user wants to buy
            #$2 for a box of 20 bullets
    #bullets = bullet_box * 20
            #caluclate bill(oxen + food + bullets)
    print("A wagon part (wheels, axels, tongues) costs $10.0.")   #directions for buying wagon parts
    wagon_parts_cost = 1000000.0    #ensures that loop works when the user has no more money
    while wagon_parts_cost > player.get_money():
        wagon_parts = float(input("How many parts do you wish to purchase?: ")) #option for user to buy a quantity of wagon parts
        wagon_parts_cost = wagon_parts * (10.0 * price_increase)     #a part costs $10
        if wagon_parts_cost > player.get_money():
            print("Sorry, you don't have enough money to purchase that many wagon parts. Pick a different amount.")
        else:                                               #part of the loop that updates values
            add_wagon_parts = player.get_mis() + int(wagon_parts) #gets amount of wagon parts plus the parts that were just bought
            player.set_mis(add_wagon_parts)                       #updates amount of wagon parts
            new_money = player.get_money() - wagon_parts_cost     #gets amount of money they have minus the money spent on wagon parts                       
            player.set_money(new_money)                           #updates amount of money left
            bill = bill + wagon_parts_cost                        #updates bill
    if player.get_money() == 0.0:          #if the player has no money, they can't buy anything
        return print("You don't have any money to continue shopping at the store.")
            #a wagon part -> $10
                #ask how many 
            #a medical kit -> $15
                #ask how many
    print("A medical aid kit costs $15.0.")                       #directions for buying wagon parts
    med_kit_cost = 1000000.0        #ensures that loop works when the user has no more money
    while med_kit_cost > player.get_money():
        med_kits = float(input("How many kits do you wish to purchase?: "))     #option for user to buy a quantity of med kits
        med_kit_cost = (15.0 * price_increase) * med_kits              #a kit costs $15
        if med_kit_cost > player.get_money():
            print("Sorry, you don't have enough money to purchase that many medical aid kits.")
        else:                                           #part of the loop that updates values
            add_meds = player.get_meds() + int(med_kits)          #gets amount of wagon parts plus the parts that were just bought
            player.set_meds(add_meds)                             #updates amount of wagon parts
            new_money = player.get_money() - med_kit_cost         #gets amount of money they have minus the money spent on wagon parts   
            player.set_money(new_money)                           #updates amount of money left
            bill = bill + med_kit_cost                            #updates bill
    print()     #space
    print("Your final bill is: ", bill)       #prints updated bill
    print()     #space
    print("You finally have: $", player.get_money(), ". Thanks you for visiting the store")  #amount of money left after shopping
    print()     #space
            #calculate bill(oxen + food + bullets + misc)
        #if attempted purchase exceeds funds, print "insufficienct funds, etc."
    


def misfortunes(player, com1, com2, com3, com4, date):
    """This function is called within the take_turn() function and based on
    a 30% probability generate a random misfortune: traveling member gets sick
    ox dies, thief attack, wagon breaks, or there is bad weather. Based on what
    happens the player will be able to respond to the misfortune."""
    
    misfortune = random.random() * 3 #30% probability
    if misfortune <= 3:                                   #if within 30% probability
        bad_thing = random.randrange(1, 6)             #five possibilities
        if bad_thing == 1:                    #sickness
            print("A member of your party has become sick.")
            who_is_sick = random.randrange(1, 6)                               #five possibilities for who gets sick
            if who_is_sick == 1:                                               #their condition is updated in class companions
                who_is_sick = com1
                if who_is_sick.get_condition() == "dead":                      #if that person is already sick, the sickness afflicts another member of the party
                    who_is_sick = 2                                            
            if who_is_sick == 2:
                who_is_sick = com2
                if who_is_sick.get_condition() == "dead":
                    who_is_sick == 3
            if who_is_sick == 3:
                who_is_sick = com3
                if who_is_sick.get_condition() == "dead":
                    who_is_sick = 4
            if who_is_sick == 4:
                who_is_sick = com4
                if who_is_sick.get_condition() == "dead":
                    who_is_sick = 5
            if who_is_sick == 5:
                who_is_sick = player
            #if person already sick, they die
            #resting or hunting will bring person back to full health
            #if not resting, recovery time is 5 days
            #if party has medical kit, recovery time is 2 days
            if who_is_sick.get_condition() == "sick":
                if who_is_sick == player:
                    print("You contracted a second illness and died.")         #if the player gets sick a second time, they die 
                    who_is_sick.set_condition("dead")
                else:
                    print(who_is_sick.get_name(), "contracted a second illness and died.") #if another member gets sick a second time, they die
                    who_is_sick.set_condition("dead")
            
            
            else:
                sickness = random.randrange(1, 7)     #randomly generates which disease the person contracts and updates their status to "sick"
                if sickness == 1:
                    if who_is_sick == player:
                        print("You have contracted typhoid")
                        who_is_sick.set_condition("sick")
                    else:
                        print(who_is_sick.get_name(), "has contracted typhoid.")
                        who_is_sick.set_condition("sick")
                elif sickness == 2:
                    if who_is_sick == player:
                        print("You have contracted cholera")
                        who_is_sick.set_condition("sick")
                    else:
                        print(who_is_sick.get_name(), "has contracted cholera.")
                        who_is_sick.set_condition("sick")
                elif sickness == 3:
                    if who_is_sick == player:
                        print("You have contracted diarrhea")
                        who_is_sick.set_condition("sick")
                    else:
                        print(who_is_sick.get_name(), "has contracted diarrhea.")
                        who_is_sick.set_condition("sick")
                elif sickness == 4:
                    if who_is_sick == player:
                        print("You have contracted measles")
                        who_is_sick.set_condition("sick")
                    else:
                        print(who_is_sick.get_name(), "has contracted measles.")
                        who_is_sick.set_condition("sick")
                elif sickness == 5:
                    if who_is_sick == player:
                        print("You have contracted dysentery")
                        who_is_sick.set_condition("sick")
                    else:
                        print(who_is_sick.get_name(), "has contracted dysentery.")
                        who_is_sick.set_condition("sick")
                elif sickness == 6:
                    if who_is_sick == player:
                        print("You have contracted a fever")
                        who_is_sick.set_condition("sick")
                    else:
                        print(who_is_sick.get_name(), "has contracted a fever.")
                        who_is_sick.set_condition("sick")
        
        elif bad_thing == 2:                    #oxen death
            print("One of your oxen has died.")
            new_oxen = player.get_oxen() - 1
            player.set_oxen(new_oxen)
            #if all oxen die, party cannot continue(party dies)
        
        elif bad_thing == 3:                    #thievery
            print("A thief has attacked and stolen some of your food supply.") 
            stolen_food = random.randrange(10, 26)    #a random amount of food between 10 and 25 pounds is stolen
            new_food = player.get_food() - stolen_food            #gets amount of food they have minus food that is lost
            player.set_food(new_food)                             #updates amount of food
            #steals 10-25 lbs.
        
        elif bad_thing == 4:                    #wagon has broken
            if player.get_mis() > 0:
                print("Your wagon has broken you must wait one day while you repair it.")
                set_date(date, 1)                 #adds a day to time passed
                new_wagon_parts = player.get_mis() - 1           #gets number of wagon parts minus the one that is used
                player.set_mis(new_wagon_parts)                  #updates number of wagon parts
                new_food = player.get_food() - player.get_food_con()           #gets amount of food minus food for all people for 1 day
                player.set_food(new_food)                                      #updates amount of food
                if player.get_condition() == "sick":             #if the user is sick, they are now well
                    player.set_condition("healthy")
                if com1.get_condition() == "sick" or com2.get_condition() == "sick" or com3.get_condition() == "sick" or com4.get_condition() == "sick":
                    com1.set_condition("healthy")                #if a party member is sick, they are now well
                    com2.set_condition("healthy")
                    com3.set_condition("healthy")
                    com4.set_condition("healthy")
            else:
                player.set_wagon("broken")                 #the wagon cannot be fixed
                #the party cannot continue and the game is lost
            
        elif bad_thing == 5:                    #bad weather
            weather_type = random.randrange(0, 5)                #randomly picks one of 4 types of bad weather
            #food goes down at daily rate
            #health improves
            if weather_type == 0:
                print("There are heavy rains. You have to wait for 1 day.")    #people who are sick become well, food goes down at daily rate and is updated
                set_date(date, 1)
                new_food = player.get_food() - player.get_food_con()
                player.set_food(new_food)
                if player.get_condition() == "sick":
                    player.set_condition("healthy")
                if com1.get_condition() == "sick" or com2.get_condition() == "sick" or com3.get_condition() == "sick" or com4.get_condition() == "sick":
                    com1.set_condition("healthy")
                    com2.set_condition("healthy")
                    com3.set_condition("healthy")
                    com4.set_condition("healthy")
            
            if weather_type == 1:
                print("There is a storm. You have to wait for 3 days.")        #people who are sick become well, food goes down at daily rate and is updated
                set_date(date, 3)
                new_food = player.get_food() - (player.get_food_con() * 3)
                player.set_food(new_food)
                if player.get_condition() == "sick":
                    player.set_condition("healthy")
                if com1.get_condition() == "sick" or com2.get_condition() == "sick" or com3.get_condition() == "sick" or com4.get_condition() == "sick":
                    com1.set_condition("healthy")
                    com2.set_condition("healthy")
                    com3.set_condition("healthy")
                    com4.set_condition("healthy")
                
            if weather_type == 2:
                print("There is hail. You have to wait for 1 day.")            #people who are sick become well, food goes down at daily rate and is updated
                set_date(date, 1)
                new_food = player.get_food() - player.get_food_con()
                player.set_food(new_food)
                if player.get_condition() == "sick":
                    player.set_condition("healthy")
                if com1.get_condition() == "sick" or com2.get_condition() == "sick" or com3.get_condition() == "sick" or com4.get_condition() == "sick":
                    com1.set_condition("healthy")
                    com2.set_condition("healthy")
                    com3.set_condition("healthy")
                    com4.set_condition("healthy")
                
            if weather_type == 3:
                print("There is a blizzard. You have to wait for 3 days.")     #people who are sick become well, food goes down at daily rate and is updated
                set_date(date, 3)
                new_food = player.get_food() - (player.get_food_con() * 3)
                player.set_food(new_food)
                if player.get_condition() == "sick":
                    player.set_condition("healthy")
                if com1.get_condition() == "sick" or com2.get_condition() == "sick" or com3.get_condition() == "sick" or com4.get_condition() == "sick":
                    com1.set_condition("healthy")
                    com2.set_condition("healthy")
                    com3.set_condition("healthy")
                    com4.set_condition("healthy")
                    
            if weather_type == 4:
                print("There is a tornado. You have to wait for 5 days.")      #people who are sick become well, food goes down at daily rate and is updated
                set_date(date, 5)
                new_food = player.get_food() - (player.get_food_con() * 5)
                player.set_food(new_food)
                if player.get_condition() == "sick":
                    player.set_condition("healthy")
                if com1.get_condition() == "sick" or com2.get_condition() == "sick" or com3.get_condition() == "sick" or com4.get_condition() == "sick":
                    com1.set_condition("healthy")
                    com2.set_condition("healthy")
                    com3.set_condition("healthy")
                    com4.set_condition("healthy")
    
    
def raider_attack(player):
    """This function is called after the misfortunes function in the take_turn 
    function. Based on a probability which decreases as the distance traveled
    increases, the player has a chance to be attacked by raiders. If the player
    and their party is attack they have a choice to run, attack, or surrender."""
    prob_of_attack = ((((player.get_miles() / 100 - 4) ** 2) + 72) / (((player.get_miles() / 100 - 4) ** 2) + 12)) - 1      #probability of raider attack formula
    attack = random.random() * 10          #wheather raiders attack
    if attack <= prob_of_attack:
        run = int(input("You are being attacked by raiders, do you want to run(1), fight back(2), or surrender(3)? "))    #user chooses which option to take
        if run == 1:
            print("In your panic to get away you left behind 1 ox, 10 lbs of food, and 1 wagon part.")    #you lose a bunch of items, all are updated in the classes
            new_oxen = player.get_oxen() - 1
            player.set_oxen(new_oxen)
            new_food = player.get_food() - 10
            player.set_food(new_food)
            new_mis = player.get_mis() - 1
            player.set_mis(new_mis)
        elif run == 2:                                                         
            win_fight = puzzle()                                               #the user must win the game to successfully fight the raiders off
            if win_fight:
                print("Nice!!! You fought the raiders back and gained 50 lbs of food and 50 bullets!!!")   #if they win, new stuff is aquired and items are updated in the classes
                new_food = player.get_food() + 50
                player.set_food(new_food)
                new_ammo = player.get_ammo() + 50
                player.set_ammo(new_ammo)
            else:
                print("Oh NO!!! You lost to the raiders and they stole a quarter of your cash after you used 50 bullets trying to fight them.") #the raiders win and take a bunch of stuff, all is updated
                new_money = player.get_money() - (player.get_money() / 4)
                player.set_money(new_money)
                new_ammo = player.get_ammo() - 50
                player.set_ammo(new_ammo)
        elif run == 3:                                                         #the user gives money to raiders to get them to leave, money is updated
            print("By surrendering you gave up a quarter of your cash so the raiders would leave you alone.")
            new_money = player.get_money() - (player.get_money() / 4)
            player.set_money(new_money)
            
            
def milestones(player, com1, com2, com3, com4, date, milestone_num, mile_stones):
    """This function will be called after the raider_attack function in the 
    take_turn function. This will compare the distance traveled to the next
    milestone. If the distance traveled is the exact distance or further than 
    the nearest milestone they are at that milestone. If not this function 
    ends. When they reach a milestone they will have a choice to rest or cross
    the river, at a river, or rest and go to the store, at a fort."""
    which_milestone = milestone_num
    current_milestone = mile_stones.readline()
    if which_milestone in [0, 1, 2, 3, 4, 5, 6, 7]:
        landmark_mile = mile_stones.readline()
        miles_to_landmark = int(landmark_mile[1] + landmark_mile[2] + landmark_mile[3])
    elif which_milestone in [8, 9, 10, 11, 12, 13, 14]:
        landmark_mile = mile_stones.readline()
        miles_to_landmark = int(landmark_mile[1] + landmark_mile[2] + landmark_mile[3] + landmark_mile[4])

    if player.get_miles() >= miles_to_landmark:
        print("You have come to", current_milestone)
        
        if which_milestone in [2, 4, 7, 10, 12, 14]:
            has_continued = False
            while has_continued == False:
                current_option = 1
                while current_option == 1:
                    rest = input("Do you want to rest? Y/N")
                    if rest == "y" or rest == "Y":
                        print("You can rest again if you like.")
                        rest_t = random.randrange(1,3)
                        set_date(date, rest_t)
                        used_food = rest_t * (com1.get_num_of_com() + 1) * player.get_food_con()
                        new_food = player.get_food() - used_food
                        player.set_food(new_food)
                        if player.get_condition() == "sick":
                            player.set_condition("healthy")
                        if com1.get_condition() == "sick" or com2.get_condition() == "sick" or com3.get_condition() == "sick" or com4.get_condition() == "sick":
                            com1.set_condition("healthy")
                            com2.set_condition("healthy")
                            com3.set_condition("healthy")
                            com4.set_condition("healthy")
                    elif rest == "n" or rest == "N":
                        current_option = 2
                
                while current_option == 2:
                    to_visit = input("Would you like to visit the store? Y / N")
                    if to_visit == "y" or to_visit == "Y":
                        visit_store(player, True, which_milestone)
                        print("You can visit the store again if you like.")
                    elif to_visit == "n" or to_visit == "N":
                        current_option = 3
    
                while current_option == 3:
                    cont = input("Do you want to continue? Y/N")
                    if cont == "y" or cont == "Y":
                        set_date(date, 14)
                        used_food = 14 * player.get_food_con() * (com1.get_num_of_com() + 1)
                        new_food = player.get_food() - used_food
                        player.set_food(new_food)
                        m_traveled = random.randrange(70, 140)
                        new_m_traveled = m_traveled + player.get_miles()
                        player.set_miles(new_m_traveled)
                        current_option = 0
                        has_continued = True
                        which_milestone = int(which_milestone + 1)
                        current_milestone = mile_stones.readline()
                        if which_milestone in [0, 1, 2, 3, 4, 5, 6, 7]:
                            landmark_mile = mile_stones.readline()
                            miles_to_landmark = int(landmark_mile[1] + landmark_mile[2] + landmark_mile[3])
                        elif which_milestone in [8, 9, 10, 11, 12, 13, 14]:
                            landmark_mile = mile_stones.readline()
                            miles_to_landmark = int(landmark_mile[1] + landmark_mile[2] + landmark_mile[3] + landmark_mile[4])
                    elif cont == "n" or cont == "N":
                        current_option = 1
            
        elif which_milestone in [0, 1, 3, 5, 6, 8, 9, 11, 13]:
            has_continued = False
            while has_continued == False:
                if which_milestone in [0, 1, 8, 11]:
                    current_option = 1
                    while current_option == 1:
                        rest = input("Do you want to rest? Y/N")
                        if rest == "y" or rest == "Y":
                            print("You can rest again if you like.")
                            rest_t = random.randrange(1,3)
                            set_date(date, rest_t)
                            used_food = rest_t * (com1.get_num_of_com() + 1) * player.get_food_con()
                            new_food = player.get_food() - used_food
                            player.set_food(new_food)
                            if player.get_condition() == "sick":
                                player.set_condition("healthy")
                            if com1.get_condition() == "sick" or com2.get_condition() == "sick" or com3.get_condition() == "sick" or com4.get_condition() == "sick":
                                com1.set_condition("healthy")
                                com2.set_condition("healthy")
                                com3.set_condition("healthy")
                                com4.set_condition("healthy")
                        elif rest == "n" or rest == "N":
                            current_option = 2
                        
                    while current_option == 2:
                        cont = input("Do you want to continue? Y/N")
                        if cont == "y" or cont == "Y":
                            print("Since this river is deeper than 3ft. you had to pay $5 before you continued.")
                            new_money = player.get_money() - 5
                            player.set_money(new_money)
                            set_date(date, 14)
                            used_food = 14 * player.get_food_con() * (com1.get_num_of_com() + 1)
                            new_food = player.get_food() - used_food
                            player.set_food(new_food)
                            m_traveled = random.randrange(70, 140)
                            new_m_traveled = m_traveled + player.get_miles()
                            player.set_miles(new_m_traveled)
                            current_option = 0
                            has_continued = True
                            which_milestone = int(which_milestone + 1)
                            current_milestone = mile_stones.readline()
                            if which_milestone in [0, 1, 2, 3, 4, 5, 6, 7]:
                                landmark_mile = mile_stones.readline()
                                miles_to_landmark = int(landmark_mile[1] + landmark_mile[2] + landmark_mile[3])
                            elif which_milestone in [8, 9, 10, 11, 12, 13, 14]:
                                landmark_mile = mile_stones.readline()
                                miles_to_landmark = int(landmark_mile[1] + landmark_mile[2] + landmark_mile[3] + landmark_mile[4])
                        elif cont == "n" or cont == "N":
                            current_option = 1
                
                elif which_milestone in [3, 5, 6, 9, 11, 13]:
                    current_option = 1
                    while current_option == 1:
                        rest = input("Do you want to rest? Y/N")
                        if rest == "y" or rest == "Y":
                            print("You can rest again if you like.")
                            rest_t = random.randrange(1,3)
                            set_date(date, rest_t)
                            used_food = rest_t * (com1.get_num_of_com() + 1) * player.get_food_con()
                            new_food = player.get_food() - used_food
                            player.set_food(new_food)
                            if player.get_condition() == "sick":
                                player.set_condition("healthy")
                            if com1.get_condition() == "sick" or com2.get_condition() == "sick" or com3.get_condition() == "sick" or com4.get_condition() == "sick":
                                com1.set_condition("healthy")
                                com2.set_condition("healthy")
                                com3.set_condition("healthy")
                                com4.set_condition("healthy")
                        elif rest == "n" or rest == "N":
                            current_option = 2
                        
                    while current_option == 2:
                        cont = input("Do you want to continue? Y/N")
                        if cont == "y" or cont == "Y":
                            set_date(date, 14)
                            used_food = 14 * player.get_food_con() * (com1.get_num_of_com() + 1)
                            new_food = player.get_food() - used_food
                            player.set_food(new_food)
                            m_traveled = random.randrange(70, 140)
                            new_m_traveled = m_traveled + player.get_miles()
                            player.set_miles(new_m_traveled)
                            current_option = 0
                            has_continued = True
                            which_milestone = int(which_milestone + 1)
                            current_milestone = mile_stones.readline()
                            if which_milestone in [0, 1, 2, 3, 4, 5, 6, 7]:
                                landmark_mile = mile_stones.readline()
                                miles_to_landmark = int(landmark_mile[1] + landmark_mile[2] + landmark_mile[3])
                            elif which_milestone in [8, 9, 10, 11, 12, 13, 14]:
                                landmark_mile = mile_stones.readline()
                                miles_to_landmark = int(landmark_mile[1] + landmark_mile[2] + landmark_mile[3] + landmark_mile[4])
                        elif cont == "n" or cont == "N":
                            current_option = 1
    return [which_milestone, miles_to_landmark]

def set_date(date, days):
    """This function will keep track of the date and the number of days that the journey has been going on."""
    num_days = date.get_day() + days             #gets number of days of the journey
    date.set_day(num_days)                       #updates days
    if date.get_day() > 30 and (date.get_month() in [4, 6, 9, 11]): #dates for months with 30 days
        new_month = date.get_month() + 1
        date.set_month(new_month)
        new_day = date.get_day() - 30
        date.set_day(new_day)
    elif date.get_day() > 31 and (date.get_month() in [3, 5, 7, 8, 10]): #dates for months with 31 days
        new_month = date.get_month() + 1
        date.set_month(new_month)
        new_day = date.get_day() - 31
        date.set_day(new_day)


def puzzle():
    print("Pick a number between 1 and 10. If it is the correct number you win this event. You have 3 tries, good luck!")
    answer = random.randrange(1, 10)
    guess_num = 0
    while guess_num < 3:
        guess = input("Guess a number between 1 and 10. ")
        if int(guess) == answer:
            return True
        elif int(guess) != answer and guess_num == 2:
            return False
        else:
            guess_num = guess_num + 1


def take_turn(player, com1, com2, com3, com4, date, next_milestone):
    """This function displays the player's stats, gives them the option to 
    rest, continue, hunt, or quit"""
    print("The date is ", date.get_month(), "/", date.get_day(), "/", date.get_year())
    print("You have traveled ", player.get_miles())
    print("The next landmark is ", (next_milestone - player.get_miles()), " miles away.")
    print("You have ", player.get_food(), " pounds of food.")
    print("You have ", player.get_ammo(), " bullets.")
    print("You have ", player.get_money(), " dollars.")
    
    player_choice = 1
    while player_choice != 0:
        while player_choice == 1:    #resting
            rest = input("Do you want to rest? Y/N")
            if rest == "y" or rest == "Y":
                rest_t = random.randrange(1,3)
                set_date(date, rest_t)
                used_food = rest_t * (com1.get_num_of_com() + 1) * player.get_food_con()
                new_food = player.get_food() - used_food
                player.set_food(new_food)
                if player.get_condition() == "sick":
                    player.set_condition("healthy")
                if com1.get_condition() == "sick" or com2.get_condition() == "sick" or com3.get_condition() == "sick" or com4.get_condition() == "sick":
                    com1.set_condition("healthy")
                    com2.set_condition("healthy")
                    com3.set_condition("healthy")
                    com4.set_condition("healthy")
                player_choice = 0
            elif rest == "n" or rest == "N":
                player_choice = 2
    
        while player_choice == 2:   #continuing
            cont = input("Do you want to continue? Y/N")
            if cont == "y" or cont == "Y":
                set_date(date, 14)
                used_food = 14 * player.get_food_con() * (com1.get_num_of_com() + 1)
                new_food = player.get_food() - used_food
                player.set_food(new_food)
                m_traveled = random.randrange(70, 140)
                new_m_traveled = m_traveled + player.get_miles()
                player.set_miles(new_m_traveled)
                player_choice = 0
            elif cont == "n" or cont == "N":
                player_choice = 3
    
        while player_choice == 3:   #hunting
            hunt = input("Do you want to hunt? Y/N")
            if hunt == "y" or hunt == "Y":
                #days of hunting added to date
                set_date(date, 1)
            
                #chances of encountering different animals
                animals1 = random.randrange(1, 100) 
                animals2 = random.randrange(1, 100)
            
                #recovery
                if player.get_condition() == "sick":
                    player.set_condition("healthy")
                if com1.get_condition() == "sick" or com2.get_condition() == "sick" or com3.get_condition() == "sick" or com4.get_condition() == "sick":
                    com1.set_condition("healthy")
                    com2.set_condition("healthy")
                    com3.set_condition("healthy")
                    com4.set_condition("healthy")
            
                #hunting
                if animals1 >= 1 and animals1 <= 50:
                    to_hunt = input("YOU GOT LUCKY! YOU ENCOUNTERED A RABBIT! DO YOU WANT TO HUNT? Y/N")
                    if to_hunt == "y" or to_hunt == "Y":
                        if player.get_ammo() < 10:
                            print("You don't have enough bullets! Your hunt was unsuccessful.")
                        elif player.get_ammo() > 10:
                            hunt_result = puzzle()
                            if hunt_result == True:
                                print("Your hunt was a success!")
                                new_food = player.get_food() + 2
                                player.set_food(new_food)
                                new_ammo = player.get_ammo() - 10
                                player.set_ammo(new_ammo)
                
                if animals1 >= 51 and animals1 <= 75:
                    to_hunt = input("YOU GOT LUCKY! YOU ENCOUNTERED A FOX! DO YOU WANT TO HUNT? Y/N")
                    if to_hunt == "y" or to_hunt == "Y":
                        if player.get_ammo() < 10:
                            print("You don't have enough bullets! Your hunt was unsuccessful.")
                        elif player.get_ammo() > 10:
                            hunt_result = puzzle()
                            if hunt_result == True:
                                print("Your hunt was a success!")
                                new_food = player.get_food() + 5
                                player.set_food(new_food)
                                new_ammo = player.get_ammo() - 8
                                player.set_ammo(new_ammo)
            
                if animals2 >= 1  and animals2 <= 20:
                    to_hunt = input("YOU GOT LUCKY! YOU ENCOUNTERED A DEER! DO YOU WANT TO HUNT? Y/N")
                    if to_hunt == "y" or to_hunt == "Y":
                        if player.get_ammo() < 10:
                            print("You don't have enough bullets! Your hunt was unsuccessful.")
                        elif player.get_ammo() > 10:
                            hunt_result = puzzle()
                            if hunt_result == True:
                                print("Your hunt was a success!")
                                deer_meat = random.randrange(35, 60)
                                new_food = player.get_food() + deer_meat
                                player.set_food(new_food)
                                new_ammo = player.get_ammo() - 5
                                player.set_ammo(new_ammo)
            
                if animals2 >= 21 and animals2 <= 30:
                    to_hunt = input("YOU GOT LUCKY! YOU ENCOUNTERED A BEAR! DO YOU WANT TO HUNT? Y/N")
                    if to_hunt == "y" or to_hunt == "Y":
                        if player.get_ammo() < 10:
                            print("You don't have enough bullets! Your hunt was unsuccessful.")
                        elif player.get_ammo() > 10:
                            hunt_result = puzzle()
                            if hunt_result == True:
                                print("Your hunt was a success!")
                                bear_meat = random.randrange(100, 300)
                                new_food = player.get_food() + bear_meat
                                player.set_food(new_food)
                                new_ammo = player.get_ammo() - 10
            
                if animals2 >= 31 and animals2 <= 35:
                    to_hunt = input("YOU GOT LUCKY! YOU ENCOUNTERED A MOOSE! DO YOU WANT TO HUNT? Y/N")
                    if to_hunt == "y" or to_hunt == "Y":
                        if player.get_ammo() < 10:
                            print("You don't have enough bullets! Your hunt was unsuccessful.")
                        elif player.get_ammo() > 10:
                            hunt_result = puzzle()
                            if hunt_result == True:
                                print("Your hunt was a success!")
                                bear_meat = random.randrange(300, 700)
                                new_food = player.get_food() + bear_meat
                                player.set_food(new_food)
                                new_ammo = player.get_ammo() - 10
                                player.set_ammo(new_ammo)
                
                food_consumption = 0              #sets amount of food consumed by each person, each day
                while food_consumption == 0:
                    food_consumption = input("How well do you want to eat? (1) Poorly: 2 lbs per person, per day; (2) Moderately: 3 lbs per person, per day; or (3) Well: 5 lbs per person, per day. ")
                    if int(food_consumption) == 1:
                        player.set_food_con(2)
                        food_consumption = 1
                    elif food_consumption == 2:
                        player.set_food_con(3)
                        food_consumption = 1
                    elif food_consumption == (3):
                        player.set_food(5)
                        food_consumption = 1
                player_choice = 0
        
    

def game_end(player, date):
    """This function will take the player's current_food, current_oxen, 
    wagon_broken, and player_alive values. These values will be compared
    to the game end values(criteria) and if any of them match the game will
    end with them winning or Game Over."""
    if player.get_food() <= 0:
        print("""You don't have any food left to continue your journey.
You lose.
GAME OVER""")
        return True
        #stop game
    
    elif player.get_oxen() <= 0:
        print("""You don't have any oxen left to pull your wagon.
You lose.
GAME OVER""")
        return True
        #stop game
        
    elif player.get_wagon() == True:
        print("""You don't have a wagon to continue traveling.
You lose.
GAME OVER""")
        return True
        #stop game
        
    elif player.get_condition() == "dead":
        print("""All of the members of your party died.
You lose.
GAME OVER""")
        return True
        #stop game
        
    elif player.get_miles() == 2040:
        print("""You survived... IMPRESSIVE!!! Welcome to Oregon! 
YOU WIN!!!""")
        return True
        #stop game
    
    elif date.get_month() > 11:
        print("""You didn't reach Oregon city in the alotted time.
You lose.
GAME OVER""")
        return True
    else:
        return False
    
    
    


if __name__ == "__main__":
    #milestones = open("milestones.txt", "r")
    #current_ms = milestones.readline()
    #game_end_m = 2040
    #game_end_d = tuple(11, 30, 1847)
    #player_name = ""
    #companion_names = []
    #miles_traveled = int
    #money = 1600
    #c_date = list(3, 28, 1847)
    #current_oxen = int
    #current_food = int
    #current_ammo = int
    #current_mis = int
    #current_meds = int
    #is_player_alive = boolean
    mile_stones = open("/Users/timothylenahan/Documents/Spyder_CODE/milestones.txt", "r")
    milestone_num = 0
    next_milestone = 102
    player = trailblazer.Trailblazer("name", 0, 1400, 0, 0, 0, 0, 0, 0, "healthy", 3)
    
    date = date.Date(3, 28, 1847)
    
    com1 = companions.companion("name", "healthy", 4)
    com2 = companions.companion("name", "healthy", 0)
    com3 = companions.companion("name", "healthy", 0)
    com4 = companions.companion("name", "healthy", 0)
    
    
    
    
    #1 initial_conditions
    to_visit = initial_conditions(player, date, com1, com2, com3, com4)
    #1a-name = input("What is your name?")
    #1b-companions = []
    #1c-companions:
        #for number of companion(4) input("What is name of companion")
        #add_name_to_list
        #return list of companions
    #1c- s_date = input("Will you you start on March 28, 1847?")
        #if yes, start date is default
        #if no, create a loop to input desire date in tuple between (3, 1, 1847) and (5, 1, 1847)
        #return value of start date    
    
    #2 visit_store
    visit_store(player, to_visit, milestone_num)
    start_date(date)
        #2a - stor_info = open(store_info.txt, "r")
        #o_price
        #f_price
        #a_price
        #m_price
        #oxen = int
        #food = int
        #ammo = int
        #mis = int
        #current bill = ("", int)
        
        #stor_info.readlines
        #how_many_oxen(input):
            
        #how_much_food(input):
            
        #how_many_bullets(input):
            
        #what_mis_supplies(input):
        
        #update_prices
    GAME_OVER = False    
    while GAME_OVER == False:
    #3 take_turn(player)
        take_turn(player, com1, com2, com3, com4, date, next_milestone)
        #print("status_update")
        #want_to_rest():
        
        #continue():
            #misfortune()
        
        #hunt():
            #puzzle()
            #misfortune()
        misfortunes(player, com1, com2, com3, com4, date)    
        #quit:
        
        #3a - misfortunes():
            #traveler_sick:
            #ox_dies:
            #wagon_breaks:
            #bad_weather:
        
        #3b - raider_attack():
        raider_attack(player)
                #fight = Y or N:
                    #if Y:
                        #number = input("guess number between 1-10 ")
                        #n_to_guess = random.randrange(1, 11)
                        #n_of_tries = 0
                        #while n_of_tries <= 3:
                            #if number == n_to_guess:
                                #player wins fight
                            #elif: number != n_to_guess:
                                #n_of_tries = n_of_tries + 1
        milestone = milestones(player, com1, com2, com3, com4, date, milestone_num, mile_stones)
        next_milestone = milestone[1]
        milestone_num = milestone[0]
        #3c - milestones(miles_traveled):
            #if miles_traveled == milestone:
                    #is the milestone a river
                        #"do you want to rest(as long as you want)?"
                        #"do you want to cross the river?"
                            #is the river deeper than 3 ft
                    #is the milestone a fort
                        #"do you want to rest?"
                        #"do you want to visit the store?"
                        #"do you want ot continue?"
            #milestones.readline()
                        
                
        GAME_OVER = game_end(player, date)
    #8 game_end(current_food, current_oxen, wagon_broken, player_alive, player_miles):
        #if game_end conditions met
        
        

