import os
import sys
import xlrd
reload(sys)
sys.setdefaultencoding("utf-8")
############################################################################
def writeXlsToBin(tableObj,xlsName,binDataName,titleMap):
	print('convert '+xlsName+' to '+binDataName+' ...')
	xlsData = xlrd.open_workbook(xlsName)
	for table in xlsData.sheets():
		for row in range(table.nrows):
			if row > 0:
				entry = tableObj.list.add()
			for col in range(table.ncols):
				if row == 0:
					continue
				else:
					attrName = titleMap[table.cell(0,col).value]
					attrType = type(getattr(entry,attrName))
					#print('convert row '+str(row)+' col '+str(col)+' type is '+str(attrType)+' ...')
					attrValue = (attrType)(table.cell(row,col).value)
					setattr(entry,attrName,attrValue)
	f=open(binDataName,"wb")
	f.write(tableObj.SerializeToString())
	f.close()

#############################################################################
def readMetaFromBin(tableObj,binDataName):
	f=open(binDataName,"rb")
	tableObj.ParseFromString(f.read())
	f.close()
#############################################################################
#import re
def printObj(tableObj):
	it = 0
	for entry in tableObj.list:
		entry_string=""
		if 0 == it:
			for attr in entry.ListFields():
				entry_string += str(attr[0].name) + '\t'
			print(entry_string)
			it=1
		entry_string=""
		for attr in entry.ListFields():
			entry_string += str(getattr(entry,str(attr[0].name))) + '\t'
		print(entry_string)
#############################################################################



