# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:25:16 2022

@author: rbwagner
"""


import matplotlib.pyplot as plt 


def makeplot(data): 
    plt.figure()
    for key in data.keys():
        plt.plot(data[key]['Amp'],data[key]['Phase'])         

    
