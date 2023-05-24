### Lab9: Designing a simple Graphical User Interface and using database operations
### Instructions:

In today’s lab, you will read a file and put the data into MySql database. You will create a table according to the followig steps.
First, please download “Marvel.txt” from Blackboard under Lab 9 folder. You will read this file into your script.

1. The file contains several lines in this format:
```
ID  MOVIE     DATE       MCU-PHASE
--  -----   ---------   ----------
4    Thor   May6,2011     Phase1
```

2. Create a table according to the information given in 1. You have ID(int), MOVIE(String), DATE(date) and MCU_PHASE (String). 

3. After you create the table and your database is ready, read the file line by line and populate your table.

4. Please design an interface which is a box with 2 buttons, 1 dropdown list and a textBox.

5. The dropdown list should have the id’s. When you choose one, it will be printed on the text box. If you choose another id, you need to remove the previous contents in the text box and put new data.

6. The first button is called “Add” and when clicked it will open up a pop up box with a textBox and 2 buttons inside. First button is “Ok”, second “Cancel”. “Ok” will try to add the textBox contents to database. “Cancel” just closes the pop up box without doing nothing. Try adding to following:
```
ID          MOVIE               DATE        MCU-PHASE 
--  ----------------------   -----------   ----------
23  Spider-Man:FarFromHome    July2,2019     Phase3
```

7. The second button is called “LIST ALL” and when clicked, it will print everything from database to textBox.

Output:

![ezgif com-gif-maker](https://github.com/tareqalhammoodi/SE226-Lab/assets/44919941/32d7c354-7e42-43ca-adce-dd07ae1092d8)


Databse check:


<img width="850" alt="Screenshot" src="https://github.com/tareqalhammoodi/SE226-Lab/assets/44919941/813a0097-db46-4bd9-b7a1-0e5e545e3fc4">
