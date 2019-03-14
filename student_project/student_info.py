# file: student.py
    
def input_student():
    L = []  # 创建一个列表,准备存放学生数据的字典
    while True:
        n = input("请输入姓名: ")
        if not n:  # 如果用户输入空字符串就结束输入
            break
        try:
            a = int(input("请输入年龄: "))
            s = int(input("请输入成绩: "))
        except ValueError:
            print("您的输入有错，请重新输入!!!")
            continue
        d = {}  # 一定要每次都创建一个新的字典
        d['name'] = n
        d['age'] = a
        d['score'] = s
        L.append(d)   # 把d加入列表中L
    return L

def output_student(L):
    print("+---------------+----------+----------+")
    print("|     姓名      |   年龄   |   成绩   |")
    print("+---------------+----------+----------+")
    for d in L:
        name = d['name']
        age = str(d['age'])  # 转为字符串
        score = str(d['score'])  # 转为字符串
        print("|%s|%s|%s|" % (name.center(15), 
                            age.center(10),
                            score.center(10)))
    print("+---------------+----------+----------+")

def delete_student(L):
    name = input("请输入要删除学生的姓名: ")
    i = 0  # i 代表列表的索引
    while i < len(L):
        d = L[i]  # d绑定字典
        if d['name'] == name:
            del L[i]
            print("删除", name, "成功!")
            break
        i += 1
    else:
        print("删除失败!")

def modify_student_score(L):
    pass


def output_by_score_desc(L):
    def get_score(d):
        return d['score']
    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)

def output_by_score_asc(L):
    L2 = sorted(L, key=lambda d:d['score'])
    output_student(L2)

def output_by_age_desc(L):
    L2 = sorted(L, key=lambda d:d['age'], reverse=True)
    output_student(L2)

def output_by_age_asc(L):
    L2 = sorted(L, key=lambda d:d['age'])
    output_student(L2)


def read_from_file():
    L = []  # 创建一个准备存放字典的列表
    try:
        # 1. 打开文件
        # f = open("./si.txt")
        # f = open("si.txt")
        f = open("/home/tarena/aid1812/pbase/day16/student_project/si.txt")
        # 2. 读取信息
        try:
            while True:
                line = f.readline()  # line='xiaozhang,20,100\n'
                if not line:  # 到达文件尾
                    break
                s = line.strip()  # 去掉左右两端的空白字符'xiaozhang,20,100'
                lst = s.split(',')  # ['xiaozhang', '20', '100']
                n = lst[0]
                a = int(lst[1])
                scr = int(lst[2])
                d = dict(name=n, age=a, score=scr)
                L.append(d)
        finally:
            # 3. 关闭文件
            f.close()
            print("读取数据成功")
    except OSError:
        print("读取数据失败")
    except ValueError:
        print("数据类型错误！")
    return L

def save_to_file(L):
    try:
        f = open("si.txt", 'w')
        # 循环写入每个学生的信息
        for d in L:
            # 每次写入一个学生的信息
            f.write(d['name'])  # 姓名
            f.write(',')
            f.write(str(d['age']))  # 年龄
            f.write(',')
            f.write(str(d['score']))  # 成绩
            f.write('\n')  # 换行
        f.close()
        print("保存成功")
    except OSError:
        print("保存失败!")
