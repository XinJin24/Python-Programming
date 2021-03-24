# 2X^2+x-45=0
a=2
b=1
c=-45
import math
t=math.sqrt((b**2)-(4*a*c))
if t>0:
       print ("X=",(-b+t)/(2*a),"or",(-b-t)/(2*a))
elif t==0:
       print ("X=",(-b+t)/(2*a))
else:
       print ("none")
