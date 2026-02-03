import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nome = 'Giulio'
eta = 21
luogo = 'Perugia'

# formattazione generica
stringa = 'Ciao, mi chiamo {:}, ho {:} anni e vivo a {:}'.format(nome,eta,luogo)
print(stringa)

# formattazione con numeri reali, specifica sulle cifre significative
stringa = 'le prime 5 cifre decimali del pi greco sono {:.5f}'.format(np.pi)
print(stringa)

# formattazione con stringa con 5 caratteri allineata a sinistra
stringa = '{:<10} {:2d}'.format('Giulio',21)
print(stringa)

"""

Questo è un commento su piu righe

"""