
# 1.What is the syntax for creating an empty list in Python?
# my_list = []
# print(my_list)

# 2.How do you access the third element in a list named my_list?
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(my_list[2])

# 3.Write a Python code snippet to add an element 'apple' to the end of a list named fruits.
# fruits = ["mango", "orange", "lemon", "tangerine", "lime"]
# fruits.append("apple") #using the .append() to add an item to the list
# print(fruits)

# 4.How do you remove the third element from a list named numbers?
# numbers = [0, 1, 2, 3, 4, 5, 6, 7]
# numbers.pop(2)
# print(numbers)

# 5.Explain the difference between the append() and extend() methods in Python lists.

# #APPEND
# places = ["ikeja", "balogun", "cms", "lekki", "ipaja"] # making a list of places
# places.append("egbeda")     # using APPEND method to add an object to the list
# print(places)

# #EXTEND
# more_places = ["ayobo", "ajah"] # making a list of more places
# more_places.extend(places) # using the extend method to add anoth list within the list
# print(more_places)

# # both methods are used to add objects to the end of the list, the list method will treat the object being inserted as a 
# #single object while the extend method will treat the new object like a list.

# 6.Write a Python code snippet to check if an element 'banana' exists in a list named fruits.
# fruit_names = ["orange", "lemon", "grape", "banana", "ginger"]
# if "banana" in fruit_names:
#     print("found banana")

# 7. What will be the output of len(['a', 'b', 'c'])?
# lenght1 = len(["a", "b", "c"])
# print(lenght1) #the output is 3

# 8. How do you reverse the order of elements in a list named my_list?
# my_list = ["orange", "lemon", "grape", "banana", "ginger"]
# reverse_list = my_list[::-1]
# print(reverse_list)

# 9.Explain the purpose of the sort() method in Python lists.
# num1 = [10, 40, 20, 90, 30, 500, 15]
# num1.sort() #the sort method is used to rearrange numbers either in ascending or descending order
# print(num1)

# 10.Write a Python code snippet to create a list containing the squares of numbers from 
# number = [3,4,5,6,55,4,322,33,34]
# nums = [x**2 for x in number]
# print(nums)

# 11. What is a string in Python?
# string is one of the fundamental data types in python, it could be numbers or alphabeth or symbols.
# it is indicated by a single or double or tripple quotation mark
# it is the most used data type in python

# print("hello world") # hello world here is a string.

# 12. How do you create an empty string?
# emp_str = ""
# print(emp_str) #example of an emplty string

# 13. Can you access characters in a string using indexing?
# test_str = "i love python"
# print(test_str[2:]) #example of accessing a string using indexing
# 14. How do you find the length of a string?

# test_str = "i love python"
# print(len(test_str)) #you can check the lenght of a string using the len() method

# 13. How do you concatenate two strings?

# name = "kelvin"
# name2 = "smith"
# print(name + " " + name2 + " "+ "ogbewele")

# 14. How do you convert a string to uppercase?
# test_str = "i love python"
# print(test_str.upper())

# 15. How do you convert a string to lowercase?
# test_str = "i love PYTHON"
# print(test_str.lower())

# 16. How do you check if a substring exists in a string?

# test_str = "i love python"
# print(test_str.find("py"))

# 17. How do you make a string into a list of substrings?

# test_str = "i love python"
# test = test_str.split()
# print(test)

#converting a list to a string with .join()
# names = ["kelvin", "smith", "loves python"]
# string = " ".join(names)
# print(string)

# 18. How do you replace occurrences of a substring within a string?
# python = "i hate python"
# old_word = "hate"
# new_word = "love"
# new_python = python.replace(old_word, new_word)
# print(new_python)

# # 19. How do you find the index of a substring within a string?
# python = "i love python"
# print(python.index("love"))

# 20. How do you iterate over the characters of a string?
# python = "i love python"
# for i in python:
#     print(i)

# 21. How do you reverse a string in Python?
# python = "i love python"
# print(python[::-1])

# 22. How do you convert an integer or float to a string?
# num1 = 555
# print(str(num1))

# # 23. How do you check if a string contains only digits?
# python = "i love python 123"
# print(python.isalnum())

# 24. Write a Python code snippet to create an empty list.
# emp_list = []
# print(emp_list)

# 25. How do you add an element to the end of a list in Python?
# names = ["dog", "rat"]
# names.append("duck")
# print(names)

# 27. Write a Python function to find the sum of all elements in a list of numbers.
# list = [1,3,2,33,445,3,2]
# sum1 = 0
# for i in list:
#     sum1 = sum1 + i
# print(sum1)
# print(sum(list))

# 29. Write a Python function to find the maximum and minimum elements in a list of numbers.
# list = [1,3,2,33,445,3,2]
# max_num = max(list)
# min_num = min(list)
# print(max_num)
# print(min_num)


# 30. Explain the concept of list comprehension in Python with an example.
#list comprehension is the creation of a list within a list using a single line of code
# list = [1,3,20,33,445,3,2]
# evens = []
# odd = []
# for num in list:
#     if num % 2 ==0:
#         evens.append(num)
#     elif num % 2 ==1:
#         odd.append(num)
# print("the even numbers are:" + str(evens))
# print(odd)
# even = [num1 for num1 in list if num1 %2 ==0]
# odds = [num2 for num2 in list if num2 %2 ==1]
# print(even)
# print(odds)


# # 31. How do you check if a specific element exists in a list in Python?
# list = ["sarah", "romeo", "tina"]
# if "tina" in list:
#     print("yes, found it")
# else:
#     print("false oh")


# 32. how do you reverse a list.
# list = ["sarah", "romeo", "tina"]
# list.reverse()
# print(list)