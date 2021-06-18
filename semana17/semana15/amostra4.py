import pandas as pd
import os

def carregar_arquivo(arquivo, caminho):
    df = pd.read_csv(caminho + '\\' + arquivo, delimiter=',', dtype='unicode')
    return df

def separa_por_ano(df, caminho):

    if os.path.exists(f'{caminho}\\separado_por_ano') == False:
        os.mkdir(f'{caminho}\\separado_por_ano')
    
    anos = df['ano_eleicao'].unique()
    print('\nSeparando dados por ano:')
    for ano in anos:
        print(f'Exportando Ano: {ano}')
        df_ano = df.loc[df['ano_eleicao'] == ano]
        df_ano.to_csv(f'{caminho}\\separado_por_ano\\eleicao_{ano}.csv', sep=';')

if __name__ == "__main__":
    caminho = os.path.dirname(__file__)
    print('Carregando arquivo candidatura.csv')
    df = carregar_arquivo('candidatura.csv', caminho)

    separa_por_ano(df, caminho)
    print('\nSeparação Finalizada!')
