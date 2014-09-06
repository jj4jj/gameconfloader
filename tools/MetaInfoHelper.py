#!/usr/bin/python
#-*-coding:utf-8-*- 


import sys
reload(sys)
sys.setdefaultencoding("utf-8")
'''
-------------------------------------------------------------------------
demo_desc.py describe the xls title line every title map a entry sub attr
it's recursively .
eg.

A=[
{},
{},
]
B=[
{A},
{},
]
Meta=[
{A}
{B}
]

--------------------------------------------------------------------------
Algorithm1.get a meta sub attr from a desc string
--------------------------------------------------------------------------
mpTitleMap.match(title)
	#if all matched return 
	#return attr.name.substr(atitle)
	(atitle,id,tdesc) <- title
	if [atitle]
		#id
		return ([atitile],id)
	else
		return nil
GetAttr(attrName)
	id=attrName.id
	attr = self.attrName
	if(id > 0)
		while(len(attr) < id)
			attr.add()
		idx = id - 1
		return attr[idx]
	else
		return attr
	
setTileValue(metaObj,title,value)
	if(title is nil)
		metaObj = value
	else 
		attrName = metaObj.mpTitleMap.match(title)
		if(attrName is nil)
			title can't find title map
			return -1
		attrObj = metaObj.GetAttr(attrName)				
		setTitleValue(attrObj,title-attrName,value)


'''
import re


def DistillTitleMap(metaObjName,metaObj,titleMap,md,typeMapFlag,debugMode=1,level = 0):
	if(debugMode>0):
		print(' '*level*4+'add title map :'+metaObjName)
	for entry in metaObj:
		if entry.get('struct',None) != None and entry.get(entry['type'],None) == None:
			entryMetaObj = getattr(md,entry['type'])
			typeMapFlag[entry['type']] = {}
			titleMap[entry['type']] = DistillTitleMap(entry['type'],entryMetaObj,{},md,typeMapFlag,debugMode,level+1) 
	for entry in metaObj:
		if  entry.get('name',None) == None :
			print('Error : meta name \''+metaObjName+'.[Type='+entry['type']+']\' has no name attr!')
			return titleMap
		if  entry.get('cname',None) == None :
			print('Warnning : meta name \''+metaObjName+'.'+entry['name']+'\' has no cname attr use name default !')
		if(debugMode>0):
			print(' '*(level+1)*4+'add entry :'+entry['cname']+'->'+entry['name'])
		titleMap[entry['cname']] = entry['name']
	return titleMap
def DumpTitleMap(titleMap,Name,level):
	if(level > 4):
		return
	print(' '*4*level+Name)
	for key in titleMap.keys():
		if isinstance(titleMap[key],str):
			print(' '*4*(level+1)+key+'->'+titleMap[key])
		else:
			DumpTitleMap(titleMap[key],key,level+1)

import string
def SetAttrFromMetaTitle(metaObj,curTitleMap,title,rootTitleMap,v):
	#if all matched return 
	#return attr.name.substr(atitle)
	#string.int.string
	if title == "":
		return metaObj	
	#######################################
	aTitle = ""
	tid = ""
	tTitle = ""
	#find machest aTitle
	def titleSortKey(a):
		if(title.startswith(a)):
			return len(a)
		else:
			return 0
	mostLike = sorted(curTitleMap.keys(),key = titleSortKey,reverse = True) 
	aTitle = (mostLike[0])	
	#print(mostLike)
	#print('most like '+title+'->'+aTitle)
	if len(title) > len(aTitle):
		idx = title.index(aTitle)
		#print(idx,title[idx:],len(title),len(aTitle))
		if( unicode(title[len(aTitle):len(aTitle)+1]).isdigit() ):
			tid = title[len(aTitle):len(aTitle)+1]
			tTitle = title[len(aTitle)+1:]
		else:
			tTitle = title[len(aTitle):]
	#(atitle,id,tdesc) <- title
	#######################################
	#print('aTitle('+aTitle+') id('+tid+') tTitle('+tTitle+')')
	#DumpTitleMap(titleMap,'Root',0)
	if curTitleMap.get(aTitle,None) != None:
		#get attr = meta.name object		
		attrName = curTitleMap[aTitle]
		attrObj = getattr(metaObj,attrName)
		#get attr obj type
		typeName = attrObj.__class__.__name__
		#if attr obj is a array
		if tid != "" and int(tid) > 0:
			idx = int(tid) - 1
			while(len(attrObj) < idx + 1):
				try:
					attrObj.add()
				except Exception,ex:
					print('Fatal Error: not support simple type array !')
					exit(-1)
			realAttrObj = attrObj[idx]
			typeName = realAttrObj.__class__.__name__
			#print('realTypeName:'+typeName)
			#print('typeName='+typeName+' realTypeName='+realTypeName+'map='+rootTitleMap.get(realTypeName,'None'))
			if(rootTitleMap.get(typeName,None) != None):
				return SetAttrFromMetaTitle(attrObj[idx],rootTitleMap[typeName],tTitle,rootTitleMap,v)

			typeInfo = type(realAttrObj)
			attrObj[idx] = (typeInfo)(v)
			return realAttrObj
		else:
			#print('typeName:'+typeName+' title:'+tTitle)
			if(rootTitleMap.get(typeName,None) != None):
				return SetAttrFromMetaTitle(attrObj,rootTitleMap[typeName],tTitle,rootTitleMap,v)
			typeInfo = type(attrObj)
			#attrObj = (typeInfo)(v)
			#print(typeInfo,attrName)
			setattr(metaObj,attrName,(typeInfo)(v))
			return attrObj
	else:
		print('Error: the Title '+aTitle+' not found in titleMap !')
		return None;
	return None


def SetMetaObjValueByTitle(metaObj,titleMap,title,v):
	#print('set titile '+title+' value = '+str(v))
	attrObj = SetAttrFromMetaTitle(metaObj,titleMap,title,titleMap,v)
	if (attrObj == None):
		print('Error: title not found !')

##give the first meta object 
##convert it to a proto message
##supporting recursively
'''
--------------------------------------------------------------------------
Algorithm3.generate meta proto
--------------------------------------------------------------------------
GeneratePrimtiveProto(metaObj,level)
	proto = '\t'{level}
	proto = 'message '+metaObj.name
	for entry in metaObj
		proto += entryToLine(entry)
	return proto

GenerateProto(metaObj,level)
	#topology sort
	#most dependly meta will generate first
	for entry in metaObj
		if entry.struct
			GenerateProto(metaObj,level+1)
	proto += GeneratePrimtiveProto(metaObj,level)
	return proto	
'''
	
def GenerateProtoMeta(metaObjName,metaObj,level,gened,md):
	proto = ""
	gened[metaObjName] = 1
	#print('generate proto:'+metaObjName+'->'+str(type(metaObj)))
	for entry in metaObj:
		if 'struct' in entry.keys() and entry['struct'] > 0 and entry['type'] not in gened.keys() :
			entryMetaObj = getattr(md,entry['type'])
			proto += GenerateProtoMeta(entry['type'],entryMetaObj,level,gened,md)
	proto += "\t"*level + 'message '+metaObjName+' {\n'
	tag = 1
	for attr in metaObj:
		proto +='\t'*(level+1)
		if('array' in attr.keys() and attr['array'] > 0):
			proto += 'repeated\t';
		elif('pk' in attr and attr['pk'] > 0):
			proto += 'required\t';	
		else:
			proto += 'optional\t';
		proto += attr['type']+'\t';
		proto += attr['name']+'\t';
		proto += '=\t';
		proto += str(tag)+' ';
		if('default' in attr and  attr['default'] > 0):
			proto += '[default='+attr['default']+']'
		if('array' in attr and  attr['array'] > 0 and 'struct' not in attr ):
			proto += '[packed=true]'
		proto += ' ; '
		proto += '\t//'+attr['desc']+' --cname='+attr['cname'];
		tag = tag+1
		proto += '\n'
	proto += "\t"*level + '}\n'
	return proto

def GenerateProto(metaObjName,metaObj,level,gened,md):
	proto = GenerateProtoMeta(metaObjName,metaObj,level,gened,md)
	proto += '\nmessage '+metaObjName+'Table {\n'
	proto += '\trepeated\t'+metaObjName+'\tlist\t=\t1 ;\n'
	proto += '}\n'
	return proto
