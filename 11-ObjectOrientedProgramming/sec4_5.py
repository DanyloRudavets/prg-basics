class Thermometer:
    def __init__(self):
        self.is_on=False
    def temp_measured(self):
        import random
        self.g=random.randint(34.0,42.0)
        return self.g
    def display_measures(self):
        if self.g>=37.0:
            if self.g>=41:
                return f'Temperature: {self.g} (fever) \n CRITICAL TEMPERATURE!!'
            return f'Temperature: {self.g} (fever)'
        elif self.g>=34.0 and self.g<=37:
            return f'Temperature: {self.g} (normal)'
    def ther_on(self):
        self.is_on=True
        return self.is_on
    def ther_off(self):
        self.is_on=False
        return self.is_on
    
            