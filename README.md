#gameconfloader

a loader that convert many xls files to a binary file or text file to supporting program reading .
##usage
* Environment requiration
 - python 2.6 later need
 - protobuf-python need installed
 -- U can got it in github google , then setup.py build/install
 - xlrd python module need installed
* Let your data ready
 - add the table entry description file <demo_desc.py> into 'meta' dir
 - add your excel data files into 'xls' dir
* Orgonize your file with editing the convert talbe description
 - edit conf.py add your convert files description (reffer to demo)
* Convert it !
```sh
>python gameconcvt.py
```
##todo list
* Meta keywords with array 
* Data keywords map a real data
* A friendly GUI
