# Modes:
# w - write(rewrites file)(It's overwrite content by default evwn when you really didn't write nothing)
# r - read
# a - change file(append something to it)
# x - Open file only if it dosn't exist
# b - binary?

FILE = 'demo.txt'

file = open(FILE, mode='w')
file.write('Hello World from Python')
file.close() #If remove this file wouldn't be updated before code is fully executed

user_input = input('Please enter input:')


def do_stuff():
    file = open(FILE, mode='r')
    file_content = file.read()
    lines = file.readlines() # You can see that file is already fully readed
    file.close()
    print(file_content)
    print(lines)
    
    file = open(FILE, mode='r')
    lines = file.readlines() # Content is readed as list where each element represent line in file.
    file_content = file.read() # We already read all lines from file so read will not work...
    file.close()
    print(lines)
    print(file_content)
    
    # You also can read file line by line
    file = open(FILE, mode='r')
    first_line_content = file.readline()# This will read first line
    file.close()
    print(first_line_content)
    
    #Read file in a loop
    file = open(FILE, mode='r')
    line = file.readline()# This will read first line
    while(line):
        print(line)
        line = file.readline()# read next line
    file.close() 
    
    with open(FILE, mode='a') as f:
        f.write(f'\nWe already have {len(lines)}. Now lets write one more. This line is writed using WITH!')  
    

do_stuff()

file = open(FILE, mode='a')
file.write('Add one more line') #Actually it doesn't add new line :-(
file.write('\nThis will :-)')
file.write(f'\n{user_input}')
file.close()

do_stuff()