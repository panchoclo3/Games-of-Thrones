import pandas as pd


def reducir_data(file_path, list_columnas):
    df = pd.read_csv(file_path)
    df = df[list_columnas]
    return df


df = reducir_data(
    'deaths.csv', ['Name', 'Allegiances', 'Death Year', 'Gender'])

df['Alive'] = df['Death Year'].isnull()
df.drop(df.columns[2], axis=1, inplace=True)

gk = df.groupby('Allegiances')

for name, group in gk:
    print(type(name))
    print(group)
    print()
