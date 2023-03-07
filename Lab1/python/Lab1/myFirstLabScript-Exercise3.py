#SE226 – LAB#1
#Exercise-3
StudentName  = input("Please enter your Full Name : ")
labGrade     = input("Please enter your Lab grade : ")
midtermGrade = input("Please enter your Midterm grade : ")
finalGrade   = input("Please enter your Final grade : ")
lastScore    = ((int(labGrade) * 25 / 100) + (int(midtermGrade) * 35 / 100) + (int(finalGrade) * 40 / 100))
print(
"============= Printing Data =============" + "\n" +
    "Name:       " + StudentName + "\n" +
    "Lab:        " + str(labGrade) + "\n" +
    "Midterm:    " + str(midtermGrade) + "\n" +
    "Final:      " + str(finalGrade) + "\n" +
    "Last score: " + str(lastScore) + "\n"
)