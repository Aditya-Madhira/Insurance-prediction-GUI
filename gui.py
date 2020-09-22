from tkinter import *
import joblib
from tkinter.ttk import *
import  numpy as np
predictor=joblib.load('model.pkl')
def f():

    final_array=[]
    region_array=[]
    region=regionbox.get()
    age=int(ageinp.get())
    gender=genderbox.get()
    bmi=float(bmiinp.get())
    children=int(childinp.get())
    smoker=smokerbox.get()
    if(region=='NorthEast'):
        region_array=[1.0,0.0,0.0,0.0]
        final_array=region_array.copy()
    elif(region=='NorthWest'):
        region_array = [0.0, 1.0, 0.0, 0.0]
        final_array = region_array.copy()
    elif(region=='SouthEast'):
        region_array = [0.0, 0.0, 1.0, 0.0]
        final_array = region_array.copy()
    elif(region=='SouthWest'):
        region_array = [0.0, 0.0, 0.0, 1.0]
        final_array = region_array.copy()

    final_array.append(age)
    if(gender=='Male'):
        final_array.append(1)
    elif(gender=='Female'):
        final_array.append(0)
    final_array.append(bmi)
    final_array.append(children)
    if(smoker=='Yes'):
        final_array.append(1)
    elif(smoker=='No'):
        final_array.append(0)
    feedarray=np.array(final_array)
    feedarray=feedarray.reshape(1,-1)
    ans=predictor.predict(feedarray)
    newwin=Tk()
    newwin.geometry('400x400')
    anslab = Label(newwin, text=ans, font=('Ariel', 20)).pack()











mywin=Tk()
mywin.geometry('1400x900')
Title_label=Label(mywin,text="Insurance Predictor",font=('Ariel',30)).pack()







#region

region_label=Label(mywin,text="Choose region",font=('Ariel',15)).place(x=50,y=120)
regionvalues=['NorthEast','NorthWest','SouthEast','SouthWest']
regionbox=Combobox(mywin,values=regionvalues,width=20)
regionbox.place(x=320,y=120)

#age
age_label=Label(mywin,text="Enter Age",font=('Ariel',15)).place(x=50,y=240)
ageinp=StringVar()
ageentry=Entry(mywin,textvariable=ageinp).place(x=320,y=240)
#gender
gender_label=Label(mywin,text="Choose Gender",font=('Ariel',15)).place(x=50,y=350)
gendervalues=['Male','Female']
genderbox=Combobox(mywin,values=gendervalues,width=20)
genderbox.place(x=320,y=350)
#bmi
bmi_label=Label(mywin,text="Enter bmi in decimals",font=('Ariel',15)).place(x=50,y=480)
bmiinp=StringVar()
bmientry=Entry(mywin,textvariable=bmiinp).place(x=320,y=480)
#children
child_label=Label(mywin,text="Enter number of children",font=('Ariel',15)).place(x=50,y=560)
childinp=StringVar()
childentry=Entry(mywin,textvariable=childinp).place(x=320,y=560)
#smoker
smoker_label=Label(mywin,text="Are you a smoker?",font=('Ariel',15)).place(x=50,y=670)
smokervalues=['Yes','No']
smokerbox=Combobox(mywin,values=smokervalues,width=20)
smokerbox.place(x=320,y=670)

button=Button(mywin,text='Submit',width=50,command=f).place(x=400,y=720)




mywin.mainloop()