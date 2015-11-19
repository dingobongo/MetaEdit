#MetaWriteWavs

import subprocess, os

from Tkinter import *
import tkMessageBox

def folder_error():
    tkMessageBox.showerror("Error", "Folder is not set. Or metadata. csv hasn't been written")
    
def permission_error():
    tkMessageBox.showerror("Error","You don't have permission to write to this folder.")

def write_wavs(folder):
    writecheck = tkMessageBox.askyesno("Warning","This will write metadata into all wavs in the selected folder. Are you sure?")
    

    if writecheck == True:
        try:
            
            subprocess.call([os.path.join(os.getcwd(),"bwfmetaedit"), "--in-core="+os.path.join(folder,"metadata.csv")])

        except FileNotFoundError:
            folder_error()
        except PermissionError:
            permission_error()

        tkMessageBox.showinfo("Complete","Wavs Write Complete")
        
    return
        
