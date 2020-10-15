# Numbers: Consist of integers, floating points and etc..
# Strings: Consist of characters that are wrapped within a '' (single quote) or "" (double quotes)
# Lists: Consist of a group of elements within brackets []
# Tuples: Are like list, however, tuples are immutable
# Dictionaries: Which are also like objects; contain a key and value such as {key:value}

#------NUMBERS------
# 4 * (6 + 5) = 44
print(4 * (6 + 5))
# 4 * 6 + 5 = 29
print(4 * 6 + 5)
# 4 + 6 * 5 = 50 --> wrong: PEMDAS still applies
print(4 + 6 * 5)
# type(3 + 1.5 + 4) --> 'float'
print(type(3 + 1.5 + 4))
# to find a number's square root: import math then math.sqrt(x)
# to find a number's square: x**y

#------STRINGS------
s = 'hello'
print(s[1]) # --> grabs 'e'
# reverse the string using slicing
print(s[::-1])
# give two methods to print the 'o' in 'hello'
print(s[4])
print(s[4:])

#------LISTS------
a_list = [0,0,0]
print(a_list)
#second way
a_list[0] = 0
a_list[1] = 0
a_list[2] = 0
print(a_list)

# change 'hello' to 'goodbye'
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

# sort the list
list4 = [5,3,4,6,1]
list4.sort()
print(list4)

#------DICTIONARIES------
# grab the word 'hello' from the following dictionaries
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# you cannot sort a dictionary; why -->

#------TUPLES------
# The major difference between tuples and list is that tuples are immuatble where list are mutable
# To create a tuple you use (), ex: mylist = (1,2,3)

#------SETS------
# Sets are unique because they only contain unique values
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

#FINAL QUESTION (BONUS)
# --> FALSE