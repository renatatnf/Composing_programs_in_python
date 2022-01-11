def head(L):
    return L[0]

 
def tail(L):
    return L[1]
    

def py2ll(L):
    if not L:
        return None        
    else: 
        return (L[0], py2ll(L[1:]))
    
def ll2py(L):
    if not L:
        return [] 
    else: 
        return [head(L)] + ll2py(tail(L))

def size(L):
    if not L:
        return 0 
    else: 
        return 1+size(tail(L))

def sorted(L):
    if not L:
        return True 
    if not tail(L):
        return True     
    else: 
        return head(L)<=head(tail(L)) and sorted(tail(L))

def sum(L):
    if not L:
        return 0
    if not tail(L):
        return head(L)  
    else: 
        return head(L)+sum(tail(L))

def split(L):
    if not L:
        return (None,None)
    if not tail(L):
        return ((head(L),None),None)    
        #return (L,None)
    else: 
        L0,L1 = split(tail(tail(L)))
        return (head(L),L0),((head(tail(L))),L1)
        #H0 = head(L)
        #H1 = head(tail(L))
        #(T0, T1) = split(tail(tail(L)))
        #return ((H0, T0), (H1, T1))

def merge(L0, L1):
    if not L1:
        return L0
    if not L0:
        return L1      
    else: 
        if head(L0)<=head(L1):
            return (head(L0),merge(L1,tail(L0)))
        else:
            return (head(L1),merge(L0,tail(L1)))


def mSort(L):
    if not L:
        return None  
    if not tail(L):
        return L   
    else: 
        (L0, L1) = split(L)
        return merge(mSort(L0), mSort(L1))

def max(L):
    if not L:
        return 0  
    if not tail(L):
        return head(L)   
    else: 
        if head(L) > head(tail(L)):
            return max((head(L),tail(tail(L))))
        else:
            return max(tail(L))          
        
def get(L, N):
    if N==0:
        return head(L)   
    else: 
        return get(tail(L),N-1)