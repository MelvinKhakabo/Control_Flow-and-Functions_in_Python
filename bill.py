#using if statement
# bill = 2500
# if bill > 2000:
#     print("Your bill is greater than 2000")
# else:
#     print("Your bill is below 2000")


#example 2
# work_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# day = input("What day of is it today? ")
# if work_day:
#     print("wake up at 6:30")
# else:
#     print("sleep in")


#example 3 if, elif, else
# grade = int(input("What is your score? "))
# if grade >= 90:
#     print(f"You have an:", "A")
# elif grade >= 80:
#     print(f"You have a:", "B")
# elif grade >= 70:
#     print(f"You have a:", "C")
# elif grade >= 60:
#     print(f"You have a:", "D")
# else:
#     print(f"You have an:", "F")


#nested loops
number = float(input("Enter a number "))
#outer if statement
if number >= 0:
    #inner if statement
    if number ==  0:
        print('Number is 0')
    #inner else statement
    else:
        print('Number is positive')
#outer else statement
else:
    print('Number is negative')


#checking pass or fail
# score = int(input("Enter your score "))
# if score >= 50:
#     print("Congratulations. You have passed the test")
# else:
#     print("Sorry. You have failed the test")


#pH
# pH = 2
# if pH < 7:
#     print("acidic")
# elif pH > 7:
#     print("basic")
# else:
#     print("Neutral")

#while loop
count = 0
while count <= 2:
    #loop
    print(count)
    count += 1