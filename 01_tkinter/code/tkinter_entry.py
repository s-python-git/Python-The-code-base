# tkinter_entry.py


import tkinter

root = tkinter.Tk()

# 创建一个Entry
entry = tkinter.Entry(root)
entry.pack()

# 创建一个Button
def get_text():
    text = entry.get()  # 获取文本框的内容
    print(text)

btn = tkinter.Button(root, text='获取entry的数据',
                    command=get_text)
btn.pack()

root.mainloop()