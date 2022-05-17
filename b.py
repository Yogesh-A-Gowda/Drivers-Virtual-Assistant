import tkinter
from tkinter import *
from PIL import Image,ImageTk

root=Tk()



#bg = PhotoImage("car.jpg")
#an=Canvas(root)
#can.pack()
#can.create_image(0,0,image=bg,anchor="nw")

root.title("Drivers Virtual Assistant")
lab1 = Label(root, text="Driver's Virtual Assistant", font=("agency FB", 70, 'bold'), fg='purple').pack(side='top', pady=30)




img = Image.open('car.jpg')
a = ImageTk.PhotoImage(img.resize((550,200)))
lab2 = Label(root, image = a).pack(side='top', fill='both', expand='false' , padx=300, pady=60)


img = Image.open('mic.jpg')
b = ImageTk.PhotoImage(img.resize((100,80)))
lab2 = Label(root, image = b).pack(side='left', padx=265)




img = Image.open('mute.jpg')
c = ImageTk.PhotoImage(img.resize((100,80)))
lab3 = Label(root, image = c).pack(side='left', padx=275)


btn1 = tkinter.Button(root, text="Speak", bg='green', fg='white')
btn1.pack()
btn1.config(width=35, height=2)
btn1.place(x=200,y=650)



btn2 = tkinter.Button(root, text="Mute", bg='red', fg='black')
btn2.pack()
btn2.config(width=35, height=2)
btn2.place(x=840,y=650)



root.mainloop()
