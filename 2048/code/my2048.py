# my2048.py

# 2048的地图数据
_map_data = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# _map_data = [
#     [0, 0, 0, 2],
#     [4, 0, 4, 2],
#     [0, 8, 8, 0],
#     [2, 0, 0, 0]
# ]

def _left_move_number(line):
    for _ in range(3):
        for i in range(3):
            if line[i] == 0:  # 右侧的过来填充
                line[i] = line[i+1]
                line[i+1] = 0

def _left_merge_number(line):
    '''合同相邻数字'''
    for i in range(3):  # i代表索引
        if line[i] == line[i+1]:
            line[i] *= 2
            line[i+1] = 0

def _left_move_aline(line):
    '''此算函数如果line=[2, 0, 2, 8],
      让line = [4, 8, 0, 0]'''
    # 第一步,让左侧有0的数字左移, line=[2, 2, 8, 0]
    _left_move_number(line)
    # 第二步,让两个相邻的数合并
    _left_merge_number(line)
    # 第三步,让左侧有的数字左移
    _left_move_number(line)


def left():
    print("左键按下")
    for line in _map_data:
        _left_move_aline(line)

def right():
    print("右键按下")
    for line in _map_data:
        line.reverse()
        _left_move_aline(line)
        line.reverse()

def up():
    print("上键按下")
    for c in range(4):  # c 代表列索引
        # 把一列数据放在line中
        line = [0, 0, 0, 0]  # 初始化一个列表
        for r in range(4):
            line[r] = _map_data[r][c]
        # 把line内的数据左移
        _left_move_aline(line)
        # 再把line中的数据放回到c 代表的列中
        for r in range(4):
            _map_data[r][c] = line[r]
    


def down():
    print("下键按下")
    _map_data.reverse()
    up()  # 向上
    _map_data.reverse()

def get_space_count():
    '''此方法返回地图中0的个数'''
    count = 0
    for line in _map_data:
        count += line.count(0)  # line.count(0)返回0的个数
    return count
    

def fill2():
    '''此函数将向 _map_data中添加一个2到空位置'''
    blank_count = get_space_count()  # 得到地图上的空白位置
    if 0 == blank_count:
        print("地图已满,不添加!")
        return
    import random
    pos = random.randrange(0, blank_count)  # 生成位置
    offset = 0  # 记录当前的走到的位置
    for line in _map_data:  # line绑定一行的列表
        for c in range(4):  # c为行的索引
            if 0 == line[c]:
                if offset == pos:
                    line[c] = 2  # 在此位置添加2
                    return   # 成功添加并返回
                offset += 1


def main():
    import tkinter
    root = tkinter.Tk()

    def on_key_down(event):
        '''键盘按下事件处事函数'''
        if event.keysym  in ('Left', 'a'):
            left()
            fill2()
        elif event.keysym in ('Right', 'd'):
            right()
            fill2()
        elif event.keysym in ('Up', 'w'):
            up()
            fill2()
        elif event.keysym in ('Down', 's'):
            down()
            fill2()
        update_ui()  # 有按键按下后更新界面

    root.bind('<KeyPress>', on_key_down)

    def update_ui():
        '根据地图数据,重新设置UI的Label中的数字和颜色等信息'
        for r in range(4):  # r行的索引
            for c in range(4):  # c为列的索引
                number = _map_data[r][c]  # 获取数字
                label = map_labels[r][c]  # 获取数字对应的lable
                label['text'] = \
                    str(number) if number > 0 else ''

    map_labels = []  # 此列表保存所有的显示数字的label

    # 添加两个2
    fill2()
    fill2()
    # 创建2048地图
    for r in range(4):
        row = []  # 创建一个新的列表,用来绑定一行label
        for c in range(4):
            number = _map_data[r][c]
            txt = str(number) if number > 0 else ''
            label = tkinter.Label(root,
                     text=txt,
                     width=4, height=2,
                     font=('黑体', 30, 'bold'),
                     bg='#cdc1b4')
            label.grid(row=r, column=c,
            padx=5, pady=5)
            row.append(label)  # 保存,后续修改时使用
        map_labels.append(row)  # 加入一行labels

    root.mainloop()

main()

