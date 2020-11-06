# def say_hello(name='Default'):
#     print(f'Hello {name}')

# def add_num(num1,num2):
#     return num1 + num2

# res = add_num(3,4)


# def print_result(a,b):
#     print(a+b)

# def return_result(a,b):
#     return a + b

# res = print_result(10,20)

# def even_check(number):
#     return number % 2 == 0

# print(even_check(20))

# ~~~~~~~RETURN TRUE IF ANY NUMBER IS EVEN INSIDE OF A LIST~~~~~
# def check_even_list(num_list):

#     # placeholder variables
#     even_numbers = []

#     for number in num_list:
#         if number % 2 == 0:
#             even_numbers.append(number)
#         else:
#             pass

#     return even_numbers

# print(check_even_list([1,3,5]))

# print(check_even_list([1,2,3,45,67,88,94,101]))


# stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]
# for ticker,price in stock_prices:
#     print(price + (0.1*price))


# work_hours = [('Abby',100),('Billy',4000),('Cassie',800)]

# def employee_check(work_hours):

#     current_max = 0
#     employee_of_month = ''

#     for employee,hours in work_hours:
#         if hours > current_max:
#             current_max = hours
#             employee_of_month = employee
#         else:
#             pass

#     # Return
#     return (employee_of_month,current_max)

# print(employee_check(work_hours))
# result = employee_check(work_hours)
# name,hours = employee_check(work_hours)

# print(result)
# print(name)
# print(hours)

# example = [1,2,3,4,5,6,7]

# from random import shuffle

# def shuffle_list(mylist):
#     shuffle(mylist)
#     return mylist

# mylist = [' ','O',' ']

# def player_guess():
#     guess = ''

#     while guess not in ['0','1','2']:
#         guess = input('Pick a number: 0,1, or 2 ')
#     return int(guess)

# def check_guess(mylist,guess):
#     if mylist[guess] == 'O':
#         print("Correct!")
#     else:
#         print('Wrong guess!')
#         print(mylist)

# # INITIAL LIST
# mylist = [' ', 'O', ' ']
# # SHUFFLE LIST
# mixedup_list = shuffle_list(mylist)
# # USER GUESS
# guess = player_guess()
# # CHECK GUESS
# print(check_guess(mixedup_list,guess))

# def myfunc(a,b,c=0,d=0):
#     # Returns 5% of the sum of a and b 
#     return sum((a,b,c,d)) * 0.05

# print(myfunc(40,60,100,200))

# def myfunc(*args):
#     for item in args:
#         print(item)

# print(myfunc(40,60,100))

# def myfunc1(**kwargs):
#     if 'fruit' in kwargs:
#         print('My fruit of choice is {}'.format(kwargs['fruit']))
#     else:
#         print('I did not find any fruit here')

# print(myfunc1(fruit = 'apple', veggie = 'lettuce'))

# def myfunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print('I would like {} {}'.format(args[0],kwargs['fruit']))

# myfunc(10,20,30,fruit = 'orange', food = 'eggs',animal = 'dog')

# def myfunc(*args):
#     mylist = []

#     for i in args:
#         mylist.append(i)

#     return mylist

# print(myfunc(1,2,3,4,5,6))

def myfunc(str):
    mylist = []
    newlist = []

    for x in str:
        mylist.append(x)
        if mylist.index(x) % 2 == 0:
            newlist.append(x.upper())
        elif mylist.index(x) % 2 != 0:
            newlist.append(x.lower())
        else:
            pass

    y = ''.join(newlist)
    return y


print(myfunc('Anthropology'))