import numpy as np
import os
import re
import matplotlib
import pylab as plt

import pdb
import SBCcode as sbc
from SBCcode.DataHandling.ReadBinary import ReadBlock as rb

def loaddata(runid='20170619_3', ev=0):
	datadir = '/Users/reustudent/SBCdata'
	loadlist = ['fastDAQ']
	thisevent = sbc.get_event(os.path.join(datadir, runid), ev, *loadlist)
	return thisevent

def plottrace(thisevent, channel=0, ni=1, ne=10):
	plt.figure()
	for i in range(ni, ne+1):
		plt.clf()
		plt.plot(thisevent['PMTtraces']['traces'][i,channel,:])
		plt.draw()
		plt.waitforbuttonpress()

def loadrecon(runid, ev):
    recondir='/Users/reustudent/SBCcode/UserCode/jjimenez/output'
    return rb(os.path.join(recondir,'AcousticAnalysis_all.bin'))

def loadrecon1(runid, ev):
    recondir='/Users/reustudent/SBCcode/UserCode/jjimenez/output'
    return rb(os.path.join(recondir,'DytranAnalysis_all.bin'))

def loadrecon2(runid, ev):
    recondir='/Users/reustudent/SBCcode/UserCode/jjimenez/output'
    return rb(os.path.join(recondir,'EventAnalysis_all.bin'))

def loadrecon3(runid, ev):
    recondir='/Users/reustudent/SBCcode/UserCode/jjimenez/output'
    return rb(os.path.join(recondir,'HistoryAnalysis_all.bin'))

def loadrecon4(runid, ev):
    recondir='/Users/reustudent/SBCcode/UserCode/jjimenez/output'
    return rb(os.path.join(recondir,'HumanGetBub_all.bin'))

def loadrecon5(runid, ev):
    recondir='/Users/reustudent/SBCcode/UserCode/jjimenez/output'
    return rb(os.path.join(recondir,'PMTfastDAQalignment_all.bin'))

def loadrecon6(runid, ev):
    recondir='/Users/reustudent/SBCcode/UserCode/jjimenez/output'
    return rb(os.path.join(recondir,'PMTpheAnalysis_all.bin'))

def loadrecon7(runid, ev):
    recondir='/Users/reustudent/SBCcode/UserCode/jjimenez/output'
    return rb(os.path.join(recondir,'PMTpulseAnalysis_all.bin'))

def loadrecon8(runid, ev):
    recondir='/Users/reustudent/SBCcode/UserCode/jjimenez/output'
    return rb(os.path.join(recondir,'TimingAnalysis_all.bin'))