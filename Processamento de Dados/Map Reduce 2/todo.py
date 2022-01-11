# -*- coding: utf8


from collections import Counter # RECOMENDADO!


def conta_um_arquivo(fpath):
    DicCounter = Counter()
    with open(fpath) as input_file:
        for line in input_file:
            line = line.lower().strip()
            if line:
                palavras = line.split()
                DicCounter += Counter(palavras)
    return DicCounter


def reduz(contagens_1, contagens_2):
    # Soma as contagens de dois dicionários
    return contagens_1 + contagens_2
    