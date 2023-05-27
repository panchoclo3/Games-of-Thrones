'''Crear una columna en el dataset deaths.csv que muestre en cuantos libros aparece
cada personaje.'''

import pandas as pd

df = pd.read_csv('deaths.csv')

print(df.info())  # para saber si existen valores nulos en las columnas a utilizar

df.insert(6, 'Appearances per book', df[[
    'GoT', 'CoK', 'SoS', 'FfC', 'DwD']].sum(axis=1))

filtro_importantes = df['Appearances per book'] == 5

df_importantes = df[filtro_importantes]

df_importantes.reset_index(drop=True, inplace=True)

print(df_importantes[['Name', 'Allegiances']])
