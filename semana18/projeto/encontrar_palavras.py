import os
import glob

def palavra_no_arquivo(palavra, arquivo):
    with open(arquivo, 'r') as f:
        for line in f:
            return palavra in line
    return False

def todos_arquivos_txt():
    looking_for = '**/*.txt'
    matched = glob.glob(looking_for, recursive=True)
    return matched

def encontrar_palavra(palavra):
    encontrado_em = []
    arquivos = todos_arquivos_txt()
    for arquivo in arquivos:
        if palavra_no_arquivo(palavra, arquivo):
            encontrado_em.append(arquivo)
    return encontrado_em

busca_napp1 = encontrar_palavra('napp')
busca_napp2 = encontrar_palavra('NaPp')