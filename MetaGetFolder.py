import os
import sys

import tkinter as tk
from tkinter import filedialog
from tkinter import *

class open_folder(object):
    def __init__ (self):
        self.current = "Select folder"
    def getFolder(self):
        self.current= filedialog.askdirectory(initialdir="/",title='Please select a directory')
        
    def getCurrent(self):
        return self.current
