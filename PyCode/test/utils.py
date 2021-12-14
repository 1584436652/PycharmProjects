import json
import os

def is_file_exist(file_name):
    # 删除旧文件
    # 如果文件存在
    if os.path.exists(file_name):
        # 则删除
        os.remove(file_name)


def extract_first(xpath_res:list):
    """对xpath的结果取第一个元素"""
    return  xpath_res[0].strip() if xpath_res and xpath_res[0] else None

def json2csv(file_name):
    """json转csv"""
    #  文件 --> python对象                       li \


    # datas = []
    with open(file_name) as f:
        #for line in f:
            # datas.append(json.loads(line[:2]))
        datas = [json.loads(line[:-2]) for line in f]
    import pandas as pd
    data_pd = pd.DataFrame(datas)
    data_pd.to_csv(
        file_name.replace("json","csv"),
        index=False,
        encoding="gbk"
    )




if __name__ == '__main__':
    file_name = "dacheng.json"
    json2csv(file_name)





