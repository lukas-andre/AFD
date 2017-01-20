
class Af():

    def __init__(self,Q,alfabeto,transiciones,q0,qF):
        self.Q = Q
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.q0 = q0
        self.qF = qF

    def is_in_tm5(self,palabra,qActual):
        if  str(palabra) == "" and qActual in self.qF:
            return True
        if qActual == self.q0 and len(palabra) == 0:
            return True
        else:
            try:
                entrada = int(palabra[0])
            except Exception as e:
                return False
            if (qActual,entrada) in self.transiciones:
                return self.is_in_tm5(palabra[1:],self.transiciones[qActual,entrada])
            else:
                return False

    def is_in(self,palabra,qActual):
        if  str(palabra) == "" and qActual in self.qF:
            return True
        if qActual == self.q0 and len(palabra) == 0:
            return True
        else:
            try:
                entrada = palabra[0]
            except Exception as e:
                return False
            if (qActual,entrada) in self.transiciones:
                return self.is_in(palabra[1:],self.transiciones[qActual,entrada])
            else:
                return False


    def validate(self, palabra,):
        validate = False
        for i in range(len(palabra)):
            if (str(palabra[i]) in str(self.alfabeto)):
                validate = True
        if len(palabra) == 0:
            validate = True
        return validate
