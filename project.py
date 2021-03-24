#function
def cunygrade(grade):
    if grade>=97: #A+
        return 4.0
    elif 93<=grade<=96.9:#A
        return 4.0
    elif 90<=grade<=92.9:#A-
        return 3.7
    elif 87<=grade<=89.9:#B+
        return 3.3
    elif 83<=grade<=86.9:#B
        return 3.0
    elif 80<=grade<=82.9:#B-
        return 2.7
    elif 77<=grade<=79.9:#C+
        return 2.3
    elif 73<=grade<=76.9:#C
        return 2.0
    elif 70<=grade<=72.9:#C-
        return 1.7
    elif 67<=grade<=69.9:#D+
        return 1.3
    elif 60<=grade<=66.9:#D
        return 1.0
    elif 0<=grade<=59.9:#D
        return 0
#define five arrays:credit array,grade array,class array,and grade's corresponding creditpoint array, and gpa array
creditarray=[]
gradearray=[]
classarray=[]
gpaarray=[]
creditpointarray=[]
# set count to get how many time user input data,and how many clsses he/she has
count=0
# set x to get data in arrays by using while loop(make comparison with data total length:count)
x=0
#use while True loop to receive classes as much as user has,till user enter "break"
while True:
   classinfo=input("what is class's name?")
   #if class is existed, it is not gonna store in array, and ask user to retype class by keyword "continue"
   if classinfo in classarray:
        print("this class registered before!")
        print("please re-type!")
        continue
    #if class is not existed in array, then ask more info about this class 
   else:
       #store class name in array
       classarray.append(classinfo)
       #get this class's credit and grade
       credit,grade=eval(input("enter the credit and grade you got in this class:(separate by comma)"))
       # add these two input to their own arrays
       gradearray.append(grade)
       creditarray.append(credit)
       #get credit point according to the grade in function
       creditpoint=cunygrade(grade)
       # store credit point to array
       creditpointarray.append(creditpoint)
       gpa=(creditpointarray[count]*creditarray[count])/creditarray[count]
       gpa=round(gpa,2)
       # add gpa value to the array
       gpaarray.append(gpa)
       # output corresponding class name and its gpa by identify their address:count
       print("your class",classarray[count],"'s gpa is ",gpa)
       #count plus one so we can indentify next class's arrays corresponding value
       count=count+1
       print("the average gpa of all the classes you entered is ",round((sum(gpaarray)/count),2))
       
   condition=input("you have more classes?(yes/no)")
   #if user have more class, use "continue back to while True loop to add more class info as much as he/she wants"
   if condition=="yes":
       continue
   elif condition=="no":
       #if user has no more class,program will print all the class infomations and show each class's info for user to double check
       #make comparison between x and count, so i am able to get all the class's data by using while loop
       for a in range(count):
           #got average gpa: sum gpa them divide class amount
          totalgpa=sum(gpaarray)/count
          totalgpa=round(totalgpa,2)
          print("your class",classarray[a], "its credit is",creditarray[a]," , its grade is",gradearray[a],"and its gpa is",gpaarray[a])
       print("average pga of those",count,"classes is ",totalgpa)
   else:
       # if user type something else, this part of progrma is gonna remind him to retype
       print("your input was invalid!")
       condition=input("you have more classes?(yes/no)")
       if condition=="yes":
          continue
       elif condition=="no":
          for a in range(count):
              totalgpa=sum(gpaarray)/count
              totalgpa=round(totalgpa,2)
              print("your class",classarray[a], "its credit is",creditarray[a]," , its grade is",gradearray[a],"and its gpa is",gpaarray[a])
          print("average pga of those",count,"classes is ",totalgpa)
       
       
 
 
 

    
    

