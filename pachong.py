from tkinter import *
from tkinter import scrolledtext

import requests
import re
import threading

def get(ID):
    varl.set('已经获取到第%s本书'%ID)
    html = requests.get("https://book.douban.com/top250?start=" + str(ID))
    print(html.text)
    reg = re.compile(r'<table width="100%">.*?class="pl2".*?<a.*?>(.*?)</a>.*?class="pl">(.*?)</p>.*?rating_nums.*?>(.*?)</span>.*?pl.*?(\d+)人评价.*?</span>.*?</table>',re.S)
    list = re.findall(reg, html.text)
    return list

def write():
    ID = 0
    a = []
    b = []
    s = 0
    while ID <= 240:
        L = get(ID)
        ID +=20
        for i in L:
            s += 1
            a.append(float(i[2]))
            b.append(float(i[3]))
            text.insert(END,'书名%s'   '评分%s'              '评价数：%s\n'%(i[0],i[2],i[3]))
    text.insert(END,'--------------------------\n')
    text.insert(END,'该分类书本总数量：%s\n'%s)
    text.insert(END,'书本总评分：%s分\n' % sum(a))
    text.insert(END,'书本总评价数：%s条\n' % sum(b))
    text.insert(END,'书本平均评分%2f分\n' % (sum(a)/s))
    fn = open('read.text', 'w', encoding='utf-8')
    fn.write(text.get(1.0, END))
    fn.close()
    varl.set('处理完毕')

def th():
    t1 = threading.Thread(target=write)
    t1.start()

#GUI部分
root = Tk()   #创建窗口
root.title('西安优盛信息技术有限公司')
root.geometry('700x530') #设置窗口大小
text = scrolledtext.ScrolledText(root,font = ('微软雅黑',10))
text.grid()  #布局方法

button = Button(root, text ='开始分析',font = ('微软雅黑',10),command = th)
button.grid()

varl = StringVar()   #设置变量，文字会发生变化
label = Label(root,font = ('微软雅黑',10),fg = 'red',textvariable = varl)
label.grid()

varl.set('准备中...')
root.mainloop()
