# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:38:04 2022

@author: rbwagner
"""


import glob 
import import_data
import plot_data


filelist = glob.glob('Data\*.ibw')  
data = import_data.gen_data(filelist)
plot_data.makeplot(data)