import os
import sys
import xlrd
reload(sys)
sys.setdefaultencoding("utf-8")


sys.path.append('tools')
mh = __import__('MetaInfoHelper')
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
					attrTitleName = unicode(table.cell(0,col).value)
					attrValue = table.cell(row,col).value
					mh.SetMetaObjValueByTitle(entry,titleMap,attrTitleName,attrValue)
	f=open(binDataName,"wb")
	f.write(tableObj.SerializeToString())
	f.close()

#######################################
######################################
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
				entry_string += unicode(attr[0].name) + '\t'
			print(entry_string)
			it=1
		entry_string=""
		for attr in entry.ListFields():
			entry_string += unicode(getattr(entry,str(attr[0].name))) + '\t'
		print(entry_string)
#############################################################################



