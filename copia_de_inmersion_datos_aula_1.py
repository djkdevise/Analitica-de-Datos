# -*- coding: utf-8 -*-
"""Copia de INMERSION_DATOS_AULA_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OMuvEFNhm3fKnLp3tk7zmR-Qp0-Fnmso

Bienvenido a nuestro primer encuentro de inmersión de datos.
"""

from google.colab import drive

drive.mount('/content/drive')

import pandas as pd

inmuebles = pd.read_csv('/content/drive/MyDrive/Curso Analisis de Datos Coursera/inmersion_datos/inmuebles_bogota.csv')
inmuebles.head()

inmuebles.shape

inmuebles.columns

columnas = {'Baños':'Banos','Área':'Area'}
inmuebles = inmuebles.rename(columns=columnas)
inmuebles.sample(10)

inmuebles.info()

inmuebles.iloc[300]

inmuebles.iloc[300:305]

inmuebles['Valor'][300]

type(inmuebles['Valor'][300:305])

inmuebles.columns

inmuebles.Area.mean()

inmuebles.sample(100)

(inmuebles.Barrio == 'Chico Reservado')

sum((inmuebles.Barrio == 'Chico Reservado'))

inmuebles_chico = (inmuebles.Barrio == 'Chico Reservado')
type(inmuebles_chico)

chico_reservado = inmuebles[inmuebles_chico]
chico_reservado

chico_reservado.Area.mean()

inmuebles.Area.mean()

len(inmuebles.Barrio.value_counts())

inmuebles.Barrio.value_counts()

len(inmuebles.UPZ.value_counts())

inmuebles_barrio = inmuebles.Barrio.value_counts()
inmuebles_barrio.plot.bar()

inmuebles_barrio.head(10).plot.bar()

"""**Desafío**


1. Promedio de área de todos los inmuebles en los barrios en el dataset. El top 10.

2. Consultar otros datos estadísticos, conteo, mediana, valores mínimo y máximo.

#**Aula 2**
"""

