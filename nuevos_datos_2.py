import pandas as pd
# Definir función para reducir los datos según columnas específicas


def reducir_data(file_path, list_columnas):
    df = pd.read_csv(file_path)
    df = df[list_columnas]
    return df


# Llamar a la función para reducir los datos del archivo 'deaths.csv'
df = reducir_data(
    'deaths.csv', ['Name', 'Allegiances', 'Death Year', 'Gender'])

# Crear una nueva columna 'Alive' que indica si el personaje está vivo o no
df['Alive'] = df['Death Year'].isnull()

# Eliminar la columna 'Death Year'
df.drop(df.columns[2], axis=1, inplace=True)

# Mover la columna 'Allegiances' al principio del DataFrame
first_column = df.pop('Allegiances')
df.insert(0, 'Allegiances', first_column)

# Eliminar filas con valores nulos en cualquier columna
df.dropna(inplace=True)

# Eliminar filas que tengan 'Allegiances' igual a "Night's Watch"
df = df.drop(df[df.Allegiances == "Night\'s Watch"].index)

# Eliminar filas que tengan 'Allegiances' igual a "Wildling"
df = df.drop(df[df.Allegiances == "Wildling"].index)

# Aplicar una función lambda a la columna 'Allegiances' para agregar 'House' al principio del valor si tiene menos de 2 palabras
df.Allegiances = df.Allegiances.apply(
    lambda x: 'House ' + x if len(x.split()) < 2 else x)

print(df)

# Crear un diccionario para almacenar los resultados
data = {
    'Casas Nobles': [],
    'Cantidad de Nobles': [],
    'Porcentaje hombres': [],
    'Porcentaje mujeres': [],
    'Integrantes vivos': [],
    'Integrantes muertos': [],
}

# Agrupar el DataFrame por 'Allegiances' y obtener los valores requeridos
for name, value in df.groupby('Allegiances'):
    data['Casas Nobles'].append(name)
    data['Cantidad de Nobles'].append(len(value))
    data['Porcentaje hombres'].append(
        ((value['Gender'] == 1).sum() / len(value) * 100).round(1))
    data['Porcentaje mujeres'].append(
        ((value['Gender'] == 0).sum() / len(value) * 100).round(1))
    data['Integrantes vivos'].append((value['Alive'] == True).sum())
    data['Integrantes muertos'].append((value['Alive'] == False).sum())

# Crear un DataFrame a partir del diccionario de datos
result = pd.DataFrame(data)

# Imprimir el resultado