import numpy as np
from LightFM.datasets import fetch_movilens
from LightFM import LightFM

# Fetch and format the data
data = fetch_movilens(min_rating=4.0)
loader = LightFM.DataLoader(data)

# Create training and testing datasets
train_data = loader.create_ratings_dataset()
test_data = loader.create_testing_split(train_data)

# Print training and testing data
print(train_data)
print(test_data)


#create model
model = LightFM(loss = 'wrap')
#train model
model.fit(data['train'],epochs = 30, num_threads=2)

def sample_recommendation(model,data,user_ids):
    
    #number of users and movies in training data
    n_users, n_items = data['train'].shape
    
    #generate recommendations for each user we input
    for user_id in user_ids:
        #movies they alreqdy like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
        
        #movies our model predicts they will like
        scores = model.predict(user_id,np.arange(n_items))
        top_items = data['item_labels'][np.argsort(-scores)]
        
        #print out the resuts
        print("User %s" % user_id)
        
        for x in known_positives [:3]:
            print(" %s" % x)
        print ("Recommended:")
        
        for x in top_items[:3]:
            print(" %s" % x)
            
sample_recommendation(model,date, [3,25,450])
            
        
        



