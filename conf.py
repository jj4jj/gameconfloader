#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
#############################################################################################3
convTableList=(
#################custom conv define#########################################
{
	'name':ur'示例显示表',#display name
	'metaName':'Demo',#meta name
	'metaFile':'demo.desc',#meta name
	'xls':'demo.xls',#default name is same with meta 
	'bin':'demo.bin',#default name is same with meta
	'count':100, #default is 16
	'sort':'asc',#default is asc
	'group':1,#default is 1
},

#################custom conv define#########################################
)

def GetConvertTableList():
	return convTableList
