class Temperature(object):
    '''
    Used to model the temperature 
    value = 0 - Not known
    value = 1 - < 25 degrees
    value = 2 - => 25
    '''

    def __init__(self, value = 0, created = False):
        self.value = value
        self.created = created

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < 0 or value > 2:
            raise Exception("Invalid Temperature")
        else:
            self._value = value

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value