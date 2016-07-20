"""
createEXE.py

Created by Bill X Zhang
Email: xiaoyan.zhang@nyu.edu
All rights not reserved. (LOL Jk) All rights reserved!

Edit with: Python 3.4.4

Purpose: Converting .py to .exe w/ cx_Freeze

"""

"""
from distutils.core import setup
import py2exe


setup(console=["PC_Sign_Off.py"])
"""

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = 'Console'

setup(  name = "PC_Sign_Off",
        version = "0.1",
        description = "Sign off check tool.",
        #options = {"build_exe": build_exe_options},
        executables = [Executable("PC_Sign_Off.py", base=base)])
