
import MySQLdb as  DB
import time

my = DB.connect("127.0.0.1","root","111111","data" ,charset="utf8")
db = my.cursor()

sql = "select * from ids  where id=2000"
db.execute(sql)
ax = db.fetchone()


def ntoiw(name):
	lenx = len(name)
	for i in range(lenx):
		print ord(name[i])
		print name[i]



def model_svm(ax):
	lenx = len(ax[2])
	g = 0
	if ax[3] == 'F':
		g = 1
		 
	mstr = ''
	mrow = []
	mrow.append('%d'%g)
	for i in range(lenx):
		ik = ord(ax[2][i])
		mrow.append("%d:%d"%(i,ik))
		
	
	mstr = ' '.join(mrow)
	print mstr
		

id = 1
while id<5488396:

	sql = "select * from ids  where id=%d"%id
	db.execute(sql)
	ax = db.fetchone()
	#print sql
	#print ax
	if ax:
		model_svm(ax)
	id += 1
#print  ax
#model_svm(ax)
