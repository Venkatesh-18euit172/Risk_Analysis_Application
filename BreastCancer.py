from tkinter import Tk, mainloop, PhotoImage, Label, Entry, Button, Frame, font
from tkinter.font import Font

try:
    import Tkinter as tk
except:
    import tkinter as tk

from PIL import ImageTk , Image


import pandas as pd
import numpy as np

dataset = pd.read_csv("riskdataset.csv")
x = dataset.iloc[ : , : -1 ]
y = dataset.iloc[ : , 5]

from sklearn.preprocessing import LabelEncoder
x = x.apply(LabelEncoder().fit_transform)

from sklearn.tree import DecisionTreeClassifier
decisiontree = DecisionTreeClassifier()
decisiontree.fit(x.iloc[ : , 0:5 ] , y)


root = Tk()
root.title('Breast Cancer Risk Analysis')
root.geometry('1000x650+230+60')

l=[]

image = Image.open("D:\\Downloads\\Images\\All.jpg")
image = image.resize((1000, 650), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)
background_label = Label(root, image=background_image)
background_label.pack()

begin_test = Button(root, text="Start Analysis", bg='white', fg='black', font='Times 25', width=15 , command= lambda : page1()).place(x=170, y=350)
label = Label(root, text="Breast Cancer Risk ", bg='white', fg='black', font='Verdana 30 bold').place(x=100, y=150)
label1 = Label(root, text="Analysis", bg='white', fg='black', font='Verdana 30 bold').place(x=200, y=200)

def page1():
    l.clear()
    root1 = tk.Toplevel()
    root1.title('Breast Cancer Risk Analysis')
    root1.geometry('1000x650+230+60')

    image1 = Image.open("D:\\Downloads\\Images\\All.jpg")
    image1 = image1.resize((1000, 650), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(image1)
    label1=Label(root1, image=background_image1)
    label1.image=background_image1
    label1.pack()

    Label(root1, text="Do you consume more than 2 drinks of alcohol per day?", bg='white', fg='black', font='Verdana 20 bold').place(x=50,y=30)
    var = tk.StringVar()  # used to get the 'value' property of a tkinter.Radiobutton
    tk.Radiobutton(root1,text='Yes', indicatoron = 0,variable=var, value="yes",bg='white', fg='black', font='Times 30 bold', height=3, width =15 ,command=lambda : page2(var.get())).place(x=50,y=150)
    tk.Radiobutton(root1,text='No', indicatoron = 0,variable=var,value="no",bg='white', fg='black', font='Times 30 bold', height=3, width =15 ,command=lambda : page2(var.get())).place(x=50,y=350)

def page2(value):
    l.append(value)
    root1 = tk.Toplevel()
    root1.title('Breast Cancer Risk Analysis')
    root1.geometry('1000x650+230+60')

    image1 = Image.open("D:\\Downloads\\Images\\All.jpg")
    image1 = image1.resize((1000, 650), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(image1)
    label1=Label(root1, image=background_image1)
    label1.image=background_image1
    label1.pack()

    Label(root1, text="Have you used birth control hormones,implants or IUDs?", bg='white', fg='black',
          font='Verdana 20 bold').place(x=50, y=30)
    var = tk.StringVar()  # used to get the 'value' property of a tkinter.Radiobutton
    tk.Radiobutton(root1, text='Yes', indicatoron=0, variable=var, value="yes", bg='white', fg='black',
                   font='Times 30 bold', height=3, width=15, command=lambda: page3(var.get())).place(x=50, y=150)
    tk.Radiobutton(root1, text='No', indicatoron=0, variable=var, value="no", bg='white', fg='black',
                   font='Times 30 bold', height=3, width=15, command=lambda: page3(var.get())).place(x=50, y=350)

def page3(value):
    l.append(value)
    root1 = tk.Toplevel()
    root1.title('Breast Cancer Risk Analysis')
    root1.geometry('1000x650+230+60')

    image1 = Image.open("D:\\Downloads\\Images\\All.jpg")
    image1 = image1.resize((1000, 650), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(image1)
    label1=Label(root1, image=background_image1)
    label1.image=background_image1
    label1.pack()

    Label(root1, text="Are you obese?", bg='white', fg='black',
          font='Verdana 30 bold').place(x=55, y=30)
    var = tk.StringVar()  # used to get the 'value' property of a tkinter.Radiobutton
    tk.Radiobutton(root1, text='Yes', indicatoron=0, variable=var, value="yes", bg='white', fg='black',
                   font='Times 30 bold', height=3, width=15, command=lambda: page4(var.get())).place(x=50, y=150)
    tk.Radiobutton(root1, text='No', indicatoron=0, variable=var, value="no", bg='white', fg='black',
                   font='Times 30 bold', height=3, width=15, command=lambda: page4(var.get())).place(x=50, y=350)

def page4(value):
    l.append(value)
    root1 = tk.Toplevel()
    root1.title('Breast Cancer Risk Analysis')
    root1.geometry('1000x650+230+60')

    image1 = Image.open("D:\\Downloads\\Images\\All.jpg")
    image1 = image1.resize((1000, 650), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(image1)
    label1 = Label(root1, image=background_image1)
    label1.image = background_image1
    label1.pack()

    Label(root1, text="Do you have a family history of breast cancers?", bg='white', fg='black',
          font='Verdana 25 bold').place(x=55, y=30)
    var = tk.StringVar()  # used to get the 'value' property of a tkinter.Radiobutton
    tk.Radiobutton(root1, text='Yes', indicatoron=0, variable=var, value="yes", bg='white', fg='black',
                   font='Times 30 bold', height=3, width=15, command=lambda: page5(var.get())).place(x=50, y=150)
    tk.Radiobutton(root1, text='No', indicatoron=0, variable=var, value="no", bg='white', fg='black',
                   font='Times 30 bold', height=3, width=15, command=lambda: page5(var.get())).place(x=50, y=350)

def page5(value):
    l.append(value)
    root1 = tk.Toplevel()
    root1.title('Breast Cancer Risk Analysis')
    root1.geometry('1000x650+230+60')

    image1 = Image.open("D:\\Downloads\\Images\\All.jpg")
    image1 = image1.resize((1000, 650), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(image1)
    label1 = Label(root1, image=background_image1)
    label1.image = background_image1
    label1.pack()

    Label(root1, text="Do you have physical activity everyday?", bg='white', fg='black',
          font='Verdana 25 bold').place(x=55, y=30)
    var = tk.StringVar()  # used to get the 'value' property of a tkinter.Radiobutton
    tk.Radiobutton(root1, text='Yes', indicatoron=0, variable=var, value="yes", bg='white', fg='black',
                   font='Times 30 bold', height=3, width=15, command=lambda: page6(var.get())).place(x=50, y=150)
    tk.Radiobutton(root1, text='No', indicatoron=0, variable=var, value="no", bg='white', fg='black',
                   font='Times 30 bold', height=3, width=15, command=lambda: page6(var.get())).place(x=50, y=350)

def page6(value):
    l.append(value)
    root1 = tk.Toplevel()
    root1.title('Breast Cancer Risk Analysis')
    root1.geometry('1000x650+230+60')

    image1 = Image.open("D:\\Downloads\\Images\\All.jpg")
    image1 = image1.resize((1000, 650), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(image1)
    label1 = Label(root1, image=background_image1)
    label1.image = background_image1
    label1.pack()

    a={"yes":1,"no":0}
    n1=a[l[0]]
    n2=a[l[1]]
    n3=a[l[2]]
    n4=a[l[3]]
    n5=a[l[4]]

    Label(root1, text="Your risk level is:", bg='white', fg='black', font='Verdana 30 bold').place(x=100,y=50)
    var = tk.StringVar()  # used to get the 'value' property of a tkinter.Radiobutton
    tk.Radiobutton(root1, text='Re-assessment', indicatoron=0, variable=var, value="Yes", bg='white', fg='black',
                   font='Times 20 bold', height=2, width=12, command=lambda: page1()).place(x=50, y=350)
    tk.Radiobutton(root1, text='Quit', indicatoron=0, variable=var, value="No", bg='white', fg='black',
                   font='Times 20 bold', height=2, width=10, command=lambda: root.destroy()).place(x=280, y=350)

    test_data = np.array([n1, n2, n3, n4, n5])
    output = decisiontree.predict([test_data])

    Label(root1, text=output[0], bg='white', fg='black', font='Verdana 30 bold').place(x=200 , y=200)

mainloop()