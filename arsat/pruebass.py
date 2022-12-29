# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 16:22:27 2022

@author: crist
"""

import pandas as pd

from openpyxl import load_workbook

wb = load_workbook(filename = r"C:\Users\crist\Desktop\satelite\scrips\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\0841-3900-6PCOP-021-J_Battery_cell_package_bypassing.xlsm")
sheet_names = wb.get_sheet_names()
name = sheet_names[5]
sheet_ranges = wb[name]
df = pd.DataFrame(sheet_ranges.values)