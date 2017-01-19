from Tm5 import Tm5
from Af import Af
from Quintupla import Quintupla

class Menu():

    def __init__(self):
        print "1.- Iniciar automata multiplos de 5 en binario. "
        print "2.- Ingresar Quintupla."
        op = raw_input("Ingrese opcion: ")
        if op == "1":
            self.op1()
        if op == "2":
            self.op2()

    def op1(self):
        tm5 = Tm5() # Mapa del automata.
        automata = Af( tm5.Q, tm5.alfabeto, tm5.transiciones, tm5.q0, tm5.qF ) # se cargar Af su mapa (quintupla).
        palabra = raw_input("Inegrese palabra :")
        if automata.validate(palabra):
            print automata.is_in_tm5(palabra,automata.q0) # is_in_tm5() valida por campos tipo int
            self.op1()
        else:
            print "No se reconoce lenguaje le recomendamos usar palabras este Alfabeto:" + str(automata.alfabeto)
        if palabra == "back":
            Menu()

    def op2(self):
        quintupla = Quintupla()
        self.op2_estados(quintupla)

    def op2_estados(self,quintupla): # Step 1
        estados = {} #diccionario vacio de estados.
        n_stado = 0
        while n_stado >= 0:
            estado = raw_input("ingrese estados: ")
            if estado != 'ok':
                estados[str(estado)] = n_stado ##Cuidado con esta linea fixeala luego
                n_stado +=1
                print estados,"~> 'ok' finalizar ingreso de estados "
            if estado == 'ok':
                quintupla.set_Q(estados)
                self.op2_alfabeto(quintupla)

    def op2_alfabeto(self,quintupla): # Step 2
        alfabeto = raw_input("Ingrese lenaguaje: ")
        if alfabeto:
            #print "se refiere a :", self.separar(alfabeto)
            confirmacion = raw_input("se refiere a " + str(self.separar(alfabeto)) + " y/n?... ")
            if confirmacion == 'y':
                quintupla.set_alfabeto(alfabeto)
                self.op2_transiciones(quintupla)
            else:
                self.op2_alfabeto

    def op2_transiciones(self,quintupla): # Step 3
        print "\nTransiciones\n"
        transiciones = {}
        estados = quintupla.get_Q()
        for num_estado in estados: # i = num del estado
            for caracter in quintupla.get_alfabeto():
                transicion = raw_input("En " + str(num_estado) + " leyendo '" + str(caracter) + "' voy a : ") ## aca igual cuidado
                if quintupla.validar_transicion(transicion):
                    #print "trancision validad"
                    transiciones[num_estado,caracter] = transicion ## CUIDADO ACA antes era transiciones[estados[num_estado],caracter] = transicion
                    #print transiciones
                else:
                    print "transicion invalidad ingresar de nuevo"
                    quintupla.borrar_transiciones()
                    self.op2_transiciones(quintupla)

        quintupla.set_transiciones(transiciones)
        self.op2_estado_inicial(quintupla)

    def op2_estado_inicial(self,quintupla): # Step 4
        q0 = raw_input("Ingrese estado inicial: ")
        if quintupla.valida_estado(q0):
            quintupla.set_q0(q0)
            self.op2_estado_final(quintupla)
        else:
            print "estado no valido"
            self.op2_estado_inicial(quintupla)

    def op2_estado_final(self,quintupla): # Step 5
        qF = raw_input("Ingrese estado final: ")
        if quintupla.valida_estado(qF):
            quintupla.set_qF(qF)
            quintupla.mostrar()
            self.validar_lenguaje(quintupla)
        else:
            print "estado no valido"
            self.op2_estado_final(quintupla)

    def validar_lenguaje(self,quintupla):
        # Se cargar el automata
        automata = Af(quintupla.Q, quintupla.alfabeto, quintupla.transiciones, quintupla.q0, quintupla.qF)
        palabra = raw_input("Inegrese palabra a validar por el automata :")
        if automata.validate(palabra):
            print automata.is_in(palabra,automata.q0)
            self.validar_lenguaje(quintupla)
        else:
            print "No se reconoce lenguaje le recomendamos usar palabras este Alfabeto:" + str(automata.alfabeto)
            self.validar_lenguaje(quintupla)
        if palabra == "back":
            Menu()

    def separar(self,alfabeto):
        alf = []
        for i in range(len(alfabeto)):
            if alfabeto[i] != ',':
                alf.append(alfabeto[i])
        return alf
