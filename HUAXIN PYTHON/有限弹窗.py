import tkinter as tk
from tkinter import messagebox
import threading
import time
i = tk.Tk()#创建窗口
def c_3_command_():
    i_2 = tk.Toplevel()
    c_4 = tk.Label(i_2,text='你的电脑要炸了！')
    c_4.pack()

    i_2.title('123')

def 后台进程():
    s_2 = c_2.get()
    s_3 = int(s_2) - 1
    for s_1 in range(int(s_3)):
        c_3_command_()
        print(s_1)

    c_3_command_()

def c_3_command():
    global 后台进程_
    后台进程_.start()

后台进程_ = threading.Thread(target=后台进程)


c_1 = tk.Label(i,text='次数')
c_2 = tk.Entry(i)
c_3 = tk.Button(text='start',command=c_3_command)

c_1.pack()
c_2.pack()

c_3.pack()
i.title('1')
i.mainloop()