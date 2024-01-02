import numpy as np
from lightfm.datasets import fetch_movilens
from lightfm import LightFM

#fetch date and format it
data = fetch_movilens(min_rating = 4.0)

#printtraining and testing data
print(repr(data['train']))
print(repr(data['test']))