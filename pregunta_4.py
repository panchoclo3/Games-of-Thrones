'''Basandose en las muertes de los personajes, 
¿Cual es la casa que mas muertes de aliados tuvo por cada año?'''

import pandas as pd

from nuevos_datos_2 import reducir_data

df_7 = reducir_data('battles.csv', ['name' ,'attacker_size', 'defender_size', 'attacker_outcome'])


df_7.drop(df_7[df_7['name'] == 'Siege of Winterfell'].index, inplace=True)

df_7.fillna(0, inplace=True)

df_7.drop(df_7[df_7['attacker_size'] == df_7['defender_size']].index, inplace=True)

df_7.reset_index(drop=True, inplace=True)

caso_1 = df_7['attacker_size'] > df_7['defender_size']

caso_2 = df_7['attacker_size'] < df_7['defender_size']

df_7['mas_grande_gana'] = caso_1 & (df_7['attacker_outcome'] == 'win') | caso_2 & (df_7['attacker_outcome'] == 'loss')

result = df_7['mas_grande_gana'].value_counts()

print(f'Los ejercitos mas grandes ganan {result[True]} veces y pierden {result[False]} veces')

