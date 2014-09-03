

conv_tables={}
conv_table={
	meta='demo.des',--meta name
	xls='demo.xls',--default name is same with meta 
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
	tips = "conv talbe "..k.." : "..v.meta.." from "..v.xls.." to "..v.bin
	print(tips)
	--call python script generate proto 
	--call protobuff genetae python or cpp gen
	--call python script genetate bin from xls with proto
end

