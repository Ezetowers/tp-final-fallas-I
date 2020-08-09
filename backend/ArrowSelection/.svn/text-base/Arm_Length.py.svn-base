class Arm_Length(object):
    '''
    Used to model the Length of the shooter 
    value = 0 - Not known
    value = 1 - <= 26 ''
    value = 2 - 27-30 ''
    value = 3 - => 31 
    '''

    def __init__(self, value = 0, created = False):
        self.value = value
        self.created = created

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < 0 or value > 3:
            raise Exception("Invalid Length value")
        else:
            self._value = value

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value