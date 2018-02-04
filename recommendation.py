import numpy as np
import sklearn as skl

# Load dataset: User ID, Movie ID, Rating (1/0)
X = np.loadtxt('ratings_small.csv', delimiter=',', skiprows=1, usecols=(0,1,2))
n,d = X.shape

# Modify dataset to binary ratings
for i in range(n):
	if X[i,2] >= 3.0:
		X[i,2] = 1
	else:
		X[i,2] = 0

# Create sparse user vectors

# Given random binary vector, find KNN

# Output user ID's
