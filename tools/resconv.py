#!/usr/bin/python

import sys
import xlrd
############################################################################
def writeXlsToBin(tableObj,xlsName,binDataName,titleMap):
	xlsData = xlrd.open_workbook(xlsName)	
	if not vars().has_key(titleMap):
		#list all attr name
		#set map attr name equal with value
		print(dir(tableObj.list))

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
					attrValue = (attrType)(table.cell(row,col).value)
					setattr(entry,attrName,attrValue)
					print('set attr',attrName,'=',attrValue)
	f=open(binDataName,"wb")
	f.write(tableObj.SerializeToString())
	f.close()

#############################################################################
def readBinToObj(tableObj,binDataName):
	f=open("demo.bin","rb")
	tableObj.ParseFromString(f.read())
	f.close()
#############################################################################

def printObj(tableObj):
	for entry in tableObj.list:
		for attr in dir(entry):
			print(getattr(entry,attr))


#############################################################################