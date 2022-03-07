# Import Module
#from cgitb import text

from engine import junkfileremover
from tkinter import *
import tkinter
import hashlib
import os
from tkinter import filedialog
from tkinter import messagebox
from numpy import empty




malware_hashes=list(open("virushash.unibit","r").read().split('\n'))
virusinfo = list(open("virusinfo.unibit","r").read().split('\n'))

def sha256_hash(filename):

    try:
        with open(filename, "rb") as f:
            bytes= f.read()
            sha256hash=hashlib.sha256(bytes).hexdigest()
            f.close()
        
    
        return sha256hash

    except:
        return 0


    



#now detect malware
def malware_detector(pathoffile):
    global malware_hashes
    global virusinfo
    h_m_check= sha256_hash(pathoffile)

    Counter=0

    for i in malware_hashes:
        if i == h_m_check:
            return virusinfo[Counter]
        counter =+1
        
    return 0
    

#malware detect in folder
virusName =[]
virusPath = []      # when the virus is detect then they go to this folder 

def folderScanner(path):

    dir_list = list()

    # Get the list of all files in directory tree at given part 
    for (dirpath,dirnames,filenames) in os.walk(path):
       


    
        dir_list += [os.path.join(dirpath, file) for file in filenames]
    
    

    for i in dir_list:
        print(i)
        if malware_detector(i)!=0:
            virusName.append(malware_detector(i)+":: File :: "+i)
            virusPath.append(i)


    

msg=[]
        
def virusRemover(path):
    folderScanner(path)
    if virusPath:
        for i in virusPath:
            os.remove(i)
            msg=[1]
    else:
        return 0





# file browsing

def scanfile():
    filepath= filedialog.askdirectory()
    folderScanner(filepath)
    if not virusName:

         messagebox.showinfo("Alert", "This file is  safe!!!!")
    else:
        messagebox.showinfo("Alert", "This file is not safe!!!!")


# virus removel
def removefile():
    filepath= filedialog.askdirectory()
    virusRemover(filepath)

    if not msg:

         messagebox.showinfo("done", " virus removed")
    else:
        messagebox.showinfo("Alert", "virus not removed")
    
    

def ramBooster():
    tasklist = ['notepad.exe',"cmd.exe"]

    # Task Kill

    for i in tasklist:

        os.system ("taskkill /f /im {}".format(i))

def engine_run():
    junkfileremover()
    messagebox.showinfo("done", " junkfiles removed")
    


    

    


roo_ueuron =tkinter. Tk()

roo_ueuron.title('Antivirus')
roo_ueuron['bg'] = 'black'


roo_ueuron.geometry('500x600')

#title label
title_lbl=Label(roo_ueuron, text="ATIVIRUS APP", 
        font=("times new roman",25,"bold","italic",'underline'),
        bg="sky blue",
        fg="black"
        )     

title_lbl.place(x=0,y=10,width=500,height=45)  


detect_btn = tkinter.Button (roo_ueuron,text='scan file',command=scanfile,width=15, height=1,font=('time new roman',12,'bold'),bg='red',fg='white')
detect_btn.place(x=150,y=100)


detect_btn = tkinter.Button (roo_ueuron,text='virus remove',command=removefile,width=15, height=1,font=('time new roman',12,'bold'),bg='sky blue',fg='white')
detect_btn.place(x=150,y=200)

detect_btn = tkinter.Button (roo_ueuron,text='junk file remove',command=engine_run,width=15, height=1,font=('time new roman',12,'bold'),bg='orange',fg='white')
detect_btn.place(x=150,y=300)

detect_btn = tkinter.Button (roo_ueuron,text='ramboost',command=ramBooster,width=15, height=1,font=('time new roman',12,'bold'),bg='blue',fg='white')
detect_btn.place(x=150,y=400)


# Execute Tkinter
roo_ueuron.mainloop()
