

#include <iostream>
#include <fstream>
#include <../include/Demo.pb.h>
#include <cassert>

using namespace std;

char buffer[512*1024];
int main()
{
	ifstream ifs("../data/demo.bin",std::ifstream::binary);
	ifs.seekg(0, ifs.end);
	int length = ifs.tellg();
	ifs.seekg(0, ifs.beg);
	cout<<length<<endl;
	assert(length < sizeof(buffer));
	ifs.read(buffer,length);
	DemoTable dt;
	dt.ParseFromString(buffer);
	cout<<dt.list_size()<<endl;
	cout<<dt.list(2).name()<<endl;
	cout<<dt.list(1).desc()<<endl;
	cout<<dt.list(1).id()<<endl;
	cout<<dt.list(0).id()<<endl;
	cout<<dt.list(2).id()<<endl;
	dt.Ser

	return 0;
}
