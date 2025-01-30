#Defining and assigning variables
name = input('Please enter your name: ')#'Yuriy'
age = input('Please enter your age: ')#31

#Constant data
decade = 10

#Functions used for assignment
def message(name = 'Yuriy', age = 31):
    """
    Form response string
        Arguments:
        :name: Name
        :age: Age
    """
    return f'My name is {name}. I am {age} years old.'


def display_some_data(data0, data1):
    """ Print some data """
    print(message(data0, data1))
    
    
def count_decades(age = 31):
    """ Count number of dacedes based on age"""
    print(f'You already lived {int(age)//decade} decades')    
    

display_some_data(name, age)
count_decades(age)    