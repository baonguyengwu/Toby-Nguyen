#Created on Thu Nov 22 23:09:54 2018

#@author: bnguy
#Peer evaluation:
#Elmi Salad- coordinating schedules for meetings, providing an agenda, and acquiring resources for the team. Worked with creating READMEFILE and instructions to play the game. 
#Dieter Linder- wrote required reports, leading presentations, and answering all questions from classmates during the presentation. Worked creating the flowchart for our game and the PowerPoint .
#Bao Chia Nguyen- developed the algorithms, writing, and certifying the code. Worked with creating the program for our game

#import random module in advance to use the module
import random
#set the location as the headquarter Washington DC
location = 'Washington DC'
#set the times/turns at 30
times = 15
int(times)
#set the amount of car in the garage as 0
carsale = 0
int(carsale)
#set the amount of Bugatti in the garage as 0
amount_of_BGT = 0
int(amount_of_BGT)
#set the amount of Nissan GTR in the garage as 0
amount_of_NS = 0
int(amount_of_NS)
#set the amount of Mercedes S-Class in the garage as 0
amount_of_MC = 0
int(amount_of_MC)
#set the amount of Corvette Sting gray in the garage as 0
amount_of_CV = 0
int(amount_of_CV)
#set the amount of Lexus RCF in the garage as 0
amount_of_LX = 0
int(amount_of_LX)
#set the amount of Mustang GT in the garage as 0
amount_of_MT = 0
int(amount_of_MT)
#set the initial money for every player as 500,000
money = 500000
int(money)
#set up the random price for each category cars
bugattiPrice = random.randrange(95000, 105999)

nissanPrice = random.randrange(81000, 90999)

mercedesPrice = random.randrange(71000, 80999)

corvettePrice = random.randrange(61000, 70999)

lexusPrice = random.randrange(51000, 60999)

mustangPrice = random.randrange(49000, 50999)
#set the challenge_encounter as 0 or Flase
challenge_encounter = 0
#the buy car function is about buy car where it will plus up the number of car in garage, and  subtract the budget by the car player buy
def buyCar(money, carsale, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT):
#use the handling error(try/except) to eliminate error in the input for the category
    try:
        item = input("""What type of car you want to buy? 
Choices: (B)ugatti, (N)issan GTR, (Mer)cedes S-Class, (C)orvette, (L)exus, (Mus)tang \n\n""")
        #if player hit bugatti or b it will assign to the bugatti category
        if item.lower() in ('bugatti', 'b'):
            #using the divide quotitent as the way to know how many car player can afford
            if money // bugattiPrice > 0:
                quantity = money//bugattiPrice#the quotitent division
                print("You can afford", quantity, "quantity of Bugatti.")
                #also using the handling error(try/except) to eliminate the error in the input for the amount of car
                try:
                    amountBuy = int(input("How many do you want to buy? \n"))
                    #if the budget money is less than the price(also the amount) player wish to buy return no money, press any key to return to the main page
                    if money < (amountBuy * bugattiPrice):
                        print("You do not have enough money!")
                        input("Press enter to return to the main page.")
                        amountBuy = 0
                #the except to show that the input is wrong
                except:
                    print("You must enter in a whole number!")
                    amountBuy = 0
                    int(amountBuy)
                #here is the formula to calculate the budget, amount of total car in garage, and amount of bugatti.
                money = money - (amountBuy * bugattiPrice)
                carsale = carsale + amountBuy
                amount_of_BGT += amountBuy
            #if the money can not afford for a bugatti come next time
            else:
                print("You do not have enough money to afford a Bugatti.")
                print("Please come next time!!!")
#all the methods and formula in the buyCar function will be applied as the same
#Only change the name of category and the variable assign with the category
                
        #if player hit nissan GTR or n it will assign to the nissan category
        elif item.lower() in ('nissan GTR', 'n'):
            if money // nissanPrice > 0:#using the divide quotitent as the way to know how many car player can afford
                quantity = money//nissanPrice
                print("You can afford", quantity, "quantity of Nissan GTR.")
                #also using the handling error(try/except) to eliminate the error in the input for the amount of car
                try:
                    amountBuy = int(input("How many do you want to buy? \n"))
                     #if the budget money is less than the price(also the amount) player wish to buy return no money, press any key to return to the main page
                    if money < (amountBuy * nissanPrice):
                        print("You do not have enough money!")
                        input("Press enter to return to the main page.")
                        amountBuy = 0
                #the except to show that the input is wrong
                except:
                    print("You must enter in a whole number!")
                    amountBuy = 0
                    int(amountBuy)
                #here is the formula to calculate the budget, amount of total car in garage, and amount of nissan
                money = money - (amountBuy * nissanPrice)
                carsale = carsale + amountBuy
                amount_of_NS += amountBuy
            #if the money can not afford for a bugatti come next time
            else:
                print("You do not have enough money to afford a Nissan GTR.")
                print("Please come next time!!!")
        #if player hit mercedes s-class or mer it will assign to the mercedes category
        elif item.lower() in ('Mercedes S-Class', 'mer'):
            if money // mercedesPrice > 0:#using the divide quotitent as the way to know how many car player can afford
                quantity = money//mercedesPrice
                print("You can afford", quantity, "quantity of Mercedes S-class.")
                #also using the handling error(try/except) to eliminate the error in the input for the amount of car
                try:
                    amountBuy = int(input("How many do you want to buy? \n"))
                    #if the budget money is less than the price(also the amount) player wish to buy return no money, press any key to return to the main page
                    if money < (amountBuy * mercedesPrice):
                        print("You do not have enough money!")
                        input("Press enter to return to the main page.")
                        amountBuy = 0
                #the except to show that the input is wrong
                except:
                    print("You must enter in a whole number!")
                    amountBuy = 0
                    int(amountBuy)
                #here is the formula to calculate the budget, amount of total car in garage, and amount of mercedes
                money = money - (amountBuy * mercedesPrice)
                carsale = carsale + amountBuy
                amount_of_MC += amountBuy
            #if the money can not afford for a bugatti come next time
            else:
                print("You do not have enough money to afford a Mercedes S-Class.")
                print("Please come next time!!!")
        #if player hit corvette or c it will assign to the corvette category
        elif item.lower() in ('Corvette', 'c'):
            if money // corvettePrice > 0:#using the divide quotitent as the way to know how many car player can afford
                quantity = money//corvettePrice
                print("You can afford", quantity, "quantity of Corvette Sting gray.")
                #also using the handling error(try/except) to eliminate the error in the input for the amount of car
                try:
                    amountBuy = int(input("How many do you want to buy? \n"))
                    #if the budget money is less than the price(also the amount) player wish to buy return no money, press any key to return to the main page
                    if money < (amountBuy * corvettePrice):
                        print("You do not have enough money!")
                        input("Press enter to return to the main page.")
                        amountBuy = 0
                #the except to show that the input is wrong
                except:
                    print("You must enter in a whole number!")
                    amountBuy = 0
                    int(amountBuy)
                #here is the formula to calculate the budget, amount of total car in garage, and amount of corvette
                money = money - (amountBuy * corvettePrice)
                carsale = carsale + amountBuy
                amount_of_CV += amountBuy
            #if the money can not afford for a bugatti come next time
            else:
                print("You do not have enough money to afford a Corvette Sting gray.")
                print("Please come next time!!!")
        #if player hit lexus or l it will assign to the lexus category
        elif item.lower() in ('Lexus RCF', 'l'):
            if money // lexusPrice > 0:#using the divide quotitent as the way to know how many car player can afford
                quantity = money//lexusPrice
                print("You can afford", quantity, "quantity of Lexus RCF.")
                #also using the handling error(try/except) to eliminate the error in the input for the amount of car
                try:
                    amountBuy = int(input("How many do you want to buy? \n"))
                    #if the budget money is less than the price(also the amount) player wish to buy return no money, press any key to return to the main page
                    if money < (amountBuy * lexusPrice):
                        print("You do not have enough money!")
                        input("Press enter to return to the main page.")
                        amountBuy = 0
                #the except to show that the input is wrong
                except:
                    print("You must enter in a whole number!")
                    amountBuy = 0
                    int(amountBuy)
                #here is the formula to calculate the budget, amount of total car in garage, and amount of lexus
                money = money - (amountBuy * lexusPrice)
                carsale = carsale + amountBuy
                amount_of_LX += amountBuy
            #if the money can not afford for a bugatti come next time
            else:
                print("You do not have enough money to afford a Lexus RCF.")
                print("Please come next time!!!")
        #if player hit mustang or m it will assign to the mustang category
        elif item.lower() in ('mustang', 'mus'):
            if money // mustangPrice > 0:#using the divide quotitent as the way to know how many car player can afford
                quantity = money//mustangPrice
                print("You can afford", quantity, "quantity of Mustang GT.")
                #also using the handling error(try/except) to eliminate the error in the input for the amount of car
                try:
                    amountBuy = int(input("How many do you want to buy? \n"))
                    #if the budget money is less than the price(also the amount) player wish to buy return no money, press any key to return to the main page
                    if money < (amountBuy * mustangPrice):
                        print("You do not have enough money!")
                        input("Press enter to return to the main page.")
                        amountBuy = 0
                #the except to show that the input is wrong
                except:
                    print("You must enter in a whole number!")
                    amountBuy = 0
                    int(amountBuy)
                #here is the formula to calculate the budget, amount of total car in garage, and amount of mustang
                money = money - (amountBuy * mustangPrice)
                carsale = carsale + amountBuy
                amount_of_MT += amountBuy
            #if the money can not afford for a bugatti come next time
            else:
                print("You do not have enough money to afford a Mustang GT.")
                print("Please come next time!!!")
        #if not of the input is match with the type of car, please try again   
        else:
            print("Please try again!")
    #the except have to eliminate error input, if error is yes. press any key to return to the main page
    except:
        print("That's not a valid choice!")
        input("Press enter to return to the main page.")

    return money, carsale, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT

#in the sellCar function is selling car with asking the type of car, amount of car the player want to sell.
def sellCar(money, carsale, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT):
#use the handling error(try/except) to eliminate error in the input for the category
    try:
        item = input("""What type of car you want to sell? 
Choices: (B)ugatti, (N)issan GTR, (Mer)cedes S-Class, (C)orvette, (L)exus, (Mus)tang\n\n""")
        #if player hit bugatti or b it will assign to the bugatti category
        if item.lower() in ('bugatti', 'b'):
            print ("You have ", amount_of_BGT, "amount of Bugatti.")
            #if the amount of bugatti is greater than or equal to 1, which mean there is a available car. Start to work on the formula
            if amount_of_BGT >= 1:
                #using the handling error(try/except) to eliminate the error in the input for the amount of car
                try: 
                    amount_sell_BGT = int(input("How many Bugatti you wanna sell? \n"))
                except:
                    print("You must enter a whole number.\n")
                    input("Press enter to return to the main page.")
                    amount_sell_BGT = 0
            #if the number the player wish to sell the bugatti greater than the total car in the garage (mean wrong)
            elif amount_sell_BGT > carsale:
                print("That is more than your currenty quantity. \n")
                input("Press enter to return to the main page.")
                amount_sell_BGT = 0
            #there is none of bugatti in the garage
            else:
                print ("You do not have any Bugatti in your garage.")
                input("Press enter to return to the main menu")
            #the formula to calculate the budget, total car in garage, amount of bugatti player is owning
            money = money + (amount_sell_BGT * bugattiPrice)
            carsale = carsale - amount_sell_BGT
            amount_of_BGT = amount_of_BGT - amount_sell_BGT 
        #if player hit nissan GTR or n it will assign to the Nissan GTR category
        elif item.lower() in ('Nissan GTR', 'n'):
            print ("You have ", amount_of_NS, "amount of Nissan GTR.")
            #if the amount of bugatti is greater than or equal to 1, which mean there is a available car. Start to work on the formula
            if amount_of_NS >= 1:
                #using the handling error(try/except) to eliminate the error in the input for the amount of car
                try: 
                    amount_sell_NS = int(input("How many Nissan GTR you wanna sell? \n"))
                except:
                    print("You must enter a whole number.\n")
                    input("Press enter to return to the main page.")
                    amount_sell_NS = 0
            #if the number the player wish to sell the nissan greater than the total car in the garage (mean wrong)    
            elif amount_sell_NS > carsale:
                print("That is more than your currenty quantity. \n")
                input("Press enter to return to the main page.")
                amount_sell_NS = 0
            #there is none of nissan in the garage
            else:
                print ("You do not have any Nissan GTR in your garage.")
                input("Press enter to return to the main menu")
            #the formula to calculate the budget, total car in garage, amount of Nissan GTR player is owning       
            money = money + (amount_sell_NS * nissanPrice)
            carsale = carsale - amount_sell_NS
            amount_of_NS = amount_of_NS - amount_sell_NS
        #if player hit mercedes S-Class or mer it will assign to the mercedes category
        elif item.lower() in ('Mercedes S-Class', 'mer'):
            print ("You have ", amount_of_MC, "amount of Mercedes S-Class.")
            #if the amount of bugatti is greater than or equal to 1, which mean there is a available car. Start to work on the formula
            if amount_of_MC >= 1:
                #using the handling error(try/except) to eliminate the error in the input for the amount of car
                try: 
                    amount_sell_MC = int(input("How many Mercedes S-Class you wanna sell? \n"))
                except:
                    print("You must enter a whole number.\n")
                    input("Press enter to return to the main page.")
                    amount_sell_MC = 0
            #if the number the player wish to sell the mercedes greater than the total car in the garage (mean wrong)
            elif amount_sell_MC > carsale:
                print("That is more than your currenty quantity. \n")
                input("Press enter to return to the main page.")
                amount_sell_MC = 0
            #there is none of mercedes in the garage
            else:
                print ("You do not have any Nissan GTR in your garage.")
                input("Press enter to return to the main menu")
            #the formula to calculate the budget, total car in garage, amount of Mercedes S-Class player is owning    
            money = money + (amount_sell_MC * mercedesPrice)
            carsale = carsale - amount_sell_MC
            amount_of_MC = amount_of_MC - amount_sell_MC
        #if player hit corvette or c it will assign to the mercedes category
        elif item.lower() in ('Corvette', 'c'):
            print ("You have ", amount_of_CV, "amount of Corvette Sting gray.")
            #if the amount of bugatti is greater than or equal to 1, which mean there is a available car. Start to work on the formula
            if amount_of_CV >= 1:
                #using the handling error(try/except) to eliminate the error in the input for the amount of car
                try: 
                    amount_sell_CV = int(input("How many Corvette you wanna sell? \n"))
                    
                except:
                    print("You must enter a whole number.\n")
                    input("Press enter to return to the main page.")
                    amount_sell_CV = 0
            #if the number the player wish to sell the corvette greater than the total car in the garage (mean wrong)
            elif amount_sell_CV > carsale:
                print("That is more than your currenty quantity. \n")
                input("Press enter to return to the main page.")
                amount_sell_CV = 0
            #there is none of corvette in the garage
            else:
                print ("You do not have any Corvette Sting gray in your garage.")
                input("Press enter to return to the main menu")
            #the formula to calculate the budget, total car in garage, amount of Corvette Sting gray player is owning     
            money = money + (amount_sell_CV * corvettePrice)
            carsale = carsale - amount_sell_CV
            amount_of_CV = amount_of_CV - amount_sell_CV
        #if player hit Lexus RCF or l it will assign to the mercedes category    
        elif item.lower() in ('Lexus RCF', 'l'):
            print ("You have ", amount_of_LX, "amount of Lexus RCF.")
            #if the amount of bugatti is greater than or equal to 1, which mean there is a available car. Start to work on the formula
            if amount_of_LX >= 1:
                #using the handling error(try/except) to eliminate the error in the input for the amount of car
                try: 
                    amount_sell_LX = int(input("How many Lexus RCF you wanna sell? \n"))
                
                except:
                    print("You must enter a whole number.\n")
                    input("Press enter to return to the main page.")
                    amount_sell_LX = 0
            #if the number the player wish to sell the Lexus greater than the total car in the garage (mean wrong)
            elif amount_sell_LX > carsale:
                print("That is more than your currenty quantity. \n")
                input("Press enter to return to the main page.")
                amount_sell_LX = 0
            #there is none of lexus in the garage
            else:
                print ("You do not have any Lexus RCF in your garage.")
                input("Press enter to return to the main menu")
            #the formula to calculate the budget, total car in garage, amount of Lexus RCF player is owning          
            money = money + (amount_sell_LX * lexusPrice)
            carsale = carsale - amount_sell_LX
            amount_of_LX = amount_of_LX - amount_sell_LX
        #if player hit Mustang GT or mus it will assign to the mercedes category     
        elif item.lower() in ('mustang', 'mus'):
            print ("You have ", amount_of_MT, "amount of Mustang GT.")
            #if the amount of bugatti is greater than or equal to 1, which mean there is a available car. Start to work on the formula
            if amount_of_MT >= 1:
                #using the handling error(try/except) to eliminate the error in the input for the amount of car
                try: 
                    amount_sell_MT = int(input("How many Mustang GT you wanna sell? \n"))
                    
                except:
                    print("You must enter a whole number.\n")
                    input("Press enter to return to the main page.")
                    amount_sell_MT = 0
            #if the number the player wish to sell the Mustang GT greater than the total car in the garage (mean wrong)
            elif amount_sell_MT > carsale:
                print("That is more than your currenty quantity. \n")
                input("Press enter to return to the main page.")
                amount_sell_MT = 0
            #there is none of Mustang GT in the garage
            else:
                print ("You do not have any Bugatti in your garage.")
                input("Press enter to return to the main menu")
            #the formula to calculate the budget, total car in garage, amount of Mustang GT player is owning          
            money = money + (amount_sell_MT * mustangPrice)
            carsale = carsale - amount_sell_MT
            amount_of_MT = amount_of_MT - amount_sell_MT
        #the input is wrong, try again
        else:
            print("Please try again!")
    #the except have to eliminate error input, if error is yes. press any key to return to the main page
    except:
        print("That's not a valid choice!")
        input("Press enter to return to the main page.")
        
    return money, carsale, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT
#the travel function is use to travel from different location    
def travel(carsale, money, location, times, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter):
    #There are four input choices, when travel to different city, count down the times remaining
    choice = input("""Travel to another location?
Choices: (W)ashington DC, (M)anassas, (B)altimore, (F)alls Church\n""")
    #washington DC
    if choice.lower() in ("washington", "w"):
        location = "Washington DC"
        #set the value to every location to be match
        carsale, money, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter = price_update(carsale, money, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter)
        times -= 1
    #manassas
    elif choice.lower() in ("manassas", "m"):
        location = "Manassas"
        #set the value to every location to be match
        carsale, money, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter = price_update(carsale, money, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter)
        times -= 1
    #baltimore
    elif choice.lower() in ("baltimore", "b"):
        location = "Baltimore"
        #set the value to every location to be match
        carsale, money, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter = price_update(carsale, money, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter)
        times -= 1
    #falls churhc
    elif choice.lower() in ("falls church", "f"):
        location = "Falls Church"
        #set the value to every location to be match
        carsale, money, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter = price_update(carsale, money, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter)
        times -= 1
    #invalid input and back to washington DC
    else:
        print("That's not a valid choice!")
        input("Press enter to return to the main shell.")
        location = "Washington"
        
    return carsale, money, location, times, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter
#the price update is the way to get the random price every time travel to different location
#also have a hint of challenge encounter to add up the entertain to the game
def price_update(carsale, money, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter):
    number = random.randint(1,20)
    #if the number from 1 to 10 the random price will be in that range
    if number <= 10:
        bugattiPrice = random.randrange(95000, 105999)

        nissanPrice = random.randrange(81000, 90999)

        mercedesPrice = random.randrange(71000, 80999)

        corvettePrice = random.randrange(61000, 70999)

        lexusPrice = random.randrange(51000, 60999)

        mustangPrice = random.randrange(49000, 50999)
    #from 11 to 20 a different random price with is higher     
    else:
        bugattiPrice = random.randrange(100000, 110999)

        nissanPrice = random.randrange(91000, 99999)

        mercedesPrice = random.randrange(81000, 90999)

        corvettePrice = random.randrange(71000, 80999)

        lexusPrice = random.randrange(61000, 70999)

        mustangPrice = random.randrange(55000, 60999)
    #here is the chanllenge encounter, have different story and different value
    #it could be great new or bad new
    #but the total of car in the garage much be greater than when travel to activate the challenge
    if carsale > 1:
        if number == 1:
            challenge_encounter = 1
            print("You just own your lawsuit and were awarded $100,000!!")
            money += 100000
            print("Here is your budget ", money, "$ left.\n")
        elif number == 2:
            challenge_encounter = 1
            print("Trump's tariffs just cost you $10,000!!")
            money -= 10000
            print("Here is your budget ", money, "$ left.\n")
        elif number == 3:
            challenge_encounter = 1
            print("Trump's tax cuts just made you $10,000 richer!!")
            money -= 10000
            print("Here is your budget ", money, "$ left.\n")
        elif number == 4:
            challenge_encounter = 1
            print("Climate change created another hurricane costing you $10,000!!")
            money -= 10000
            print("Here is your budget ", money, "$ left.\n")
        elif number == 5:
            challenge_encounter = 1
            print("The Bureau of consumer protection got a complaint costing you $10,000")
            money -= 10000
            print("Here is your budget ", money, "$ left.\n")
        elif number == 6:
            challenge_encounter = 1
            print("Nissan GTR's just got recalled, lose 1 if you have any")
            amount_of_NS -= 1
            carsale -= 1
            money = money - nissanPrice
            print("Here is your budget ", money, "$ left.\n")
        elif number == 7:
            challenge_encounter = 1
            print("Unfortunatley your grampa passed away but on the bright side he left you a Buggati!!")
            amount_of_BGT += 1
            carsale += 1
            money = money + bugattiPrice
            print("Here is your budget ", money, "$ left.\n")
        elif number == 8:
            challenge_encounter = 1
            print("Mustangs just got recalled, lose if you have any")
            amount_of_MT -= 1
            carsale -= 1
            money = money - mustangPrice
            print("Here is your budget ", money, "$ left.\n")
        elif number == 9:
            challenge_encounter = 1
            print("Bitcoin stock just exploded and you made $50,000!!")
            money += 50000
            print("Here is your budget ", money, "$ left.\n")
        elif number == 10:
            challenge_encounter = 1
            print("Bitcoin stock just crashed and you lost $50,000!!")
            money -= 50000
            print("Here is your budget ", money, "$ left.\n")
        elif number == 11:
            challenge_encounter = 1
            print("You just won a Mercedes by playing the lottery!!")
            amount_of_MC += 1
            carsale += 1
            money = money + mercedesPrice
            print("Here is your budget ", money, "$ left.\n")
        else:
            challenge_encounter = 0
            print("You've made it to your destination")
            
    return carsale, money, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter
#the gameStatus is show the menu status of the player
def gameStatus():
    print("\n\nYour money :", money)
    print("---------------------------")
    print("Amount of car: ", carsale)
    print("Number of Bugatti: ", amount_of_BGT)
    print("Number of Nissan GTR: ", amount_of_NS)
    print("Number of Mercedes S-Class: ", amount_of_MC)
    print("Number of Corvette Sting gray: ", amount_of_CV)
    print("Number of Lexus RCF: ", amount_of_LX)
    print("Number of Mustang GT: ", amount_of_MT)
    print("----------------------------")
    print("Price of Bugatti:", bugattiPrice)
    print("Price of Nissan GTR:", nissanPrice)
    print("Price of Mercedes S-Class: ", mercedesPrice)
    print("Price of Corvette Sting gray: ", corvettePrice)
    print("Price of Lexus RCF: ", lexusPrice)
    print("Price of Mustang GT: ", mustangPrice)
    print("-----------------------------")
    print("Location:", location)
    print("-----------------------------")
    print("Number of times left:", times, "\n\n")

#input the playerName        
def getPlayer():
    playerName = input("Please enter your name to be put on the leaderboard\n")
    return playerName

def saveScore(playerName, money):
    playerScore = playerName + "  " + str(money)
    return playerScore, money
#ask if the the player want to play or not
responseToPlay = input("Start CAR WARS game? (y/n) \n\n")
#if yes start the game
if responseToPlay in ("yes", "y"):
    #print the rule of the game in the beginning
    print("""                 +++++++++++++++++ RULES +++++++++++++++++
        -       To play the game you either press Y(start) the game or N(leave)
	⁃	You start off in Washington D.C and can travel to the locations we provide in the game. Prices will vary in different locations.
	⁃	The initial amount of money is $500,000 
	⁃	You chose as many cars with the amount of money you have
	⁃	The program  challenge you at random and you may lose or gain money
	⁃	You have 30 days to sell and buy as many cars as you like and you lose a day each time you travel
	⁃	You can buy/sell car(s) depending on how much money you have.
	⁃	The user with the most amount of money left wins the game.\n
""")
    #open the text file 
    score_file = open("WallofFame.txt", "a")
    #ask the player to input their usename
    playerName = getPlayer()
    #print out the status in the beginning
    gameStatus()
    #start the loop
    while times > 0:
        #6 action the player can do in the game
        choice = input("""\nWhat action to take?

    Choices: (b)uy, (s)ell, (t)ravel, (st)atus, (q)uit, (r)ules \n""")

        if choice.lower() in ("buy", "b"):
            #assign the value of the buyCar function
            money, carsale, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT = buyCar(money, carsale, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT)
            #always show status
            gameStatus()
            
        elif choice.lower() in ("sell", "s"):
            #assign the value of the sellCar function
            money, carsale, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT = sellCar(money, carsale, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT)
            #always show status
            gameStatus()
                        
        elif choice.lower() in ("travel", "t"):
            #assign the value of the travel function
            carsale, money, location, times, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter = travel(carsale, money, location, times, amount_of_BGT, amount_of_NS, amount_of_MC, amount_of_CV, amount_of_LX, amount_of_MT, bugattiPrice, nissanPrice, mercedesPrice, corvettePrice, lexusPrice, mustangPrice, challenge_encounter)
            #always show status
            gameStatus()
            
        elif choice.lower() in ("quit", "q"):
            #quit the game and show the balance for the player but will not save to the Wall of Fame
            times = 0
            gameStatus()
            print("This is the money you have made: ", money,"$", "in", times, "day.")

        elif choice.lower() in ("status", "st"):
            gameStatus()

        elif choice.lower() in ("rules", "r"):
            print("""               +++++++++++++++++ RULES +++++++++++++++++
        -       To play the game you either press Y(start) the game or N(leave)
	⁃	You start off in Washington D.C and can travel to the locations we provide in the game. Prices will vary in different locations.
	⁃	The initial amount of money is $500,000 
	⁃	You chose as many cars with the amount of money you have
	⁃	The program  challenge you at random and you may lose or gain money
	⁃	You have 30 days to sell and buy as many cars as you like and you lose a day each time you travel
	⁃	You can buy/sell car(s) depending on how much money you have.
	⁃	The user with the most amount of money left wins the game.
""")
                            
        else:
            input("That's not a valid choice!  Press enter to continue.")
    #save the score and player name to the WallofFame.txt 
    playerScore = playerName + "  " + str(money)
    score_file.write(playerScore + "\n")
    print("Your score have been save")
    score_file.close()
    
#if hit no thank you for stop by        
else:
    input("\n\nThank you for stopping by!  Press enter to close the program.")
    
#here is to print out the wall of fame with the top 10 player
#open the WallofFame.txt as a readlines(), mean read every line in the text file
score_file = open("WallofFame.txt").readlines()
#create a tuples
score_tuples = []
#run the loop for each line in the text file
for eachline in score_file:
    #assign the player name as the 1st column
    playerName = eachline.split()[0]
    #assign the player score as the second column
    playerScore = int(eachline.split()[1])
    #the tuples will have a list of playerName and playerScore
    score_tuples.append((playerName, playerScore))
#sort the tuple, assign the sorting on the second column, which is the money column player earn, and in the descending sorting
score_tuples.sort(key = lambda t: t[1], reverse = True)
#print out the Wall of Fame
print("++++Wall of Fame++++ \n")

print("---------------------")

for count,(playerName, playerScore) in enumerate (score_tuples[:10]):
    print("{}. Player:{} - Earn:{}".format(count+1, playerName, playerScore))
