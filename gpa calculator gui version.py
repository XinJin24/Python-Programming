from tkinter import *
import tkinter as tk
def cunygrade(grade):
    if grade == "A+":  # A+
        return 4.0
    elif grade == "A":  # A
        return 4.0
    elif grade == "A-":  # A-
        return 3.7
    elif grade == "B+":  # B+
        return 3.3
    elif grade == "B":  # B
        return 3.0
    elif grade == "B-":  # B-
        return 2.7
    elif grade == "C+":  # C+
        return 2.3
    elif grade == "C":  # C
        return 2.0
    elif grade == "C-":  # C-
        return 1.7
    elif grade == "D+":  # D+
        return 1.3
    elif grade == "D":  # D
        return 1.0
    elif grade == "F":  # F
        return 0

def Clicked1():
    classinfo = a1.get()
    classarray.append(classinfo)
    credit = b.get()
    creditarray.append(credit)
    grade = c.get()
    gradearray.append(grade)
    creditpoint = cunygrade(grade)
    creditpointarray.append(creditpoint)
    classinfo.clear()
    credit.clear()
    grade.clear()
    
    
def Clicked2():
    count=0
    for a in classarray:
        gpa= (int(creditpointarray[count]) * int(creditarray[count])) / int(creditarray[count])
        gpa = round(gpa, 2)
        gpaarray.append(gpa)
        count = count + 1
    average= sum(gpaarray)/count
    t.insert(1.0,average)

creditarray=[]
gradearray=[]
classarray=[]
gpaarray=[]
creditpointarray=[]

top = tk.Tk()
top.title("GPA CALCULATOR")
labelHello = tk.Label(top,text = "Classname", height = 5, width = 20, fg = "black").pack()
a1 =StringVar()
entryCd = tk.Entry(top,textvariable=a1)
entryCd.pack()

labelHello1 = tk.Label(top, text = "Credit", height = 5, width = 20, fg = "blue").pack()
b =StringVar()
entryCd1 = tk.Entry(top,textvariable=b).pack()

labelHello2 = tk.Label(top, text = "Grade", height = 5, width = 20, fg = "gray").pack()
c=StringVar()
entryCd2 = tk.Entry(top,textvariable=c).pack()

btn1 = tk.Button(top, text = "ADD THIS CLASS", command = Clicked1,foreground="green",background="white").pack()
btn = tk.Button(top, text = "CALCULATE ALL", command = Clicked2,background="black",foreground="white").pack()


labelHello3 = tk.Label(top, text = "AVERAGE GPA", height = 5, width = 20, fg = "blue").pack()

t = Text(top,height = 1.5, width = 20)
t.pack()

top.mainloop()












