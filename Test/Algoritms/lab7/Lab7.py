import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pylab import *


distance = np.array([497,3454.6,540.9,497,410,442,1184,541,448,442,497,2534,630,410,497,442,541,387])
price = np.array([1.10,4,1.35,1.20,1.15,1.15,1.25,1.35,1.35,1.20,1.20,4,1.20,1,1.10,1.15,2,1.10])
print(distance)
#price = 25 + (distance + np.random.normal(3.0, 1.0, 18)) * 3
scatter(distance, price)
plt.show()

print(np.corrcoef(distance, price))
slope, intercept, _, _, _ = stats.linregress(distance, price)


def predict(x):
    return slope * x + intercept


fitLine = predict(distance)

plt.scatter(distance, price)
plt.plot(distance, fitLine, c='r')
plt.show()


distance_ = 600
print("Дальність і час перельоту ", distance_, ":", predict(distance_))