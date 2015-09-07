from sklearn import datasets
from sklearn import metrics
from sklearn import svm

iris = datasets.load_iris()
digits = datasets.load_digits()    
clf = svm.SVC(gamma=0.001, C=100.)    
clf.fit(digits.data[:-1], digits.target[:-1])      
pred = clf.predict(digits.data[:20])    
print pred 
print digits.target[:20]

m_precision = metrics.precision_score(digits.target[:20], pred)
m_recall = metrics.recall_score(digits.target[:20], pred)
print 'precision:{0:.3f}'.format(m_precision)
print 'recall:{0:0.3f}'.format(m_recall)
