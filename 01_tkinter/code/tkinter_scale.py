# tkinter_scale.py

""" scale
"""
def resize(event=None):
    print(scale.get())

import tkinter
root = tkinter.Tk()
scale = tkinter.Scale(root, from_=12, to=40, orient=tkinter.HORIZONTAL,
command=resize)
scale.set(20)
scale.pack()

scale2 = tkinter.Scale(root, from_=12, to=40, orient=tkinter.VERTICAL,
command=resize)
scale2.pack()

root.mainloop()