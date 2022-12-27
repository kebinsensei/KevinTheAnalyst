# MSBA 502: Analytics Programming I
# Homework 2: Galaxy Analyzer SUBMITTED October 1 2022
# Kevin A. Howard

#This is a Galaxy Analyzer tool. It asks the user how many galaxies and planets they want to analyze in a certain quadrant,
#it asks the user to input income sums for planets, then produces limited summary statistics, then asks if they'd like to analyze another quadrant



name = input("Hi! What is your name, space travler?: ")
if name.isdigit():
    print()
    print("Hmmmm, are you a robot? That's okay.")
    print()
else:
    print()
valid_name = name.capitalize().strip()
print("Thanks, " + valid_name +"!")
print()
print("""Welcome to the Galaxy Analyzer Calculator. This tool will ask you for the number of galaxies you want to analyze
and how many planets reside in each galaxy. It will then ask you to input each planets income (in trillions) from the previous year.
After each planet's incomes are entered for each galaxy you want to analyze, the calculator will produce the following summary statistics:

1. Number of galaxies, total galactic income, and average income per galaxy.

2. Number of planets, total planet income across galaxies, and average income per planet.

3. Count of galaxies where the income sum of planets for each galaxy falls within the annotated income distribution.""")

print()
print("Let's get started!")
print()



SuperDuperBIG_list = [] #collects a list of list i.e. planetary incomes for each galaxy i.e. all the user input we need for the assignment

repeat = "yes"

while "y" in repeat.lower().strip(): #loop captures if the traveler would like to analyze another quadrant after analyzing the first

    galaxy_number = int(input("How many GALAXIES would you like to analyze?: "))
    print()

    for x in range(1, galaxy_number +1): #first loop asks for number of galaxies to analyze
        planets_in_galaxy = int(input(f"How many PLANETS are in Galaxy {x}?: "))
        planet_income = []
        print()
        for y in range(1, planets_in_galaxy +1, 1): #nested loop within the galaxy loop asks for planets information, repeats for n # galaxies entered
            planet_income_input = float(input(f"What is PLANET {y}'s income? "))
            planet_income.append(planet_income_input)
        print()
        
        SuperDuperBIG_list.append(planet_income) #annotates every planet income for each galaxy. creates a list of incomes for each galaxy. 
 
 
    print()   
    print("Here's a summary of your quadrant's statistics!")
    print()


    #number of galaxies
    galaxy_count = len(SuperDuperBIG_list) #since it's a list of a list, len works to count galaxies
    print("Total Galaxies:",galaxy_count)

    #total galactic income, used for calculations
    total_income = 0 #initialize total income in order to iterate through the big list and sum galactic income
    for money in SuperDuperBIG_list:
        list_total =sum(money)
        total_income += list_total
    print("Total Galactic income: $",round(total_income,2))

    #Average Galactic Income
    average_galactic_income = total_income/galaxy_count
    print("Average Income per Galaxy: $",round(average_galactic_income,2))
    print()


    #number of planets
    count_planet = 0 #initialize in order to use len to interate through and count the big list of list elements, which are planets
    for a in SuperDuperBIG_list: 
        amount = len(a)
        count_planet += amount    
    print("Total Planets:",count_planet)

    #Planets per galaxy: e.g. 1.5 (float)
    planets_per_galaxy = float(count_planet/galaxy_count)
    print("Planets per Galaxy:", round(planets_per_galaxy,2))

    #Average planetary income: round(233.33333333333334, 2)
    average_planetary_income = total_income/count_planet
    print("Average Income Per Planet: $",round(average_planetary_income,2))
    print()

 
    
    #initialize variables. Use for a loop to extract planet income values per galaxy,
    #sum each galaxy's planets, and evaluate each sum to add a +1 count for whichver income bucket it falls into
    below20 = 0
    between2040 = 0
    between4060 = 0
    between6080 = 0
    above80 = 0
    
    for p in SuperDuperBIG_list:
        galaxy_income_per = sum(p)
        if galaxy_income_per < 20000:
            below20 = below20 + 1
        elif galaxy_income_per > 20000 and galaxy_income_per < 40000:
            between2040 = between2040 + 1
        elif galaxy_income_per > 40000 and galaxy_income_per < 60000:
            between4060 = between4060 + 1
        elif galaxy_income_per > 60000 and galaxy_income_per < 80000:
            between6080 = between6080 + 1
        else:
            galaxy_income_per > 80000
            above80 = above80 + 1
    
    print("Galaxy Income sum less than $20000: ", below20)
    print("Galaxy Income sum between $20000 and $40000: ", between2040)
    print("Galaxy Income sum between $40000 and $60000: ", between4060)
    print("Galaxy Income sum between $60000 and $80000: ", between6080)
    print("Galaxy Income sum above $80000: ", above80)
  
    print()
    repeat = input("Would you like to analyze another quadrant?(yes/no): ")
    print()


print("Thank you for using the Galaxy Analyzer Calulator,",name+"!")
print("Be sure to check out the Citadel Gift shop for all your space traveling needs!")
print()
print("Good luck out there, space traveler!")





