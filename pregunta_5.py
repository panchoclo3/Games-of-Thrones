'''¿Cual casa tiene mas personajes no nobles importantes? Considerese importante como aquel personaje que haya estado vivo al menos por 10 capitulos desde que lo presentaron en la serie.'''
import pandas as pd


def reducir_data(file_path, list_columnas):
    df = pd.read_csv(file_path)
    df = df[list_columnas]
    return df


df = reducir_data('deaths.csv', [
    'Name', 'Allegiances', 'Nobility', 'Book Intro Chapter', 'Death Chapter'])

filtro_no_nobles = df['Nobility'] == 0

df = df[filtro_no_nobles]


df.dropna(subset=['Allegiances', 'Book Intro Chapter'], inplace=True)

df['Importante'] = pd.isna(df['Death Chapter']) | (
    df['Death Chapter'] - df['Book Intro Chapter'] >= 10)

df = df[df['Importante'] == True]

df.reset_index(drop=True, inplace=True)

print(df.info())

df = df.drop(df[df.Allegiances == "Night\'s Watch"].index)

df = df.drop(df[df.Allegiances == "Wildling"].index)

df.Allegiances = df.Allegiances.apply(
    lambda x: 'House ' + x if len(x.split()) < 2 else x)

result = df.groupby('Allegiances')[
    'Importante'].sum().sort_values(ascending=False)

print(
    f'La casa con mas personajes no nobles importantes es {result.index[0]} con {result[0]} personajes.')
