import numpy as np
import sklearn as skl
import scipy as scp 
import sys

# Load dataset: User ID, Movie ID, Rating
X = np.loadtxt('ratings_small.csv', dtype=[('userID',np.int_),('movieID',np.int_),('rating',np.float_)], 
               delimiter=',', skiprows=1, usecols=(0,1,2))

n = X.shape[0] # number of ratings
uIDs = 672 # number of user IDs + 1

# Modify dataset to binary ratings
for i in range(n):
	if X[i][2] >= 3.0:
		X[i][2] = 1
	else:
		X[i][2] = 0

# Create dictionary with user as key and array of movieIDs that were selected (value = 1)
R = {}

for i in range(n):
    userID = X[i][0]
    
    if X[i][2] == 0:
        continue
    
    if userID in R.keys():
        R[userID].append(X[i][1])
    else:
        R[userID] = [X[i][1]]

users = R.keys()

# Given user id, find KNN (k = 6 for now)
def knn(uid):
    distances = np.zeros((uIDs,2), dtype=(np.int_,np.int_)) # Each row is (distance, userID)
    
    uid_movies = np.asarray(R[uid])
    
    # Go through every user, compute euclid. distance to uid & store (dist, id) in ndarray.
    for u in users:
        u_movies = np.asarray(R[u])
        
        intersection = np.intersect1d(uid_movies, u_movies, assume_unique=True)
        union = np.union1d(u_movies, uid_movies)
        differences = np.setdiff1d(union, intersection)
        
        dist = differences.size
        distances[u,0] = dist
        distances[u,1] = u
    
    # Sort array based on closest dist.
    distances = distances[ distances[:,0].argsort() ]
    
    # return 5 closest users, excluding yourself
    nn = distances[2:7]
    
    return nn