def normal(*args, func=lambda a : int(a)):
    for arg in args:
        print(f'{func(arg):^20d}')


normal(1)       

normal(1, 2, 3, 4, 5, func=lambda a : int(a) ** 3) 