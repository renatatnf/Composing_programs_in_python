# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:39:22 2020

@author: renata.fernandes
"""

class Conta:
    
        def __init__(self, numero):
            self.__numero = numero
            self.__saldo = 0.0
        
        @property   
        def saldo(self):
            return self.__saldo 
        
        def depositar(self, valor):
            self.__saldo += valor
            
        def sacar(self, valor):
            self.__saldo -= valor

class ContaCorrente(Conta):
    
        def __init__(self, numero,taxa):
            super().__init__(numero)
            self.__taxa = taxa
            
        def cobrar_taxa(self):
            self.sacar(self.__taxa)

class ContaPoupanca(Conta):
        def __init__(self, numero,juros):
            super().__init__(numero)
            self.__juros = juros
            
        def aplicar_juros(self):
            self.depositar(self.saldo*self.__juros)
            
            
conta_corrente = ContaCorrente(1, 1.50)
conta_corrente.depositar(10)
conta_corrente.cobrar_taxa()