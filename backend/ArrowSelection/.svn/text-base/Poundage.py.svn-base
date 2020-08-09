class Poundage(object):
    '''
    Used to model the temperature 
    value = 0 - Not known
    value = 1 - 21-27 lbs
    value = 2 - 28-34 lbs
    value = 3 - > 35 lbs
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
            raise Exception("Invalid Poundage value")
        else:
            self._value = value

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value