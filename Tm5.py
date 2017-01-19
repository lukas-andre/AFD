
class Tm5(object): # tmf = transiciones multiplos de 5

    def __init__(self):
        self.Q = [0,1,2,3,4]
        self.alfabeto = [0,1]
        self.transiciones = {
                        (0,0):0,
                        (0,1):1,
                        (1,0):2,
                        (1,1):3,
                        (2,0):4,
                        (2,1):0,
                        (3,0):1,
                        (3,1):2,
                        (4,0):3,
                        (4,1):4,
                        }
        self.q0 = 0
        self.qF = 0

    def get_data_type(self): # if has one or more str datatype return str
        for i in self.alfabeto:
            if type(i) == int:
                _type = 'int'
            if type(i) == str:
                return type(i)
        return _type
