#coding=utf-8
import os
#qq2635760633
print(".                                                                             .")
path =  raw_input("please type the path of your project")

def list_all_files(rootdir):
    import os
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files

print(list_all_files(path))
for file in list_all_files(path):
    if file[-3:] == "pyc":
        print("del "+file)
        os.popen("del "+file)
    if file[-3:] == ".py":
        os.popen("add first line of the file: " + file)
        with open(file, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('#coding=utf-8\n' + content)
