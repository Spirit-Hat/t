import numpy as np
import matplotlib.pyplot as plt


distance = np.array([497,3454.6,540.9,497,410,442,1184,541,448,442,497,2534,630,410,497,442,541,387])
Time = np.array([1.10,4,1.35,1.20,1.15,1.15,1.25,1.35,1.35,1.20,1.20,4,1.20,1,1.10,1.15,2,1.10])


numerate = np.sum((distance-np.mean(distance)) * (Time - np.mean(Time)))
denominator = np.sum((distance - np.mean(distance)) ** 2)
b1 = numerate / denominator
b0 = np.mean(Time) - b1 * np.mean(distance)

def calcPredictions(x):
    return b0 + b1*x
print(calcPredictions(600))

TimePreds=calcPredictions(distance)
#plt.+(b0, b1)

plt.figure(figsize=(16,9))
plt.scatter(distance, Time)
plt.plot(distance , TimePreds, c='r')




plt.show()
# print(x)