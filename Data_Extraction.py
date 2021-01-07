import xlwt
import xlrd
import numpy as np
import os

file=xlrd.open_workbook('data_cleaned.xlsx')
data_table=file.sheets()[0]

class Database():

    def __init__(self):
        self.sun_radiation=[]
        self.ext_temperature=[]
        self.int_temperature=[]
        self.ext_humidity=[]
        self.supply_water_temperature=[] #main pipe's
        self.back_water_temperature=[]
        self.pump_cooling_total_power=[]
        self.pump_grd_total_power=[]
        self.system_total_cosumption=[]

    def extraction_one(self):
        for x in range(2,data_table.nrows):
            column=data_table.row_values(x)
            self.sun_radiation.append(column[1])
            self.system_total_cosumption.append(column[8])

