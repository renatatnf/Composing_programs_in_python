from functools import reduce
import operator 

def firstChars(L):
    """ Maps strings in L to a list with the first character of each string.
    For instance:
    firstChars(['python', 'is', 'pythy']) == ['p', 'i', 'p']
    """
    return list(map(lambda x: x[0],L))

def sum(L):
    """ Sums the elements in L """
    #return reduce(lambda acc,x: acc + x,L,0)
    return reduce(operator.add,L,0)

def avg(L):
    """ Returns the average of the elements in L """
    return sum(L)/len(L)

def maxString(L):
    """ Retorna a maior string dentre as strings em L.
    Por exemplo: maxString(['python', 'is', 'pythy']) == 'python'
    Se houver empate, retorna a primeira string encontrada.
    """
    return reduce(lambda acc,x: acc if len(acc) > len(x) else x ,L,'')

def add2Dict(D, N, S):
    """ Insere a string S na lista associada ao inteiro N dentro
    do dicionario D.
    Por exemplo, se D = {1: ['b'], 2: ['xd'], 3: ['abc']}, entao,
    add2Dict(D, 2, 'ww') produz o novo dicionario:
    {1: ['b'], 2: ['xd', 'ww'], 3: ['abc']}
    Voce pode usar essa funcao para completar buildLenFreq
    """
    D[N] = D[N] + [S] if N in D else [S]
    return D

def buildLenFreq(L):
    """ Esta funcao constroi um dicionario que associa inteiros a listas com
    palavras daquele tamanho. Por exemplo:
    buildLenFreq(['abc', 'xd', 'b', 'xxx']) = {1: ['b'], 2: ['xd'], 3: ['abc', 'xxx']}
    """
    return reduce(lambda acc,x: add2Dict(acc,len(x),x),L,{})

def incValue(D, N):
    """Esta funcao incrementa o valor associado a chave N dentro do dicionario
    D. Por exemplo, se D = {1: 2, 2: 4, 3: 11}, entao
    Voce pode usar essa funcao para completar countFirsts
    """
    D[N] = D[N] + 1 if N in D else 1
    return D

def countFirsts(L):
    """ Conta o numero de ocorrencias do primeiro caracter de cada string em L.
    Por exemplo, countFirsts(['python', 'is', 'pythy']) === {'i': 1, 'p': 2}
    Note que essa funcao retorna um dicionario com cada caracter associada ao
    numero de strings que comecam com aquele caracter.
    """
    return reduce(lambda acc,x: incValue(acc,x[0]),L,{})

def mostCommonFirstChar(L):
    """ Retorna a letra mais comum entre as primeiras letras de strings em L.
    Por exemplo:
    mostCommonFirstChar(['python', 'is', 'pythy']) === 'p'
    """
    D = countFirsts(L)
    FC = firstChars(L)
    return reduce(lambda acc,x: x if D[x]>D[acc] else acc, FC,FC[0]) 
   

