from tkinter import Tk, mainloop, PhotoImage, Label, Entry, Button, Frame, font
from tkinter.font import Font

try:
    import Tkinter as tk
except:
    import tkinter as tk

from PIL import ImageTk , Image

import pandas as pd
import numpy as np

dataset = pd.read_csv("ProjectDataset.csv")
x = dataset.iloc[ : , : -1 ]
y = dataset.iloc[ : , 5]

from sklearn.preprocessing import LabelEncoder
x = x.apply(LabelEncoder().fit_transform)

from sklearn.tree import DecisionTreeClassifier
decisiontree = DecisionTreeClassifier()
decisiontree.fit(x.iloc[ : , 0:5 ] , y)


root = Tk()
root.title('Digital Covid Test')
root.geometry('1000x650+230+60')

l=[]

image = Image.open("D:\\Downloads\\Images\\A.jpeg")
image = image.resize((1000, 650), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)
background_label = Label(root, image=background_image)
background_label.pack()

begin_test = Button(root, text="Begin the test", bg='white', fg='red', font='Times 25', width=15 , command = lambda : page1()).place(x=500, y=570)
label = Label(root, text="Digital COVID Test", bg='white', fg='red', font='Verdana 30 bold').place(x=500, y=50)

def page1():
    l.clear()
    root1 = tk.Toplevel()
    root1.title('Select Your Age')
    root1.geometry('1000x650+230+60')

    image1 = Image.open("D:\\Downloads\\Images\\Age.jpg")
    image1 = image1.resize((1000, 650), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(image1)
    label1=Label(root1, image=background_image1)
    label1.image=background_image1
    label1.pack()

    Label(root1, text="Select Your Age", bg='white', fg='red', font='Verdana 30 bold').place(x=20,y=30)
    var = tk.StringVar()  # used to get the 'value' property of a tkinter.Radiobutton
    tk.Radiobutton(root1,text='1-17', indicatoron = 0,variable=var, value="1-17",bg='white', fg='blue', font='Times 18 bold', width =20 ,command=lambda : page2(var.get())).place(x=10,y=470)
    tk.Radiobutton(root1,text='18-29', indicatoron = 0,variable=var,value="18-29",bg='white', fg='blue', font='Times 18 bold', width =20 ,command=lambda : page2(var.get())).place(x=10,y=530)
    tk.Radiobutton(root1,text='30-39', indicatoron = 0,variable=var, value="30-39",bg='white', fg='blue', font='Times 18 bold', width =20 ,command=lambda : page2(var.get())).place(x=10,y=590)
    tk.Radiobutton(root1,text='40-49', indicatoron = 0,variable=var,value="40-49",bg='white', fg='blue', font='Times 18 bold', width =20 ,command=lambda : page2(var.get())).place(x=360,y=470)
    tk.Radiobutton(root1,text='50-59', indicatoron = 0,variable=var, value="50-59",bg='white', fg='blue', font='Times 18 bold', width =20 ,command=lambda : page2(var.get())).place(x=360,y=530)
    tk.Radiobutton(root1,text='60-64', indicatoron = 0,variable=var,value="60-64",bg='white', fg='blue', font='Times 18 bold', width =20 ,command=lambda : page2(var.get())).place(x=360,y=590)
    tk.Radiobutton(root1,text='65-69', indicatoron = 0,variable=var, value="65-69",bg='white', fg='blue', font='Times 18 bold', width =20 ,command=lambda : page2(var.get())).place(x=690,y=470)
    tk.Radiobutton(root1,text='70-79', indicatoron = 0,variable=var,value="70-79",bg='white', fg='blue', font='Times 18 bold', width =20 ,command=lambda : page2(var.get())).place(x=690,y=530)
    tk.Radiobutton(root1,text='80 above', indicatoron = 0,variable=var, value="80 above",bg='white', fg='blue', font='Times 18 bold', width =20 ,command=lambda : page2(var.get())).place(x=690,y=590)

def page2(value):
    l.append(value)
    root1 = tk.Toplevel()
    root1.title('Select your Gender')
    root1.geometry('1000x650+230+60')

    image1 = Image.open("D:\\Downloads\\Images\\Gender.jpeg")
    image1 = image1.resize((1000, 650), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(image1)
    label1=Label(root1, image=background_image1)
    label1.image=background_image1
    label1.pack()

    Label(root1, text="Select your Gender", bg='white', fg='red', font='Verdana 30 bold').place(x=320,y=10)
    var = tk.StringVar()  # used to get the 'value' property of a tkinter.Radiobutton
    tk.Radiobutton(root1,text='Female', indicatoron = 0,variable=var, value="Female",bg='white', fg='blue', font='Times 30 bold',command=lambda : page3(var.get())).place(x=173,y=550)
    tk.Radiobutton(root1,text='Male', indicatoron = 0,variable=var,value="Male",bg='white', fg='blue', font='Times 30 bold',command=lambda : page3(var.get())).place(x=670,y=550)

def page3(value):
    l.append(value)
    root1 = tk.Toplevel()
    root1.title('Breathing difficulty')
    root1.geometry('1000x650+230+60')

    image1 = Image.open("D:\\Downloads\\Images\\Breathe.png")
    image1 = image1.resize((1000, 650), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(image1)
    label1=Label(root1, image=background_image1)
    label1.image=background_image1
    label1.pack()

    Label(root1, text="Do you have difficulty in breathing?", bg='white', fg='red', font='Verdana 30 bold').place(x=70,y=10)
    var = tk.StringVar()  # used to get the 'value' property of a tkinter.Radiobutton
    tk.Radiobutton(root1,text='Yes', indicatoron = 0,variable=var, value="Yes",bg='white', fg='blue', font='Times 25 bold',height=4, width =10 ,command=lambda : page4(var.get())).place(x=20,y=220)
    tk.Radiobutton(root1,text='No', indicatoron = 0,variable=var,value="No",bg='white', fg='blue', font='Times 25 bold',height=4, width =10 ,command=lambda : page4(var.get())).place(x=750,y=220)

def page4(value):
    l.append(value)
    root1 = tk.Toplevel()
    root1.title('Contact with covid person')
    root1.geometry('1000x650+230+60')

    image1 = Image.open("D:\\Downloads\\Images\\Contact.jpg")
    image1 = image1.resize((1000, 650), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(image1)
    label1 = Label(root1, image=background_image1)
    label1.image = background_image1
    label1.pack()

    Label(root1, text="Did you have contact with a covid affected person?", bg='white', fg='red', font='Verdana 25 bold').place(x=4,y=10)
    var = tk.StringVar()  # used to get the 'value' property of a tkinter.Radiobutton
    tk.Radiobutton(root1,text='Yes', indicatoron = 0,variable=var, value="Yes",bg='white', fg='blue', font='Times 20 bold',height=3, width =10 ,command=lambda : page5(var.get())).place(x=30,y=500)
    tk.Radiobutton(root1,text='No', indicatoron = 0,variable=var,value="No",bg='white', fg='blue', font='Times 20 bold',height=3, width =10 ,command=lambda : page5(var.get())).place(x=800,y=500)
    tk.Radiobutton(root1, text="Don't Know", indicatoron=0, variable=var, value="Don't Know", bg='white', fg='blue', font='Times 20 bold',height=3,width=20, command=lambda: page5(var.get())).place(x=370, y=500)

def page5(value):
    l.append(value)
    root1 = tk.Toplevel()
    root1.title('Other Symptoms')
    root1.geometry('1000x650+230+60')

    image1 = Image.open("D:\\Downloads\\Images\\Symptom.jpg")
    image1 = image1.resize((1000, 650), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(image1)
    label1 = Label(root1, image=background_image1)
    label1.image = background_image1
    label1.pack()

    Label(root1, text="Do you have any Other Symptoms?", bg='white', fg='red', font='Verdana 30 bold').place(x=100,y=10)
    var = tk.StringVar()  # used to get the 'value' property of a tkinter.Radiobutton
    tk.Radiobutton(root1,text='Yes', indicatoron = 0,variable=var, value="Yes",bg='white', fg='blue', font='Times 20 bold',height=2, width =10 ,command=lambda : page6(var.get())).place(x=270,y=550)
    tk.Radiobutton(root1,text='No', indicatoron = 0,variable=var,value="No",bg='white', fg='blue', font='Times 20 bold', height=2,width =10 ,command=lambda : page6(var.get())).place(x=510,y=550)

def page6(value):
    l.append(value)
    root1 = tk.Toplevel()
    root1.title('Result')
    root1.geometry('1000x650+230+60')

    image1 = Image.open("D:\\Downloads\\Images\\Status.jpeg")
    image1 = image1.resize((1000, 650), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(image1)
    label1 = Label(root1, image=background_image1)
    label1.image = background_image1
    label1.pack()

    a={"1-17":8,"18-29":0,"30-39":1,"40-49":2,"50-59":3,"60-64":4,"65-69":5,"70-79":6,"80 above":7}
    b={"Male":1,"Female":0}
    c={"Yes":1,"No":0}
    d={"Yes":3,"No":2,"Don't Know":1,"-":0}
    e={"Yes":2,"No":1,"-":0}
    n1=a[l[0]]
    n2=b[l[1]]
    n3=c[l[2]]
    n4=d[l[3]]
    n5=e[l[4]]

    Label(root1, text="Your Status", bg='white', fg='red', font='Verdana 30 bold').place(x=350,y=10)
    var = tk.StringVar()  # used to get the 'value' property of a tkinter.Radiobutton
    tk.Radiobutton(root1, text='Take Re-test', indicatoron=0, variable=var, value="Yes", bg='white', fg='blue',
                   font='Times 20 bold', height=2, width=10, command=lambda: page1()).place(x=280, y=500)
    tk.Radiobutton(root1, text='Quit', indicatoron=0, variable=var, value="No", bg='white', fg='blue',
                   font='Times 20 bold', height=2, width=10, command=lambda: root.destroy()).place(x=550, y=500)

    test_data = np.array([n1, n2, n3, n4, n5])
    output = decisiontree.predict([test_data])

    Label(root1, text=output[0], bg='white', fg='red', font='Verdana 30 bold').place(x=280 , y=270)

mainloop()