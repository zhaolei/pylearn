import numpy as np
import matplotlib.pyplot as pyplot
from sklearn.datasets import load_svmlight_file 
from sklearn import svm
from sklearn import metrics 
import sys

xfile = 'fpw'
if len(sys.argv) > 1:
	xfile = sys.argv[1]

#tx, ty = load_svmlight_file('fpw')
tx, ty = load_svmlight_file(xfile)
tx = tx.todense()
#print tx,ty

clf = svm.SVC()

clf.fit(tx, ty)


stx = tx[:100]
sty = ty[:100]
stty = clf.predict(stx)
p1 = metrics.precision_score(sty, stty) 
print "precision_score:%f"%p1

s1 = metrics.recall_score(sty, stty) 
print "precision_recall:%f"%s1

f1 = metrics.f1_score(sty, stty) 
print "precision_f1:%f"%f1

