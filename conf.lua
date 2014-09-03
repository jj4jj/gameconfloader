xls_path=xls
meta_path=meta
out_path=data
format=bin

----------------------------------------------------------------

#description of tables want to conv
#if there is no entries , read all xls_path files 
#and use meta name same with xls file .

#generate xls with meta with a order by key formated bin or text.
#generate include files and data

#addtables --add all xls_path files with a default conf

----------------------------------------------------------------

addgroup
{
	id=1,
	name=default,	
}


----------------------------------------------------------------

addtable
{
	meta=demo_conf.py,--meta name
	xls=demo.xlsx,--default name is same with meta 
	bin=demo.bin,--default name is same with meta
	count=100, --default is 16
	sort=asc,--default is asc
	group=1,--default is 1
}

----------------------------------------------------------------
