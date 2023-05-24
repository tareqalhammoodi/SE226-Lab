from tkinter import *
import mysql.connector
from datetime import datetime
from tkinter import messagebox

# Setup database ----------------------------------------------------------------------------------------------------------

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "000000"
)

cursorObject = dataBase.cursor()                                                          # preparing a cursor object

cursorObject.execute("CREATE DATABASE IF NOT EXISTS marveldatabase")                      # creating database

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "marveldatabase",
    password = "000000"
)

cursor = connection.cursor()                                                        

if connection.is_connected ():
    db_Info = connection.get_server_info()
    print ("Connected to MySQL server version ", db_Info)

    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)
    
    table = cursor.execute('''CREATE TABLE IF NOT EXISTS movies_data (              
                    ID int(10) NOT NULL,
                    MOVIE varchar(250) NOT NULL,
                    DATE DATE,
                    MCU_PHASE varchar(50),
                    PRIMARY KEY (ID)
                  )''')                                                                   # create movies_data table
    print("movies_data table created successfully ")

    cursor.execute("SHOW TABLES")
    for table_name in cursor:
        print(table_name)

    cursor.execute("SELECT COUNT(*) FROM movies_data;")                                   # handling duplicates
    row_count = cursor.fetchone()[0]

    if row_count > 0:
        print("Table already filled. Skipping data insertion.")
    else:
        with open('/Users/tareq2000mf/Documents/Uni/2nd year/SE226/Lab9/Marvel.txt', 'r') as file:
            for line in file:
                line = line.strip().split()
                movie_id = int(line[0])
                movie_name = line[1]
                movie_date = datetime.strptime(line[2], '%B%d,%Y').date()
                formatted_date = movie_date.strftime('%Y-%m-%d')
                mcu_phase = line[3]
                cursor.execute("INSERT INTO movies_data (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)",
                       (movie_id, movie_name, formatted_date, mcu_phase))
            print("Data inserted successfully")    
    
    # Committing the changes to the database
    connection.commit()
    
    cursor.execute("SELECT * FROM movies_data;")                                        # print all data from the table
    data = cursor.fetchall()
    for x in data:
        print(x)

    connection.close()

# GUI ---------------------------------------------------------------------------------------------------------------------

# function to handle the "Add" button click event
def addBtnClick():
    # Create a pop-up window
    popup_window = Toplevel(root)
    popup_window.title("Add New Movie")

    # create a text box and two buttons in the pop-up window and their functions
    entry_text = Text(popup_window, height = 5, width = 30)
    entry_text.pack()

    def okBtnClick():
        connection = mysql.connector.connect( host = "localhost", user = "root", database = "marveldatabase", password = "000000")
        cursor = connection.cursor()   
        entry_data = entry_text.get("1.0", END).strip()                                 # get the contents of the text box
        # Add the entry to the database 
        for line in entry_data.splitlines():
            line = line.strip().split()
            movie_id = int(line[0])
            movie_name = line[1]
            movie_date = datetime.strptime(line[2], '%B%d,%Y').date()
            formatted_date = movie_date.strftime('%Y-%m-%d')
            mcu_phase = line[3]
            cursor.execute("INSERT INTO movies_data (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)",
                    (movie_id, movie_name, formatted_date, mcu_phase))
        connection.commit()                                                             # push it to databse
        print("Data inserted successfully")    
        connection.close()
        listallBtnClick()
        messagebox.showinfo("Movie Added", f"The movie was added to the database successfully.")
        popup_window.destroy()                                                          # close the pop-up window

    ok_button = Button(popup_window, text = "Ok", command = okBtnClick)
    ok_button.pack(side = LEFT)

    def cancelBtnClick():
        popup_window.destroy()                                                          # close the pop-up window without any action

    cancel_button = Button(popup_window, text = "Cancel", command = cancelBtnClick)
    cancel_button.pack(side = LEFT)

# function that handle the "LIST ALL" button click 
def listallBtnClick():
    connection = mysql.connector.connect(host="localhost", user="root", database="marveldatabase", password="000000")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies_data;")                                        # fetch all data from the table
    data = cursor.fetchall()
    Data = {x[0]: (x[1],x[2], x[3]) for x in data}                                      # get data from the databse and store it in dic
    text_box.delete(1.0, END)                                                           # clear the text box
    for key, value in Data.items():                                                     # display the data in the text box
        text_box.insert(END, f"Key: {key}\n")
        text_box.insert(END, f"Value: {value}\n")
        text_box.insert(END, "-" * 82 + "\n")
    connection.close()

# function that handle the dropdown command 
def findData(self):
    connection = mysql.connector.connect( host = "localhost", user = "root", database = "marveldatabase", password = "000000")
    cursor = connection.cursor()   
    ID = clicked.get()[1:-2]
    cursor.execute(f"SELECT ID, MOVIE, DATE, MCU_PHASE FROM movies_data WHERE ID = {ID}")
    movieInfo = cursor.fetchall()
    connection.close()
    text_box.delete(1.0, END)                                                           # Clear the text box
    text_box.insert(END, movieInfo)                                                     # display the data in the text box
    pass 
    
# create the main window
root = Tk()
root.title("Marvel Movies")
root.geometry("600x400")
root.resizable(False, False)

# create 2 buttons, a dropdown list and a textbox
# create the "Add" button
add_button = Button(text = "Add", command = addBtnClick, height = 2, width = 15)
add_button.place(x = 275, y = 10)

# create the dropdown list
connection = mysql.connector.connect( host = "localhost", user = "root", database = "marveldatabase", password = "000000")
cursor = connection.cursor()
cursor.execute("SELECT ID FROM movies_data")
IDs = cursor.fetchall()
connection.close()
options = []
for ID in IDs:
     options.append(ID)

# datatype of menu text
clicked = StringVar(root)
# initial menu text
clicked.set("ID")
dropdown = OptionMenu(root, clicked, *options, command = findData)
dropdown.place(x = 450, y = 20)


# create the text box
text_box = Text(root, height = 25, width = 83)
text_box.place(x = 5, y = 60)

# create the "LIST ALL" button
listall_button = Button(root, text = "LIST ALL", command = listallBtnClick, height = 2, width = 15)
listall_button.place(x = 100, y = 10)

# start the Tkinter event loop
root.mainloop()
