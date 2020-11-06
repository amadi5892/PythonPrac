#lEGB RULE

# x = 25

# def printer():
#     x = 50
#     return x
# print(x)
# print(printer())

# name = 'THIS IS A GLOBAL STRING'

# def greet():
    
#     name = 'Sammy'

#     def hello():
#         print('Hello '+name)

#     hello()

# greet()





x = 50

def func():
    global x 
    print(f'X is {x}')

    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED X TO {x}')

func()