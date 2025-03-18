class Food:
    def __init__(self, name, kind):
        self.name = name
        self.__kind = kind

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    def describe(self):
        print(f'This is {self.name} and it is {self.__kind}')

    @classmethod
    def describe_as_classmethod(cls):
        print(f'WAT {cls.name}')# and {cls.__kind}')

    @staticmethod
    def describe_as_static():
        print(f'This will not work!')

    def __repr__(self):
        return f'This is {self.name} and it is {self.__kind}'


class Meat(Food):
    def __init__(self, name):
        super().__init__(name, 'Meat')

    def cook(self):
        print(f'Cooking {self.name}')
        self.name = f'Cooked {self.name}'


class Fruit(Food):
    def __init__(self, name):
        super().__init__(name, 'Fruit')
        
    def clean(self):
        print(f'Cleaning {self.name}')
        self.name = f'Cleaned {self.name}'
        
f1 = Food('Something', 'something :-)') 
f1.describe()
f1.describe_as_classmethod()
f1.describe_as_static()
print(f1)
f2 = Meat('Cheeken')            
f2.describe()
f2.describe_as_classmethod()
f2.describe_as_static()
f2.cook()
print(f2) 
f3 = Fruit('Apple')
f3.describe()
f3.describe_as_classmethod()
f3.describe_as_static()
f3.clean()
print(f3)