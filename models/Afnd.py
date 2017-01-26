from Quintupla import Quintupla

class Afnd(Quintupla):

    transiciones = {}
    alfabeto = None

    def __init__(self):
        self.set_transiciones(self.transiciones)

    def set_afnd_Q(self,Q):

        k = []
        for i in Q:
            k.append(i)
            k.sort()
        #  incertando un estado muerto al final de la lista .
        k.append('dead')
        self.Q = k

    def get_name(self):
        return "AFND"

    def get_alfabeto_afnd(self):
        return self.alfabeto

    def mod_alfabeto(self):
        if "#" not in self.alfabeto:
            self.alfabeto = str(self.get_alfabeto()) + "#"

    def get_transiciones_validas(self):
        return self.Q

    def validar_transicion_afnd(self,transicion):
        validate = False

        transiciones_validas = self.get_transiciones_validas()
        print transiciones_validas
        if type(transicion) == list:

            for estado in transicion:
                if estado in transiciones_validas:
                    validate = True
                else:
                    validate = False
                    break
            return validate

        else:
            if transicion in transiciones_validas:
                validate = True
            else:
                validate = False
            return validate

    def transformar_a_AFD(self):
        self.clean_alfabeto()
        estado_recorridos = [self.q0]
        qActual = self.q0
        nuevas_transiciones={}
        for estado in estado_recorridos:
            for simbolo in self.alfabeto:
                print "nuevas transicion: ", nuevas_transiciones
                print "estados recorridos: ",estado_recorridos

                if self.is_fix(estado):
                    print "es fixiado el estado siguiente", estado
                    transiciones_fix = self.get_fix_tranciciones(estado,simbolo)
                    print "transicion fix: ", transiciones_fix
                    if type(transiciones_fix) == list:
                        nuevo_estado = self.fix_transicion(transiciones_fix)
                    if nuevo_estado not in estado_recorridos:
                        estado_recorridos.append(nuevo_estado)
                    nuevas_transiciones[estado,simbolo] = nuevo_estado

                elif type(self.transiciones[estado,simbolo]) == list:
                    nuevo_estado = self.fix_transicion(self.transiciones[estado,simbolo])
                    estado_recorridos.append(nuevo_estado)
                    nuevas_transiciones[estado,simbolo] = nuevo_estado

                elif type(self.transiciones[estado,simbolo]) == str:
                    if self.transiciones[estado,simbolo] not in estado_recorridos and self.transiciones[estado,simbolo] != 'dead' :
                        estado_recorridos.append(self.transiciones[estado,simbolo])
                    if self.transiciones[estado,simbolo] != 'dead':
                        nuevas_transiciones[estado,simbolo] = self.transiciones[estado,simbolo]

                #compruebo si el siguiente estado es un estado compuesto o fixiado.

        return nuevas_transiciones

    #nueva_transicion recibira un estado fixiado y entregara lista con transiciones
    def get_fix_tranciciones(self,estado,simbolo):
        estados = self.separar_fixiados(estado)
        print estados
        estados_comunes = []
        for estado in estados:
            # no es necesario insertar en la lista las transiciones que no llevan a ningun lado (muertas)
            if self.transiciones[estado,simbolo] != 'dead':
                for q in self.transiciones[estado,simbolo]:
                    estados_comunes.append(q)
        print "get_fix_tranciciones: ", estados_comunes
        return self.clear_estados_comunes(estados_comunes)

    #Metodo para limpiar estados repetidos
    def clear_estados_comunes(self,estados_comunes):
        estados_comunes =list(set(estados_comunes))
        return estados_comunes

    def separar_fixiados(self,estado):
        estado = estado[1:]
        estado = estado.split('-')
        print "dentro de separar fixiados print estado split :", estado
        return estado

    def is_fix(self,qFixiado):
        if qFixiado[0] == "#":
            return True
        else:
            return False

    def fix_transicion(self,transicion):
        # se usara ''#'' para marcar estados fixiados
        fix_trans = "#"
        trans = ""
        cont = 0

        for i in transicion:
            fix_trans += i[0] + '-' # '#q1-q2-'

        while cont < len(fix_trans)-1:
            trans += fix_trans[cont]
            cont += 1

        return trans # '#q1-q2'

    def clear_q(self):
        self.Q.remove('dead')

    #Quitamos # ya que no lo necesitamos
    def clean_alfabeto(self):
        self.alfabeto = self.alfabeto[:-1]
