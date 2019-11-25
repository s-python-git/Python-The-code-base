# tkinter_button.py

def myquit():
    print("按钮被点击!")


import tkinter

root = tkinter.Tk()
img = tkinter.PhotoImage(file='mybtn.gif')

button = tkinter.Button(root, image=img, 
                        command=myquit)
button.pack()

button2 = tkinter.Button(root, bitmap='question')
# button2 = tkinter.Button(root, bitmap='error')
button2.pack()

root.mainloop()