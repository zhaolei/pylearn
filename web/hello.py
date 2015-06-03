import web
from sklearn.externals import joblib
from sklearn.naive_bayes import GaussianNB 
import numpy as np

urls = (
    '/', 'index'
)

class index:
	def GET(self):
		param = web.input()
		name = param.get('name', '')
		mrow = self.spname(name)
		maxl = 10
		lenx = len(mrow)
		zll = range(maxl - lenx)
		mrow.extend(zll)
		#mdata = np.matrix(mrow)
		#mstr = ' '.join(mrow)
		nbx = self.loadm()
		pr = nbx.predict(mrow)
		return "[%f]"%pr[0]

	def spname(self, name):
		lenx = len(name)
		mrow = []
		for i in range(lenx):
			ik = ord(name[i])
			mrow.append(ik)
		return mrow

	def loadm(self):
		nameb = joblib.load('/home/stone/data/model/nbn.lr')
		return nameb
		 

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
