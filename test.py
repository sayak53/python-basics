#1.Write a Program to input 2 numbers & print their sum.
# num1=float(input('Enter 1st number:'))
# num2=float(input('Enter 2nd number:'))
# sum = num1+num2
# print(f'the sum of {num1} and {num2} is {sum}')


#2.WAP to input 2 int numbers, a and b.
#Print True if a is greater than or equal to b. If not print False.
# a=float(input('Enter 1st number:'))
# b=float(input('Enter 2nd number:'))
# print(a>b)


#3.WAP to input user’s first name & print its length.
# str=input('Enter your first name:')
# length=len(str)
# print(f'the length of {str} is {length}')


#4.WAP to find the occurrence of ‘$’ in a String.
# str='f$hbdgh$dbkk$dghjkdhgk$gjkhgkjh$jhdgkjsh$'
# print(str.count('$'))


#5.WAP to check if a number entered by the user is odd or even.
# num=int(input('enter a number:'))
# if num%2==0:
#     print(f'{num} is even')
# else:
#     print(f'{num} is odd')


#6.WAP to find the greatest of 3 numbers entered by the user.
# num1=int(input('enter 1st number:'))
# num2=int(input('enter 2nd number:'))
# num3=int(input('enter 3rd number:'))
# if num1>num2:
#     if num1>num3:
#         print(f'{num1} is biggest')
#     else:
#         print(f'{num3} is biggest')
# elif num2>num3:
#     print(f'{num2} is biggest')
# else:
#     print(f'{num3} is biggest')


#7.WAP to check if a number is a multiple of 7 or not.
# num = float(input('enter the num:'))
# if(num%7==0):
#     print('multiplied by 7')
# else:
#     print('not multiplyed by 7')


#8.WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# movielist = []
# for i in range(3):
#     list = input('enter a movie name:')
#     movielist.append(list)   
# print(f'your favourite movies are: {movielist}')


# 9.WAP to check if a list contains a palindrome of elements.
# user_input = input('enter the list items separated with space:')
# if " " not in user_input:
#     print('please separate them with space(eg.1 2 1 3 2)')
# else:
#     original_list = user_input.split()   
# copied_list = original_list.copy()
# copied_list.reverse()
# if copied_list == original_list:
#     print('yup! its palindrome')
# else:
#     print('oops! try a diiferent pattern')


#10.WAP to count the number of students with the “A” grade in the following tuple.
# Store the above values in a list & sort them from “A” to “D”.[”C”,“D”,“A”,“A”,“B”,“B”,
# grades = ["C", "D", "A", "A", "B", "B"]

# # Count A grades
# count_A = grades.count("A")
# print("Number of students with A grade:", count_A)

# # Sort grades
# grades.sort()
# print("Sorted grades:", grades)
