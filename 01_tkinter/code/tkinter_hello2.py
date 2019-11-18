# tkinter_hello.py

# 此示例示意tkinter的基本框架的用法

# 1. 导入tkinter
import tkinter

# 2. 创建顶层窗口
root = tkinter.Tk()

# 3. 创建一个标签控件
label = tkinter.Label(root, text='hello world')

# 4. 把label 放置在root 窗口上
label.pack()

label2 = tkinter.Label(root, text='你好中国')
label2.pack()

# 5. 进入主事件循环
print("正在进入主事件循环")
root.mainloop()
print("程序退出")