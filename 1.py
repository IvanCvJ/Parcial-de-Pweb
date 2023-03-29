import pandas as pd

url = 'resultados.csv'

df = pd.read_csv(url, sep=',')
promedio_nacional = df['PUNT_MATEMATICAS'].mean()
promedio_barranquilla = df[df['ESTU_DEPTO_RESIDE'] == 'ATLANTICO']['PUNT_MATEMATICAS'].mean()
promedio_por_tipo_colegio = df.groupby('COLE_NATURALEZA')['PUNT_MATEMATICAS'].mean()




def analisis_resultados_saber11(df):
    promedio_nacional = df['MAT'].mean()
    
    barranquilla = df[df['ESTU_DEPTO_RESIDE'] == 'ATLÁNTICO']
    promedio_barranquilla = barranquilla['MAT'].mean()
    
    promedio_oficiales = df[df['COLE_DEPTO_APROB'] == 'ATLÁNTICO']['MAT'].mean()
    promedio_no_oficiales = df[df['COLE_DEPTO_APROB'] != 'ATLÁNTICO']['MAT'].mean()
    
    print('Promedio nacional en matemáticas:', promedio_nacional)
    print('Promedio en matemáticas de Barranquilla:', promedio_barranquilla)
    print('Promedio en matemáticas de colegios oficiales:', promedio_oficiales)
    print('Promedio en matemáticas de colegios no oficiales:', promedio_no_oficiales)
