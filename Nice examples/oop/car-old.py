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


car1 = Car()
car1.drive()

car1.add_warning('New warning')
hack = car1.get_warnings()
hack.append([])  # hack=-(
print(car1)
print(car1.__dict__)

car2 = Car(200)
car2.drive()
print(car2.get_warnings())

car3 = Car()
car3.warnings = ['A']
car3.drive()
print(car3.get_warnings())
print(car2.get_warnings())
print(car1.get_warnings())

car4 = Car()
car4.drive()
print(car4.get_warnings())
