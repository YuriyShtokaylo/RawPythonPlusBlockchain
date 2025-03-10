"""Used to share comman functionality"""


class Printable:
    """Provide magic method for easy printing"""

    def __repr__(self):
        return str(self.__dict__)
