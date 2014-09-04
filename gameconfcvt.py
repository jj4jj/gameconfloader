#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
convTables={}

def AddTable(conv):
	print('Add Table = '+conv['name']+' ( Meta = '+conv['metaName']+' , MetaFile = '+conv['metaFile']+' , XlsFile = '+conv['xls']+' , BinFile = '+conv['bin']+' )');
	convTables[conv['name']]=conv

#--require "conf.lua"
#for demo
#AddTable(convDemo)
############################################
ct=__import__('conf')
for cv in ct.GetConvertTableList():
	AddTable(cv)
############################################
for k in convTables.keys():
	execString = 'python convlist.py meta/'+convTables[k]['metaFile']+' '+\
		convTables[k]['metaName']+' xls/'+\
		convTables[k]['xls']+' data/'+convTables[k]['bin']
	print(execString)
	#python convlist.py meta/demo_desc.py Demo xls/demo.xlsx data/demo.bin
	#call python script generate proto 
	#call protobuff genetae python or cpp gen
	#call python script genetate bin from xls with proto
