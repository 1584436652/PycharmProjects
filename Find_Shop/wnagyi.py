import xlrd
import pandas as pd
import os

from datetime import datetime
from xlrd import xldate_as_tuple


class Distribution():

    def __init__(self):
        self.detail_table_path = r"C:\Users\Administrator\Desktop\my_work.xls"
        self.inventory_table_path = r"C:\Users\Administrator\Desktop\一部库存.xlsx"
        self.date_sort_table_path = r"C:\Users\Administrator\Desktop\排序后的表.xlsx"

    def file_address(self):
        if os.path.exists(self.date_sort_table_path):
            os.remove(self.date_sort_table_path)

    def date_sort(self):
        detail_table_path = self.detail_table_path
        df = pd.read_excel(detail_table_path, index_col=0)
        data_save = df.sort_values('付款时间', ascending=True)
        self.file_address()
        data_save.to_excel(self.date_sort_table_path)

    # 读取马帮下载的表格，把需要的字段存入字典
    def read_detail_table(self):
        detail_dicts = {}
        read_xls = xlrd.open_workbook(self.date_sort_table_path)
        xls_sheet = read_xls.sheets()[0]
        row_len = xls_sheet.nrows
        for detail_row in range(1, row_len):
            rowValues = xls_sheet.row_values(detail_row)  # 某一行数据
            date = datetime(*xldate_as_tuple(rowValues[1], 0))
            cell = date.strftime('%Y/%m/%d %H:%M:%S')   # 转成时间str
            date_list = []
            date_list.append(cell)
            for modify_date_format in date_list:
                rowValues[1] = modify_date_format
            # print(rowValues)
            if rowValues[0] not in detail_dicts:
                detail_dicts[rowValues[0]] = [[rowValues[4]], [rowValues[7]], [rowValues[1]], [rowValues[8]]]
            else:
                detail_dicts[rowValues[0]][0].append(rowValues[4])
                detail_dicts[rowValues[0]][1].append(rowValues[7])
                detail_dicts[rowValues[0]][2].append(rowValues[1])
                detail_dicts[rowValues[0]][3].append(rowValues[8])
        # print(detail_dicts)
        return detail_dicts

    # 读取库存表，把需要的字段存入字典
    def read_inventory_table(self):
        inventory_dicts = {}
        read_xls = xlrd.open_workbook(self.inventory_table_path)
        xls_sheet = read_xls.sheets()[0]
        row_len = xls_sheet.nrows
        for inventory_row in range(1, row_len):
            rowValues = xls_sheet.row_values(inventory_row)  # 某一行数据
            inventory_dicts[rowValues[0]] = int(rowValues[5])
        # print(inventory_dicts)
        return inventory_dicts

    def select_commodity(self):
        detail = self.read_detail_table()
        inventory = self.read_inventory_table()
        can_be_shipped = []
        # print(detail)
        for order, sku in detail.items():
            # 判断一个订单中是否有缺货商品
            print(order)
            print(detail[order])
            if "是" in sku[1]:
                for i, j in enumerate(sku[1]):
                    # print(sku[1][i])
                    out_of_stock = sku[0][i]
                    if sku[1][i] == "是":
                        print('订单号：{0}   SKU：{1}   马帮导出表格显示为缺货中'.format(order, out_of_stock))
                        print("我马上去库存表查询")
                        # 判断缺货的sku在库存表是否有库存，有库存则把sku对应库存-1
                        if out_of_stock in inventory and inventory[out_of_stock] > 0:
                            inventory[out_of_stock] = inventory[out_of_stock] - 1
                            print(f"查到了，{out_of_stock} 有库存")
                            print(f"{out_of_stock} 发货后库存量还剩{inventory[out_of_stock]}件")
                            sku[1][i] = "否"

                            # 缺货的sku查完库存表后再次判断一个订单中是否还有缺货sku, 没有则发货
                            if "是" not in sku[1]:
                                print(detail[order])
                                print(f'{order} 可以发货了' + '\n')
                                can_be_shipped.append(order)
                            else:
                                print(f"这里是不能发货的{order}")

                        else :
                            print(f"{order}  {out_of_stock}---暂时无库存, 不能发货" + '\n')
                    else:
                        print(f"{order} SKU：{out_of_stock} 马帮导出不缺货")
            else:
                print(f"订单号：{order} 订单中首页sku都不缺货可以发货" + '\n')
                can_be_shipped.append(order)
        with open('./shop.txt', 'w', encoding='utf8') as fp:
            for orders in can_be_shipped:
                fp.write(orders + '\n')
        print(can_be_shipped)
        return detail
        # print(inventory)

    def split_order(self):
        second_detail = self.select_commodity()


    def run(self):
        dis.date_sort()
        dis.split_order()


dis = Distribution()
dis.run()
