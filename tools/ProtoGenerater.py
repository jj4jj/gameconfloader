

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

def GenerateProto(metaObjName,metaObj,level,gened):
	proto = ""
	gened[metaObjName] = 1
	for entry in metaObj:
		if 'struct' in entry.keys() and entry['struct'] > 0 and entry['type'] not in gened.keys() :
			proto += GenerateProto(entry['type'],entry,level+1,gened)
	proto += "\t"*level + 'message '+metaObjName+' {\n'
	tag = 1
	for entry in metaObj:
		proto +='\t'*(level+1)
		if('array' in attr and attr['array'] > 0):
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
