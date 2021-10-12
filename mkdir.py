i#!/user/local/bin/python2.7
# -*- coding:utf-8 -*-
# 引入模块
import os
def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录,创建目录操作函数
        '''
        os.mkdir(path)与os.makedirs(path)的区别是,当父目录不存在的时候os.mkdir(path)不会创建，os.makedirs(path)则会创建父目录
        '''
        #此处路径最好使用utf-8解码，否则在磁盘中可能会出现乱码的情况
        os.makedirs(path.decode('utf-8')) 
        print path+' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' 目录已存在'
        return False
# 定义要创建的目录
path=r"d:\\web天下\\"
# 调用函数
mkdir(path)
