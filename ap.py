from email import message
import hashlib
import os
from tkinter import *
import tkinter
from tkinter import messagebox
#from PIL import Image, ImageTk
from tkinter import filedialog
from numpy import empty

#root = Tk()
#root.withdraw() #use to hide tkinter window


# Global Variable 
malware_hashes = list(open('virusHash.unibit','r').read().split('\n'))
virusInfo = list(open('virusHash.unibit','r').read().split('\n'))


# Get hash of file 
def sha256_hash(filename):
    try :
        with open(filename,'rb') as f :
            bytes = f.read()
            sha256_hash = hashlib.sha256(bytes).hexdigest()   

            f.close()

        # Print(sha256hash)
    except:

        return sha256_hash


# Malware detection by hash

def malware_checker (pathOffline):
    global malware_hashes
    global virusInfo


    hash_malware_check = sha256_hash(pathOffline)
    counter = 0 



    for i in malware_hashes:
        if i == hash_malware_check:
            return virusInfo[counter]
        counter += 1

    return 0


# Malware Dectection In Folder

virusName = []      # when the virus is detect then they go to this folder .
virusPath = []

def folderScanner(path):  

    # Get the list of all files in directory tree at given part .
    dir_list = list()

    for (dirpath,dirnames,filenames) in os.walk(path):

        dir_list += [ os.path.join ( dirpath,files ) for files in filenames ]

    for i in dir_list:
        print(i)
        if malware_checker(i) != 0:
            virusName.append(malware_checker(i)+' :: File :: '+i)
            virusPath.append(i)

msg=[]

# Virus Remover 
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
        message.showInfo('This File Is Safe .')
    else:
        message.showInfo('Alert','This File Is Not Safe !!!')


def removeFile():
    filepath= filedialog.askdirectory()
    virusRemover(filepath)

    if not msg:
        message.showInfo('Done','Virus Removed')
    
    else:
        message.showInfo("Virus Not found !!!")





# Create Tkinter Object
roo_ueuron =tkinter. Tk()

roo_ueuron.title('Antivirus')
roo_ueuron['bg'] = 'black'

roo_ueuron.geometry('500x600')

#left_frame = Frame(roo_ueuron, width=200, height=900)
#left_frame.grid(row=0, column=0, padx=1, pady=1)


# Read the Image
#image = Image.open("V:\Virus Remover\Antivirus_2.jpg")

# Resize the image using resize() method
#resize_image = image.resize((1600, 900))
 
#img = ImageTk.PhotoImage(resize_image)
 

# create label and add resize image
#Label(roo_ueuron,image=img).pack()
label_file_explorer = Label(roo_ueuron,  
                            text = "Antivirus", 
                            width = 100, height = 4, 
                            fg = "black"
                            ,bg = "sky blue")

label_file_explorer.config(font=("Courier", 15,'bold','underline'))

label_file_explorer.grid(column = 1, row = 1)
label_file_explorer.place(x=-350, y=0)

detect_btn = tkinter.Button (roo_ueuron,text='Malware Checker',width=15, height=1,font=('time new roman',12,'bold'),bg='green',fg='white')
detect_btn.place(x=60,y=100)
detect_btn.grid(row = 1, column = 3, pady = 110, padx = 170)


detect_btn = tkinter.Button (roo_ueuron,text='VirusScanner',width=15, height=1,font=('time new roman',12,'bold'),bg='red',fg='white')
detect_btn.place(x=60,y=220)
detect_btn.grid(row = 3, column = 3, pady = 5, padx = 170)


detect_btn = tkinter.Button (roo_ueuron,text='Junkfileremover',width=15, height=1,font=('time new roman',12,'bold'),bg='orange',fg='white')
detect_btn.place(x=60,y=340)
detect_btn.grid(row = 5, column = 3, pady=80, padx = 170)


detect_btn = tkinter.Button (roo_ueuron,text='RamBooster',width=15, height=1,font=('time new roman',12,'bold'),bg='blue',fg='white')
detect_btn.place(x=60,y=460)
detect_btn.grid(row = 7, column = 3,pady = 20 ,padx = 170)


# Execute Tkinter
roo_ueuron.mainloop()