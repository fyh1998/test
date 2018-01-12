# -*- coding:utf-8 -*-
import os
import re
folder = 'data_tag' #存储结果的文件夹，没有的话会创建一个同名的
if not os.path.exists(folder):
    os.mkdir(folder)
p3 = re.compile('"tag_id":\d{1,10},"tag_name":".{1,15}",')
p4 = re.compile('"tag_name":".{1,15}",')
p_num = re.compile('\d+')
tagpath = "/home/koh/Downloads/bilibili/bili_tag/" #这是第一步爬虫得到的 bili_tag的路径，前面部分改一下
datapath = "/home/koh/Downloads/bilibili/data_tag/" #这是第二步将要进行的数据读取后存放结果的data_tag的路径，前面部分改一下
pathDir = os.listdir(tagpath)
for allDir in pathDir:
    filepath1 = os.path.join(tagpath, allDir)
    filepath2 = os.path.join(datapath, allDir)
    f1 = open(filepath1,"r")
    f2 = open(filepath2,"w")
    datalist = p3.findall(f1.read())
    for tag in datalist:
        tag_id = p_num.findall(tag)[0]
        tag_name = p4.findall(tag)[0][12:-2]
        f2.write(tag_id+' '+tag_name+'\n')
    f1.close()
    f2.close()
