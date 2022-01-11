# -*- coding: utf8

from bs4 import BeautifulSoup
from functools import reduce

import multiprocessing as mp
import tarfile
from collections import Counter # RECOMENDADO!


def extract_and_process(member):
    # observe como cada processo abre o tar novamente
    # a extração é feita por processo
    # veja exemplos do HTML na pasta exemplo
    # Para pegar o nome de um artist use texto.strip().split('-')[-1].
    # O formato do texto no html é Música - Artista
    
    # TODO: implemente o resto
    tar = tarfile.open("dados.tar.gz", "r:gz")
    f = tar.extractfile(member)
    soup = BeautifulSoup(f, 'html.parser')
    takeArtist = lambda trackInfoUnit: trackInfoUnit.find(class_='trackName').string.strip().split('-')[-1]
    takeCounts = lambda trackInfoUnit: trackInfoUnit.find(class_='counts').string.strip().split(' ')[-2]
    
    TracksInfosSoup = soup.find_all(class_='trackInfo')
    ArtistList = list(map(takeArtist, TracksInfosSoup))   
    CountsList = map(int,list(map(takeCounts, TracksInfosSoup)))   
    # zip_iterator = zip(ArtistList, CountsList)
    # dictResult = dict(zip_iterator)
    dictResult={}
    for key, val in zip(ArtistList, CountsList):
        dictResult[key] = dictResult.get(key, 0) + val
    CounterResult = Counter(dictResult)
    return (CounterResult)

def merge_function(dict_1, dict_2):
    return dict_1 + dict_2


def mapreduce(num_cpus=2):
    tar = tarfile.open('dados.tar.gz', 'r:gz')
    if num_cpus > 1:
        with mp.Pool(num_cpus) as pool:
            intermed = pool.imap_unordered(extract_and_process,tar.getmembers())
    else:
        intermed = map(extract_and_process, tar.getmembers())
    final = reduce(merge_function, intermed)
    return final

# import os
# filepath = os.path.join('.', 'exemplo', 'most-covered-tracks_1')
# with open(filepath) as html_doc:
#     soupt = BeautifulSoup(html_doc, 'html.parser')
#     DicCounter = Counter()
#     teste = soupt.find_all(class_='trackInfo')
#     print(teste[0].find(class_='trackName').string.strip().split('-')[-1])
#     print(teste[0].find(class_='counts').string.strip().split(' ')[-2])
    
    
    
# keys_list = ["a", "b",'a']
# values_list = [1, 2,5]
# zip_iterator = zip(keys_list, values_list)
# a_dictionary = dict(zip_iterator)
# a_counter = Counter(a_dictionary)
# data={}
# for key, val in zip(keys_list, values_list):
#     data[key] = data.get(key, 0) + val 
    



