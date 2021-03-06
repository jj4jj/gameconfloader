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
		'cname':ur'名字',
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
		'cname':ur'数值',
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
		'cname':ur'等级',
		'type' : 'uint32',
		'desc' : 'desc demo',
		'pk'   : 1,
	},
	{	'name':'name',
		'cname':ur'名字',
		'type' : 'string',
		'desc' : 'desc demo',
		'default' : '\'this is a default value\'',
	},
	{	'name':'desc',
		'cname':ur'描述',
		'type' : 'string',
		'desc' : 'desc demo',
	},
	{
		'name':'attr',
		'cname':ur'属性',
		'type':'Attr',
		'desc':ur'属性描述',
		'struct':1,
		'array':1,
	},
	{
		'name':'monster',
		'cname':ur'怪物',
		'type':'Monster',
		'desc':ur'怪物描述',
		'struct':1,
	},
	{
		'name':'shape',
		'cname':ur'特点',
		'type':'uint32',
		'desc':ur'特点描述',
		'array':1,
	},
]

#########################################

