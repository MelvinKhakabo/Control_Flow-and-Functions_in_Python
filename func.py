#creating empty function
#example 1
# def add_nums():
#     print(2+13)
# add_nums()

#example 2
# def hello_func():
#     print("Hello Function!")
# hello_func()
#using return fx
# def hello_func():
#     return 'Hello Function.'
# print(hello_func())


#example 3
# def greet():
#     print("Hello")
#     print("How do you do?")
# greet()
#adding an argument
# def greet(name):
#     print("Hello", name)
#     print("How do you do?")
# greet("Melvin")

#example 4
# def add_numbers(n1, n2):
#     result = n1 + n2
#     print("The sum is", result)

# number1 = 6.7
# number2 = 5.4
# add_numbers(number1, number2)
#using return function
# def add_numbers(n1, n2):
#     result = n1 + n2
#     return result
# number_1 = 6
# number_2 = 5
# result = add_numbers(number_1, number_2)
# print("The sum is:", result)


#length fx
# marks = [55, 64, 75, 80, 34]
# length = len(marks)
# print("Length is", length)

#sum fx
# marks = [55, 64, 75, 80, 34]
# sum = sum(marks)
# print("The sum is", sum)


# #function to find average marks
# def find_average_marks(marks):
#     sum_of_marks = sum(marks)
#     total_subjects = len(marks)
#     average_marks = sum_of_marks / total_subjects
#     return average_marks

# #calculate grade
# def compute_grade(average_marks):
#     if average_marks >= 80:
#         grade = "A"
#     elif average_marks >= 60:
#         grade = "B"
#     elif average_marks >= 50:
#         grade = "C"
#     else:
#         grade = "F"
#     return grade

# marks = [55, 64, 75, 80, 65]
# average_marks = find_average_marks(marks)
# print("Your average marks is:", average_marks)

# grade = compute_grade(average_marks)
# print("Your grade is:", grade)


#function that adds and multiplies two numbers
# function to add two numbers
# def add_numbers(num1, num2):
#     return num1 + num2

# # function to multiply two numbers
# def multiply_numbers(num1, num2):
#     return num1 * num2

# number1 = 5
# number2 = 30

# sum_result = add_numbers(number1, number2)
# print("Sum is", sum_result)

# product_result = multiply_numbers(number1, number2)
# print("Product is", product_result)