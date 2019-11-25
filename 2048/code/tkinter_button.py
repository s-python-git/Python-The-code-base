# tkinter_button.py

def myquit():
    print("按钮被点击!")
    import sys
    # sys.exit()  # 退出程序(不建议这样退出)
    root.destroy()  # 退出程序


import tkinter

root = tkinter.Tk()

button = tkinter.Button(root, text='点我退出', 
                        command=myquit)
button.pack()

root.mainloop()