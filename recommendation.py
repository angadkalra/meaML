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

	if X[i,2] == 1:
		movieRating = (X[i,1],X[i,2])
	else:
		continue

	if userID in R.keys():
		R[userID].append(movieRating)
	else:
		R[userID] = [movieRating]

# Given random user, find KNN (k = 5 for now)

# Output user IDs
