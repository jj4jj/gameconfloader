#!/usr/bin/python
#-*-coding:utf-8-*- 
import sys
import os
#force load

sys.path.append('.')
convUtil=__import__('ConvUtil')
sys.path.append('tools')
mh = __import__('MetaInfoHelper')
#############################################################################


if (len(sys.argv) < 4):
	print("usage:python"+sys.argv[0]+" <meta file> <MetaName> <xlsFile> <binFile> <read check>")
	print("eg.:./convlist.py demo_desc Demo demo.xls demo.bin")
	print("	it will read meta/demo.desc file generate mid/demo_keywords.py and mid/demo.proto file")
	print("	read demo.xls file generate a DemoTable object with demo.proto and demo_keywords ")
	print("	output name is data/demo.bin")
	sys.exit(-1)
readCheck = 0
if (len(sys.argv) > 4):
	print(sys.argv[4])
	readCheck = 1	

metaFilePath=sys.argv[1]
metaName=sys.argv[2]
metaTableName=metaName+'Table'
metaFile=metaFilePath.split('/')[-1]
sys.path.append('gen')
sys.path.append('mid')
sys.path.append('meta')

metaPBPackage=metaName+"_pb2"

metaKeywords=metaName+"_keywords"

#conv desc to proto file
cvDsc = __import__('convDesc')

metaPy = metaFile.split('.')[0]

mtDesc = __import__(metaPy)
mainMeta = getattr(mtDesc,metaName)
metaProtoName= 'mid/'+metaName+'.proto'
f = open(metaProtoName,'wb')
f.write(mh.GenerateProto(metaName,mainMeta,0,{},mtDesc))
f.close()

metaTitleMap=mh.DistillTitleMap(metaName,mainMeta,{},mtDesc,{})

#mh.DumpTitleMap(metaTitleMap,'Root',0)

###############################################################################
#generate proto file
execString = 'protoc --proto_path=./mid '+metaProtoName+' --python_out=gen --cpp_out=include';
print("system is exec :'"+execString+"' , pls waiting ...")
os.system(execString)

###############################################################################
xlsFile=sys.argv[3]
binFile=sys.argv[4]
md =__import__(metaPBPackage)
#####################################
metaTableObj = getattr(md,metaTableName)()
#check
##############################################################################

convUtil.writeXlsToBin(metaTableObj,xlsFile,binFile,metaTitleMap);


#############################################################################
if(readCheck > 0):
	objTable = getattr(md,metaTableName)
	convUtil.readMetaFromBin(objTable,binFile)
	print("read check from binFile = "+binFile)
	convUtil.printObj(objTable)






