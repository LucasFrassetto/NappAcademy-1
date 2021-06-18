from integrador.classes.Contexto import Contexto

def carregar_credenciais(arquivo):
    credenciais = {}
    try:
        with open( arquivo) as file:
            for line in file:
                if((line != '\n') and (line[0] != '#')):
                    key, valor = line.split('==>')
                    valor = valor.replace('\n', '')
                    credenciais[key] = valor
    except FileNotFoundError:
        raise FileNotFoundError('Arquivo não encontrado: ' + arquivo)
    return credenciais


if __name__ == "__main__":
    arquivos = []
    arquivos += ['credenciais_texto1_modelo1.txt', 'credenciais_texto1_modelo2.txt']
    arquivos += ['credenciais_texto2_modelo1.txt', 'credenciais_texto2_modelo2.txt']

    for arquivo in arquivos:
        credenciais = carregar_credenciais(arquivo)
        context = Contexto(**credenciais)
        print(80 * '*')
        print(context.algoritmo)
        print(context.dados_armazenados())
        valor = context.executar()
        print(valor)
