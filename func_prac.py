# def lesser_of_two_evens(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         if a < b:
#             print(a)
#         else:
#             print(b)
#     elif a % 2 != 0 or b % 2 != 0:
#         print(max(a,b))
#     else:
#         pass

# lesser_of_two_evens(2,4)


# def animal_crackers(str):
#     mylist = str.lower().split()
    
#     if mylist[0][0] == mylist[1][0]:
#         return True
#     else:
#         return False

# print(animal_crackers('Crazy cat'))


# def makes_twenty(n1,n2):
#     if n1 == 20 or n2 == 20:
#         return True
#     elif (n1 + n2) == 20:
#         return True
#     else:
#         return False

# print(makes_twenty(20,10))
# print(makes_twenty(12,8))
# print(makes_twenty(2,3))


# def old_macdonald(str):
#     mylist = []
#     newlist = []

#     for x in str:
#         mylist.append(x)
#     mylist[0] = mylist[0].capitalize()
#     mylist[3] = mylist[3].capitalize()
    
#     y = ''.join(mylist)

#     return y 

# print(old_macdonald('macdonald'))


# def master_yoda(str):
#     mylist = str.split()
#     mylist.reverse()
#     y = ' '.join(mylist)
#     print(y)

# master_yoda('I am home')
# master_yoda('We are ready')


# def almost_there(n):
#     if 190 <= n <= 210 or 90 <= n <= 110:
#         return True
#     else:
#         return False

# print(almost_there(90))
# print(almost_there(104))
# print(almost_there(150))
# print(almost_there(209))


# def has_33(nums):
#     i = 0
    
#     for x in nums:
#         i +=1 
#         if nums[i] == 3 and nums[i+1] == 3:
#             return True
#         else:
#             return False

# print(has_33([1,3,3]))
# print(has_33([1,3,1,3]))
# print(has_33([3,1,3]))



# def paper_doll(str):
#     mylist = []
#     i = 0

#     for x in str:
#         mylist.append(str[i]*3)
#         i += 1

#     y = ''.join(mylist)
#     return y 

# print(paper_doll('Hello'))


# def blackjack(a,b,c):
#     if (a+b+c) <= 21:
#         return a+b+c
#     elif (a+b+c) > 21:
#         if a == 11 or b == 11 or c == 11:
#             if ((a+b+c) - 10) > 21:
#                 return 'BUST'
#             else:
#                 return (a+b+c) - 10
#         else:
#             return 'BUST'
#     else:
#         return 'BUST'

# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))


# def summer_69(arr):

#     while True:
#         if 6 not in arr:
#             return sum(arr)


#         indexOf6 = arr.index(6)
#         indexOf9 = arr.index(9)
#         del arr[indexOf6:indexOf9 + 1]

    
#     print(indexOf6)
#     print(indexOf9)
#     print(arr)

# print(summer_69([4,5,6,7,8,9,10,11,12,6,8,77,9]))


# def spy_game(nums):
#     # check for two zeros and a seven; may need a counter
#     count_for_zero = 0
#     count_for_seven = 0

#     while True:
#         for x in nums:
#             if x == 0:
#                 count_for_zero += 1
#             elif x == 7:
#                 count_for_seven += 1
#             else:
#                 pass
#         if count_for_zero == 2 and count_for_seven == 1 and nums.index(0) < nums.index(7):
#             return True
#         else:
#             return False
            


# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

# def count_primes(num):

#     #check for 0 or 1 input
#     if num < 2:
#         return 0

#     # 2 or greater

#     # Store our prime numbers
#     primes = [2]
#     # Counter going up to the input num
#     x = 3

#     # x is going through every number up to  input num
#     while x <= num:
#         # Check if x is prime
#         for y in range(3,x,2):
#             if x%y == 0:
#                 x += 2
#                 break
#             else:
#                 primes.append(x)
#                 x += 2
#         print(primes)
#         return len(primes)