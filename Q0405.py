"""
Write a program that asks a user score in percentage and display the 
grade with some remarks as follows:
Temperature	Grade	Remarks
below 60%	C	Work hard otherwise you're going to fail the exam.
61% to 70%	B	Your result is satisfactory.
71% to 80%	B+	Good Job, Keep doing better.
81% to 90%	A	Amazing Your hard work paid off.
above 90%	A+	Excellent work, Congratulations topper!!

"""
grade = int(input("Enter Your grade: "))

if grade < 60:
    print('Your grade is {grade}.\n "Work hard otherwise you  are  going to fail the exam."') 
if (grade <=60 and grade > 70):
    print('your result is satisatactory.')
if (grade <=70 and grade > 80):
    print('good job, keep doing better.')

if (grade >80 and grade <= 90):
    print('Amazing your hard wordk paid of.f')
if grade < 90:
    print("A+ '\n' Excellent work, congratulations to topper!!")










    










