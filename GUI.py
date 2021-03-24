from tkinter import*
root=Tk()
root.title("GPA Calculator")
root.geometry("500x300")

#first subject
Label(root,text='Classname:').place(x=100,y=30)
Label(root,text='  Gredit :').place(x=250,y=30)
Label(root,text='   Grade : ').place(x=400,y=30)

v1=StringVar()
v2=IntVar()
v3=StringVar()

#subject 1
Label(root,text="Subject 1:").place(x=40,y=60)
subject1_classname=Entry(root,textvariable=v1)
subject1_credit=Entry(root,textvariable=v2)
subject1_grade=Entry(root,textvariable=v3)
subject1_classname.place(x=-50,y=60)
subject1_credit.place(x=,y=60)
subject1_classname.place(x=200,y=60)


Button(root,text='ADD',width=10,background="black",foreground="white").place(x=120,y=140)


root.mainloop()
