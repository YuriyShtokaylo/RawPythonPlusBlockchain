import functools #Is used for reduce

simple_list = [1, 2, 3, 4, 5]
def mul2(el):
    return el * 2

m = map(mul2, simple_list)
r1 = list(m)
print(r1)
r2 = list(map(str, simple_list))
print(r2)

r_with_lambda = list(map(lambda el: el * 2, simple_list))
print(r_with_lambda)

s = functools.reduce(lambda pr, el: pr + el * 1, simple_list, 0)

print(s)