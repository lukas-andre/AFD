from Tm5 import *
from Af import *


x = 0
tm5 = Tm5() # Mapa del automata.
print tm5.get_data_type()
while x != 1 :
    automata = Af( tm5.Q, tm5.alfabeto, tm5.transiciones, tm5.q0, tm5.qF )
    palabra = raw_input("Ingrese palabra :")

    if automata.validate(palabra,tm5.get_data_type()):
        print automata.is_in(palabra,tm5.q0)
    else:
        print "No se reconoce lenguaje le recomendamos usar palabras este Alfabeto:" + str(tm5.alfabeto)
