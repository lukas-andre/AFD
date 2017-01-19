from Tm5 import *
from Af import *


x = 0
tm5 = Tm5() # Mapa del automata.
while x != 1 :
    automata = Af( tm5.Q, tm5.Alfabeto, tm5.transiciones, tm5.q0, tm5.qF )
    palabra = raw_input("Inegrese palabra :")
    if automata.validate_tm5(palabra):
        print automata.is_in(palabra,tm5.q0)
    else:
        print "No se reconoce lenguaje le recomendamos usar palabras este Alfabeto:" + str(tm5.Alfabeto)
