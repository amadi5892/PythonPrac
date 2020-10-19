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