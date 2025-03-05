from vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, top_speed=100):
        super().__init__(top_speed)
        self.passangers = []

    def add_group(self, passangers):
        self.passangers.extend(passangers)


bus = Bus(150)
bus.add_warning('1')
bus.add_group([1, 2, 3])
print(bus.passangers)
bus.drive()
