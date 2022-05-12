# Thompson Sampling for Slot Machines

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Setting conversion rates and the number of samples
conversionRates = [0.15, 0.04, 0.13, 0.11, 0.05]
N = 10000
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
        randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1)
        if randomBeta > maxRandom:
            betaDist[str(j+1)].append(randomBeta)
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

for i in range(d):
    a, b, loc, scale = beta.fit(betaDist[str(i+1)])
    plt.figure()
    distro = beta.pdf(np.linspace(0.001,0.999,N),a=a,b=b)
    plt.hist(distro, bins = 300)
plt.show()