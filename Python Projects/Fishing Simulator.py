# MSBA 502: Analytics Programming I
# Homework 3: Fishing Simulator / Diving & Oceanic Harvesting Simulator
# Kevin A. Howard SUBMITTED Oct 16, 2022



# Import the random function since the assignment is a simulation and need to generate random percentages
import random

# Define the function 'fishing simulator' with no specified default values
def fishing_simulator():
    """This is a fishing simulator. It simulates the financial status of a small diving and harvest operation and the Owner's outocome."""
    # Simulation keeps running as long as the user inputs any version of "yes"
    repeat = "yes"
    while repeat.lower().strip() == "yes":
        
        # Initialize key variables used for calculations, boolean evaluations, and printouts
        year_counter = 0
        profit_counter = 0
        seasonal_profit = 0
        cumulative_profit = 0
        
        # This while block loops infinitely until one of the flag conditions in the subsequent block evaluates to True
        while True: 
            print("** Year #", (year_counter+1), "**")
            # YEARLY HARVEST ORDER: 1st, dive for lobsters, then harvest Bullwhip Kelp, then dive for and harvest Urchins, and finally Bullwhip Kelp again.
            # Modulus checks for what year it is and therefore which if statement to run for the iteration. Modulus 4 works for this rotation.
            # Modulus checks of Lobster years
            if  year_counter%4 == 0:
                print("Focus this year: Lobsters")
                # Generate random number. random.random() calls a random number from 0 to 1
                random_yield = random.random()
                if random_yield <= 0.10:
                    seasonal_profit = 125000
                elif random_yield > 0.10 and random_yield <= 0.30:
                    seasonal_profit = -10000
                else:
                    seasonal_profit = 50000
                
                # Records the change in cumulative profits until one of the flag staements evaluates to True
                cumulative_profit += seasonal_profit
                
            # Modulus checks for even years, when Bullwhip Kelp is harvested
            elif year_counter%4 == 1 or year_counter%4 == 3:
                print("Focus this year: Bullwhip Kelp")
                 # Generate random number. random.random() calls a random number from 0 to 1
                random_yield = random.random()
                if random_yield <= 0.40:
                    seasonal_profit = -10000
                else:
                    seasonal_profit = 45000
                
                # Records the change in cumulative profits until one of the flag staements evaluates to True
                cumulative_profit += seasonal_profit
                
            # Modulus checks for Urchin years
            elif year_counter%4 == 2:
                print("Focus this year: Urchins")
                 # Generate random number. random.random() calls a random number from 0 to 1
                random_yield = random.random()
                if random_yield <= 0.25:
                    seasonal_profit = -5000
                else:
                    seasonal_profit = 30000
                    
                # Records the change in cumulative profits until one of the flag statements below evaluates to True    
                cumulative_profit += seasonal_profit
                
            else:
                # This should never print... here as a place holder to evaluate if statements. Flag statement conditions end the while loop, not this else block
                print("code error")
                
            # The counter counts years of consecutive profits. If a positive income was reported through 1 loop (1 year), the counter increases +1.
            # If year-end profit is negative, the counter resets. 
            if seasonal_profit > 0:
                profit_counter += 1
            else:
                profit_counter = 0
                
            # As the infinite while loop above runs, these print statements display what is happening each year and cumulatively in the simulation
            print("This year's profit/loss: $", seasonal_profit)
            print("Total profit/loss: $", cumulative_profit)
            year_counter += 1
            print()
            
            
            # The following flag statements end the infinite while loop above once one (or multiple) of the following conditions are met:
            flag = False
            if cumulative_profit < 0:
                flag = True
                print("Since the year-end total profit is negative, the owner will close the fishing operation and look for a new business venture.")
            if cumulative_profit >= 325000:
                flag = True
                print("The total profit reaches at least $325,000. The Owner will happily retire.")
            if  profit_counter == 5:
                flag = True
                print("There are five consecutive years of positive profit. The Owner will happily retire.")
            if flag == True:
                break
        
            
        print()
        # Ask of the user would like to run another fishing simulation
        repeat = input("Would you like to run another simulation (yes/no)? ")
        print()
            
# Writing out the function after definining it runs the fishing simulator and prompts the user if they would like to run it again or end session
fishing_simulator()
            
