import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



iris = pd.read_csv("iris.csv")
print(iris)
w=iris.values[:,0:1]
s=iris.values[:,2:3]

w=np.array(w)
s=np.array(s)
x = w + s
print(x)

x=[]

# z = x[]
# plt.figure(figsize=(16,9))
# plt.scatter(x[], x[])
# plt.show()
#
# for i in range(len(x)):
#
# print(x)
