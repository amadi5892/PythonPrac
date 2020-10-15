print('This is a string {}'.format('INSERTED'))
# This is a string INSERTED
print('The {0} {0} {0}'.format('fox','brown','quick'))
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