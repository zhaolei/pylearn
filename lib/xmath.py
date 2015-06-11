import math

''' y = (x-20)**2 + 30'''
def xfline(pos, fun):
	fy = math.pow((pos[0] - 20), 2) +  30
	
	if fy > pos[1]:
		return 1
	else:
		return 0 
	


class xfdata:
	data = []
	target = []
	
	def __init__(self, d, t):
		self.data = d
		self.target = t

	
	def save(self):
		num = 0	
		for xa in self.data:
			print "%d %d"%(self.target[num],xa)
	
