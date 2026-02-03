import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

"""
Definisco delle funzioni/parametri da usare i un altro script, o che possono essere usate 
in questo modulo se viene eseguito direttamente

"""

g = 9.81
def v(t):
    vel = g*t
    return vel

def s(t):
    sp = 0.5*g*(t**2)
    return sp

"""
 Se il nome assegnato è __main__ (e ciò accade quando eseguo direttamente il modulo
 senza importarlo in un altro script che eseguo) allora viene preso come
 parametro inserito dall'utente tutto ciò che scrivo dopo il comando di esecuzione,
 e faccio tutto ciò che c'è scritto dopo. Ciò è possibile importando il modulo sys,
 il quale permette di far vedere a python che inserisco dei valori interpretati come stringhe
 dopo il comando di esecuzione
"""
if __name__ == '__main__':
    tempo = float(sys.argv[1])
    print('la velocità al tempo {:} è {:} m/s, e lo spazio percorso è {:} metri'.format(tempo,v(tempo),s(tempo)))

# tale riga di codice parte solo se eseguo direttamente il modulo, altrimenti definisco semplicemente funzioni