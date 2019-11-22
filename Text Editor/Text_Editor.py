from tkinter import *
from tkinter import Tk,scrolledtext,Menu,filedialog,END,messagebox,simpledialog
import os

main=Tk(className =" Text Editor ")
textArea=scrolledtext.ScrolledText(main,width=200,height=200)

menu=Menu(main)
main.config(menu=menu)

def openfile():
    textArea.delete('1.0',END)
    file=filedialog.askopenfile(parent=main,title='Select a file',filetypes=(("Text file","*.txt"),("All Files","*.*")))
    main.title(os.path.basename(file.name)+"-Text Editor")
    if file!=None:
        contents=file.read()
        textArea.insert('1.0',contents)
        file.close()

def savefile():
    file=filedialog.asksaveasfile(mode='w',defaultextension=".txt",filetypes=(("Text file","*.txt"),("All Files","*.*")))
    if file!=None:
        data=textArea.get('1.0',END+'-1c')
        file.write(data)
        file.close()
    
def exit_editor():
    if len(textArea.get('1.0',END+'-1c'))>0:    
        messagebox.askyesno("Quit","Do you want to save the file before you quit?")
        savefile()
        main.destroy()
    else:
        main.destroy()

def about():
    label=messagebox.showinfo("About","This is a simple Text Editor")

def findtext():
    findstring=simpledialog.askstring("Find....","Enter Text")
    textdata=textArea.get('1.0',END)
    occurence=textdata.count(findstring)
    if textdata.count(findstring)>0:
        label=messagebox.showinfo("Results",findstring+" has multiple occurences,"+str(occurence))        
    else:
        label=messagebox.showinfo("Results","Mentioned text NOT FOUND")
        
def newfile():
    if len(textArea.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno("Save?","Do you wish to save?"):
            savefile()
        else:
            textArea.delete('1.0',END)
    textArea.delete('1.0',END)

def release():
    messagebox.showinfo("Releases"," 0.1 Version --Jayanth Apagundi ")

def Help():
    help_text="""This is Text Editor,Where you can Create,
Edit, Open and Modify the existing files, Save the modified files"""
    messagebox.showinfo("Help",help_text)

def cut():
    textArea.event_generate("<<Cut>>")

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def bind_shortcuts():
    textArea.bind('<Control+n>',newfile)
    textArea.bind('<Control+o>',openfile)
    textArea.bind('<Control+s>',savefile)
    textArea.bind('<Control+Shift+S>',savefile)
    textArea.bind('<Control+C>',copy)
    textArea.bind('<Control+X>',cut)
    textArea.bind('<Control+V>',paste)
    textArea.bind('<Control+F>',findtext)

fileMenu=Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",accelerator="Ctrl+N",command=newfile)
fileMenu.add_command(label="Open..",accelerator="Ctrl+O",command=openfile)
fileMenu.add_command(label="Save",accelerator="Ctrl+S",command=savefile)
fileMenu.add_command(label="Save as..",accelerator="Ctrl+Shift+S",command=savefile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=exit_editor)

editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",accelerator="Ctrl+X",command=cut)
editMenu.add_command(label="Copy",accelerator="Ctrl+C",command=copy)
editMenu.add_command(label="Paste",accelerator="Ctrl+V",command=paste)
editMenu.add_command(label="Find..",accelerator="Ctrl+F",command=findtext)

helpMenu=Menu(menu)
menu.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="View help",accelerator="Ctrl+H",command=Help)

aboutMenu=Menu(menu)
menu.add_cascade(label="About",menu=aboutMenu)
aboutMenu.add_command(label="Releases",command=release)
fileMenu.add_separator()
aboutMenu.add_command(label="About Text Editor",command=about)

textArea.pack()

main.mainloop()
