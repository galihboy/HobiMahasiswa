# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:17:37 2021

@author: galih-hermawan
"""

from objManajemenBerkas import ManajemenBerkas

nmFile = "dataMahasiswa.txt"

mb = ManajemenBerkas(nmFile) 
data = mb.BacaBerkas() # baca isi file

print(data)