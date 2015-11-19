#metacsvwriter
import csv
import subprocess, os
import sys

from tkinter import *
import tkinter.messagebox

#user hasn't set the folder
def folder_error():
    tkinter.messagebox.showerror("Error", "Folder is not set.")
    
def permission_error():
    tkinter.messagebox.showerror("Error","You don't have permission to write to this file/folder. Metadata.csv could be running in another process")


#define csv writer
def write_csv(header1,header2,header3,header4,header5,header6,header7,header8,folder,session,project,recordists,originator,originatorreference,originatordate,timereference,originationtime,codinghistory):

    try:

        fullpath = []
        description = []
        originatordata = []
        originatorreferencedata = []
        originatordatedata = []
        timereferencedata = []
        originationtimedata = []
        codinghistorydata = []

        #getlist of files and for each add the path
        for path, subdirs, files in os.walk(os.path.abspath(folder)):
            for name in files:
                if name.endswith(".wav"):
                    fullpath.append(os.path.join(path,name)) #adds path to filename and appends to fulpath list
                    name = os.path.splitext(name)[0] #splits extension and filename, returns only filename
                    if session.get() != "":
                        name = (session.get()+" "+name)
                    if project.get() != "":
                        name = (project.get()+" "+name)
                    if recordists.get() != "":
                        name = (name+" "+recordists.get())
                        
                    description.append(name)

                    description = [n.replace("_"," ") for n in description]

                    originatordata.append(originator.get())
                    originatorreferencedata.append(originatorreference.get())
                    originatordatedata.append(originatordate.get())
                    timereferencedata.append(timereference.get())
                    originationtimedata.append(originationtime.get())
                    codinghistorydata.append(codinghistory.get())
                    

        #sort out data for write
        headerdata = (header1,header2,header3,header4,header5,header6,header7,header8)
        rowdata = zip(fullpath,description,originatordata,originatorreferencedata,originatordatedata,timereferencedata,originationtimedata,codinghistorydata)

        #open metadata file for write
        with open((folder+"/"+'metadata.csv'), 'w', newline='') as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(headerdata) #write header

            for item in rowdata: #write fullpath into csv
                print (item)
                writer.writerow(item)

        csvpath = ((folder+"/"+"metadata.csv"))

        if sys.platform.startswith(('darwin')):
            subprocess.call(('open', csvpath))
        elif os.name == 'nt':
            os.startfile(csvpath)
        #elif os.name == 'posix':
        #    subprocess.call(('xdg-open', csvpath))



    except FileNotFoundError:
        folder_error()
    except PermissionError:
        permission_error()

    return

        
    
