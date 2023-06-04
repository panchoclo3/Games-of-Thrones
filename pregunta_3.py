'''Basandose en las muertes de los personajes, 
¿Cual es la casa que mas muertes de aliados tuvo por cada año?'''

import pandas as pd

def reducir_data(file_path, list_columnas):
    df = pd.read_csv(file_path)
    df = df[list_columnas]
    return df

df = reducir_data('deaths.csv', ['Name', 'Allegiances', 'Death Year'])

df.dropna(inplace=True)

df = df.drop(df[df.Allegiances == "Night\'s Watch"].index)

df = df.drop(df[df.Allegiances == "Wildling"].index)

df.Allegiances = df.Allegiances.apply(
    lambda x: 'House ' + x if len(x.split()) < 2 else x)

group = df.groupby(['Death Year' ,'Allegiances']).count()

group = group.reset_index()

group = group.sort_values(by=['Death Year', 'Name'], ascending=False)

group = group.drop_duplicates(subset=['Death Year'], keep='first')

group = group.reset_index(drop=True)

print(group)