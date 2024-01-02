import numpy as np
from lightfm.datasets import fetch_movilens
from lightfm import LightFM

# Fetch and format the data
data = fetch_movilens(min_rating=4.0)
loader = LightFM.DataLoader(data)

# Create training and testing datasets
train_data = loader.create_ratings_dataset()
test_data = loader.create_testing_split(train_data)

# Print training and testing data
print(train_data)
print(test_data)
