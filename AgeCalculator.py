from datetime import *
try:
	while(1):
		day=int(input("Enter your birth date as number: ")) 
		month=int(input("Enter your birth month as number "))
		year=int(input("Enter your birth year"))
		dob=date(year,month,day)
		print("your dob in year-month-day format =",dob)
		today=datetime.now().date()
		age=(today-dob)/timedelta(days=365.24)
		if age<0 :
			print("Please enter the correct DOB")
		else:
			print("Your age is",round(age,2),"years..!!!")
			break
except ValueError as e:
	print("Dob issue ",e)
