# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:08:27 2020

@author: rbwagner
"""


import igor.binarywave as ibw           # https://pypi.org/project/igor/
import glob 

filelist = glob.glob('*.ibw')  


for file in filelist: 
    indata = ibw.load(file)
    data = {}
    
    
    for key in enumerate(indata['wave']['labels'][1][1:]):     
        data[str(key[1])[2:-1]] = indata['wave']['wData'][:,key[0]]
        
    notedic = {}
    for item in str(indata['wave']['note']).split('\\r'):
        try: 
            notedic[item.split(':')[0]] = item.split(':')[1]
        except: 
            print("Warrning cannot parse note entry: " + item)