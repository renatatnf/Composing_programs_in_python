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
        def __find_axes_intersect(Retangulo,Ponto2D):
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
        
        @staticmethod
        def calcularIntersecaoStatic(selfRet,Retangulo):  
            WidthIntersect = 0
            HeightIntersect = 0
            
            CheckIntersect = selfRet.__find_axes_intersect(selfRet,Retangulo.esq_sup)
            if CheckIntersect:
                HeightIntersect = selfRet.intersectMeasure(Retangulo.esq_sup.y,selfRet.dir_inf.y,Retangulo.height) 
                WidthIntersect = selfRet.intersectMeasure(selfRet.dir_inf.x,Retangulo.esq_sup.x,Retangulo.width) 
            
            EI=Ponto2D(Retangulo.esq_sup.x,Retangulo.esq_sup.y-Retangulo.height)    
            CheckIntersect = selfRet.__find_axes_intersect(selfRet,EI)
            if CheckIntersect:
                HeightIntersect = selfRet.intersectMeasure(selfRet.esq_sup.y,Retangulo.dir_inf.y,selfRet.height) 
                WidthIntersect = selfRet.intersectMeasure(selfRet.dir_inf.x,Retangulo.esq_sup.x,Retangulo.width) 
              
            CheckIntersect = selfRet.__find_axes_intersect(selfRet,Retangulo.dir_inf)
            if CheckIntersect:
                HeightIntersect = selfRet.intersectMeasure(selfRet.esq_sup.y,Retangulo.dir_inf.y,Retangulo.height)   
                WidthIntersect = selfRet.intersectMeasure(Retangulo.dir_inf.x,selfRet.esq_sup.x,Retangulo.width)   
            
            DS=Ponto2D(Retangulo.dir_inf.x,Retangulo.dir_inf.y+Retangulo.height)    
            CheckIntersect = selfRet.__find_axes_intersect(selfRet,DS)
            if CheckIntersect:
                HeightIntersect = selfRet.intersectMeasure(Retangulo.esq_sup.y,selfRet.dir_inf.y,selfRet.height) 
                WidthIntersect = selfRet.intersectMeasure(Retangulo.dir_inf.x,selfRet.esq_sup.x,Retangulo.width) 
                
            return WidthIntersect*HeightIntersect    
            
        def calcularIntersecao(self,Retangulo):
            WidthIntersect = 0
            HeightIntersect = 0
            
            CheckIntersect = self.__find_axes_intersect(self,Retangulo.esq_sup)
            if CheckIntersect:
                HeightIntersect = self.intersectMeasure(Retangulo.esq_sup.y,self.dir_inf.y,Retangulo.height) 
                WidthIntersect = self.intersectMeasure(self.dir_inf.x,Retangulo.esq_sup.x,Retangulo.width) 
            
            EI=Ponto2D(Retangulo.esq_sup.x,Retangulo.esq_sup.y-Retangulo.height)    
            CheckIntersect = self.__find_axes_intersect(self,EI)
            if CheckIntersect:
                HeightIntersect = self.intersectMeasure(self.esq_sup.y,Retangulo.dir_inf.y,self.height) 
                WidthIntersect = self.intersectMeasure(self.dir_inf.x,Retangulo.esq_sup.x,Retangulo.width) 
              
            CheckIntersect = self.__find_axes_intersect(self,Retangulo.dir_inf)
            if CheckIntersect:
                HeightIntersect = self.intersectMeasure(self.esq_sup.y,Retangulo.dir_inf.y,Retangulo.height)   
                WidthIntersect = self.intersectMeasure(Retangulo.dir_inf.x,self.esq_sup.x,Retangulo.width)   
            
            DS=Ponto2D(Retangulo.dir_inf.x,Retangulo.dir_inf.y+Retangulo.height)    
            CheckIntersect = self.__find_axes_intersect(self,DS)
            if CheckIntersect:
                HeightIntersect = self.intersectMeasure(Retangulo.esq_sup.y,self.dir_inf.y,self.height) 
                WidthIntersect = self.intersectMeasure(Retangulo.dir_inf.x,self.esq_sup.x,Retangulo.width) 
                
            CheckIntersect = self.__find_axes_intersect(Retangulo,self.esq_sup)
            if CheckIntersect:
                HeightIntersect = self.intersectMeasure(self.esq_sup.y,Retangulo.dir_inf.y,self.height) 
                WidthIntersect = self.intersectMeasure(Retangulo.dir_inf.x,self.esq_sup.x,self.width) 
                 
            CheckIntersect = self.__find_axes_intersect(Retangulo,self.dir_inf)
            if CheckIntersect:
                HeightIntersect = self.intersectMeasure(Retangulo.esq_sup.y,self.dir_inf.y,self.height)  
                WidthIntersect = self.intersectMeasure(self.dir_inf.x,Retangulo.esq_sup.x,self.width)
            

            AreaIntersect =  WidthIntersect*HeightIntersect

            if AreaIntersect==0:
                return None
            else:
                return AreaIntersect
            

r1_esq_sup = Ponto2D(0, 2)
r1_dir_inf = Ponto2D(2, 0)



r2_esq_sup = Ponto2D(1, 3)
r2_dir_inf = Ponto2D(3, 1)

ret1 = Retangulo(r1_esq_sup, r1_dir_inf)
ret2 = Retangulo(r2_esq_sup, r2_dir_inf)


area1 = ret1.calcularArea() 
print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))
area2 = ret2.calcularArea()
print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))
intersecao = ret1.calcularIntersecao(ret2)
print(intersecao)