# -*- coding: utf8


import threading
import requests
import os
from numba import jit
import concurrent.futures

class Worker(threading.Thread):
    # Use requests.get para baixar um livro
    # A linha abaixo gera o link para um livro
    # id_ = 1182
    # 'http://www.gutenberg.org/files/{}/{}-0.txt'.format(id_, id_)
    # USE HTTP PARA FUNCIONAR NO MOODLE, NÃO HTTPS
    def __init__(self, bookId, **kwargs):
    	  super(Worker, self).__init__(**kwargs)
    	  self._id = bookId
    	  self._nlines = 0
          
    def run(self):
        book = requests.get('http://www.gutenberg.org/files/{}/{}-0.txt'.format(self._id, self._id))
        self._nlines = len(book.text.splitlines())
              
    def get_result(self):
        return self._nlines
    
#@jit(nopython=True, nogil=True)
def booklines(bookId):
    book = requests.get('http://www.gutenberg.org/files/{}/{}-0.txt'.format(bookId, bookId))
    #nbooklines = book.text.count('\n')
    nbooklines = len(book.text.splitlines())
    return nbooklines
                  
def crawler(num_threads):
    # Dispara N threads
    # Soma o resultado de todas
    nlinhasList = []
    filepath = os.path.join('.', 'dados', 'ids.txt')
    listIDs=[]
    with open(filepath) as input_file:
        for line in input_file:
            listIDs.append(line.strip())
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in executor.map(booklines, listIDs):
            nlinhasList.append(i)
    return sum(nlinhasList) 
            
  
    # threadsuseds=[]
    # len(listIDs)%num_threads            
    # for i in range(num_threads): 
    #     threadsuseds.append(Worker(line))
    #     threadsuseds[i].start()
    #     threadsuseds[i].join()
    #     print(threadsuseds[i].get_result())
    #         #
    # teste = Worker(1182)
    # teste.start()
    # teste.join()
    # print(teste.get_result())


