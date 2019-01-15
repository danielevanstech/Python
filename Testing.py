import sys
from tkinter import Button,mainloop
x = Button(
   text = 'Press Me - I am new here so i would like to konw what the fuck is going on!',
   command = (lambda:print('Spam\n')))
x.pack()
mainloop()