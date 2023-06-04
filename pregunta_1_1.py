'''¿Cual es el comandante que mas batallas ha ganado?'''

import pandas as pd

def reducir_data(file_path, list_columnas):
    df = pd.read_csv(file_path)
    df = df[list_columnas]
    return df

df = reducir_data('battles.csv', ['name', 'attacker_commander', 'defender_commander', 'attacker_outcome'])

df.dropna(inplace=True)

def split_column(df, column):
    df[column] = df[column].str.split(',')
    return df

df = split_column(df, 'attacker_commander')
df = split_column(df, 'defender_commander')

df = df.explode('attacker_commander')
df = df.explode('defender_commander')

print(df)