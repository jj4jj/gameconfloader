



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
def GetAttrFromMetaTitle(metaObj,titleMap,title)
	#if all matched return 
	#return attr.name.substr(atitle)
	#string.int.string
	if title == "":
		return metaObj	
	#######################################
	aTitle = ""
	tid = ""
	tTitle = ""
	pat=re.compile(ur'\d')
	match = pat.match(title)
	aTitle = title
	if match:
		aTitle = title.split(match)[0]
		tid = match
		tTitle = title.split(match)[1]	
	#(atitle,id,tdesc) <- title
	#######################################
	if aTitle in titleMap.keys():
		attrObj = getattr(metaObj,titleMap[aTitle])
		typeName = str(type(attrObj))
		if tid != "" and int(tid) > 0:
			idx = int(tid) - 1
			while(len(attrObj) < idx + 1):
				attrObj.add()
			realAttrObj = attrObj[idx]
			typeName = str(type(realAttrObj))
			return GetAttrFromMetaTitle(attrObj[idx],titleMap[typeName],tTitle)
		else:

			return GetAttrFromMetaTitle(attrObj,titleMap[typeName],tTitle)
	else:
		print('Error: the Title '+aTitle+' not found in titleMap !')
		return None;
	return None


def SetMetaObjValueByTitle(metaObj,title,v)
	attrObj = GetAttrFromMetaTitle(metaObj,titleMap,title)
	if (attrObj != None):
		attrObj = v;
	else
		print('Error: title not found !')