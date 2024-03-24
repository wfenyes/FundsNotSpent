from math import *
from tkinter import * 
from tkinter.ttk import *
import sqlite3

#create submit function to database



window = Tk()
window.title('Receipt Tracker')
window.geometry('400x400')


#Create a database or connect to one

conn = sqlite3.connect('receipt_log.db')

#create cursor

c = conn.cursor()

#create table

# c.execute("""CREATE TABLE receipts (
#           company_name text,
#           date text, 
#           amount integer,
#           purpose text)""")

#commit changes

def submit():
    #Create a database or connect to one

    conn = sqlite3.connect('receipt_log.db')

    #create cursor

    c = conn.cursor()

    #insert into table

    c.execute("INSERT INTO receipts VALUES (:entry_name, :entry_date, :entry_amount, :entry_purpose)",
              {
                'entry_name' : entry_name.get(),
                'entry_date' : entry_date.get(),
                'entry_amount' : entry_amount.get(),
                'entry_purpose' : entry_purpose.get()
              })

    #commit changes
    conn.commit()

    #close connection
    conn.close()

    #clear out entry

    entry_name.delete(0, END)
    entry_date.delete(0, END)
    entry_amount.delete(0, END)
    entry_purpose.delete(0, END)

def query():
    #create a databse connection
    conn = sqlite3.connect('receipt_log.db')

    #create cursor

    c = conn.cursor()

    #query database
    c.execute(f"SELECT {col_query_parm.get()}, oid FROM receipts WHERE {col_query_parm.get()} {operator_dropdown.get()} '{search_term.get()}'")
    records = c.fetchall()

    #loop thorugh results

    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(window, text=print_records)
    query_label.grid(row=20, column=0)
    
    #wipe entry_query_param



    conn.commit()

    conn.close()







label_name = Label(window, text="Compnay Name")
entry_name = Entry(window)
label_date = Label(window, text="Date")
entry_date = Entry(window)
label_amount = Label(window, text="Amount")
entry_amount = Entry(window)
label_purpose = Label(window, text="Purpose")
entry_purpose = Entry(window)

label_name.grid(row=0, column = 0)
entry_name.grid(row=1, column = 0)
label_date.grid(row= 3, column= 0)
entry_date.grid(row=4, column= 0 )
label_amount.grid(row=5, column=0)
entry_amount.grid(row=6, column=0)
label_purpose.grid(row=7, column=0)
entry_purpose.grid(row=8, column=0)

#create submit button

submit_button = Button(window, text="Submit", command=submit)
submit_button.grid(row=9, column=0)

#query parameters

#Dropdown for operators

operator_options = ["IN", "LIKE", "=", "NOT"]
selected_option = StringVar()
operator_dropdown = Combobox(window, textvariable=selected_option)
operator_dropdown['values'] = operator_options
operator_dropdown.grid(row=14, column=0)



label_query_parm = Label(window, text="Search Parameters")
col_query_parm = Entry(window, text="Enter Here")
label_search_term = Label(window, text="Search Word")
search_term = Entry(window, text="something")

label_query_parm.grid(row=10, column=0)
col_query_parm.grid(row=11, column=0)
label_search_term.grid(row=12, column=0)
search_term.grid(row=13, column=0)

#create query button

query_button = Button(window, text = "show records", command=query)
query_button.grid(row=15, column=0)


conn.commit()

#close connection

conn.close()


window.mainloop()

