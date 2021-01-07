import numpy as np
from PyEMD import EMD,EEMD,Visualisation

class EMD_model():

    def __init__(self):
        self.x=np.zeros(1024,)
        self.signal=np.zeros(1024,)
        self.emd_out_signal=np.zeros(1024,)
        self.eemd_out_signal=np.zeros(1024,)
    def registration(self,datalist):
        self.x=datalist
    def decomposition(self):
        self.IMFs_emd=EMD(self.x)
        self.IMFs_eemd=EEMD(self.x)
        


    

    