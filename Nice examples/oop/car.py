class Car:
    # top_speed = 100
    # warnings = []

    def __init__(self, top_speed=100):
        self.top_speed = top_speed
        self.warnings = []

    def __repr__(self):
        print('Printing...')
        return 'Top Speed: {}, warnings: {}'.format(self.top_speed, len(self.warnings))
    
    def drive(self):
        print('I am driving but certainly not faster than {}'.format(self.top_speed))


car1 = Car()
car1.drive()

car1.warnings.append('New warning')
print(car1)
print(car1.__dict__)

car2 = Car(200)
car2.drive()
print(car2.warnings)

car3 = Car()
car3.warnings=['A']
car3.drive()
print(car3.warnings)
print(car2.warnings)
print(car1.warnings)

car4 = Car()
car4.drive()
print(car4.warnings)