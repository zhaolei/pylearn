import numpy as np
import matplotlib.pyplot as pyplot

'''fun '''
def mathfun1(x):
	y = np.power((x), 2) + 10
	return y

def mathfun2(x):
	X = 500
	Y = 500
	R = 200
	sx = R**2 - (x-X)**2
	yy = np.sqrt(sx)
	return yy+Y,0-yy+Y

def circle_fun(x,y):
	X = 500
	Y = 500
	R = 200
	r1 = (x - X) ** 2 + (y-Y) ** 2
	return r1 > R**2


#pyplot.axis([0,100,0,1000])
#pyplot.show()

def rand_data(size=1000, smax=1000):
	da = np.random.randint(1,smax,(2,size))
	lx = np.arange(300,700, .5)

	xa = da[:1]
	ya = da[1:2]

	ly0,ly1 = mathfun2(lx)
	yyt = circle_fun(xa, ya)

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

	pyplot.plot(x1, y1, 'ro', x2, y2, 'bo', lx, ly0, lx, ly1)
	pyplot.scatter([500], [500], c='red', s=26000, label='red',
                alpha=0.1, edgecolors='none')
	#pyplot.plot(x1, y1, 'ro', x2, y2, 'b^')
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
