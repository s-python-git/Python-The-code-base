
import tkinter

root = tkinter.Tk()

label1 = tkinter.Label(root, text='第一行',)
label1.pack()

label2 = tkinter.Label(root, text='第二行', bg='#FF00FF')
label2.pack()

label3 = tkinter.Label(root, text='第三行', fg='#FF0000')
label3.pack()

label4 = tkinter.Label(root, text='第四行',
                       fg='#FF0000',
                       bg='#0000FF',  # 背景色
                       width=10,
                       height=3,
                       font=('黑体', 20,'bold')
                       )
label4.pack()


root.mainloop()

