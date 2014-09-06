
def DistillTitleMap(metaObjName,metaObj,titleMap):
	titleMap[metaObjName] = 1
	for entry in metaObj:
		if 'struct' in entry.keys() and entry['struct'] > 0 and entry['type'] not in titleMap.keys() :
			titleMap[entry['type']] = DistillTitleMap(entry['type'],entry,titleMap) 
	for entry in metaObj:
		if 'name' not in entry.keys():
			print('Error : meta name \''+metaObjName+'.[Type='+entry['type']+']\' has no name attr!'
			return titleMap
		if 'cname' not in entry.keys():
			print('Warnning : meta name \''+metaObjName+'.'+entry['name']+'\' has no cname attr use name default !'
		titleMap[entry['cname']] = entry['name']
	return titleMap
