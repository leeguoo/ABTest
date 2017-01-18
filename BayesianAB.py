#!/usr/bin/python

__author__ = "Guo Li"
__email__ = "leeguoo@hotmail.com"
__date__ = "Jan. 17, 2017"

from scipy.stats import beta
import numpy as np

def ABStop(dataA,dataB,threshold=0.001,APr=[1,1],BPr=[1,1],ngrid=1024):
    x = np.linspace(0,1,ngrid)
    PA = beta(APr[0]+dataA[0],APr[1]+dataA[1]-dataA[0]).pdf(x)
    PB = beta(BPr[0]+dataB[0],BPr[1]+dataB[1]-dataB[0]).pdf(x)

    PAB = np.multiply.outer(PA,PB)
    PAB /= PAB.sum()

    loss = np.subtract.outer(x,x)
   
    if dataB[0]/float(dataB[1])>dataA[0]/float(dataA[1]):
        sel = "B"
        EL = (np.maximum(loss,0)*PAB).sum()
        P = ((loss>0)*PAB).sum()
    else:
        sel = "A"
        EL = (abs(np.minimum(loss,0))*PAB).sum()
        P = ((loss<0)*PAB).sum()

    if EL<threshold:
        print "Terminate the test!"
        print "Expected loss ({0:3.2f}%) is less than Threshold of caring ({1:3.2f}%).".format(EL*100,threshold*100)
        print "Probability that {0} is greater is {1:3.2f}%.".format(sel,P*100)
    else:
        print "Continue the test!"
        print "Expected loss ({0:3.2f}%) is NOT less than Threshold of caring ({1:3.2f}%).".format(EL*100,threshold*100)

############
#Input your data here
############
kA = 21 #number of positive samples in A
nA = 500 #number of smaples in A
kB = 35 #number of positive samples in B
nB = 600 #number of smaples in B

ABStop([kA,nA],[kB,nB])

