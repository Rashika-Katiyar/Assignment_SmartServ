# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 01:24:17 2019

@author: Rashika
"""

import urllib.request, json 
import pandas as pd

def data():
    url= urllib.request.urlopen("https://s3.amazonaws.com/open-to-cors/assignment.json")
    data = json.loads(url.read().decode())
    #print(data)
    
    products= data['products']
    
    result= []
    
    
    for i in products:
        
        result.append([products[i]['title'],int(products[i]['popularity']), products[i]['price'], products[i]['subcategory']])
        
    
       
    return df    
