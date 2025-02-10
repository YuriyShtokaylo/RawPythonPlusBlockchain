class Car:
    # top_speed = 100
    # warnings = []

    def __init__(self, top_speed=100):
        self.top_speed = top_speed
        self.__warnings = []

    def __repr__(self):
        print('Printing...')
        return 'Top Speed: {}, warnings: {}'.format(self.top_speed, len(self.__warnings))
    
    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warnings.append(warning_text)
    
    def get_warnings(self):
        return self.__warnings
    
    def drive(self):
        print('I am driving but certainly not faster than {}'.format(self.top_speed))

    def brag(self):
        print('Look how cool my car is!')
        
car = Car(200)
car.add_warning([])
car.add_warning('1')
print(car)
print(car.__dict__)
car.drive()
car.brag()
print(car.get_warnings())