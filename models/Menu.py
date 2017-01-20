from Tm5 import Tm5
from Af import Af
from Quintupla import Quintupla

class Menu():

    def __init__(self):
        print "\n\t-----------------------------------"
        print "\t|             MENU                |"
        print "\t-----------------------------------"

        print "\n\t1.- Iniciar automata multiplos de 5 en binario. "
        print "\n\t2.- Ingresar Quintupla."
        print "\n\topciones extras :\n\t\n back - vuelve al menu principal"
        print  "\t\n reset - resetea cualquier proceso en desarrollo"
        print  "\t\nbeta:\n\t\n   show - muestra automata y/o quintupla"
        op = raw_input("\t\nIngrese opcion: ")
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
            estado = raw_input("\nIngrese estados: ")

            if estado == 'back':
                Menu()

            if estado == 'reset':
                print "\nreset success !"
                self.op2_estados(quintupla)

            if estado == 'show':
                quintupla.mostrar()
                self.op2_estados(quintupla)

            if estado != 'ok':

                if self.valida_unico(estado,estados):
                    estados[str(estado)] = str(n_stado) ##Cuidado con esta linea fixeala luego
                    n_stado +=1
                    print "\n",estados,"\t 'ok' finalizar ingreso de estados "

                else:
                    continue

            if estado == 'ok' and len(estados) != 0:
                quintupla.set_Q(estados)
                print "\n\t Estados -> Qs : ",quintupla.get_Q(),"\n"
                self.op2_alfabeto(quintupla)

    def op2_alfabeto(self,quintupla): # Step 2

        alfabeto = raw_input("Ingrese lenaguaje: ")

        if alfabeto:

            confirmacion = raw_input("se refiere a " + str(self.separar(alfabeto)) + " y/n?... ")

            if confirmacion == 'y':
                quintupla.set_alfabeto(alfabeto)
                self.op2_transiciones(quintupla)

            else:
                self.op2_alfabeto(quintupla)

        if alfabeto == 'back':
            Menu()

        if alfabeto == 'reset':
            op2_alfabeto(quintupla)

        if alfabeto == 'show':
            quintupla.mostrar()
            op2_alfabeto(quintupla)

    def op2_transiciones(self,quintupla): # Step 3

        print "\nTransiciones\n"

        transiciones = {}
        estados = quintupla.get_Q()

        for num_estado in estados:
            for caracter in quintupla.get_alfabeto():
                transicion = raw_input("En '" + str(num_estado) + "' leyendo '" + str(caracter) + "' voy a : ") ## aca igual cuidado

                if transicion == 'reset':
                    self.op2_transiciones(quintupla)

                if transicion == 'back':
                    Menu()

                if transicion == 'show':
                    quintupla.mostrar()
                    self.op2_transiciones(quintupla)

                if quintupla.validar_transicion(transicion):
                    transiciones[num_estado,caracter] = transicion

                else:
                    print "transicion invalidad ingresar de nuevo"
                    quintupla.borrar_transiciones()
                    self.op2_transiciones(quintupla)



        quintupla.set_transiciones(transiciones)
        self.op2_estado_inicial(quintupla)

    def op2_estado_inicial(self,quintupla): # Step 4

        q0 = raw_input("Ingrese estado inicial: ")

        if q0 == 'back':
            Menu()

        if q0 == 'reset':
            self.op2_estado_inicial(quintupla)

        if q0 == 'show':
            quintupla.mostrar()
            self.op2_estado_inicial(quintupla)

        if quintupla.valida_estado(q0):
            quintupla.set_q0(q0)
            self.op2_estado_final(quintupla)

        else:
            print "estado no valido"
            self.op2_estado_inicial(quintupla)

    def op2_estado_final(self,quintupla): # Step 5

        qF = []

        for cantidad_estados in range(len(quintupla.get_Q())):
            q = raw_input("Ingrese estado final: ")

            if q == 'ok' and len(qF) != 0:
                quintupla.set_qF(qF)
                quintupla.mostrar()
                self.validar_lenguaje(quintupla)

            if q != 'ok' and quintupla.valida_estado(q):
                if self.valida_unico(q,qF):
                    qF.append(q)
                    print "\n\t Estado(s) Final(es) :",qF , "\n\t 'ok' finalizar ingreso de estados\n"

                else:
                    print "estado repetido"

            else:
                print "estado no valido"
                self.op2_estado_final(quintupla)

            if q == 'back':
                Menu()

            if q == 'reset':
                qF = []
            if q == 'show':
                quintupla.mostrar()
                self.op2_estado_final(quintupla)


    def validar_lenguaje(self,quintupla):

        # Se cargar el automata

        automata = Af(quintupla.Q, quintupla.alfabeto, quintupla.transiciones, quintupla.q0, quintupla.qF)
        palabra = raw_input("Inegrese palabra a validar por el automata :")

        if palabra == "back":
            Menu()

        if automata.validate(palabra):
            print automata.is_in(palabra,automata.q0)
            self.validar_lenguaje(quintupla)

        else:
            print "No se reconoce lenguaje le recomendamos usar palabras este Alfabeto:" + str(automata.alfabeto)
            self.validar_lenguaje(quintupla)



    def separar(self,alfabeto):
        alf = []
        for i in range(len(alfabeto)):
            if alfabeto[i] != ',':
                alf.append(alfabeto[i])
        return alf

    def valida_unico(self,estado,estados):
        if estado == "" or len(estado) == 0:
            return False
        if estado in estados:
            return False
        else:
            return True
