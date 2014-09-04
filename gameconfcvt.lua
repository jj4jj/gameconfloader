

conv_tables={}
conv_table={
	meta_file='demo_desc.py',--meta name
	meta_name='Demo',--meta name
	xls='demo.xlsx',--default name is same with meta 
	bin='demo.bin',--default name is same with meta
	count=100, --default is 16
	sort='asc',--default is asc
	group=1,--default is 1
};

function addtable(conv)
	table.insert(conv_tables,conv);	
end

--require "conf.lua"
addtable(conv_table)

for k,v in ipairs(conv_tables) do
	execString='python convlist.py meta/'..v.meta_file..' '..v.meta_name..' xls/'..v.xls..' data/'..v.bin
	print(execString)
	--call python script generate proto 
	--call protobuff genetae python or cpp gen
	--call python script genetate bin from xls with proto
end

