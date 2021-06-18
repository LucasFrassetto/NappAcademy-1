import csv
import os
import glob

def palavra_no_txt(palavra, arquivo):
    with open(arquivo, 'r') as f:
        for line in f:
            return palavra in line
    return False

def palavra_no_csv(palavra, arquivo):
    with open(arquivo, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        in_column = False
        for line in spamreader:
            for column in line:
                if palavra in column:
                    in_column = True
    return in_column

def todos_arquivos():
    extensions = ['csv', 'txt']
    all_matched = []
    for extension in extensions:
        looking_for = f'**/*.{extension}'
        matched = glob.glob(looking_for, recursive=True)
        all_matched.extend(matched)
    return all_matched

def encontrar_palavra(palavra):
    func_map = {"csv": palavra_no_csv, 'txt': palavra_no_txt}
    encontrado_em = []
    arquivos = todos_arquivos()
    for arquivo in arquivos:
        extension = arquivo.split(".")[1]
        if extension in func_map:
            if func_map[extension](palavra, arquivo):
                encontrado_em.append(arquivo)
    return encontrado_em

busca_napp1 = encontrar_palavra('napp')
busca_napp2 = encontrar_palavra('NaPp')
print(busca_napp1)
print(busca_napp2)
