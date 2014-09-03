

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
	convTables[conv.name]=conv
end

#--require "conf.lua"
AddTable(convDemo)


############################################
for k in convTables.keys():
	tips = "conv talbe "+convTables[k]+" : "+convTable[k].metaName+" from "+metaFile+' and '+convTable[k]..xls+" to "+convTable[k].bin
	print(tips)	
	execString = 'python convlist.py meta/'+convTable[k].metaFile+' '+
		convTable[k].metaName+' xls/'+
		convTable[k].xls+' data/'+convTable[k].bin
	print(execString)
	#python convlist.py meta/demo_desc.py Demo xls/demo.xlsx data/demo.bin
	#call python script generate proto 
	#call protobuff genetae python or cpp gen
	#call python script genetate bin from xls with proto

