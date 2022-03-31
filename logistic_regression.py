# -*- coding: utf-8 -*- 
"""
Created on Thu Mar 10 09:50:17 2022

@author: arjun
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import igor.binarywave as ibw           # https://pypi.org/project/igor/
import glob 



#%%


filelist_onsurface = glob.glob('Data\On_Surface\*.ibw')  
filelist_offsurface = glob.glob('Data\Off_Surface\*.ibw')  

filelist = [filelist_onsurface, filelist_offsurface]

#filelist = glob.glob('Data\*.ibw')  



data = {}

for filetype in filelist:         
    for file in filetype: 
        indata = ibw.load(file)
        
        
        key1 = file.split('\\')[1]
        key2 = file.split('\\')[2][0:-4]
        
        try: 
            data[key1] 
        except: 
            data[key1] = {}            
        
        try: 
            data[key1][key2] 
        except: 
            data[key1][key2] = {}
            
                            
        
        for key in enumerate(indata['wave']['labels'][1][1:]):     
            data[key1][key2][str(key[1])[2:-1]] = indata['wave']['wData'][:,key[0]]
            
        notedic = {}
        for item in str(indata['wave']['note']).split('\\r'):
            try: 
                notedic[item.split(':')[0]] = item.split(':')[1]
            except: 
                print("Warrning cannot parse note entry: " + item)
        
        data[key1][key2]['note'] = notedic


#%%
   
plt.figure()
plt.plot(data['Off_Surface']['AZ_0101']['ZSnsr'],data['Off_Surface']['AZ_0101']['Amp'])    

count = 1 
plt.figure()
for key1 in data.keys(): 
    plt.subplot(2,1,count) 
    plt.title(key1)
    for key2 in data[key1].keys():
        plt.plot(data[key1][key2]['ZSnsr'],data[key1][key2]['Amp']) 
    count = count + 1

plt.tight_layout()
    

#%%

model = LogisticRegression(solver='liblinear', random_state=0)

count = 1 
plt.figure()
for key1 in data.keys(): 
    plt.subplot(2,1,count) 
    plt.title(key1)
    for key2 in data[key1].keys():
        
        
        x_train = [data[key1][key2]['ZSnsr'],data[key1][key2]['Amp']]
        y_train = [1]
        
        
        output = model.fit(x_train, y_train)
    
    
    count = count + 1

plt.tight_layout()

# x_train = data['Off_Surface']['AZ_0101']['ZSnsr']
# y_train = data['Off_Surface']['AZ_0101']['Amp']

# for 

# y= np.arrange

# model = LogisticRegression(solver='liblinear', random_state=0)

# model.fit(x_train, y_train)

# model.classes_

# pred_data = model.predict(x_test)



# model.score(x_test, y_test)

# cnf_m = confusion_matrix(y, pred_data)
# report = classification_report(y, pred_data)

#print(classification_report(y, model.predict_proba(x_train)))

# plt.tight_layout()
# plt.title('AFM')
# plt.xlabel('Material used')
# plt.ylabel('Contact made or not')
# plt.legend()
# plt.show()
