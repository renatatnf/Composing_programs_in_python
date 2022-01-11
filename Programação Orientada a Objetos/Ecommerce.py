# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 00:08:36 2020

@author: renata.fernandes
"""

from abc import ABC, abstractmethod

class Item(ABC):
        def __init__(self, nome, valor ):
            self.__nome = nome
            self.__valor = valor
            
        @property   
        def nome(self):
            return self.__nome
            
        @property   
        def valor(self):
            return self.__valor
        
        @abstractmethod 
        def valor_desconto(self,qtde):
            pass
            
        def valor_total_item(self, qtde):
            return self.valor*qtde
        

class Livro(Item):
    
        def __init__(self, nome, valor ):
            super().__init__(nome, valor)
        
        def valor_desconto(self,qtde):
            return self.valor*qtde*(1-0.03)
    
class Brinquedo(Item):
        def __init__(self, nome, valor ):
            super().__init__(nome, valor)
            
        def valor_desconto(self,qtde):
            return self.valor*qtde*(1-0.05)

class Eletronico(Item):
        def __init__(self, nome, valor ):
            super().__init__(nome, valor)
            
        def valor_desconto(self,qtde):
            return self.valor*qtde*(1-0.08)
    
class CestaCompras:
       
        def __init__(self):
            self.__itens = {}

        @property   
        def itens(self):
            return self.__itens 
            
        def adicionar_item(self, Item, quantidade ):
            self.__itens[Item] = quantidade
        
        def __valor_total(self):
            valortotal = 0
            for k, v in self.itens.items():
                valortotal += k.valor_desconto(v)
            return valortotal
            
            
        def relatorio_final(self):
            
            print ('{:.2f}'.format(self.__valor_total()))
            
            for k, v in self.itens.items():
               # print(type(k).__name__+ ', ' + k.nome + ', ' + str(v) + ', ' + str(k.valor) + ', ' + str(k.valor_item(v))+ ', ' + str(k.valor_desconto(v)))
                print('{}, {}, {}, {:.2f}, {:.2f}, {:.2f}'.format(type(k).__name__, k.nome, v, k.valor, k.valor_total_item(v), k.valor_desconto(v)))
            
            #<tipo_item, nome, quantidade, valor_unitario, total_sem_desconto, total_com_desconto>
    
      
            
            
livro1 = Livro("Senhor dos Aneis", 15.00)
brinq1 = Brinquedo("Carrinho", 12.99)

cesta = CestaCompras()
cesta.adicionar_item(livro1, 3)
cesta.adicionar_item(brinq1, 4)

cesta.relatorio_final()