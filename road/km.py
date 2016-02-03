# Author : Vincent Michel, 2010
#          Alexandre Gramfort, 2011
# License: BSD 3 clause
#print(__doc__)

import time as time
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from sklearn.feature_extraction.image import grid_to_graph
from sklearn.cluster import AgglomerativeClustering
import sys

###############################################################################
# Generate data
#lena = sp.misc.lena()

print sys.argv
if len(sys.argv) < 2:
	print 'km.py file.jpg'
	exit(0)


imfile = sys.argv[1]
cl = 15
if len(sys.argv) > 2:
	cl = int(sys.argv[2])

lena = sp.misc.imread(imfile, True)
# Downsample the image by a factor of 4
'''
print lena.shape 
lena = lena[::2, ::2] + lena[1::2, ::2] + lena[::2, 1::2] + lena[1::2, 1::2]
print lena.shape 
lena = lena[::2, ::2] + lena[1::2, ::2] + lena[::2, 1::2] + lena[1::2, 1::2]
print lena.shape 
lena = lena[::2, ::2] + lena[1::2, ::2] + lena[::2, 1::2] + lena[1::2, 1::2]
print lena.shape 
lena = lena[::2, ::2] + lena[1::2, ::2] + lena[::2, 1::2] + lena[1::2, 1::2]
print lena.shape 
'''

print lena.shape 
while lena.shape[0] * lena.shape[1] > 10000:
	if lena.shape[0]%2 != 0:
		lena = lena[1::]

	if lena.shape[1]%2 != 0:
		lr = range(lena.shape[1])
		lena = lena[:,lr[1::]]
		
	lena = lena[::2, ::2] + lena[1::2, ::2] + lena[::2, 1::2] + lena[1::2, 1::2]
	print lena.shape 
	
print lena.shape 
#lena = lena[::2, ::2] + lena[1::2, ::2] + lena[::2, 1::2] + lena[1::2, 1::2]
X = np.reshape(lena, (-1, 1))
#y = np.matrix(lena)
#print y.shape 
#print X.shape 

###############################################################################
# Define the structure A of the data. Pixels connected to their neighbors.
connectivity = grid_to_graph(*lena.shape)

###############################################################################
# Compute clustering
print("Compute structured hierarchical clustering...")
st = time.time()
n_clusters = cl  # number of regions
ward = AgglomerativeClustering(n_clusters=n_clusters,
        linkage='ward', connectivity=connectivity).fit(X)

'''label is output'''
label = np.reshape(ward.labels_, lena.shape)
print("Elapsed time: ", time.time() - st)
print("Number of pixels: ", label.size)
print("Number of clusters: ", np.unique(label).size)

print label.shape
#print label[0] 
print label 

###############################################################################
# Plot the results on an image

plt.imshow(lena, cmap=plt.cm.gray)
for l in range(n_clusters):
    plt.contour(label == l, contours=1,
                colors=[plt.cm.spectral(l / float(n_clusters)), ])
plt.xticks(())
plt.yticks(())
plt.show()

'''
plt.figure(figsize=(5, 5))
plt.imshow(lena, cmap=plt.cm.gray)
for l in range(n_clusters):
    plt.contour(label == l, contours=1,
                colors=[plt.cm.spectral(l / float(n_clusters)), ])
plt.xticks(())
plt.yticks(())
plt.show()
'''
