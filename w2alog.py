# 1.Write a Python program to check if a given number is even and divisible by 3 using if and else statements. if the number is even print BUZZ if the number is divisible by three let it print FIZZ
# num1 = int(input("please enter any number: \n"))
# if num1 %2 == 0:
#     print("BUZZ")
# elif num1 %3 ==0:
#     print("FIZZ")


# 2.Create a program that asks the user to input their age and then outputs whether they are eligible to vote or not using if and else.
# age = int(input("please enter your age: \n"))

# if age >= 18:
#     print("congratulations, you are eligible to vote.")
# else:
#     print("sorry, youre not eligible to vote.")


# 3.Write a Python program that takes a user input for a number and prints "Positive" if it's greater than zero, "Negative" if it's less than zero, and "Zero" if it's equal to zero using if, elif, and else.
# num1 = int(input("please enter a number: \n"))
# if num1 > 0:
#     print("Positive")
# elif num1 < 0:
#     print("Negative")
# else:
#     print("Zero")


# 4. Create a program that print multiplication table when a user input any number using while loop and for loop
# num1 = int(input("please enter a number: \n"))
# for i in range(1, num1):
#     print(f"{num1} {"x"} {i} {"="} {num1*i}")

# i=1
# while i <= num1:
#     print(num1, "x", i, "=", num1*i)
#     i = i+1


# 5. Write a Python program that compares two numbers provided by the user and prints the larger number using if and else.
# num1 = int(input("please enter your first number: \n"))
# num2 = int(input("please enter your second number: \n"))

# if num1 > num2:
#     print(num1, "is greater than ", num2)
# else:
#     print(num2, "is greater than ", num1)


# 6. Create a program that takes a user input for a grade such that grade between 90 - 100 should print Grade A, grade between 70 - 89 should print Grade B, grade 
# between 50 - 69 should print Grade C, grade between 40 - 49 should print  Fail and grade between 0 to 39 should print unknown Results. 

# num1 = int(input("please enter the grade: \n"))
# if num1 in range(90,100+1):
#     print("Grade A")
# elif num1 in range(70,89+1):
#     print("Grade B")
# elif num1 in range(50,69+1):
#     print("Grade C")
# elif num1 in range(40,49+1):
#     print("Fail")
# elif num1 in range(0,39+1):
#     print("unknown result")


# 7. Write a program that asks the user to input their salary and then calculates their tax based on the following conditions: if salary is less than or equal to 5000, tax is 10%; if salary is between 5001 and 10000, tax is 20%; otherwise, tax is 30% using if, elif, and else.

# salary = int(input("please enter your salary: \n"))
# percentage10 = salary * 10/100
# percentage20 = salary * 20/100
# percentage30 = salary * 30/100

# if salary <= 5000:
#     tax = percentage10
#     print("your tax for the month is: ", tax)
# elif salary in range(5001, 10000):
#     tax = percentage20
#     print("your tax for the month is: ", tax)
# else:
#     tax = percentage10
#     print("your tax for the month is: ", tax)


# 8.Create a program that asks the user to input two numbers and then checks if their sum is greater than 100. If it is, print "Sum is greater than 100", otherwise print "Sum is not greater than 100" using if and else.
# num1 = int(input("please enter your first number: \n"))
# num2 = int(input("please enter your second number: \n"))
# sum = num1 + num2
# print(sum)
# if sum > 100:
#     print("Sum is greater than 100")
# else:
#     print("Sum is not greater than 100")



# # 9.Write a Python program that takes three numbers from the user and prints the largest among them using nested if-else statements.
# num1 = int(input("please enter your first number: \n"))
# num2 = int(input("please enter your second number: \n"))
# num3 = int(input("please enter your third number: \n"))

# if (num1 > num2) and (num1 > num3):
#     print("your first number is the largest one.")
# elif (num2 > num1) and (num2 > num3):
#     print("your second number is the largest one.")
# elif (num3 > num1) and (num3 > num2):
#     print("your third number is the largest one.")



# 10. Create a program that takes a user input for their age and then checks if they are eligible for a senior citizen discount (age 60 or above). If they are eligible, print "You are eligible for a senior citizen discount", otherwise print "You are not eligible for a senior citizen discount" using if and else
# age = int(input("please enter your age: \n"))
# if age >= 60:
#     print("congratulations, you are eligible for senior citizen discount.")
# else:
#     print("you are not eligible for a senior citizen discount.")



# 11. create a program for a guessing game when the user guess right it should tell the user that your are right with a congratulation message printed and if the user get it wrong the user should be ask to conttinue trying till the user get the game right
# import random
# while True:
#     number = random.randint(1,10)
#     user = int(input("guess the number: "))
#     if user == number:
#         print("congratulations!!")
#         print(f"{number} is the correct guess")
#         break
#     elif user != number:
#         print(f"your guess is incorrect, {number} is the correct guess")

# import random
# while True:
#     number = random.randint(1, 11)
#     user = int(input("guess a number: "))
#     if user == number:
#         print("congratulations")
#         print(f" {number} is the correct number.")
#         break
#     elif user != number:
#         print(f"you didnt get, try again. the correct answer is {number}.")




# practice

# nums = int(input("please enter a number: "))
# n = 1
# while n <= nums:
#     print(f"{nums} 'x' {n} '=' {nums*n}")
#     n += 1

# nums = int(input("please enter a number: "))
# for n in range(1, nums):
#     if n <= nums:
#         print(f"{nums} 'x' {n} '=' {nums*n}")