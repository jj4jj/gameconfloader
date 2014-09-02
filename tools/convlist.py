#!/usr/bin/python
#-*-coding:utf-8-*- 



import sys
import xlrd
reload(sys)
sys.setdefaultencoding("utf-8")
############################################################################
def writeXlsToBin(tableObj,xlsName,binDataName,titleMap):
	xlsData = xlrd.open_workbook(xlsName)
	for k in titleMap.keys():
		print(k,titleMap[k])		
	for table in xlsData.sheets():
		for row in range(table.nrows):
			if row > 0:
				entry = tableObj.list.add()
			for col in range(table.ncols):
				if row == 0:
					continue
				else:
					print(table.cell(0,col).value)
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












import	demo_pb2
######################################
demotable = demo_pb2.DemoTable()
demoTitleMap={}
demoTitleMap[U'ID']='id'
demoTitleMap[U'名字']='name'
writeXlsToBin(demotable,'demo.xlsx','demo.bin',demoTitleMap);





