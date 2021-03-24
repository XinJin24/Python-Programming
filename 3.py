def hypotenus(opposite,adjacent):
    a=(opposite**2+adjacent**2)**0.5
    print("hypotenus is ",a)
def opposite(hypotenus,adjacent):
    b=(hypotenus**2-adjacent**2)**0.5
    print("oppsite is ",b)
def adjacent(opposite,hypotenus):
    c=(opposite**2-hypotenus**2)**0.5
    print("adjacent is",c)
q=input("hypotenus or opposite or adjacent??")
if q =="hypo":
    opposite=int(input("enter oppsite:"))
    adjacent=int(input("enter adjacent:"))
    hypotenus(opposite,adjacent)
if q =="oppo":
    hypotenus=int(input("enter hypotenus:"))
    adjacent=int(input("enter adjacent:"))
    opposite(hypotenus,adjacent)
if q=="adja":
    opposite=int(input("enter oppsite:"))
    hypotenus=int(input("enter hypotenus:"))
    adjacent(opposite,hypotenus)
