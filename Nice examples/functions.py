def unlimited_arguments(*args, **keyword_args):
    for argument in args:
        print(argument)
    print(keyword_args)
    for key in keyword_args:
        print(key)
    for key, value in keyword_args.items():
        print(key, value)
        

#unlimited_arguments(1, 2, 3, 4)       
#unlimited_arguments([1, 2, 3, 4])    
#unlimited_arguments(*[1, 2, 3, 4])     
unlimited_arguments(1, 2, 3, 4, name='Yuriy', age=31)  