# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:04:41 2021

@author: kjoh
"""

import tkinter as tk


#%% window & widget
main = tk.Tk()
main.title("Window")
main.geometry("300x200")

lbl = tk.Label(main, text="Label", font="Arial 20")
lbl.pack()

def appleclick():
    lbl["text"] = "Apple"
apple = tk.Button(main, text="Apple", foreground="Red", command = appleclick)
apple.pack()

def orangeclick():
    lbl["text"] = "Orange"
orange = tk.Button(main, text="Orange", foreground="Orange", command = orangeclick)
orange.pack()

main.mainloop()


#%% MessageBox
main = tk.Tk()
main.title("MessageBox")
main.geometry("300x200")

def btnclick():
    if tk.messagebox.askyesno("질문",  "당신은 미성년자입니까?"):
        tk.messagebox.showwarning("경고", "애들은 가라")
    else:
        tk.messagebox.showinfo("환영", "어서오세요. 고객님")

btn = tk.Button(main, text = "입장", foreground="Blue", command = btnclick)
btn.pack()

main.mainloop()
        

#%% simple dialog
main = tk.Tk()
main.title("Simple Dialog")
main.geometry("300x200")

def btnclick():
    name = tk.simpledialog.askstring("질문", "이름을 입력하시오")
    age = int(tk.simpledialog.askstring("질문", "나이를 입력하시오"))
    if age and name:
        tk.messagebox.showinfo("환영", "%d세 %s님 반갑습니다." % (age, name))
btn = tk.Button(main, text = "클릭", foreground = "Blue", command = btnclick)
btn.pack()

main.mainloop()


#%% menu
main = tk.Tk()
main.title("Menu")
main.geometry("300x200")

menubar = tk.Menu(main)
main.config(menu = menubar)

popup = tk.Menu(menubar)
menubar.add_cascade(label = "파일", menu = popup)

def about():
    tk.messagebox.showinfo("소개", "메뉴 사용 예제입니다.")

popup.add_command(label = "소개", command = about)
popup.add_command(label = "종료", command = main.destroy)

main.mainloop()


