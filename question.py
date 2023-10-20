# Q1 Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):
print("hello_USERNAME!")
name = Jane

print(name)
#Q2 Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
def print_add(num):
 for i in range (1,num+1):
    if i %2 !=0:
     print (i,end=",")
#Q3 Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([50, 20, -1, 100]))
#Q4 Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):
def is_leap(year):
    leap = False
    if year%400==0:
        leap = True
    elif year%4 == 0 and year%100 != 0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))
#Q5 Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))
     
list = [2, 3, 4, 5, 6]
print(checkConsecutive(list))