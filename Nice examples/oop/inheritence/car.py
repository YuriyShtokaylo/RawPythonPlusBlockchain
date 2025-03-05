from vehicle import Vehicle


class Car(Vehicle):

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
