#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
convTables={}
convDemo={
	'name':ur'示例显示表',#display name
	'metaName':'Demo',#meta name
	'metaFile':'demo.desc',#meta name
	'xls':'demo.xls',#default name is same with meta 
	'bin':'demo.bin',#default name is same with meta
	'count':100, #default is 16
	'sort':'asc',#default is asc
	'group':1,#default is 1
};
def AddTable(conv):
	convTables[conv['name']]=conv

#--require "conf.lua"
AddTable(convDemo)


############################################
for k in convTables.keys():
	tips = "conv talbe "+convTables[k]['name']+" : "+convTables[k]['metaName']+" from "+convTables[k]['metaFile']+' and '+convTables[k]['xls']+" to "+convTables[k]['bin']
	print(tips)	
	execString = 'python convlist.py meta/'+convTables[k]['metaFile']+' '+\
		convTables[k]['metaName']+' xls/'+\
		convTables[k]['xls']+' data/'+convTables[k]['bin']
	print(execString)
	#python convlist.py meta/demo_desc.py Demo xls/demo.xlsx data/demo.bin
	#call python script generate proto 
	#call protobuff genetae python or cpp gen
	#call python script genetate bin from xls with proto