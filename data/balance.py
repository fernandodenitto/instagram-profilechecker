import math
import pandas as pd
from random import sample
import numpy as np
import os


datafake = pd.read_csv("data_fake.csv")

datareal = pd.read_csv("data_real.csv")


indexes =  np.random.choice(datareal.index, datafake.index.size, replace=False)
datareal = datareal.loc[indexes].reset_index(drop=True)
data = []
data = pd.concat([datareal, datafake])
data.to_csv("balanced_data.csv",index=False) 

