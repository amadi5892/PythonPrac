# PythonPrac

testing...

tuples are very similar to lists. However, they have one key difference, they are immutable

Sets are unordered collections of unique elements. Set has to have unique values in it, it will not repeat values. 

Open a File
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