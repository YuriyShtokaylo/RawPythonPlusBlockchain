my_list = ['h', 'e', 'l', 'l', 'o']
my_text = 'hello'

#help(my_list)

#help(my_text)#this doesn't work

#help(str)

my_list[0] = 'c'
print(my_list)

#my_text[0] = 'c'#this doesn't work cause STRINGS ARE IMMUTABLE

name = 'Yuriy'
age = 31
long_way = 'I am ' + name + ' and I am ' + str(age) + ' years old.'
print(long_way)
#using_format = 'I am {} and I am {} years old.'.format(name, age)
#using_format = 'I am {0} and I am {1} years old.'.format(name, age)
#using_format = 'I am {name} and I am {years} years old.'.format(name=name, years=age)
using_format = 'I am {0} and I am {1} years old. I really am named {0}'.format(name, age)
print(using_format)
#Shorter format and escaping characters
print(f'I\'m {name} and I\'m {age} years old.')

#Formating FLOATS numbers:
funds = 150.9723

without_specific_formating = 'Funds: {}'.format(funds)
print(without_specific_formating)
let_system_know_that_it_is_float_before_formating = 'Funds: {:f}'.format(funds)
print(let_system_know_that_it_is_float_before_formating)
float_with_1digit_after_dot = 'Funds: {:.1f}'.format(funds)
print(float_with_1digit_after_dot)
float_with_10digits_and_1digit_after_dot = 'Funds: |{:10.1f}|'.format(funds)
print(float_with_10digits_and_1digit_after_dot)
default_float_with_10digits_and_1digit_after_dot = 'Funds: |{:>10.1f}|'.format(funds)
print(default_float_with_10digits_and_1digit_after_dot)
digits_first_float_with_10digits_and_1digit_after_dot = 'Funds: |{:<10.1f}|'.format(funds)
print(digits_first_float_with_10digits_and_1digit_after_dot)
digits_in_middle_float_with_10digits_and_1digit_after_dot = 'Funds: |{:^10.1f}|'.format(funds)
print(digits_in_middle_float_with_10digits_and_1digit_after_dot)
digits_in_middle_with_placeholders_float_with_10digits_and_1digit_after_dot = 'Funds: |{:-^10.1f}|'.format(funds)
print(digits_in_middle_with_placeholders_float_with_10digits_and_1digit_after_dot)