
from __future__ import division

import json
import uuid
import xlwt
import pandas as pd
# def export_excel(export):
     #将字典列表转换为DataFrame

     # export = [{"name": "10.31-星阅11点客服", "click": "64", "new_append": "5", "recharge_amount": "¥ 0"},
     #           {"name": "10.30-星阅22点客服", "click": "34", "new_append": "1", "recharge_amount": "¥ 0"},
     #       ]
# file_path = 'D:\Spider\spider_day02\qw.json'
with open('D:\Spider\spider_day02\擎天文馆.json', encoding='utf-8') as f:
     line = f.readlines()
     d = json.load(line,encoding='utf-8')
     print(d)
     print(type(d))


#      export= [d]
#      # 将字典列表转换为DataFram
#      pf = pd.DataFrame(list(export))
#      #指定字段顺序
#      order = ['name','click','new_append','recharge_amount']
#      pf = pf[order]
#      #将列名替换为中文
#      columns_map = {
#       'name':'入口',
#       'click':'点击',
#       'new_append':'新增关注',
#       'recharge_amount':'充值金额',
#      }
#      pf.rename(columns = columns_map,inplace = True)
#      #指定生成的Excel表格名称
#      rd = uuid.uuid4()
#      file_path = pd.ExcelWriter('擎天文馆.xls')
#      #替换空单元格
#      pf.fillna(' ',inplace = True)
#      #输出
#      pf.to_excel(file_path,encoding = 'utf-8',index = False)
#      #保存表格
#      file_path.save()
# if __name__ == '__main__':
#      #将分析完成的列表导出为excel表格
#      export_excel('擎天文馆.xls')