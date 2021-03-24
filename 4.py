def quadratic (a,b,c):
    condition=(b**2-4*a*c)**0.5
    if condition >0:
        value1=(-b+((b**2-4*a*c)**0.5))/2*a
        value2=(-b-((b**2-4*a*c)**0.5))/2*a
        print( "value 1 is", value1)
        print( "value 2 is", value2)
    elif condition ==0:
        value=(-b+((b**2-4*a*c)**0.5))/2*a
        print("value is ", value)
    elif condition <0:
        print("no value")
quadratic(1,1,-12)

           
