# -*- coding:utf-8 -*-

from time import sleep
import datetime
from tkinter import *


def getNowTime():
    while True:
        now_time = datetime.datetime.now()
        now_time = now_time.strftime('%Y-%m-%d  %H:%M:%S')
        return now_time
        sleep(1)

tk = Tk()
tk.title('时钟')
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
itext = canvas.create_text(80, 30, text=getNowTime())
while True:
    num = getNowTime()
    canvas.itemconfig(itext, text=num)
    #canvas.insert(itext, 12, '')
    tk.update()