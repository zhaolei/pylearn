In [82]: from sklearn import cluster, datasets

In [83]: iris = datasets.load_iris()

In [84]: k_means = cluster.KMeans(k=3)

In [85]: k_means.fit(iris.data) 
Out[85]: 
KMeans(copy_x=True, init='k-means++', k=3, max_iter=300, n_init=10, n_jobs=1,
    precompute_distances=True,
    random_state=<mtrand.RandomState object at 0x7f4d860642d0>, tol=0.0001,
    verbose=0)

In [86]: print k_means.labels_[::10]
[1 1 1 1 1 2 2 2 2 2 0 0 0 0 0]

In [87]: print iris.target[::10]
