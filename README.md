# PythonPrac

testing...

------Tuples-------
tuples are very similar to lists. However, they have one key difference, they are immutable

-------Sets-------
Sets are unordered collections of unique elements. Set has to have unique values in it, it will not repeat values. 

-------Open a File-------
To open a file use open() with double brackets in the file path "\\"
Then the read the file in the terminal
    print('variable assigned'.read())

    f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

"a" = Append - append to the end of the file
"w" = Write - will overwrite any existing content
"r" = Read - reads files

print(myfile.readlines())
# ['Hello this is a text file\n', 'this is the second line\n', 'this is the third line']

with open('d:\\Users\\User\\Desktop\\Python Notes & Resources\\test.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)

File creation example:
path = 'd:\\Users\\User\\Desktop\\Python Notes & Resources\\'
with open(path + 'test2.txt', 'w') as f:
    f.write('I CREATED THIS FILE!')

with open(path + 'test2.txt', 'r') as f:
    print(f.read())

------Python Practice Resources------
Basic Practice:

http://codingbat.com/python

More Mathematical (and Harder) Practice:

https://projecteuler.net/archives

List of Practice Problems:

http://www.codeabbey.com/index/task_list

A SubReddit Devoted to Daily Practice Problems:

https://www.reddit.com/r/dailyprogrammer

A very tricky website with very few hints and touch problems (Not for beginners but still interesting)

http://www.pythonchallenge.com/


-------LEGB RULE------
LEGB RULE:
    L: Local -- Names assigned in any way within a function (def or lambda), and not declared global in that function. 
    
    E: Enclosing function locals --  Names in the local scopoe of any and all enclosing functions (def or lambda), from inner to outer. 

    G: Global (module) -- Names assigned at the top-level of a module file, or declared global in a def within the file. 

    B: Built-in (Python) -- Names preassigned in the built-in names module: open, range, SyntaxError,...