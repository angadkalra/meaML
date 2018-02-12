import numpy as np
import sklearn as skl
import scipy as scp 

# Load dataset: User ID, Movie ID, Rating (1 or 0)
X = np.loadtxt('ratings_small.csv', delimiter=',', skiprows=1, usecols=(0,1,2))
n,d = X.shape

# Modify dataset to binary ratings
for i in range(n):
	if X[i,2] >= 3.0:
		X[i,2] = 1
	else:
		X[i,2] = 0

# Create dictionary with user as key and array of tuples as value where each tuple 
# is (movie_id, 1)
R = {}

for i in range(n):
    userID = X[i,0]
    
    if X[i,2] == 0:
        continue
    
    if userID in R.keys():
        R[userID].append(X[i,1])
    else:
        R[userID] = [X[i,1]]

users = R.keys()

# Given user id, find KNN (k = 6 for now)
def knn(uid):
# Go through every user, compute euclid. distance & store (dist, id) in ndarray. 
# Sort array based on closest dist. Return 6 closest users. 
    
    distances = np.ndarray((n,2), dtype=(np.int_,np.int_))
    
    uid_movies = np.asarray(R[uid])
    
    for u in users:
        u_movies = np.asarray(R[u])
        
        intersection = np.intersect1d(uid_movies, u_movies, assume_unique=True)
        union = np.union1d(u_movies, uid_movies)
        differences = np.setdiff1d(union, intersection)
        
        dist = differences.size
        distances[u,0] = dist
        distances[u,1] = u
        
    
    return 0
    