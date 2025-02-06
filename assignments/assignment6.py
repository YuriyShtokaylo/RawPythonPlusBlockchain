import json
import pickle


INPUT_FILE = 'demo.txt'
JSON_FILE = 'demo1.txt'
PICKLE_FILE = 'demo2.txt'


def read_file():
    with open(INPUT_FILE, mode='r') as f:
        line = f.readline()
        while line:
            print(line)
            line = f.readline()


def print_json(data):
    with open(JSON_FILE, mode='w') as f:
        json.dump(data, f)


def print_pickle(data):
    with open(PICKLE_FILE, mode='wb') as f:
        f.write(pickle.dumps(data))


def do_stuff():
    work = True
    user_input = []
    while work:
        data = input()
        user_input.append(data)
        with open(INPUT_FILE, mode='a') as f:
            row = f'{data}\n'
            f.write(row)
        if data == 'q':
            work = False
        elif data == 'o':
            read_file()
        elif data == 'p':
            print_json(user_input)
            print_pickle(user_input)
         
      
do_stuff()                   