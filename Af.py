
class Af(object):

    def __init__(self,Q,Alfabeto,Transiciones,q0,qF):
        self.Q = Q
        self.alfabeto = Alfabeto
        self.transiciones = Transiciones
        self.q0 = q0
        self.qF = qF

    def is_in(self,palabra,qActual):
        if  str(palabra) == "" and qActual == self.qF:
            return True
        else:
            try:
                entrada = int(palabra[0])
            except Exception as e:
                return False
            if (qActual,entrada) in self.transiciones:
                return self.is_in(palabra[1:],self.transiciones[qActual,entrada])
            else:
                return False

    def validate_tm5(self, palabra):
        validate = False
        for i in range(len(palabra)):
            if (int(palabra[i]) in self.alfabeto):
                validate = True
            else:
                validate = False
        return validate
