# Thompson Sampling for Slot Machines

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Setting conversion rates and the number of samples
conversionRates = [0.15, 0.04, 0.13, 0.11, 0.05] # different probabilities for each slot machine.
N = 10000 # Number of total trials (times the all of the slot machines were used)
d = len(conversionRates)

# Creating the dataset
X = np.zeros((N, d))
for i in range(N):
    for j in range(d):
        if np.random.rand() < conversionRates[j]:
            X[i][j] = 1

# Making arrays to count our losses and wins
nPosReward = np.zeros(d)
nNegReward = np.zeros(d)

# Taking our best slot machine through beta distibution and updating its losses and wins
betaDist = dict()
betaDist['1'] = []
betaDist['2'] = []
betaDist['3'] = []
betaDist['4'] = []
betaDist['5'] = []

for i in range(N):
    selected = 0
    maxRandom = 0
    for j in range(d):
        randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1) # Extracts the beta probability at each iteration for each slot
        if randomBeta > maxRandom:
            betaDist[str(j+1)].append(randomBeta) # This contains the beta distribution based on the slot machine used
            maxRandom = randomBeta
            selected = j
    if X[i][selected] == 1:
        nPosReward[selected] += 1
    else:
        nNegReward[selected] += 1

# Showing which slot machine is considered the best
nSelected = nPosReward + nNegReward 
for i in range(d):
    print('Machine number ' + str(i + 1) + ' was selected ' + str(nSelected[i]) + ' times')
print('Conclusion: Best machine is machine number ' + str(np.argmax(nSelected) + 1))

# Set to extract the number of wins and the number of times where the slot machines did not win
print(" ")
for i in range(d):
    print(f"Machine number {str(i+1)} won {str(nPosReward[i])} times.")
    print(f"Machine number {str(i+1)} lost {str(nNegReward[i])} times.")

# Set of plots that provide the figures required for the assignment

plt.figure(1)
plt.title("Beta Distribution of Slot Machine 1 (bin=3200)")
plt.xlabel("Probabilities")
plt.ylabel("Number of Selections")
plt.hist(betaDist['1'], bins=3200)


plt.figure(2)
plt.title("Beta Distribution of Slot Machine 2 (bin=50)")
plt.xlabel("Probabilities")
plt.ylabel("Number of Selections")
plt.hist(betaDist['2'], bins=50)


plt.figure(3)
plt.title("Beta Distribution of Slot Machine 3 (bin=200)")
plt.xlabel("Probabilities")
plt.ylabel("Number of Selections")
plt.hist(betaDist['3'], bins=200)


plt.figure(4)
plt.title("Beta Distribution of Slot Machine 4 (bin=200)")
plt.xlabel("Probabilities")
plt.ylabel("Number of Selections")
plt.hist(betaDist['4'], bins=200)


plt.figure(5)
plt.title("Beta Distribution of Slot Machine 5 (bin=50)")
plt.xlabel("Probabilities")
plt.ylabel("Number of Selections")
plt.hist(betaDist['5'], bins=50)

# NOTE: The number of bins is different for some cases due to the amount of times each machine was used. This was to better demonstrates the distribution.

plt.show()
