from tkinter import *
root = Tk()

group = LabelFrame(root,text='世界上最好的脚本语言是：',padx=5,pady=5)

group.pack(padx=10,pady=10)
LANGS = [
    ('Python',1),
    ('Perl',2),
    ('Ruby',3),
    ('Lua',4)]

v = IntVar()

for lang,num in LANGS:
    b = Radiobutton(group,text=lang,variable=v,value=num)
    b.pack(fill=X)

mainloop()