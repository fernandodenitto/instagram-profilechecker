import math
import pandas as pd
from random import sample
import numpy as np
import os


datafake = pd.read_csv("data_fake.csv")
datareal = pd.read_csv("data_real.csv")

if datareal.index.size > datafake.index.size:
    indexes =  np.random.choice(datareal.index, datafake.index.size, replace=False)
    datareal = datareal.loc[indexes].reset_index(drop=True)
else:
    indexes =  np.random.choice(datafake.index, datareal.index.size, replace=False)
    datafake = datafake.loc[indexes].reset_index(drop=True)

data = []
data = pd.concat([datareal, datafake])
datareal.to_csv("balanced_data_real.csv",index=False) 
datafake.to_csv("balanced_data_fake.csv",index=False) 
data.to_csv("balanced_data.csv",index=False) 

