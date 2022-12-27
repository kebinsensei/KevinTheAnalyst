# MSBA 503: Analytics Programming II
# Homework 5: API Cryptocurrency Converter
# Kevin A. Howard DUE November 21, 2022


""" SUMMARY: This program uses an API to obtain the current value of a crypto currency,
which is then used to generate a report of how much in USD it would cost to buy the specified amount.
It uses a graphical user interface (GUI) to facilitate the exchange rate conversions. """

import tkinter, tkinter.messagebox # tkinter needed to create GUIs, messsagebox needed to alert the user via messagebox
import tkmacosx # needed to actualize GUI COLORS on Mac OS systems 
from tkmacosx import Button # specifically, need tkmacosx and BUTTON to actualize color on GUI buttons for Mac OSX
import requests # needed to retrieve API data from coinlayer.com, needed to sign up in order to get 100 free API calls
import json # needed to write data retrieved from API and calculations thereof to csv
import os # needed to create/find the file path of crypto_conversions.csv. If the file doesn't exist, allows to create a new csv
import csv # needed for csv procedures to write/append data to csv

# welcome message
print("Hello! Welcome to the CRYPTOCURRENCY CONVERTER!")
print()
print("Connecting to the live database, please standby...")
print()


# use requests.get() to retrieve data provided by the API web link and unique user generated API key
api_response = requests.get("http://api.coinlayer.com/api/live?access_key=a6c72dff2cf73e4793ccb482b5c08f60")

# use if statement to determine if API connection can be established. If true, create GUIs, if not, exit
if api_response:
    # check to see if API is connecting and retriving necessary data
    # data = json.loads(api_response.text)
    # print(json.dumps(data, indent = 4))
    print("Successfully connected to live data! Let\'s get started.")
    print("Please enter the number of units for each currency you would like to calculate: ")
    # create the MAIN GUI window that will house labels and buttons to facilitate the crypto conversion
    main_window = tkinter.Tk()
    main_window.title("Cryptocurrency Exchange Rate Calculator")
    # this size is appropriate to fit the entry boxes, labels, and convert/end buttons
    main_window.geometry("650x100")
    main_window.configure(bg = "bisque")

    # create the BTC label first, and then the entry box the user will input quantities of crypto the user wants to purchase
    btc_label = tkinter.Label(main_window, text = "BTC: ", bg = "bisque", fg = "black")
    btc_label.grid(column = 0, row = 0)
    btc_entry = tkinter.Entry(main_window)
    btc_entry.configure(bg = "white", fg = "black")
    btc_entry.grid(column = 1, row = 0)

    # create the ETH label first, and then the entry box the user will input quantities of crypto the user wants to purchase
    eth_label = tkinter.Label(main_window, text = "ETH: ", bg = "bisque", fg = "black")
    eth_label.grid(column = 2, row = 0)
    eth_entry = tkinter.Entry(main_window)
    eth_entry.configure(bg = "white", fg = "black")
    eth_entry.grid(column = 3, row = 0)

    # create the BNB label first, and then the entry box the user will input quantities of crypto the user wants to purchase
    bnb_label = tkinter.Label(main_window, text = "BNB: ", bg = "bisque", fg = "black")
    bnb_label.grid(column = 0, row = 2)
    bnb_entry = tkinter.Entry(main_window)
    bnb_entry.configure(bg = "white", fg = "black")
    bnb_entry.grid(column = 1, row = 2)

    # create the XRP label first, and then the entry box the user will input quantities of crypto the user wants to purchase
    xrp_label = tkinter.Label(main_window, text = "XRP: ", bg = "bisque", fg = "black")
    xrp_label.grid(column = 2, row = 2)
    xrp_entry = tkinter.Entry(main_window)
    xrp_entry.configure(bg = "white", fg = "black")
    xrp_entry.grid(column = 3, row = 2)

    # create the pale green convert button OPTIMIZED FOR MACOSX. Regular tkinter doesn't display button colors for Mac users
    # padx and pady help with properly spacing the layout of the GUI elements
    convert_button = tkmacosx.Button(main_window, text = "Convert Currency")
    convert_button.configure(bg = "pale green", fg = "black", width = 175,)
    convert_button.grid(column = 4, row = 0, padx = 6, pady = 6)

    # create the close button that ends the program by closing the GUI window and exiting
    # padx and pady help with properly spacing the layout of the GUI elements
    close_button = tkmacosx.Button(main_window, text = "Close Converter")
    close_button.configure(bg = "dark orange", fg = "black", width = 175)
    close_button.grid(column = 4, row = 2, padx = 6, pady = 6)

    
else:
    # if not able to connect to API, don't create the GUI. Instead, exit the program. if-else effectively does this
    print("Could not connect successfully.")
    exit()
   

# create a function that will run when a user clicks the pale green convert currency button
# TO BETTER OPTIMIZE ERROR HANDLING USER INPUT: Use default values for Entry boxes if user doesn't enter anything
def convert_currency():
    
    # use try/except block to handle user GUI input, handling API data and calculations, and writing info to csv
    try:
    
    
        # retrieve the data the user input into the GUI window for this conversion session
        btc_user = float(btc_entry.get())
        eth_user = float(eth_entry.get())
        bnb_user = float(bnb_entry.get())
        xrp_user = float(xrp_entry.get())
        
        
        # retrieve the current rate for the crypto currencies from the API
        btc_rate = float(api_response.json()["rates"]["BTC"])
        eth_rate = float(api_response.json()["rates"]["ETH"])
        bnb_rate = float(api_response.json()["rates"]["BNB"])
        xrp_rate = float(api_response.json()["rates"]["XRP"])
        
        # multiply user quantities of what they'd like to convert with the current price of each crypto currency
        btc_user_rate = btc_user * btc_rate
        eth_user_rate = eth_user * eth_rate
        bnb_user_rate = bnb_user * bnb_rate
        xrp_user_rate = xrp_user * xrp_rate
        
        # calculate how much $1 of each currency is worth i.e. USD:COIN 
        btc_exchange_rate = 1/btc_rate
        eth_exchange_rate = 1/eth_rate
        bnb_exchange_rate = 1/bnb_rate
        xrp_exchange_rate = 1/xrp_rate
        
        
        # use the os module to see if there is a crypto_conversion.csv in the filepath, if not, create it
        # set the is_file variable to evaluate the filepath, then use them in an if staement to facilitate how to write/append the csv
        if os.path.exists("crypto_conversions.csv"):
            is_file = "yes"
        else:
            is_file = "no"
            
        # open the crypto_conversion.csv 
        with open("crypto_conversion.csv", "a") as f:
            # use a variable to create a csv writer to write each row of information to include on the csv
            crypto_file = csv.writer(f, lineterminator = "\n")
            # if there is no crypto_conversion.csv in the filepath, set is_file to no, create the headers, and write the rows
            if is_file == "no":
                # only write the header if crypto_conversion.csv does not exist in the file path
                header = ["CURRENCY", "PRICE", "QUANTITY", "COST(USD)", "Exchange Rate USD:COIN"]
                crypto_file.writerow(header)
                
                # compile the rows of data to be written to csv
                # use str() to standardize variables as strings, so that they are writable to csv
                btc_info = ("BTC", str(btc_rate), str(btc_user), str(btc_user_rate), str(btc_exchange_rate))
                eth_info = ("ETH", str(eth_rate), str(eth_user), str(eth_user_rate), str(eth_exchange_rate))
                bnb_info = ("BNB", str(bnb_rate), str(bnb_user), str(bnb_user_rate), str(bnb_exchange_rate))
                xrp_info = ("XRP", str(xrp_rate), str(xrp_user), str(xrp_user_rate), str(xrp_exchange_rate))
                spacer = ("--", "--", "--", "--", "--")
                total = ("Total", "--", "--", str(btc_user_rate + eth_user_rate + bnb_user_rate + xrp_user_rate), "--")
                
                # write the compiled information to csv
                crypto_file.writerow(btc_info)
                crypto_file.writerow(eth_info)
                crypto_file.writerow(bnb_info)
                crypto_file.writerow(xrp_info)
                crypto_file.writerow(spacer)
                crypto_file.writerow(total)
                
                # show a messagebox message to the user when a csv is successfully generated
                tkinter.messagebox.showinfo(title = "Complete!", message = "The conversions were stored in crypto_conversions.csv")  
            
                
                
                     
            else:
                # if the file path for crypto_conversion.csv exists, don't write headers. only compile the data and append to csv
                is_file == "yes"
                
                # compile the rows of data to be written to csv
                # use str() to standardize variables as strings, so that they are writable to csv
                btc_info = ("BTC", str(btc_rate), str(btc_user), str(btc_user_rate), str(btc_exchange_rate))
                eth_info = ("ETH", str(eth_rate), str(eth_user), str(eth_user_rate), str(eth_exchange_rate))
                bnb_info = ("BNB", str(bnb_rate), str(bnb_user), str(bnb_user_rate), str(bnb_exchange_rate))
                xrp_info = ("XRP", str(xrp_rate), str(xrp_user), str(xrp_user_rate), str(xrp_exchange_rate))
                
                # write the compiled information to csv
                crypto_file.writerow(btc_info)
                crypto_file.writerow(eth_info)
                crypto_file.writerow(bnb_info)
                crypto_file.writerow(xrp_info)
                tkinter.messagebox.showinfo("The conversions were stored in crypto_conversions.csv")
                    
                # show a messagebox message to the user when a csv is successfully generated
                tkinter.messagebox.showinfo(title = "Complete!", message = "The conversions were stored in crypto_conversions.csv")    
        
        # clear the GUI boxes after the user inputs info and a csv was successfully created. Resets the session
        btc_entry.delete(0, tkinter.END)
        eth_entry.delete(0, tkinter.END)
        bnb_entry.delete(0, tkinter.END)
        xrp_entry.delete(0, tkinter.END)
        
        
    # show the user a warning that the csv could not be written. Doesn't end the session, but prompts them to enter valid values   
    except Exception as e:
        # print(e)
        tkinter.messagebox.showwarning(title = "Error!", message = "Sorry, the report could not be written. Check that only numeric values are entered, including zero for blank boxes.")


# create a function attached to the close converter button, to close the GUI window and end program            
def close_converter():
    main_window.destroy()
    exit()

# attach the convert_currency function to the convert button
convert_button.configure(command = convert_currency)
# attach the closer_converter function the close button 
close_button.configure(command = close_converter)
# run the program until the user chooses to exit
main_window.mainloop()



