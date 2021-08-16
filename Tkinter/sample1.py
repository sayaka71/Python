# coding: utf-8
# Udemy講座 "TkinterでGUI制作"
# Tkinter: GUIを簡単に作成できるライブラリ

import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title('Sayaka')
root.iconbitmap('./python.ico')
root.geometry('300x800')
root.config(bg='pink')

# サブウィンドウ
sub_window = tkinter.Toplevel()
sub_window.title('Sub_Sayaka')
sub_window.config(bg='#123123')
sub_window.geometry('300x800+400+400') # 重ならないよう

# ウインドウのループ処理をすることで表示ができる
root.mainloop() #一番最後に記述




