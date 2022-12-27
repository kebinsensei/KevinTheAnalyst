# MSBA 503: Analytics Programming II
# Final Project: Data Science Salary Quick Finder
# Kevin A. Howard DUE December 14th, 2022


# import the modules needed to create the "Data Science Salary Quick Finder
import pandas as pd
import csv
import os
import tkinter.messagebox
import tkinter.ttk
import tkinter as tk
import tkmacosx 
from tkmacosx import Button # necessary to activate button colors for Mac users


# read in the clean dataset of 600+ Data Science salary entries from Kaggle: https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries
df = pd.read_csv("/Users/kevina.howard/Desktop/ds_salaries.csv")
# check to see what the data looks like
# print(df.shape)
# print(df.head())

# adjust the dataset... very light cleaning... 
df2 = df.drop(df.columns[[0, 1]], axis = 'columns')

# testing out how to query the dataset and organize how I want to view the output
# sample_query = (df2.query('job_title=="Data Scientist"'))
# print(sample_query)


# upon brainstorming how I want the user interaction to flow, create a function that creates a csv output when basic, key work preferences are selected displaying only key, critical information
def find_salary():
    """ Upon making combo box selections from the dropdown menus and pressing the "Find Salary" button, the user is shown a message.
    If successful, the user is notified as such and a csv of the search results based on selected preferences is created. If unsuccessful, an error message occurs and prompts the user to try again."""
    
    # global variables needed for the GUI to function properly with user inputs
    global exp_label_cb
    global emp_label_cb
    global hybrid_label_cb
    global bl_label_cb
    
    # use try and except block to run the series of if statements. If a combo of preferences isn't programmed for, an error occurs prompting the user to try again. 
    try:
        # the series of 32 if statements evaluates the users combo box selection upon selecting the "Find Salary" button. comments in this first block are iterable through the remainder of the this if block
        if exp_label_cb.get() == "Entry/Jr Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "United States":
            # adjust the dataframe to match the user's input. 
            box1_1 = (df2.query('experience_level=="EN" & employment_type=="FT" & remote_ratio==100 & company_location=="US"'))
            # reogranize the dataframe into the column output order I want to see and filtering the number columns/information displayed
            box1pack = box1_1.iloc[:, [2, 8, 7, 5]]
            # sort the results by job title. this allows me the most powerful use: quickly scanning the salary range for given job titles/location/remote-work % of interest. Gives me the information I need, very fast. 
            box1pack = box1pack.sort_values("job_title")
            # print the reorganized dataframe to a csv printout
            box1pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            # let the user know that their search was a success
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            # reset the combo boxes
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box1pack)
            
        elif exp_label_cb.get() == "Mid-level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "United States":
            box1_2 = (df2.query('experience_level=="MI" & employment_type=="FT" & remote_ratio==100 & company_location=="US"'))
            box2pack = box1_2.iloc[:, [2, 8, 7, 5]]
            box2pack = box2pack.sort_values("job_title")
            box2pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box2pack)
        elif exp_label_cb.get() == "Senior Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "United States":
            box1_3 = (df2.query('experience_level=="SE" & employment_type=="FT" & remote_ratio==100 & company_location=="US"'))
            box3pack = box1_3.iloc[:, [2, 8, 7, 5]]
            box3pack = box3pack.sort_values("job_title")
            box3pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box3pack)
        elif exp_label_cb.get() == "Executive Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "United States":
            box1_4 = (df2.query('experience_level=="EX" & employment_type=="FT" & remote_ratio==100 & company_location=="US"'))
            box4pack = box1_4.iloc[:, [2, 8, 7, 5]]
            box4pack = box4pack.sort_values("job_title")
            box4pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box4pack)
            
        elif exp_label_cb.get() == "Entry/Jr Level" and emp_label_cb.get() == "Part-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "United States":
            box2_1 = (df2.query('experience_level=="EN" & employment_type=="PT" & remote_ratio==100 & company_location=="US"'))
            box5pack = box2_1.iloc[:, [2, 8, 7, 5]]
            box5pack = box5pack.sort_values("job_title")
            box5pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box5pack)
            
        elif exp_label_cb.get() == "Mid-level" and emp_label_cb.get() == "Part-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "United States":
            box2_2 = (df2.query('experience_level=="MI" & employment_type=="PT" & remote_ratio==100 & company_location=="US"'))
            box6pack = box2_2.iloc[:, [2, 8, 7, 5]]
            box6pack = box6pack.sort_values("job_title")
            box6pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box6pack)
        elif exp_label_cb.get() == "Senior Level" and emp_label_cb.get() == "Part-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "United States":
            box2_3 = (df2.query('experience_level=="SE" & employment_type=="PT" & remote_ratio==100 & company_location=="US"'))
            box7pack = box2_3.iloc[:, [2, 8, 7, 5]]
            box7pack = box7pack.sort_values("job_title")
            box7pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box7pack)
        elif exp_label_cb.get() == "Executive Level" and emp_label_cb.get() == "Part-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "United States":
            box2_3 = (df2.query('experience_level=="EX" & employment_type=="PT" & remote_ratio==100 & company_location=="US"'))
            box8pack = box2_3.iloc[:, [2, 8, 7, 5]]
            box8pack = box8pack.sort_values("job_title")
            box8pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box8pack)
              
        elif exp_label_cb.get() == "Entry/Jr Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "50%" and bl_label_cb.get() == "United States":
            box3_1 = (df2.query('experience_level=="EN" & employment_type=="FT" & remote_ratio==50 & company_location=="US"'))
            box9pack = box3_1.iloc[:, [2, 8, 7, 5]]
            box9pack = box9pack.sort_values("job_title")
            box9pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box9pack)
        elif exp_label_cb.get() == "Mid-level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "50%" and bl_label_cb.get() == "United States":
            box3_2 = (df2.query('experience_level=="MI" & employment_type=="FT" & remote_ratio==50 & company_location=="US"'))
            box10pack = box3_2.iloc[:, [2, 8, 7, 5]]
            box10pack = box10pack.sort_values("job_title")
            box10pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box10pack)
        elif exp_label_cb.get() == "Senior Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "50%" and bl_label_cb.get() == "United States":
            box3_3 = (df2.query('experience_level=="SE" & employment_type=="FT" & remote_ratio==50 & company_location=="US"'))
            box11pack = box3_3.iloc[:, [2, 8, 7, 5]]
            box11pack = box11pack.sort_values("job_title")
            box11pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box11pack)
        elif exp_label_cb.get() == "Executive Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "50%" and bl_label_cb.get() == "United States":
            box3_4 = (df2.query('experience_level=="EX" & employment_type=="FT" & remote_ratio==50 & company_location=="US"'))
            box12pack = box3_4.iloc[:, [2, 8, 7, 5]]
            box12pack = box12pack.sort_values("job_title")
            box12pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box12pack)
            
        elif exp_label_cb.get() == "Entry/Jr Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "In-Office Only" and bl_label_cb.get() == "United States":
            box4_1 = (df2.query('experience_level=="EN" & employment_type=="FT" & remote_ratio==0 & company_location=="US"'))
            box13pack = box4_1.iloc[:, [2, 8, 7, 5]]
            box13pack = box13pack.sort_values("job_title")
            box13pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box13pack)
        elif exp_label_cb.get() == "Mid-level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "In-Office Only" and bl_label_cb.get() == "United States":
            box4_2 = (df2.query('experience_level=="MI" & employment_type=="FT" & remote_ratio==0 & company_location=="US"'))
            box14pack = box4_2.iloc[:, [2, 8, 7, 5]]
            box14pack = box14pack.sort_values("job_title")
            box14pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box14pack)
        elif exp_label_cb.get() == "Senior Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "In-Office Only" and bl_label_cb.get() == "United States":
            box4_3 = (df2.query('experience_level=="SE" & employment_type=="FT" & remote_ratio==0 & company_location=="US"'))
            box15pack = box4_3.iloc[:, [2, 8, 7, 5]]
            box15pack = box15pack.sort_values("job_title")
            box15pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box15pack)
        elif exp_label_cb.get() == "Executive Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "In-Office Only" and bl_label_cb.get() == "United States":
            box4_4 = (df2.query('experience_level=="EX" & employment_type=="FT" & remote_ratio==0 & company_location=="US"'))
            box16pack = box4_4.iloc[:, [2, 8, 7, 5]]
            box16pack = box16pack.sort_values("job_title")
            box16pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box16pack)             
            
        elif exp_label_cb.get() == "Entry/Jr Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "International (Outside US)":
            box5_1 = (df2.query('experience_level=="EN" & employment_type=="FT" & remote_ratio==100 & company_location!="US"'))
            box17pack = box5_1.iloc[:, [2, 8, 7, 5]]
            box17pack = box17pack.sort_values("job_title")
            box17pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box17pack)
        elif exp_label_cb.get() == "Mid-level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "International (Outside US)":
            box5_2 = (df2.query('experience_level=="MI" & employment_type=="FT" & remote_ratio==100 & company_location!="US"'))
            box18pack = box5_2.iloc[:, [2, 8, 7, 5]]
            box18pack = box18pack.sort_values("job_title")
            box18pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box18pack)
        elif exp_label_cb.get() == "Senior Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "International (Outside US)":
            box5_3 = (df2.query('experience_level=="SE" & employment_type=="FT" & remote_ratio==100 & company_location!="US"'))
            box19pack = box5_3.iloc[:, [2, 8, 7, 5]]
            box19pack = box19pack.sort_values("job_title")
            box19pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box19pack)
        elif exp_label_cb.get() == "Executive Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "International (Outside US)":
            box5_4 = (df2.query('experience_level=="EX" & employment_type=="FT" & remote_ratio==100 & company_location!="US"'))
            box20pack = box5_4.iloc[:, [2, 8, 7, 5]]
            box20pack = box20pack.sort_values("job_title")
            box20pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box20pack)
            
        elif exp_label_cb.get() == "Entry/Jr Level" and emp_label_cb.get() == "Part-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "International (Outside US)":
            box6_1 = (df2.query('experience_level=="EN" & employment_type=="PT" & remote_ratio==100 & company_location!="US"'))
            box21pack = box6_1.iloc[:, [2, 8, 7, 5]]
            box21pack = box21pack.sort_values("job_title")
            box21pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box21pack)
        elif exp_label_cb.get() == "Mid-level" and emp_label_cb.get() == "Part-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "International (Outside US)":
            box6_2 = (df2.query('experience_level=="MI" & employment_type=="PT" & remote_ratio==100 & company_location!="US"'))
            box22pack = box6_2.iloc[:, [2, 8, 7, 5]]
            box22pack = box22pack.sort_values("job_title")
            box22pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box22pack)
        elif exp_label_cb.get() == "Senior Level" and emp_label_cb.get() == "Part-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "International (Outside US)":
            box6_3 = (df2.query('experience_level=="SE" & employment_type=="PT" & remote_ratio==100 & company_location!="US"'))
            box23pack = box6_3.iloc[:, [2, 8, 7, 5]]
            box23pack = box23pack.sort_values("job_title")
            box23pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box23pack)
        elif exp_label_cb.get() == "Executive Level" and emp_label_cb.get() == "Part-Time" and hybrid_label_cb.get() == "100%" and bl_label_cb.get() == "International (Outside US)":
            box6_4 = (df2.query('experience_level=="EX" & employment_type=="PT" & remote_ratio==100 & company_location!="US"'))
            box24pack = box6_4.iloc[:, [2, 8, 7, 5]]
            box24pack = box24pack.sort_values("job_title")
            box24pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box24pack)        
            
        elif exp_label_cb.get() == "Entry/Jr Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "50%" and bl_label_cb.get() == "International (Outside US)":
            box7_1 = (df2.query('experience_level=="EN" & employment_type=="FT" & remote_ratio==50 & company_location!="US"'))
            box25pack = box7_1.iloc[:, [2, 8, 7, 5]]
            box25pack = box25pack.sort_values("job_title")
            box25pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box25pack)
        elif exp_label_cb.get() == "Mid-level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "50%" and bl_label_cb.get() == "International (Outside US)":
            box7_2 = (df2.query('experience_level=="MI" & employment_type=="FT" & remote_ratio==50 & company_location!="US"'))
            box26pack = box7_2.iloc[:, [2, 8, 7, 5]]
            box26pack = box26pack.sort_values("job_title")
            box26pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box26pack)
        elif exp_label_cb.get() == "Senior Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "50%" and bl_label_cb.get() == "International (Outside US)":
            box7_3 = (df2.query('experience_level=="SE" & employment_type=="FT" & remote_ratio==50 & company_location!="US"'))
            box27pack = box7_3.iloc[:, [2, 8, 7, 5]]
            box27pack = box27pack.sort_values("job_title")
            box27pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box27pack)
        elif exp_label_cb.get() == "Executive Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "50%" and bl_label_cb.get() == "International (Outside US)":
            box7_4 = (df2.query('experience_level=="EX" & employment_type=="FT" & remote_ratio==50 & company_location!="US"'))
            box28pack = box7_4.iloc[:, [2, 8, 7, 5]]
            box28pack = box28pack.sort_values("job_title")
            box28pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box28pack)
            
        elif exp_label_cb.get() == "Entry/Jr Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "In-Office Only" and bl_label_cb.get() == "International (Outside US)":
            box8_1 = (df2.query('experience_level=="EN" & employment_type=="FT" & remote_ratio==0 & company_location!="US"'))
            box29pack = box8_1.iloc[:, [2, 8, 7, 5]]
            box29pack = box29pack.sort_values("job_title")
            box29pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box29pack)
        elif exp_label_cb.get() == "Mid-level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "In-Office Only" and bl_label_cb.get() == "International (Outside US)":
            box8_2 = (df2.query('experience_level=="MI" & employment_type=="FT" & remote_ratio==0 & company_location!="US"'))
            box30pack = box8_2.iloc[:, [2, 8, 7, 5]]
            box30pack = box30pack.sort_values("job_title")
            box30pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box30pack)
        elif exp_label_cb.get() == "Senior Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "In-Office Only" and bl_label_cb.get() == "International (Outside US)":
            box8_3 = (df2.query('experience_level=="SE" & employment_type=="FT" & remote_ratio==0 & company_location!="US"'))
            box31pack = box8_3.iloc[:, [2, 8, 7, 5]]
            box31pack = box31pack.sort_values("job_title")
            box31pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box31pack)
        elif exp_label_cb.get() == "Executive Level" and emp_label_cb.get() == "Full-Time" and hybrid_label_cb.get() == "In-Office Only" and bl_label_cb.get() == "International (Outside US)":
            box8_4 = (df2.query('experience_level=="EX" & employment_type=="FT" & remote_ratio==0 & company_location!="US"'))
            box32pack = box8_4.iloc[:, [2, 8, 7, 5]]
            box32pack = box32pack.sort_values("job_title")
            box32pack.to_csv("datasciencesalaries.csv", header=["Job Title", "Base Location", "Remote Amount", "Salary in USD"], index = False)
            tk.messagebox.showinfo(title = "Success!", message = "Your search was found and a datasciencesalaries.csv was created!")
            exp_label_cb.delete(0, tkinter.END)
            emp_label_cb.delete(0, tkinter.END)
            hybrid_label_cb.delete(0, tkinter.END)
            bl_label_cb.delete(0, tkinter.END)
            #print(box32pack)
            
        else:
            # if a combination wasn't programmed due to lack of information for that search, display an error message and encourage the user to try a different search
            tk.messagebox.showwarning(title = "Error", message = "Sorry, there was an error with your query. Please try again.")
       
    # show the user a warning for a bad search  
    except Exception as e:
        # print(e)
        tk.messagebox.showwarning(title = "Error", message = "Sorry, there was an error with your query. Please try again.")

    
# create a definition to close the main GUI window if the user wishes to exit the program        
def close_window():
    tk.messagebox.showwarning(title = "Bye!", message = "Thanks for stopping by! We wish you success. Good luck!")
    main_window.destroy()


# greet the user and ask if they are indeed here to use the tool, otherwise bid them well
user = input("Hello! Welcome to the Data Science Salary Quick Search. Shall we get started (yes/no)? ")
# if the user is indeed here for the quick finder, prompt the construction of the GUI and widgets
if user.lower().strip() == "yes":
    main_window = tk.Tk()
    main_window.title("Data Science Salary Quick Search")
    main_window.configure(bg = "azure")
    main_window.geometry("700x150")

    exp_label = tk.Label(main_window, text = "Experience Level: ", bg = "bisque", fg = "black")
    exp_label.grid(column = 0, row = 0, padx = 5, pady = 5)
    exp_label_cb = tk.ttk.Combobox(main_window, values = ["Entry/Jr Level", "Mid-level", "Senior Level", "Executive Level"], state = "readonly")
    exp_label_cb.current(0)
    exp_label_cb.grid(column = 1, row = 0, padx = 5, pady = 5)

    emp_label = tk.Label(main_window, text = "Employment Type: ", bg = "bisque", fg = "black")
    emp_label.grid(column = 2, row = 0, padx = 5, pady = 5)
    emp_label_cb = tk.ttk.Combobox(main_window, values = ["Full-Time", "Part-Time"], state = "readonly")
    emp_label_cb.current(0)
    emp_label_cb.grid(column = 3, row = 0, padx = 5, pady = 5)

    hybrid_label = tk.Label(main_window, text = "Hybrid Amount: ", bg = "bisque", fg = "black")
    hybrid_label.grid(column = 0, row = 1, padx = 5, pady = 5)
    hybrid_label_cb = tk.ttk.Combobox(main_window, values = ["100%", "50%", "In-Office Only"], state = "readonly")
    hybrid_label_cb.current(0)
    hybrid_label_cb.grid(column = 1, row = 1, padx = 5, pady = 5)

    bl_label = tk.Label(main_window, text = "Base Location: ", bg = "bisque", fg = "black")
    bl_label.grid(column = 2, row = 1, padx = 5, pady = 5)
    bl_label_cb = tk.ttk.Combobox(main_window, values = ["United States", "International (Outside US)"], state = "readonly")
    bl_label_cb.current(0)
    bl_label_cb.grid(column = 3, row = 1, padx = 5, pady = 5)
    
    fs_button = tk.Button(main_window, text = "Find Salary")
    fs_button = tkmacosx.Button(main_window, text = "Find Salary", command = find_salary)
    fs_button.configure(bg = "forest green", fg = "black", width = 200)
    fs_button.grid(column = 1, row = 3, padx = 5, pady = 5)

    exit_button = tk.Button(main_window, text = "Exit")
    exit_button = tkmacosx.Button(main_window, text = "Exit", command = close_window)
    exit_button.configure(bg = "dark red", fg = "black", width = 50)
    exit_button.grid(column = 3, row = 4, padx = 5, pady = 5) 

    main_window.mainloop()
        
# if the user types something other than some form of "yes" to initiate the program, show the user a warning and end the program     
else:
    tk.messagebox.showwarning(title = "Bye!", message = "Thanks for stopping by! We wish you success. Good luck!")



