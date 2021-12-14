from __future__ import division
import uuid
import xlwt
import pandas as pd
# 保存擎天文官平台数据
def export_excel(export):
     #将字典列表转换为DataFrame

     export=[{"name": "11.11-九霄10：30客服", "click": "649", "new_append": "10", "recharge_amount": "¥ 180.00"},
{"name": "11.11-七点10：30客服", "click": "826", "new_append": "25", "recharge_amount": "¥ 134.00"},
{"name": "11.10-七点11点客服", "click": "919", "new_append": "39", "recharge_amount": "¥ 0"},
{"name": "11.10-九霄11点客服", "click": "586", "new_append": "22", "recharge_amount": "¥ 480.00"},
{"name": "11.8-九霄群发5", "click": "378", "new_append": "36", "recharge_amount": "¥ 510.00"},
{"name": "11.8-九霄群发2", "click": "552", "new_append": "25", "recharge_amount": "¥ 551.00"},
{"name": "11.8-九霄群发1", "click": "2234", "new_append": "244", "recharge_amount": "¥ 3,025.00"},
{"name": "11.8-七点-历史5", "click": "998", "new_append": "43", "recharge_amount": "¥ 0"},
{"name": "11.8-七点-历史3", "click": "1212", "new_append": "60", "recharge_amount": "¥ 50.00"},
{"name": "11.8-七点-历史1", "click": "4517", "new_append": "458", "recharge_amount": "¥ 1,038.00"},
{"name": "10.31-星阅11点客服", "click": "84", "new_append": "7", "recharge_amount": "¥ 30.00"},
{"name": "10.30-星阅22点客服", "click": "43", "new_append": "1", "recharge_amount": "¥ 0"},
{"name": "10.30-灵锋19点客服", "click": "272", "new_append": "4", "recharge_amount": "¥ 0"},
{"name": "10.30-星阅19点客服", "click": "102", "new_append": "1", "recharge_amount": "¥ 0"},
{"name": "10.30-龙吟11点客服", "click": "70", "new_append": "5", "recharge_amount": "¥ 50.00"},
{"name": "10.30-灵锋11点客服", "click": "449", "new_append": "20", "recharge_amount": "¥ 0"},
{"name": "10.30-九霄11点客服", "click": "164", "new_append": "4", "recharge_amount": "¥ 0"},
{"name": "10.30-七点11点客服", "click": "504", "new_append": "11", "recharge_amount": "¥ 0"},
{"name": "10.30-清风11点客服", "click": "321", "new_append": "10", "recharge_amount": "¥ 0"},
{"name": "10.30-星阅11点客服", "click": "87", "new_append": "9", "recharge_amount": "¥ 30.00"},
{"name": "10.29-龙吟19点客服", "click": "57", "new_append": "1", "recharge_amount": "¥ 0"},
{"name": "10.29-灵锋19点客服", "click": "376", "new_append": "13", "recharge_amount": "¥ 0"},
{"name": "10.29-九霄19点客服", "click": "138", "new_append": "3", "recharge_amount": "¥ 0"},
{"name": "10.29-七点19点客服", "click": "647", "new_append": "24", "recharge_amount": "¥ 300.00"},
{"name": "10.29-清风19点客服", "click": "438", "new_append": "17", "recharge_amount": "¥ 460.00"},
{"name": "10.29-星阅19点客服", "click": "70", "new_append": "3", "recharge_amount": "¥ 0"},
{"name": "10.29-龙吟-11点客服", "click": "48", "new_append": "1", "recharge_amount": "¥ 0"},
{"name": "10.29-灵锋-11点客服", "click": "389", "new_append": "12", "recharge_amount": "¥ 0"},
{"name": "10.29-九霄-11点客服", "click": "121", "new_append": "4", "recharge_amount": "¥ 0"},
{"name": "10.29-七点-11点客服", "click": "237", "new_append": "4", "recharge_amount": "¥ 0"},
{"name": "10.29-清风-11点客服", "click": "252", "new_append": "9", "recharge_amount": "¥ 80.00"},
{"name": "10.29-星阅-11点客服", "click": "43", "new_append": "2", "recharge_amount": "¥ 30.00"},
{"name": "10.28-藏天22点客服", "click": "922", "new_append": "24", "recharge_amount": "¥ 100.00"},
{"name": "10.28-九霄22点客服", "click": "1282", "new_append": "24", "recharge_amount": "¥ 250.00"},
{"name": "10.28-七点22点客服", "click": "1363", "new_append": "39", "recharge_amount": "¥ 110.00"},
{"name": "10.28-清风22客服", "click": "1099", "new_append": "35", "recharge_amount": "¥ 337.00"},
{"name": "10.28-藏天19点客服", "click": "402", "new_append": "11", "recharge_amount": "¥ 250.00"},
{"name": "10.28-九霄19点客服", "click": "462", "new_append": "9", "recharge_amount": "¥ 30.00"},
{"name": "10.28-七点19点客服", "click": "763", "new_append": "32", "recharge_amount": "¥ 349.00"},
{"name": "10.28-清风19点客服", "click": "504", "new_append": "15", "recharge_amount": "¥ 120.00"},
{"name": "10.28-藏天11点客服", "click": "304", "new_append": "7", "recharge_amount": "¥ 0"},
{"name": "10.28-九霄11点客服", "click": "313", "new_append": "8", "recharge_amount": "¥ 180.00"},
{"name": "10.28-七点11点客服", "click": "711", "new_append": "9", "recharge_amount": "¥ 67.00"},
{"name": "10.28-清风11点客服", "click": "595", "new_append": "19", "recharge_amount": "¥ 51.00"},
{"name": "10.28-龙吟-11时客服", "click": "128", "new_append": "5", "recharge_amount": "¥ 60.00"},
{"name": "10.28-轩辕-11时客服", "click": "41", "new_append": "0", "recharge_amount": "¥ 0"},
{"name": "10.28-龙吟-19时客服", "click": "100", "new_append": "4", "recharge_amount": "¥ 0"},
{"name": "10.28-轩辕-19时客服", "click": "30", "new_append": "0", "recharge_amount": "¥ 0"},
{"name": "10.27-龙吟-22时客服", "click": "86", "new_append": "5", "recharge_amount": "¥ 0"},
{"name": "10.27-轩辕-22时客服", "click": "22", "new_append": "1", "recharge_amount": "¥ 0"},
{"name": "10.27-龙吟-19时客服", "click": "104", "new_append": "5", "recharge_amount": "¥ 199.00"},
{"name": "10.27-轩辕19时客服", "click": "18", "new_append": "2", "recharge_amount": "¥ 0"},
{"name": "10.27-龙吟-11时客服", "click": "111", "new_append": "3", "recharge_amount": "¥ 0"},
{"name": "10.27-轩辕-11时客服", "click": "26", "new_append": "1", "recharge_amount": "¥ 0"},
{"name": "10.27-藏天19点客服", "click": "387", "new_append": "8", "recharge_amount": "¥ 0"},
{"name": "10.27-九霄19点客服", "click": "336", "new_append": "18", "recharge_amount": "¥ 550.00"},
{"name": "10.27-七点19点客服", "click": "664", "new_append": "21", "recharge_amount": "¥ 230.00"},
{"name": "10.27-清风19点客服", "click": "538", "new_append": "18", "recharge_amount": "¥ 230.00"},
{"name": "10.27-藏天11点客服", "click": "961", "new_append": "41", "recharge_amount": "¥ 810.00"},
{"name": "10.27-九霄11点客服", "click": "877", "new_append": "27", "recharge_amount": "¥ 1,350.00"},
{"name": "10.27-七点11点客服", "click": "1075", "new_append": "46", "recharge_amount": "¥ 230.00"},
{"name": "10.27-清风11点客服", "click": "1014", "new_append": "56", "recharge_amount": "¥ 397.00"},
{"name": "10.25-九霄-历史2", "click": "621", "new_append": "74", "recharge_amount": "¥ 1,467.00"},
{"name": "10.25-清风-历史5", "click": "534", "new_append": "57", "recharge_amount": "¥ 150.00"},
{"name": "10.25-清风-历史4", "click": "958", "new_append": "125", "recharge_amount": "¥ 470.00"},
{"name": "10.25-清风-历史3", "click": "881", "new_append": "44", "recharge_amount": "¥ 420.00"},
{"name": "10.25-清风-历史2", "click": "1514", "new_append": "175", "recharge_amount": "¥ 1,487.00"},
{"name": "10.25-清风-历史1", "click": "5269", "new_append": "587", "recharge_amount": "¥ 6,810.00"},
{"name": "10.25-九霄-历史4", "click": "1059", "new_append": "121", "recharge_amount": "¥ 1,297.00"},
{"name": "10.25-九霄-历史3", "click": "414", "new_append": "28", "recharge_amount": "¥ 830.00"},
{"name": "10.25-藏天群发4", "click": "1414", "new_append": "136", "recharge_amount": "¥ 597.00"},
{"name": "10.25-藏天群发3", "click": "661", "new_append": "44", "recharge_amount": "¥ 100.00"},
{"name": "10.25-九霄-历史1", "click": "1919", "new_append": "165", "recharge_amount": "¥ 3,104.00"},
{"name": "10.25-藏天群发2", "click": "739", "new_append": "44", "recharge_amount": "¥ 979.00"},
{"name": "10.25-藏天群发1", "click": "3661", "new_append": "389", "recharge_amount": "¥ 3,905.00"},
{"name": "10.25-七点-历史4", "click": "2121", "new_append": "174", "recharge_amount": "¥ 334.00"},
{"name": "10.25-七点-历史3", "click": "1074", "new_append": "54", "recharge_amount": "¥ 110.00"},
{"name": "10.25-轩辕群发5", "click": "31", "new_append": "3", "recharge_amount": "¥ 0"},
{"name": "10.25-七点-历史2", "click": "1823", "new_append": "72", "recharge_amount": "¥ 1,067.00"},
{"name": "10.25-轩辕群发4", "click": "77", "new_append": "8", "recharge_amount": "¥ 0"},
{"name": "10.25-轩辕群发3", "click": "35", "new_append": "0", "recharge_amount": "¥ 0"},
{"name": "10.25-七点-历史1", "click": "5353", "new_append": "542", "recharge_amount": "¥ 3,604.00"},
{"name": "10.25-轩辕群发2", "click": "49", "new_append": "2", "recharge_amount": "¥ 0"},
{"name": "10.25-轩辕群发1", "click": "194", "new_append": "21", "recharge_amount": "¥ 100.00"},
{"name": "10.26-龙吟-22时客服", "click": "137", "new_append": "9", "recharge_amount": "¥ 50.00"},
{"name": "10.26-龙吟-19时客服", "click": "115", "new_append": "6", "recharge_amount": "¥ 0"},
{"name": "10.26-藏天-19点客服", "click": "760", "new_append": "29", "recharge_amount": "¥ 400.00"},
{"name": "10.26-灵锋-19点客服", "click": "1093", "new_append": "42", "recharge_amount": "¥ 50.00"},
{"name": "10.26-九霄-19点客服", "click": "763", "new_append": "33", "recharge_amount": "¥ 707.00"},
{"name": "10.26-七点-19点客服", "click": "1070", "new_append": "41", "recharge_amount": "¥ 301.00"},
{"name": "10.26-清风-19点客服", "click": "718", "new_append": "32", "recharge_amount": "¥ 140.00"},
{"name": "10.25-藏天11点客服", "click": "892", "new_append": "36", "recharge_amount": "¥ 34.00"},
{"name": "10.25-灵锋11点客服", "click": "1619", "new_append": "50", "recharge_amount": "¥ 700.00"},
{"name": "10.25-九霄11点客服", "click": "568", "new_append": "33", "recharge_amount": "¥ 424.00"},
{"name": "10.25-七点11点客服", "click": "1577", "new_append": "58", "recharge_amount": "¥ 330.00"},
{"name": "10.25-清风11点客服", "click": "435", "new_append": "29", "recharge_amount": "¥ 184.00"},
{"name": "10.24-龙吟-22时客服", "click": "73", "new_append": "6", "recharge_amount": "¥ 30.00"},
{"name": "10.25-龙吟-11时客服", "click": "80", "new_append": "3", "recharge_amount": "¥ 0"},
{"name": "10.24-龙吟-21时客服", "click": "44", "new_append": "2", "recharge_amount": "¥ 0"},
{"name": "10.24-藏天19点客服", "click": "471", "new_append": "23", "recharge_amount": "¥ 190.00"},
{"name": "10.24-灵锋19点客服", "click": "635", "new_append": "22", "recharge_amount": "¥ 0"},
{"name": "10.24-九霄19点客服", "click": "178", "new_append": "8", "recharge_amount": "¥ 100.00"},
{"name": "10.24-七点19点客服", "click": "454", "new_append": "16", "recharge_amount": "¥ 184.00"},
{"name": "10.24-清风19点客服", "click": "456", "new_append": "29", "recharge_amount": "¥ 47.00"},
{"name": "10.24-龙吟-11时客服", "click": "97", "new_append": "6", "recharge_amount": "¥ 0"},
{"name": "10.24-藏天11点客服", "click": "522", "new_append": "25", "recharge_amount": "¥ 50.00"},
{"name": "10.24-灵锋11点客服", "click": "881", "new_append": "35", "recharge_amount": "¥ 240.00"},
{"name": "10.24-九霄11点客服", "click": "334", "new_append": "27", "recharge_amount": "¥ 740.00"},
{"name": "10.24-七点11点客服", "click": "654", "new_append": "48", "recharge_amount": "¥ 180.00"},
{"name": "10.24-清风11点客服", "click": "751", "new_append": "55", "recharge_amount": "¥ 190.00"},
{"name": "10.24菜单2-5", "click": "241", "new_append": "2", "recharge_amount": "¥ 0"},
{"name": "10.24菜单2-4", "click": "311", "new_append": "0", "recharge_amount": "¥ 0"},
{"name": "10.24菜单2-3", "click": "202", "new_append": "2", "recharge_amount": "¥ 0"},
{"name": "10.24菜单2-2", "click": "293", "new_append": "0", "recharge_amount": "¥ 0"},
{"name": "10.24菜单2-1", "click": "615", "new_append": "1", "recharge_amount": "¥ 50.00"},
{"name": "10.24-龙吟-11时客服", "click": "0", "new_append": "0", "recharge_amount": "¥ 0"},

]

     # 将字典列表转换为DataFram
     pf = pd.DataFrame(list(export))
     #指定字段顺序
     order = ['name','click','new_append','recharge_amount']
     pf = pf[order]
     #将列名替换为中文
     columns_map = {
      'name':'入口',
      'click':'点击',
      'new_append':'新增关注',
      'recharge_amount':'充值金额',
     }
     pf.rename(columns = columns_map,inplace = True)
     #指定生成的Excel表格名称
     rd = uuid.uuid4()
     file_path = pd.ExcelWriter('擎天文馆%s.xls' % rd)
     #替换空单元格
     pf.fillna(' ',inplace = True)
     #输出
     pf.to_excel(file_path,encoding = 'utf-8',index = False)
     #保存表格
     file_path.save()
if __name__ == '__main__':
     #将分析完成的列表导出为excel表格
     export_excel('擎天文馆.xls')