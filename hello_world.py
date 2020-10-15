print('This is a string {}'.format('INSERTED'))
# This is a string INSERTED
# print('The {0} {0} {0}'.format('fox','brown','quick'))
# The fox fox fox //if there are more arguments than the ones being used, an error will be presented, but code still runs
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))
# The quick brown fox

result = 100/777
result = 104.12345
print('The result was {r}'.format(r = result))
print('The result was {r:10.5f}'.format(r = result))

name = "Jose"
print(f'Hello, his name is {name}') #formatted string literals

name = 'Sam'
age = 3
print(f'{name} is {age} years old.')

my_list = [1,2,3]
my_list = ['STRING',100,23.2]
print(len(my_list))

mylist = ['one','two','three']
print(mylist[1:])
another_list = ['four','five']
new_list = mylist + another_list
new_list[0] = 'ONE ALL CAPS'
print(new_list)
new_list.append('six')
# .append() adds items to the end of a list
print(new_list)
print(new_list.pop())
# .pop() removes an item from the end of a list
print(new_list)
new_list.pop(0)
print(new_list)

new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]
new_list.sort()
print(new_list)
# A None object is a return value for something that doesn't have a value
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)

my_dict = {'key1' : 'value1','key2':'value2'} #dictionary
print(my_dict)
prices_lookup = {'apple':2.99,'oranges':1.99,'milk':5.99}
print(prices_lookup['apple'])
d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}
print(d['k3']['insideKey'])
print(d['k2'])

d = {'key1':['a','b','c']}
my_list = d['key1']
letter = my_list[2]
print(letter.upper())
print(d['key1'][2].upper())
d['key3']=100
print(d)

# Tuple
t = (1,2,3)
mylist = [1,2,3]
print(type(t))
t = ('a','a','b')
print(t.count('a'))
mylist[0] = 'NEW'

# Sets
myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)

# Booleans
print(1 == 1)

myfile = open('d:\\Users\\User\\Desktop\\Python Notes & Resources\\test.txt')
print(myfile.readlines())
# ['Hello this is a text file\n', 'this is the second line\n', 'this is the third line']

with open('d:\\Users\\User\\Desktop\\Python Notes & Resources\\test.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)

with open('d:\\Users\\User\\Desktop\\Python Notes & Resources\\test.txt','r') as f:
    print(f.read())

path = 'd:\\Users\\User\\Desktop\\Python Notes & Resources\\'
with open(path + 'test2.txt', 'w') as f:
    f.write('I CREATED THIS FILE!')

with open(path + 'test2.txt', 'r') as f:
    print(f.read())

hungry = True

if hungry:
    print('FEED ME!')
else:
    print("I'm not hungry")