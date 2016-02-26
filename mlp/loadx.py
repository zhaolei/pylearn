import cPickle

fp = open('stock.pkl', 'rb')

w = cPickle.load(fp)
print len(w)    
