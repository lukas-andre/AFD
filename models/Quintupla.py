
class Quintupla():

    def __init__(self):
        self.Q = None
        self.alfabeto = None
        self.transiciones = None
        self.q0 = None
        self.qF = None

    def set_Q(self,Q):
        self.Q = Q

    def set_alfabeto(self,alfabeto):
        self.alfabeto = alfabeto

    def set_transiciones(self,transiciones):
        self.transiciones = transiciones

    def set_q0(self,q0):
        self.q0 = q0

    def set_qF(self,qF):
        self.qF = qF

    def get_Q(self):
        return self.Q

    def get_alfabeto(self):
        return self.alfabeto

    def borrar_transiciones(self):
        self.transiciones = None

    def valida_estado(self,q0):
        if q0 in self.Q:
            return True
        else:
            return False

    def validar_transicion(self,transicion):
        if transicion in self.Q:
            return True
        else:
            return False

    def mostrar(self):
        print "\n\n\n\t\tCARGANDO AUTOMATA....\n\n\n\t\t"
        print "Estados -> Q's ->", self.Q
        print "Alfabeto -> ", self.alfabeto
        print "Transiciones: "
        self.listar_transiciones()
        print "Estado inicial -> q0 ->", self.q0
        print "Estado final -> qF ->", self.qF

    def listar_transiciones(self):
        for i in self.transiciones:
            print "\t",i,"->",self.transiciones[i]
