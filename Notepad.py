from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root = Tk()
root.geometry('800x500')
root.title('Notepad')
root.iconbitmap('1.ico')

def NewFile():
    root.title('Untitled - Notepad')
    textarea.delete(1.0, END)

def OpenFile():
    global file
    file = askopenfilename(defaultextension='.txt',
                    filetypes=[('All Files', '*.*'),
                               ('Text Documents', '*.txt')])
    if file == '':
        file = None
    else:
        root.title(os.path.basename(file)+ ' - Notepad')
        textarea.delete(1.0, END)
        f = open(file, 'r')
        textarea.insert(1.0, f.read())
        f.close()

def SaveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',
                          defaultextension='.txt',
                          filetypes=[('All Files', '*.*'),
                          ('Text Documents', '*.txt')])

        if file == 'mk':
            file=None
        else:
            f = open(file, 'w')
            f.write(textarea.get(1.0, END))
            f.close
            root.title(os.path.basename(file)+ ' - Notepad')
    else:
        f = open(file, 'w')
        f.write(textarea.get(1.0, END))
        f.close()



def Cut():
    textarea.event_generate(('<<Cut>>'))

def Copy():
    textarea.event_generate(('<<Copy>>'))

def Paste():
    textarea.event_generate(('<<Paste>>'))

def About():
    showinfo('About Me', 'Python Tkinter Notepad Project \nBy: Mohit Kumhar')




textarea = Text(font='lucida 12')
file = None
textarea.pack(expand=True, fill=BOTH)

scroll = Scrollbar(textarea)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)


menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New', command=NewFile)
filemenu.add_command(label='Open', command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label='Save', command=SaveFile)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=exit)
menubar.add_cascade(label='File', menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Cut', command=Cut)
editmenu.add_command(label='Copy', command=Copy)
editmenu.add_command(label='Paste', command=Paste)
menubar.add_cascade(label='Edit', menu=editmenu)

aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label='About', command=About)
menubar.add_cascade(label='About', menu=aboutmenu)

root.config(menu=menubar)









root.mainloop()