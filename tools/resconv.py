#!/usr/bin/python
#-*-coding:utf-8-*- 


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
def readBinToObj(tableObj,binDataName):
	f=open("demo.bin","rb")
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
#force load


#############################################################################


if (len(sys.argv) < 4):
	print("usage:./convlist.py <meta file> <MetaName> <xlsFile> <binFile>")
	print("eg.:./convlist.py demo.desc Demo demo.xls demo.bin")
	print("	it will read meta/demo.desc file generate mid/demo_keywords.py and mid/demo.proto file")
	print("	read demo.xls file generate a DemoTable object with demo.proto and demo_keywords ")
	print("	output name is data/demo.bin")
	sys.exit(-1)

metaFile=sys.argv[1]
metaName=sys.argv[2]
metaTableName=metaName+'Table'

sys.path.append('gen')
sys.path.append('mid')
sys.path.append('meta')
sys.path.append('.')
import os

metaPBPackage=metaName+"_pb2"
metaKeywords=metaName+"_keywords"

#conv desc to proto file
cvDsc = __import__('convDesc')

metaPy = metaFile.partition('.')[0]
mtDesc = __import__(metaPy)

metaProtoName=metaName+'.proto'
f = open(metaProtoName,'wb')
f.write(cvDsc.ConvDescToProtoCode(metaName,mtDesc.Meta))
f.close()


f = open(metaKeywords+'.py','wb')
f.write(cvDsc.ConvDescToPyKeywords(mtDesc.Meta))
f.close()

###############################################################################
#generate proto file
execString = 'protoc '+metaProtoName+' --python_out=gen';
print("system is exec :'"+execString+"' , pls waiting ...")
os.system(execString)

###############################################################################
xlsFile=sys.argv[3]
binFile=sys.argv[4]
md =__import__(metaPBPackage)
mdk = __import__(metaKeywords)
#####################################
metaTableObj = getattr(md,metaTableName)()
metaTitleMap = getattr(mdk,'TitleMap')()
#check
##############################################################################
writeXlsToBin(metaTableObj,xlsFile,binFile,metaTitleMap);