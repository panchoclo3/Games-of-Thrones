'''Existe relacion entre el tipo de batalla y taza de mortalidad?'''

import pandas as pd

def reducir_data(file_path, list_columnas):
    df = pd.read_csv(file_path)
    df = df[list_columnas]
    return df

df = reducir_data('battles.csv', ['name', 'battle_type', 'major_death'])

df = df.drop(df[df['name'] == 'Siege of Winterfell'].index)

df['major_death'].replace({0: False, 1: True})

result = df.groupby('battle_type')['major_death'].value_counts(normalize=True).mul(100).round(1).unstack(fill_value=0)

print(result)


