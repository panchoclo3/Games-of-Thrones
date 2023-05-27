'''Hay personajes que sabemos que estan muertos, pues nos aparece el año de su muerte, pero no sabemos como murieron. 
Suponiendo que murieron en batalla, indique en que batalla pudieron haber muerto. 
En caso de haber mas de una batalla posible, quedese con aquella donde combatio la mayor cantidad de gente. 
Justifique bien su razonamiento para resolver el ejercicio'''
import pandas as pd


def reducir_data(file_path, list_columnas):
    df = pd.read_csv(file_path)
    df = df[list_columnas]
    return df


df_battles = reducir_data('battles.csv', ['name', 'year', 'attacker_1', 'attacker_2', 'attacker_3', 'attacker_4', 'defender_1',
                                          'defender_2', 'defender_3', 'defender_4', 'attacker_size', 'defender_size'])

filtro = df_battles[['attacker_1', 'attacker_2',
                     'attacker_3', 'attacker_4', 'defender_1', 'defender_2', 'defender_3',  'defender_4']]

df_battles['participants'] = [[e for e in row if e == e]
                              for row in filtro.values.tolist()]

df_battles.drop(filtro, axis=1, inplace=True)

df_battles.fillna(0, inplace=True)

df_battles['total_size'] = df_battles['attacker_size'] + \
    df_battles['defender_size']

df_battles.drop(['attacker_size', 'defender_size'], axis=1, inplace=True)

df_deaths = reducir_data('deaths.csv', ['Name', 'Allegiances', 'Death Year'])

df_deaths.dropna(inplace=True)

group = df_battles.groupby('year')

print(group.columns)
