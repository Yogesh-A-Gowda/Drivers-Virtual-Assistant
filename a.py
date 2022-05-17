import tkinter
from tkinter import *
from PIL import Image,ImageTk

img=''

root=Tk()



root.geometry('1360x768')
load=Image.open('carbgf.jpg')
rend=ImageTk.PhotoImage(load)
img=Label(root,image=rend)
img.place(x=0, y=0)

#**************************************************************************************************
#hereeeeeeeee
#liste=['1', '2', '3']
#lis=Listbox(root)
#lis.pack(side='left')
#for item in liste:
 #   lis.insert("end",item)




#bg = PhotoImage("car.jpg")
#an=Canvas(root)
#can.pack()
#can.create_image(0,0,image=bg,anchor="nw")

root.title("Drivers Virtual Assistant")
lab1 = Label(root, text="Driver's Virtual Assistant", font=("agency FB", 70, 'bold'), fg='#883935',bg='#1A1112', activebackground='#1A1112').pack(side='top', pady=30)


img = Image.open('gmic1.jpg')
b = ImageTk.PhotoImage(img.resize((25,49)))
lab2 = Label(root, image = b)
lab2.place(x=500,y=480)
#lab2.place(x=100,y=100)
#b=Button(root, image=img)
#b.place(x=200,y=520)
#1E1415'

img1 = PhotoImage(file='spkb.png')
b2= Button(root, image=img1, bg='black')
b2.place(x=430,y=560)



img2 = Image.open('rmute.png')
b3 = ImageTk.PhotoImage(img2.resize((49,25)))
lab3 = Label(root, image = b3)
lab3.place(x=780,y=500)
#lab2.place(x=100,y=100)
#b=Button(root, image=img)
#b.place(x=200,y=520)


img3 = PhotoImage(file='muteb.png')
b4= Button(root, image=img3, bg='black')
b4.place(x=730,y=560)



#img1 = PhotoImage(file='muteb.png')
#b1 = Button(root, image=img1, bg='black')

#b1.place(x=400,y=520)


#img = Image.open('car.jpg')
#a = ImageTk.PhotoImage(img.resize((550,200)))
#lab2 = Label(root, image = a, bg= 'white').pack(side='top', fill='both', expand='false' , padx=300, pady=60,)


#img = Image.open('mic.jpg')
#b = ImageTk.PhotoImage(img.resize((100,80)))
#lab2 = Label(root, image = b, bg='black').pack(side='left', padx=265)




#img = Image.open('mute.jpg')
#c = ImageTk.PhotoImage(img.resize((100,80)))
#lab3 = Label(root, image = c).pack(side='left', padx=275)


#btn1 = tkinter.Button(root, text="Speak", bg='green', fg='white')
#btn1.pack()
#btn1.config(width=35, height=2)
#btn1.place(x=200,y=520)



#btn2 = tkinter.Button(root, text="Mute", bg='red', fg='black')
#btn2.pack()
#btn2.config(width=35, height=2)
#btn2.place(x=840,y=650)



root.mainloop()
