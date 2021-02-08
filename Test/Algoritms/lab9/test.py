
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn.cluster import KMeans


iris = datasets.load_iris()
X = iris.data
y = iris.target

print(X)
print(y)

plt.scatter(tsne_representation[:, 0], tsne_representation[:, 1])
plt.figure(figsize=(12, 12))