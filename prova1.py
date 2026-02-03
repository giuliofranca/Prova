import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# DATA FRAME DA ARRAY
a1 = np.arange(1,11)
a2 = np.arange(2,12)
a3 = np.arange(3,13)

dataframe = pd.DataFrame(columns=['1','2','3'])
dataframe['1'] = a1
dataframe['2'] = a2
dataframe['3'] = a3
print(dataframe)


# accedo a elementi del dataframe, che sono colonne di array
print(dataframe['1'][0])

# il comando head() restituisce la testa del data frame, le prime righe

#c il comando iterrows scorre sule ighe del data frame
for i,j in dataframe.iterrows():
    print(i,j['2'])

# il comando iloc seleziona solo righe comprese tra start e stop di una tabella
dataframe_selez = dataframe.iloc[2:5]
print(dataframe_selez)

# seleziono colonne basandomi sul contenuto delle colonne
mydf = dataframe.loc[(dataframe['1']<3) | (dataframe['1']>6), '3']
print(mydf)

# posso aggiungere una colonna al data frame
print('il nuovo dataframe è')
nuovo_array = np.linspace(1,4,10)
dataframe['A'] = nuovo_array
print(dataframe)

# scatter plot
dati = np.linspace(1,10,20)
y1 = np.linspace(1,10,20)
y2 = np.logspace(1,20,20)
plt.scatter(dati, y1, color='royalblue', s=40, label='cinini')
plt.xlabel('X')
plt.ylabel('Y')
plt.scatter(dati,y2,color='tomato', s=68, label='bebi')
plt.legend(loc = 'upper left')
plt.show()


# istogrammi
estrazione = np.random.normal(100,20,400)
n, bins, p = plt.hist(estrazione, bins = 20, color='gold')
plt.xlabel('valore estratto')
plt.show()