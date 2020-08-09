class Arrow_Model(object):
    '''
    value = 0 - Could not be determined
    value = 1 - Not known yet
    value = 2 - 75
    value = 3 - Apollo
    value = 4 - X7
    '''

    def __init__(self, value = 1, created = True):
        self.value = value
        self.created = created

        self._models = ['Could not be determined', 'Not known yet', '75', 'Apollo', 'X7']

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < 0 or value > 4:
            raise Exception("Invalid model value")
        else:
            self._value = value

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value

    def get_model_name(self):
        return self._models[self._value]