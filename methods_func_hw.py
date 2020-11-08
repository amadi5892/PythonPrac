# # Volume of Sphere
# import math
# def vol(rad):
#     return (4/3)*math.pi*(rad ** 3)

# print(vol(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low)

# def ran_check(num,low,high):
#     if low < num < high:
#         return f'{num} is in the range between {low} and {high}'

# print(ran_check(5,2,7))



# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# def up_low(s):

#     # Original String
#     print(f'Original String : {s}')
#     # Counters
#     up_count = 0
#     low_count = 0
#     # Check for upper case and lowercase letters
#     for x in s:
#         if x.isupper() == True:
#             up_count += 1
#         elif x.islower() == True:
#             low_count += 1
#         else:
#             pass

#     print(f'No. of Upper Case Characters : {up_count}')
#     print(f'No. of Lower Case Characters : {low_count}')

# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# up_low(s)



# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# def unique_list(lst):
#     new_set = set(lst)
#     uni_list = list(new_set)
#     return uni_list

# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))



# Write a Python function to multiply all the numbers in a list.

# def multi(nums):

#     # holder
#     counter = 1

#     for x in nums:
#         counter *= x

#     return counter

# smpl_lst = [1,2,3,-4]

# print(multi(smpl_lst))



# Write a Python function that checks whether a word or phrase is palindrome or not

# def palindrome(s):

#     if s[::-1] == s:
#         return True
#     else:
#         return False

# print(palindrome('blue'))



# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

import string

def ispangram(str1, alphabet=string.ascii_lowercase):

    # Remove spaces from string
    no_space = str1.replace(' ','')
    low_no_space = no_space.lower()

    # find unique values
    new_set = set(low_no_space)
    
    # put values into a list
    new_list = list(new_set)
    # sort list
    new_list.sort()
    
    str1 = ''.join(new_list)

    if str1 == string.ascii_lowercase:
        return True
    else:
        return False

s = 'The quick brown fox jumps over the lazy dog'

print(ispangram(s))
