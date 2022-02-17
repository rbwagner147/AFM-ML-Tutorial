# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:08:27 2020

@author: rbwagner
"""


import igor.binarywave as ibw           # https://pypi.org/project/igor/
#import glob 


#filelist = glob.glob('*.ibw')  

def gen_data(filelist): 
    
    data = {}
    
    for file in filelist: 
        indata = ibw.load(file)
        file = file.split('\\')[1]

        
        try:  
            data[file[0:-4]] 
        except: 
            data[file[0:-4]] = {}
        
        for key in enumerate(indata['wave']['labels'][1][1:]):     
            data[file[0:-4]][str(key[1])[2:-1]] = indata['wave']['wData'][:,key[0]]
            
        notedic = {}
        for item in str(indata['wave']['note']).split('\\r'):
            try: 
                notedic[item.split(':')[0]] = item.split(':')[1]
            except: 
                print("Warrning cannot parse note entry: " + item)
        
        data[file[0:-4]]['note'] = notedic
        

    return(data)     
