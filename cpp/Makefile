CFLAGS=-I. -I/usr/local/include -lprotobuf -L/usr/local/lib
reader:../include/Demo.pb.cc reader.cpp
	g++ -o $@  $^ ${CFLAGS}
