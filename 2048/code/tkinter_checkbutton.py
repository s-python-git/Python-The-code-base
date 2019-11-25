# tkinter_checkbutton.py

import tkinter

root = tkinter.Tk()

def onCheckBtn():
    v = myvar.get() 
    print("checkbutton按钮被点击, v=", v)

myvar = tkinter.IntVar(root)  # 创建一个整型变量对象
checkbtn = tkinter.Checkbutton(root, 
                   text='自动登陆',
                   command=onCheckBtn,
                   variable=myvar)  # 让checkbtn关联myvar
checkbtn.pack()

myvar2 = tkinter.IntVar(value=1)  # 默认为选中
checkbtn2 = tkinter.Checkbutton(root, text='真值',
                    variable=myvar2)
checkbtn2.pack()
root.mainloop()


