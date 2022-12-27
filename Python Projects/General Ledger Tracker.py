# MSBA 503: Analytics Programming II
# Homework 4: NIGHTCITY TRANSACTION TRACKER
# Kevin A. Howard SUBMITTED Novemeber 9th, 2022


"""SUMMARY: This program tracks financial transactions by maintaining updated records on transaction data. Allows users to load new transaction data and analyze existing transaction data."""

# os is used to create the transaction_ledger.csv directory if it doesn't already exist in the current file path of the users machine
# csv is used to create the transaction_ledger.csv, read imported csv content, and write/append content to csv
import csv, os


def Import_Files(new_file, transaction_file):
    """Function 1 of 2 required to construct the Tracker: Import_Files used to read in csv content and append non-duplicate rows to transaction_ledger.csv"""
    
    # initialize the count of successfully uploaded transaction records. Resets after every user session. 
    transaction_upload_count = 0
    
    # use try/except block to handle file errors
    try:
        # use block version of opening files for better efficiency. Reads in content as strings forming a list for each line of content. 
        with open(new_file, "r") as user_file:
            file_contents = csv.reader(user_file)
            # iterate over the file contents, each row is a list and row elements are delimited by commas
            for element in file_contents:
                # grab the transaction id from each row 
                transaction_id = element[0]
                
                # Check transaction ids of an imported file for duplicates. If a duplicate exists, print a message saying so and do not add it to transaction_ledger.csv an additional time
                if transaction_id in transaction_id_list:
                    print()
                    # use the print(f"----{changing variable}----) format to print each duplicate transaction id as they are read in from an imported csv
                    print(f"Transaction ID: {transaction_id} already exists. Disregarding entry.")
                else:
                    # if a new transaction id is unique, add it to the transaction id list
                    transaction_id_list.append(transaction_id)
                    # use the transaction_file variable established in the following while loop block to write new rows to the transaction_ledger.csv, for each file imported 
                    transaction_file.writerow(element)
                    # counter to keep track of number of new non-duplicate rows successfully imported per user session
                    transaction_upload_count += 1
                          
            # UI formatting        
            print()
            # use the print(f"----{changing variable}----) format to print the aggregate count of successful transactions uploaded from a csv import
            print(f"{transaction_upload_count} new transaction records successfully uploaded.")
      
    except Exception as e:
        # print(e): used initially to capture errors messages and have a starting point to correct errors
        print()
        print("Sorry, that file could not be found. Please try again.")      



def Statistics():
    """Function 2 of 2 required to construct the Tracker: Statistics() used to report the count of current transactions and current total PENDING amount that exist in transaction_ledger.csv"""
    
    # initialize the count of existing transaction records in transaction_ledger.csv; count starts at -1 to account for row headers, effectively setting the count to 0 per each user session for accurate reporting
    current_transaction_count = -1
    # initialize the aggregate amount of transaction records that have a status of "pending" per user session
    transaction_pending_amount = 0.0
     
    #use try/except block to report statistics on existing transaction data or handle the prevelent error of the user selecting the Statistics option, when no data was uploaded first 
    try:
        # use block version of opening files for better efficiency. Reads in content as strings forming a list for each line of content.
        with open("transaction_ledger.csv", "r") as file:
            file_contents = csv.reader(file)
            # iterate of over the existing content
            for each_line in file_contents:
                # checks if there is rows of data in the first place. if not, runs except block
                if len(each_line) != 0:
                    # if the is data, +1 for each row
                    current_transaction_count += 1
                    # identifies transaction records with a "PENDING" status (the other status option is "COMPLETE") 
                    if each_line[4] == "PENDING":
                        # grabs the amount associated with each record with a "PENDING" status; needs to be converted to a float since it grabs a string, so it can be added to the transaction_pending_amount counter
                        transaction_pending_amount += float(each_line[3])
        # UI formatting
        print()
        # Use special print format to report changing variables for the initialized counters directly under the Statistics() function docstring
        print(f"Total Transactions Count: {current_transaction_count}")
        print(f"Total PENDING Transactions Amount: {transaction_pending_amount}")
        print()
        
        
    except Exception as e:
        # print(e): used initially to capture errors messages and have a starting point to correct errors
        # use if statement to evaluate the boolean identifier (-1) for running this function when no data was uploaded first
        if current_transaction_count == -1:
            print()
            print("Sorry, no transaction data was loaded yet. Please upload data first, then try again.")
        # This else statement is superceded by the if statement proceeding it, because if there is data i.e. current_transaction_count > -1, then the try block will run first
        else:
            print()


# this list is placed outside of either function and the while loop to keep track of transaction ids that have been uploaded to transaction_ledger.csv in the current file path
transaction_id_list = []

# welcome message to the program, a user defined loop with 2 main functions. Placed outside of functions and the following while loop, since it only needs to run once per user session
print("Welcome to the Adrek Robotics Transaction Tracker in Night City!")

# user defined while loop that uses an if statement to evaluate which of the two functions to run per user analysis
repeat = "yes"
while repeat.lower().strip() == "yes":       
    # prompt the user to make a decision, which starts either of the two functions
    decision = input("What would you like to perform (Import/Statistics)? ")
    # use strip and lower for better handling. User invokes the Import_Files() function
    if decision.strip().lower() == "import":
        # use os to create/identify the file path for transaction_ledger.csv. use if statement and variables to evaluate and record if the file path exists
        if os.path.exists("transaction_ledger.csv"):
            is_file = "yes"
        else:
            is_file = "no"
       # open transaction_ledger.csv with "a" for append to be able to write successfully imported transaction records to the general ledger when the import function is invoked   
        with open("transaction_ledger.csv", "a") as f:
            # use transaction_file as the variable to write new successful transaction r
            transaction_file = csv.writer(f, lineterminator = "\n")
             # use new_file to capture which file the user would like to import   
            new_file = input("Which transaction file would you like to import? ")  
            # if the file path for transaction_ledger.csv doesn't exist, create it with headers the first time a user selects import for the session 
            if is_file == "no":
                header = ["ID", "COMPANY NAME", "DATE", "AMOUNT", "STATUS"]
                transaction_file.writerow(header)
                # start the Import_Files() function now that transaction_ledger.csv has been created with headers
                Import_Files(new_file, transaction_file)
            # if the directory for transaction_ledger.csv exists, run the Import_Files() function since the file is open here       
            elif is_file == "yes":
                Import_Files(new_file, transaction_file)
            # this else block is not really functional, its place holder to explicity define the if and elif block preceeding it. Probably not needed but keeping for review purposes   
            else:
                print()
    # user invokes the Statistics() function. use lower and strip for better user input handling      
    elif decision.lower().strip() == "statistics":
        Statistics()
    
    # user entered in something other than "import" or "statistics", which isn't supported by this transaction analyzer program
    else:
        print("Invalid request. Please try again.")
        
    # ask the user  if they would like to do another analysis. if yes, keeps the data recorded from the last analysis. Counters reset after each user session (any input outside of "yes")      
    repeat = input("Would you like to run another analysis (yes/no)? ")
    
    # extra account for the "repeat" variable in order to account for the user inputting "no" or and invalid input that ends the session
    if repeat.lower().strip() == "yes":
        continue
    else:
        print()
        # End of user session goodbye message
        print("Thank you for using the Adrek Robotics Transaction Tracker in Night City!") 
