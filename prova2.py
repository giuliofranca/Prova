import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# definisco una funzione a 2 parametri, il secondo è uno se non specificato
def myfun(a,b=1):
    return a + b

print(myfun(1))
print(myfun(1,2))

# definisco una funzione con un numero indefinito di parametri usando args
def funzione(*args):
    somma = 0
    if(len(args)>0):
        somma = args[0]
        if(len(args)>1):
            somma = somma + args[1]
    print(args[-1])
    return somma

print(funzione(1,2,'ciao'))