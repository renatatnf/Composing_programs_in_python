# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:40:30 2020

@author: renata.fernandes
"""

class Ponto2D:
    
        def __init__(self, x=0.0, y=0.0):
            self.__x = x
            self.__y = y
            
        @property
        def x(self):
            return self.__x
        
        @property
        def y(self):
            return self.__y

class Retangulo:
    
        def __init__(self, esq_sup, dir_inf):
            self.__esq_sup = esq_sup
            self.__dir_inf = dir_inf
        
        @property
        def esq_sup(self):
            return self.__esq_sup
        
        @property
        def dir_inf(self):
            return self.__dir_inf
            
        @property
        def width(self):
            return self.dir_inf.x - self.esq_sup.x
        
        @property
        def height(self):
            return self.esq_sup.y - self.dir_inf.y
        
        @staticmethod    
        def find_axes_intersect(Retangulo,Ponto2D):
            intersectX=False
            intersectY=False
            Intersect=False
            #axes x intersect
            if Ponto2D.x >= Retangulo.esq_sup.x and Ponto2D.x <= Retangulo.dir_inf.x:
                intersectX =True
            #axes y intersect
            if Ponto2D.y <= Retangulo.esq_sup.y and Ponto2D.y >= Retangulo.dir_inf.y:
                intersectY =True
            if intersectX and intersectY:
                Intersect = True
            return Intersect 
            
        @staticmethod
        def intersectMeasure(M1,M2,Measure):
            MeasureIntersect = M1 - M2
            if MeasureIntersect > Measure:
                MeasureIntersect = Measure
            return MeasureIntersect   
        
        def calcularArea(self):
            return self.width*self.height
            
        def calcularIntersecao(self,Retangulo):
            WidthIntersect = 0
            HeightIntersect = 0
            CheckIntersect = self.find_axes_intersect(self,Retangulo.esq_sup)
            if CheckIntersect:
                HeightIntersect = self.intersectMeasure(Retangulo.esq_sup.y,self.dir_inf.y,Retangulo.height) 
                WidthIntersect = self.intersectMeasure(self.dir_inf.x,Retangulo.esq_sup.x,Retangulo.width) 
                
            CheckIntersect = self.find_axes_intersect(self,Retangulo.dir_inf)
            if CheckIntersect:
                HeightIntersect = self.intersectMeasure(self.esq_sup.y,Retangulo.dir_inf.y,Retangulo.height)   
                WidthIntersect = self.intersectMeasure(Retangulo.dir_inf.x,self.esq_sup.x,Retangulo.width)   
  
            CheckIntersect = self.find_axes_intersect(Retangulo,self.esq_sup)
            #print(CheckIntersect)
            if CheckIntersect:
                HeightIntersect = self.intersectMeasure(self.esq_sup.y,Retangulo.dir_inf.y,Retangulo.height) 
                WidthIntersect = self.intersectMeasure(Retangulo.dir_inf.x,self.esq_sup.x,Retangulo.width) 
                 
            CheckIntersect = self.find_axes_intersect(Retangulo,self.dir_inf)
            #print(CheckIntersect)
            if CheckIntersect:
                HeightIntersect = self.intersectMeasure(Retangulo.esq_sup.y,self.dir_inf.y,Retangulo.height)  
                WidthIntersect = self.intersectMeasure(Retangulo.dir_inf.x,self.esq_sup.x,Retangulo.width)                 
            
            #HeightIntersect = max(HeightIntersect1,HeightIntersect2,HeightIntersect3,HeightIntersect4)
            #WidthIntersect = max(WidthIntersect1,WidthIntersect2,WidthIntersect3,WidthIntersect4)

            AreaIntersect =  WidthIntersect*HeightIntersect  
            if AreaIntersect==0:
                return None
            else:
                return AreaIntersect
            
ret1_ES = Ponto2D(-6.5,5.0)
ret1_DI = Ponto2D(-2.0,2.5)
ret1 = Retangulo(ret1_ES,ret1_DI)   

ret2_ES = Ponto2D(-4.5,4.0)
ret2_DI = Ponto2D(-1.0 -1.0)
ret2 = Retangulo(ret2_ES,ret2_DI) 

InterArea = ret1.calcularIntersecao(ret2)

InterArea2 = ret2.calcularIntersecao(ret1)