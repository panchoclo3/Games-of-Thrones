
'''Cuantas mujeres que sean nobles, que esten vivas y de casas aliadas que han ganado
al menos una batalla aparecen por cada libro?'''

import pandas as pd

def reducir_data(file_path, list_columnas):
    df = pd.read_csv(file_path)
    df = df[list_columnas]
    return df

df = df = reducir_data('deaths.csv', ['Name', 'Allegiances', 'Gender', 'Nobility'])
df.dropna(inplace=True)
df = df.drop(df[df.Gender == 1].index)
df = df.drop(df[df.Nobility == 0].index)

df_battles = reducir_data('battles.csv', ['name', 'attacker_1', 'defender_1', 'attacker_outcome'])

def whatever(atk, defen, outcome):
    if outcome == 'win':
        return atk
    else:
        return defen
    
df_battles['winner'] = df_battles.apply(lambda x: whatever(x['attacker_1'], x['defender_1'], x['attacker_outcome']), axis=1)

lista = df_battles.winner.unique()

df['nueva wea'] = df['Allegiances'] in lista

print(df.head(10))
