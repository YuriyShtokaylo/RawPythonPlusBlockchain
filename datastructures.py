simple_list = [1, 2, 3, 4]
simple_list.extend([5, 6, 7])
print(type(simple_list))
print(simple_list)

del(simple_list[0])
print(simple_list)
del simple_list[0]
print(simple_list)

d = {'name': 'Yuriy'}
print(type(d))
print(d.items())
for k, v in d.items():
    print(k, v)
del(d['name'])
print(d)

single = (1,)    
print(type(single))
t = (1,2,3)   
print(t.index(1))
#This will not work couse TUPLES ARE IMMUTABLE
#del(t[0])
#print(t)

s = {'Yuriy', 'Oleksandra', 'Yuriy'}
print(type(s))
#This will not work SETS ARE NOT ITERABLE THEY DON'T HAVE ANY INDEXES
# del(s['Yuriy'])
print(s) 