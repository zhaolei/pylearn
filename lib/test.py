import numpy as np
import matplotlib.pyplot as pyplot

def rand_data(size=100, smax=1000):
	da = np.random.randint(1,smax,(2,size))
	lx = np.arange(200)

	xa = da[:1]
	ya = da[1:2]

	ly = (80-lx)**2 + 10
	yx = (80-xa)**2 + 10
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
	pyplot.show()


rand_data()
		
