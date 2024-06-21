#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:43:12 2024

@author: shrutika
"""

import pandas as pd

data=pd.read_excel("/Users/SHRITHIKA/Downloads/Online Retail.xlsx")
print(data)


filter=data[(data['Quantity'] <0 ) | (data['UnitPrice'])]
filter["Revenue"]=filter['Quantity']*filter['UnitPrice']
print(filter)

filter.to_excel("/Users/SHRITHIKA/Downloads/Filter_Retail.xlsx")

