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
    
fileMenu=Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",command=newfile)
fileMenu.add_command(label="Open",command=openfile)
fileMenu.add_command(label="Save",command=savefile)
fileMenu.add_command(label="Save as..",command=savefile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=exit_editor)

editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_cascade(label="Cut")
editMenu.add_cascade(label="Copy")
editMenu.add_cascade(label="Paste")
editMenu.add_cascade(label="Find..",command=findtext)

helpMenu=Menu(menu)
menu.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="View help",command=Help)

aboutMenu=Menu(menu)
menu.add_cascade(label="About",menu=aboutMenu)
aboutMenu.add_command(label="Releases",command=release)
fileMenu.add_separator()
aboutMenu.add_command(label="About Text Editor",command=about)

textArea.pack()

main.mainloop()
