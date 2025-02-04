persons = [
    {
        'name': 'Yuriy',
        'age': 31,
        'hobbies': ['astronomy', 'tourism', 'biking']
    },
    {
        'name': 'Pavlo',
        'age': 31,
        'hobbies': ['astronomy', 'crafting', 'cars']
    },
    {
        'name': 'Oleg',
        'age': 32,
        'hobbies': ['drawing', 'tourism', 'biking']
    },
    {
        'name': 'Bogdan',
        'age': 27,
        'hobbies': ['photography', 'tourism', 'gaming']
    },
    {
        'name': 'Roman',
        'age': 32,
        'hobbies': ['programming', 'history', 'chess']
    },
]

names = [person['name'] for person in persons]

are_older_then_20 = all([person['age'] > 20 for person in persons])

copy_persons = [person.copy() for person in persons]

print(persons)
print(names)
print(are_older_then_20)
print(copy_persons)
copy_persons[3]['age'] = 25
print(copy_persons)
print(persons)

Yuriy, Pavlo, Oleg, Bogdan, Roman = persons

print(Yuriy)
print(Pavlo)
print(Oleg)
print(Bogdan)
print(Roman)