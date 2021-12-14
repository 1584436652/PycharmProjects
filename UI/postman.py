import random
import string
import os


def modify_suffix(dirname,old_suffix,new_suffix):
    """
    :param dirname:操作的目录
    :param old_suffix: 之前的后缀名
    :param new_suffix: 新的后缀名
    :return:
    """
    # 1.判断查找的目录是否存在，如果不存在，报错
    if os.path.exists(dirname):
        # 2.找出所有以old_suffix(.png)结尾的文件
        pngfile = [filename for filename in os.listdir(dirname)
                   if filename.endswith(old_suffix)]
        # 3.将后缀名和文件名分开，留下文件名
        basefiles = [os.path.splitext(filename)[0]
                     for filename in pngfile]
        # 4.重命名文件
        for filename in basefiles:
            oldname = os.path.join(dirname,filename+old_suffix)
            newname = os.path.join(dirname,filename+new_suffix)
            os.rename(oldname,newname)
            print('%s命名为%s成功' %(oldname,newname))
    else:
        print('%s不存在,不能操作...' %(dirname))

modify_suffix(r'C:\Users\Administrator\Desktop\PP', '.CSV', '.png')
