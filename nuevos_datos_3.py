import pandas as pd

def reducir_data(file_path, list_columnas):
    df = pd.read_csv(file_path)
    df = df[list_columnas]
    return df


df = reducir_data(
    'battles.csv', ['attacker_commander', 'attacker_outcome'])

#group = df.groupby(['attacker_commander', 'attacker_outcome']).count()
#print(group)
df2 = (
 df.assign(proportion=df['attacker_commander'].str.split())
   .explode('attacker_commander')
   .reset_index(drop=True)
)
print(df2)

