class Model(object):
    def __init__(self, 
                 arm_length = -1, 
                 height = -1,
                 poundage = -1, 
                 temperature = -1,
                 target_distance = -1,
                 arrow_model = 1,
                 question = 0):

        self.arm_length = arm_length
        self.height = height
        self.poundage = poundage
        self.temperature = temperature
        self.target_distance = target_distance
        self.arrow_model = arrow_model
        self.question = question


    @property
    def arm_length(self):
        return self._arm_length


    '''
    arm_length = 0 - Not known
    arm_length = 1 - <= 26 
    arm_length = 2 - 27-30 
    arm_length = 3 - => 31
    '''
    @arm_length.setter
    def arm_length(self, arm_length):
        if arm_length > 3:
            raise Exception("Invalid Arm_Length")
        else:
            self._arm_length = arm_length


    @property
    def height(self):
        return self._height


    '''
    height = 0 - <= 1.60 metres
    height = 1 - Between 1.60 metres and 1.90 metres
    height = 2 - >= 1.90 metres
    '''
    @height.setter
    def height(self, height):
        if height > 2:
            raise Exception("Invalid Height")
        else:
            self._height = height


    @property
    def poundage(self):
        return self._poundage


    ''' 
    poundage = 0 - Not known
    poundage = 1 - 21-27 lbs
    poundage = 2 - 28-34 lbs
    poundage = 3 - > 35 lbs
    '''
    @poundage.setter
    def poundage(self, poundage):
        if poundage > 3:
            raise Exception("Invalid Poundage")
        else:
            self._poundage = poundage


    '''
    value = 0 - Not known
    value = 1 - < 25 degrees
    value = 2 - => 25
    '''
    @property
    def temperature(self):
        return self._temperature


    @temperature.setter
    def temperature(self, temperature):
        if temperature > 2:
            raise Exception("Invalid Temperature")
        else:
            self._temperature = temperature


    @property
    def target_distance(self):
        return self._target_distance


    '''
    target_distance = 0 - 18 metres
    target_distance = 1 - 25 metres
    '''
    @target_distance.setter
    def target_distance(self, target_distance):
        if target_distance > 1:
            raise Exception("Invalid target_distance")
        else:
            self._target_distance = target_distance


    @property
    def question(self):
        return self._question


    @question.setter
    def question(self, question):
        if question < 0 or question > 5:
            raise Exception("Invalid Question number")
        else:
            self._question = question


    @property
    def arrow_model(self):
        return self._arrow_model


    @arrow_model.setter
    def arrow_model(self, arrow_model):
        if arrow_model < 0 or arrow_model > 4:
            raise Exception("Invalid Arrow Model")
        else:
            self._arrow_model = arrow_model