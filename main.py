import tkinter as tk
import chuLi
import paQu
import send
class APP:
    def __init__(self, width=500, height=250):
        self.w = width
        self.h = height
        self.title = '就业招聘爬取系统'
        self.root = tk.Tk(className=self.title)
        self.a = tk.StringVar()
        self.v = tk.IntVar()
        self.v.set(1)

        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)
        frame_4 = tk.Frame(self.root)

        # Menu菜单
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        # 控件内容设置
        group = tk.Label(frame_1, text='就业招聘爬取系统:', padx=10, pady=10)
        label1 = tk.Label(frame_2, text="请输入要处理内容：")
        entry = tk.Entry(frame_2, textvariable=self.a, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        label2 = tk.Label(frame_2, text=" ")
        paQu1 = tk.Button(frame_2, text="爬取", font=('黑体', 12), fg='Purple', width=8, height=1, command=self.paQu)
        label3 = tk.Label(frame_2, text=" ")
        chuLi1 = tk.Button(frame_3, text="处理", font=('楷体', 12), fg='Purple', width=8, height=1, command=self.chuli)
        label4 = tk.Label(frame_3, text=" ")
        send1 = tk.Button(frame_3, text="发送", font=('楷体', 12), fg='Purple', width=8, height=1, command=self.send)

        # 控件布局
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        group.grid(row=0, column=0)
        label1.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        paQu1.grid(row=0, column=3, ipadx=10, ipady=10)
        label3.grid(row=0, column=4)
        chuLi1.grid(row=0, column=5, ipadx=10, ipady=10)
        label4.grid(row=0, column=6)
        send1.grid(row=0, column=7, ipadx=10, ipady=10)


    def paQu(self):
        b = self.a.get()
        if not b:
            return
        b = self.a.get()
        paQu.paQufun(b)

    def chuli(self):
        b = self.a.get()
        if not b:
            return
        b = self.a.get()
        chuLi.chuLifun(b)

    def send(self):
        send.sendfun()

# 居中
    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws / 2) - (self.w / 2))
        y = int((hs / 2) - (self.h / 2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    def loop(self):
        # 禁止修改窗口大小
        self.root.resizable(False, False)
        # 窗口居中
        self.center()
        self.root.mainloop()

if __name__ == '__main__':
    # 实例化APP对象
    app = APP()
    # loop等待用户事件
    app.loop()
