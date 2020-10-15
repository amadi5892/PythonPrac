mylist = [1,2,3,4,5,6,7,8,9,10]
for jelly in mylist:
    print('hello')

for num in mylist:
    #Check for even
    if num % 2 == 0:
        print(f'Even Number: {num}')
    else:
        print(f'Odd Number: {num}')