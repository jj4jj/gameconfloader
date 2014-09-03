#######################################################
def ConvDescToProtoCode(name,dsc):
	proto = '////////// generate protobuf proto file begin meta = '+name+' //////////\n'
	proto += 'message '+name+' {\n'
	tag=1
	for attr in dsc:
		proto +='\t';
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
		##if('array' in attr and  attr['array'] > 0):
		##	proto += '[packed=true]'
		proto += ' ; '
		proto += '\t//'+attr['desc']+' //'+attr['cname'];
		tag = tag+1
		proto += '\n'
	proto += '}\n'
	proto += '\nmessage '+name+'Table {\n'
	proto += '\trepeated\t'+name+'\tlist\t=\t1 ;\n'
	proto += '}\n'
	proto += '//////////// generate protobuf proto file end meta = '+name+' ////////\n'
	return proto
#########################################################
def ConvDescToPyKeywords(dsc):
	proto = '##### generate dsc keywords file begin #######\n'
	proto +='#-*-coding:utf-8-*-\n' 
	proto += 'def TitleMap():\n\tmp={\n';
	for attr in dsc:	
		proto += '\t\tur\'';
		proto += attr['cname']+'\':\'';
		proto += attr['name'] +'\',\n'
	proto += '\t}\n\treturn mp\n';
	proto += '##### generate dsc keywords file end  #######\n'
	return proto

#########################################################