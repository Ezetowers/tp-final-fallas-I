class Question(object):
    '''
    Questions
    number = 0 - No Question 
    number = 1 - Arrow_Length 
    number = 2 - Shooter Height
    number = 3 - Poundage
    number = 4 - Temperature
    number = 5 - Target Distance
    '''

    def __init__(self, number = 1, created = True):
        self.number = number
        self.created = created

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number < 0 or number > 5:
            raise Exception("Invalid Question number")
        else:
            self._number = number

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value