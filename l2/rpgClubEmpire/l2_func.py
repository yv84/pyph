import random
import math

class l2_func():
   
   distXYdist = lambda self, X,Y: ( (X.x - Y.x)**2 + (X.y - Y.y)**2 ) ** (1/2)  # distanciya mejdu tochkami
   distXYZdist = lambda self, X,Y: ( (X.x - Y.x)**2 + (X.y - Y.y)**2 + (X.z - Y.z)**2 ) ** (1/2) #distanciya medju tochkami
   g_XY = lambda self, BG, X, Y : ( BG * (X.x - Y.x)/dist(X, Y) + Y.x, BG * (X.y - Y.y)/dist(X, Y) + Y.y )  #koordinati tochki na otrezke mejdu dvumya tochkami
   procent = lambda self, A, B : int(A *100 / B)
   random = lambda self, A, B: random.randint(A, B) # Возвращает случайное число от a до b (включительно)
   xdiff = lambda self, X, Y : abs(X.x - Y.x) # Возвращает разность в X координате между вашим чаром и указанным объектом.
   ydiff = lambda self, X, Y : abs(X.y - Y.y) # Возвращает разность в Y координате между вашим чаром и указанным объектом.
   zdiff = lambda self, X, Y : abs(X.z - Y.z) # Возвращает разность в Z координате между вашим чаром и указанным объектом.
   l2StringToByte = lambda self, s : (s.encode("utf-16le")+b"\x00\x00")
   l2ByteToString = lambda self, b : (b+b"\x00\x00\x00").decode("utf-16le") 
   l2StringToByteNp = lambda self, s : (s.encode("utf-16le")+b"\x00\x00")
   l2ByteToStringNp = lambda self, b : b.tostring().decode("utf-16le") 


   def do(self):
     pass
     #self.do =  
     #self.ComeTo = lambda x y z d r, dtype :

   def pointIsInPoligonRange(self, obj, pol): #<obj> : (X,Y); <pol>: ((X,Y),)
     f = False
     VCnt = len(pol)
     for n1 in (range(VCnt)):
       n2 = (n1 + 1) % VCnt
       if ( obj.Y > pol[n1].Y ) ^ ( obj.Y > pol[n2].Y ):
         if ( obj.X > pol[n1].X ) + \
            ( pol[n2].X - pol[n1].X )*( obj.Y - pol[n1].Y ) \
            /( pol[n2].Y - pol[n1].Y ) : f = not(f)
     return f
