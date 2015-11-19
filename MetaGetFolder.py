import os
import sys

import Tkinter as tk
from Tkinter import *
import tkFileDialog


class open_folder(object):
    def __init__ (self):
        self.current = "Select folder"
    def getFolder(self):
        self.current= tkFileDialog.askdirectory(initialdir="/",title='Please select a directory')
        
    def getCurrent(self):
        return self.current
