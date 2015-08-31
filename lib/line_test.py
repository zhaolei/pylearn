import numpy as np
import matplotlib.pyplot as pyplot


'''fun '''
def mathfun1(x):
	#y = (10 +  x)**(2) + 10
	y = np.power((x), 2) + 10
	return y

def mathfun2(x):
	#y = (50 +  x)**(2) + 10
	y = np.power(abs(x-500), 1.2) + 350 
	return y

#pyplot.axis([0,100,0,1000])
#pyplot.show()

def rand_data(size=1000, smax=1000):
	da = np.random.randint(1,smax,(2,size))
	lx = np.arange(size)

	xa = da[:1]
	ya = da[1:2]

	#ly = (80-lx)**2 + 10
	#yx = (80-xa)**2 + 10
	yx = mathfun2(xa)
	ly = mathfun2(lx)
	yyt = yx > ya

	num = 0
	x1 = []
	y1 = []
	x2 = []
	y2 = []
	for ti in yyt[0]:
		if ti:
			x1.append(xa[0][num])
			y1.append(ya[0][num])
		else:
			x2.append(xa[0][num])
			y2.append(ya[0][num])
		num += 1

	pyplot.plot(x1, y1, 'ro', x2, y2, 'b^', lx, ly)
	pyplot.axis([0,1000,0,1000])
	pyplot.show()
	return x1,y1,x2,y2


def data2file(sfile, x1, y1, x2,y2):
	fp = open(sfile, "w")
	num = 0
	'''ok '''
	for k1, k2 in zip(x1, y1):
		stw = "1 0:%d 1:%d\n"%(k1, k2)
		fp.write(stw)

	'''false'''
	for k1, k2 in zip(x1, y1):
		stw = "0 0:%d 1:%d\n"%(k1, k2)
		fp.write(stw)

	fp.close()
	

x1, y1, x2, y2 = rand_data()

data2file('fpw', x1, y1, x2,y2)

