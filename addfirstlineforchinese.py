#coding=utf-8
import os
#作者QQ:2635760633，版权归作者所有
#此py文件专门为中国人,因为很多github开源代码都不加#coding=utf-8就发布，然后一大堆写了注释忘记改编码，习惯很不好不说，给其他人也带来了比较大的麻烦

#还有打个小广告，最近喜欢上了手游CF(穿越火线枪战王者)，自己和朋友开发了其透视辅助，QQ群696655788

print(u"打个小广告，最近喜欢上了手游CF(穿越火线枪战王者)，自己和朋友开发了其透视辅助，QQ群696655788")
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


#作者QQ:2635760633，版权归作者所有
#此py文件专门为中国人,因为很多github开源代码都不加#coding=utf-8就发布，然后一大堆写了注释忘记改编码，习惯很不好不说，给其他人也带来了比较大的麻烦

#还有打个小广告，最近喜欢上了手游CF(穿越火线枪战王者)，自己和朋友开发了其透视辅助，QQ群696655788
