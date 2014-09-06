#!/usr/bin/python
#-*-coding:utf-8-*- 

Monster = [
	{	'name':'id',
		'cname':ur'ID',
		'type' : 'uint32',
		'desc' : 'desc demo',
		'pk'   : 1,
	},
	{	'name':'name',
		'cname':ur'Name',
		'type' : 'string',
		'desc' : 'desc demo',
		'default' : '\'this is a default value\'',
	},
]
Attr = [
	{	'name':'id',
		'cname':ur'ID',
		'type' : 'uint32',
		'desc' : 'desc demo',
		'pk'   : 1,
	},
	{	'name':'value',
		'cname':ur'CValue',
		'type' : 'uint32',
		'desc' : 'value desc',
		'default' : '24',
	},
]

Demo = [
	{	'name':'id',
		'cname':ur'ID',
		'type' : 'uint32',
		'desc' : 'desc demo',
		'pk'   : 1,
	},
	{	'name':'lv',
		'cname':ur'Level',
		'type' : 'uint32',
		'desc' : 'desc demo',
		'pk'   : 1,
	},
	{	'name':'name',
		'cname':ur'Name',
		'type' : 'string',
		'desc' : 'desc demo',
		'default' : '\'this is a default value\'',
	},
	{	'name':'desc',
		'cname':ur'Desc',
		'type' : 'string',
		'desc' : 'desc demo',
	},
	{
		'name':'attr',
		'cname':ur'CAttr',
		'type':'Attr',
		'desc':ur'属性描述',
		'struct':1,
		'array':1,
	},
	{
		'name':'monster',
		'cname':ur'CMonster',
		'type':'Monster',
		'desc':ur'怪物描述',
		'struct':1,
	},
	{
		'name':'shape',
		'cname':ur'CSP',
		'type':'uint32',
		'desc':ur'特点描述',
		'array':1,
	},
]

#########################################

