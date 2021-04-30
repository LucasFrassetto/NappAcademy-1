from integrador.classes.Abstracao import Abstracao


def carregar_credenciais(arquivo):
    credenciais = {}
    try:
        with open(arquivo) as file:
            for line in file:
                if not line.startswith('#'):
                    if not line.startswith('\n'):
                        key, valor = line.split('==>')
                        valor = valor.replace('\n', '')
                        credenciais[key] = valor
    except FileNotFoundError:
        raise FileNotFoundError('Arquivo não encontrado: ' + arquivo)
    return credenciais


if __name__ == "__main__":
    arquivos = []
    arquivos += ['credenciais1.txt', 'credenciais2.txt']
    arquivos += ['credenciais3.txt', 'credenciais4.txt']

    for arquivo in arquivos:
        credenciais = carregar_credenciais(arquivo)
        context = Abstracao(**credenciais)
        dados = context.extrair_dados()
        dados_relatorio = context.relatorio_simples()
        print(dados_relatorio)
        context.criar_relatorio()
        print(80 * '*')
