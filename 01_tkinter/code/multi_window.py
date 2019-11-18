
import tkinter
root = tkinter.Tk()

def onBtn():
    import tkinter.messagebox
    mb = tkinter.messagebox.askokcancel(
        title='gameover',
        message='是否继续!'
    )
    if mb:
        print("你点的是确定")
    else:
        print("你点的是取消")

btn = tkinter.Button(root, text='弹出窗口',
        command=onBtn)
btn.pack()  # 打包布局
root.mainloop()

