def cylinder(radius,height):
   volume=((radius**2)*3.1415926)*height
   print("the volume of this cylinder is ",volume)
#def circle():
   #circle has volume??????
def cone(radius,height):
   volume=(((radius**2)*3.1415926)*height)*(1/3)
   print("the volume of this cone is ",volume)
def sphere(radius):
   volume=(3/4)*3.1415926*(radius**2)
   print("the volume of this cone is ",volume)

question=input("what shape you want to calculate(cylinder,#circle,cone,sphere?)::")
if question=="cylinder":
   print("you need to enter radius and height of cylinder")
   radius= int(input("enter radius"))
   height=int(input("enter height"))
   cylinder(radius,height)
elif question=="circle":
   print("circle has no volume, right???")
elif question=="cone":
   print("you need to enter radius and height for cone")
   radius= int(input("enter radius"))
   height=int(input("enter height"))
   cone(radius,height)
elif question=="sphere":
   print("you need to enter radius for this sphere")
   radius= int(input("enter radius"))
   sphere(radius)
else:
   print("we can only calculate these four shapes!!")
   
   
   
   
