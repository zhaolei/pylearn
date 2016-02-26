# -*- coding: utf-8 -*-  
import os
import sys
#import MySQLdb as  DB
import numpy as np
import random
import cPickle

#my = DB.connect("127.0.0.1","root","root","data" ,charset="utf8")
#db = my.cursor()

xfile = sys.argv[1]

fp = open(xfile, 'r')

line = fp.readline()
arMax = {}
arMaxNum = {}

'''id      stock   datetime        open    high    low     close   num     closex'''
def getOr(ar):
    ops = float(ar[3])
    hgs = float(ar[4])
    lws = float(ar[5])
    cls = float(ar[6])
    num = int(ar[7])
    clxs = float(ar[8])
    stk = ar[1]
    return {'stk':stk, 'ops':ops, 'hgs':hgs, 'lws':lws, 'cls':cls,'clxs':clxs,'num':num}


def getLab(ar):
    ax = arStok[ar['stk']][9]

    kp = float(ax['ops'])
    z = kp - float(ar['ops'])
    if z > 0:
        pz = z/float(ar['ops'])
        if pz > 0.08: 
            return 1
        else:
            return 0 
    
    else:
       return 0 
def printData(dm, xxdd):
    npd = np.array(xxdd)
    nps = npd.shape
    npi = nps[0] 
    dda = tuple(npd.reshape(npi))

    fstr = '%f,'*len(dda)
    fstr = fstr[:-1]
    fstr = fstr%dda

    dstr = '%d'
    dstr = dstr%dm

    lstr = '%s,%s'%(dstr, fstr)
    print lstr
    
            

period = 12 
arStok = {} 

for i in range(period):
    line = fp.readline()
    ar = line.split('\t')
    org = getOr(ar)
    if arStok.has_key(org['stk']):
        arStok[org['stk']].append(org)
    else:
        arStok[org['stk']] = []

    #arStok.append(fp.readline())

arList = {}

aa1 = []
aa2 = []

dnumx = 0
dddx = 0
train_set_x = []
train_set_y = []
valid_set_x = []
valid_set_y = []
test_set_x = []
test_set_y = []
while line:
    line = fp.readline()
    line = line.strip()

    ar = line.split('\t')
    if len(ar) < 6 :
        break;
    org = getOr(ar)
    if arStok.has_key(org['stk']):
        arStok[org['stk']].append(org)
    else:
        arStok[org['stk']] = []

    
    if len(arStok[org['stk']]) < 11:
        continue    

    #get first one
    org = arStok[org['stk']][0]    
    arStok[org['stk']] = arStok[org['stk']][1:]    

    #mo = getMo(org, mi, mu)

    dm = getLab(org)
    if arList.has_key(org['stk']):
        arList[org['stk']]['ops'].append(org['ops'])
        arList[org['stk']]['lws'].append(org['lws'])
        arList[org['stk']]['hgs'].append(org['hgs'])
        arList[org['stk']]['cls'].append(org['cls'])
        arList[org['stk']]['num'].append(org['num'])
    else:
        arList[org['stk']] = {'ops':[], 'lws':[], 'hgs':[], 'cls':[], 'num':[]} 

    '''预测依赖周期30day'''
    daylen = 30
    if len(arList[org['stk']]['ops']) >= 30:
        
        rr = int(random.random() * 1000)%10        
        if rr == 1:
            valid_set_y.append(arList[org['stk']]['ops']) 
            valid_set_y.append(arList[org['stk']]['lws']) 
            valid_set_y.append(arList[org['stk']]['hgs']) 
            valid_set_y.append(arList[org['stk']]['cls']) 
            valid_set_x.append(dm) 
        elif rr == 2:
            test_set_y.append(arList[org['stk']]['ops']) 
            test_set_y.append(arList[org['stk']]['lws']) 
            test_set_y.append(arList[org['stk']]['hgs']) 
            test_set_y.append(arList[org['stk']]['cls']) 
            test_set_x.append(dm)
        else:
            train_set_y.append(arList[org['stk']]['ops']) 
            train_set_y.append(arList[org['stk']]['lws']) 
            train_set_y.append(arList[org['stk']]['hgs']) 
            train_set_y.append(arList[org['stk']]['cls']) 
            train_set_x.append(dm)
            

        arList[org['stk']]['ops'] = arList[org['stk']]['ops'][1:]
        arList[org['stk']]['lws'] = arList[org['stk']]['lws'][1:]
        arList[org['stk']]['hgs'] = arList[org['stk']]['hgs'][1:]
        arList[org['stk']]['cls'] = arList[org['stk']]['cls'][1:]
        arList[org['stk']]['num'] = arList[org['stk']]['num'][1:]

        

    #print "%d %f "%mo 

rval = [(train_set_x, train_set_y), (valid_set_x, valid_set_y), (test_set_x, test_set_y)]        

fp = open('stock.pkl','wb')
cPickle.dump(rval, fp)
fp.close()    
#print alllist            
