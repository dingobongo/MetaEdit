#metadatamain v2.0
import os
import sys
import time
import ConfigParser


import Tkinter as tk
from Tkinter import *

from MetaCsvWriter import *
from MetaGetFolder import *
from MetaWavsWriter import *
from MetaHelp import *

config = configparser.ConfigParser()

configpath = "MetaDefaults.ini"

def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

config.read(configpath)

folder = open_folder()
project = ""
session = ""
originator = ""
originatorreference = ""
originatordate = ""
timereference = ""
originationtime = ""
codinghistory = ""


pathdefault = "Select Folder"

header1 = "FileName"
header2 = "Description"
header3 = "Originator"
header4 = "OriginatorReference"
header5 = "OriginationDate"
header6 = "TimeReference"
header7 = "OriginationTime"
header8 = "CodingHistory"

class TestApp(App):
    def Build(self):
        return Button(text="Hello World")
    
TestApp().run()


#exit
def master_quit():
    master.destroy()
    sys.exit()

def get_folder():
    folder.getFolder()
    if folder.current == "":
        labelpath.set(pathdefault)
    else:
        labelpath.set(folder.current)
    return (labelpath,folder.current)

def get_help():
    meta_help()

#master ui
master = Tk()
master.wm_title("Metadata Generator")
master.resizable(width=FALSE, height=FALSE)
master.configure(background="SkyBlue1")

labelpath = StringVar()

if (ConfigSectionMap("Meta Defaults")['folder path']) != "":
    labelpath.set((ConfigSectionMap("Meta Defaults")['folder path']))
else:
    labelpath.set(pathdefault)

defvar = []
varlist = []

default_project = StringVar()
default_session = StringVar()
default_recordists = StringVar()
default_originator = StringVar()
default_originatorreference = StringVar()
default_originatordate = StringVar()
default_timereference = StringVar()
default_originationtime = StringVar()
default_codinghistory = StringVar()

default_project.set((ConfigSectionMap("Meta Defaults")['project']))
default_session.set((ConfigSectionMap("Meta Defaults")['session']))
default_recordists.set((ConfigSectionMap("Meta Defaults")['recordists']))
default_originator.set((ConfigSectionMap("Meta Defaults")['originator']))
default_originatorreference.set((ConfigSectionMap("Meta Defaults")['originator reference']))
default_codinghistory.set((ConfigSectionMap("Meta Defaults")['coding history']))

default_originatordate.set(time.strftime("%Y-%m-%d"))
default_originationtime.set(time.strftime("%H:%M:%S"))
default_timereference.set(time.strftime("%H%M%S00"))

Label(master, text="Metadata Generator", bg="SkyBlue1", font="Verdana 20 bold").grid(row=0, columnspan=5, padx=4, pady=4)
Label(master, textvariable = labelpath, bg="SkyBlue1").grid(row=1, columnspan=5, padx=4, pady=4)
Label(master, text="Descrition Fields", bg="SkyBlue1").grid(row=2, column=2, padx=4, pady=4)
Label(master, text="Project", bg="SkyBlue1").grid(row=3,column=1, padx=4, pady=4)
Label(master, text="Session", bg="SkyBlue1").grid(row=4,column=1, padx=4, pady=4)
Label(master, text="Recordists", bg="SkyBlue1").grid(row=5,column=1, padx=4, pady=4)
Label(master, text="Bext Info", bg="SkyBlue1").grid(row=6, column=2, padx=4, pady=4)
Label(master, text="Originator", bg="SkyBlue1").grid(row=7,column=1, padx=4, pady=4)
Label(master, text="Originator Reference", bg="SkyBlue1").grid(row=8,column=1, padx=4, pady=4)
Label(master, text="Originator Date", bg="SkyBlue1").grid(row=9,column=1, padx=4, pady=4)
Label(master, text="Time Reference", bg="SkyBlue1").grid(row=10,column=1, padx=4, pady=4)
Label(master, text="Origination Time", bg="SkyBlue1").grid(row=11,column=1, padx=4, pady=4)
Label(master, text="Coding History", bg="SkyBlue1").grid(row=12,column=1, padx=4, pady=4)

project = Entry(master, textvariable = default_project)
session = Entry(master, textvariable = default_session)
recordists = Entry(master, textvariable = default_recordists)
originator = Entry(master, textvariable = default_originator)
originatorreference = Entry(master, textvariable = default_originatorreference)
originatordate = Entry(master, textvariable = default_originatordate)
timereference = Entry(master, textvariable = default_timereference)
originationtime = Entry(master, textvariable = default_originationtime)
codinghistory = Entry(master, textvariable = default_codinghistory)

project.grid(row=3, column=2, padx=4, pady=4)
session.grid(row=4, column=2, padx=4, pady=4)
recordists.grid(row=5, column=2, padx=4, pady=4)
originator.grid(row=7, column=2, padx=4, pady=4)
originatorreference.grid(row=8, column=2, padx=4, pady=4)
originatordate.grid(row=9, column=2, padx=4, pady=4)
timereference.grid(row=10, column=2, padx=4, pady=4)
originationtime.grid(row=11, column=2, padx=4, pady=4)
codinghistory.grid(row=12, column=2, padx=4, pady=4)

Button(master, text="Open Folder",command=lambda: get_folder()).grid(row=13, column=0, padx=4, pady=8)
Button(master, text="Help",command=lambda: get_help()).grid(row=13, column=3, padx=4, pady=8)
Button(master, text="Quit",command=lambda: master_quit()).grid(row=13, column=4, padx=4, pady=8)
Button(master, text="Write CSV",command=lambda: write_csv(header1,header2,header3,header4,header5,header6,header7,header8,folder.current,session,project,recordists,originator,originatorreference,originatordate,timereference,originationtime,codinghistory)).grid(row=13, column=1, padx=4, pady=8)
Button(master, text="Write Wavs",command=lambda: write_wavs(folder.current)).grid(row=13, column=2, padx=4, pady=8)


master.mainloop()

