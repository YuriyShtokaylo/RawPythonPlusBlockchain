names = ['Ivan', 'Pavlo', 'Yuriy', 'Oleg', 'Roman', 'Bogdan', 'Mykola']

for name in names:
    print(name, len(name))

for name in names:
    l = len(name)
    if l > 5:
        print(name) 
    if 'n' in name or 'N' in name:
        print('Yes')
    else:
        print('No')        
        
l = len(names)

print(names)
while l > 0:
    names.pop()
    print(names)
    l -= 1           