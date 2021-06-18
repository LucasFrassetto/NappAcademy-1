from integrador.classes.Contexto import Contexto


def carregar_credenciais(arquivo):
    credenciais = {}
    try:
        with open(arquivo) as file:
            for line in file:
                if line.startswith("#"):
                    continue
                if line == '\n':
                    continue
                key, valor = line.split('==>')
                valor = valor.replace('\n', '')
                credenciais[key] = valor
    except FileNotFoundError:
        raise FileNotFoundError('Arquivo não encontrado: ' + arquivo)
    return credenciais


if __name__ == "__main__":
    arquivos = []
    arquivos += ['credenciais_modelo_1.txt', 'credenciais_modelo_2.txt']
#    arquivos += ['credenciais1.txt', 'credenciais2.txt']
#    arquivos += ['credenciais3.txt']
#    arquivos += ['credenciais4.txt', 'credenciais5.txt']
#    arquivos += ['credenciais6.txt']

    for arquivo in arquivos:
        credenciais = carregar_credenciais(arquivo)
        context = Contexto(**credenciais)
        print(80 * '*')
        print(context.algoritmo)
        print(context.dados_armazenados())
        valor = context.executar()
        print(context.executar())
