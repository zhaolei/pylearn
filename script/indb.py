
import MySQLdb as  DB
import time

#my = DB.connect("127.0.0.1","root","111111","data" )
#db = my.cursor()

#db.execute('select * from ids')

fp = open('/home/stone/data/name.csv', 'r')
#fp.readline()
da=fp.readline()
while da:
	da=fp.readline()
	ar=da.split(' ')

	if(len(ar)<3) :
		continue
	
	gender = ar[2].strip()
	if(len(gender)==0):
		#print 'error 1:', da
		continue
	bid = ar[0].strip()
	name = ar[1].strip()
	if(len(name) < 2 and len(name) > 15):
		#print 'error a:', da
		continue
		 
	ft = time.time()
	ft = int(ft)
	#if(len(ar) > 6): 
	name = DB.escape_string(name)
	gender = DB.escape_string(gender)
	sql = "insert into ids(bid, name, gender, datetime) values('%s','%s','%s','%d');"%(bid, name, gender, ft)
	print sql
	#db.execute(sql)
	#my.commit()







