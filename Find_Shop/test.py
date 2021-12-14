import xlrd
import pandas as pd
import os
import PySimpleGUI as sg
from datetime import datetime
# from xlrd import xldate_as_tuple
from dateutil.parser import parse


class Distribution():

    def __init__(self):
        self.detail_table_path = r"D:\Verification\order.xls"
        self.inventory_table_path = r"D:\Verification\一部库存.xlsx"
        self.date_sort_table_path = r"D:\Verification\After_Treatment\排序后的表.xlsx"
        self.can_be_shipped_path = r"D:\Verification\can_be_shipped.txt"
        self.split_order_path = r"D:\Verification\split_order.txt"


    # def PySimpleGUI_choose_file(self):
    #     file_address = sg.popup_get_file('请选择你要读取的表格文件：')
    #     return file_address

    def file_address(self):
        if os.path.exists(self.date_sort_table_path):
            os.remove(self.date_sort_table_path)

    def date_sort(self):
        detail_table_path = self.detail_table_path
        df = pd.read_excel(detail_table_path, index_col=0)
        data_save = df.sort_values('付款时间', ascending=True)
        select = data_save.loc[data_save['商品状态'] == "正常销售"]
        self.file_address()
        select.to_excel(self.date_sort_table_path)

    # 读取马帮下载的表格，把需要的字段存入字典
    def read_detail_table(self):
        detail_dicts = {}
        read_xls = xlrd.open_workbook(self.date_sort_table_path)
        xls_sheet = read_xls.sheets()[0]
        row_len = xls_sheet.nrows
        for detail_row in range(1, row_len):
            rowValues = xls_sheet.row_values(detail_row)  # 某一行数据
            # print(rowValues)
            # print(type(rowValues[1]))
            # date = datetime(*xldate_as_tuple(rowValues[1], 0))
            # cell = date.strftime('%Y/%m/%d %H:%M:%S')   # 转成时间str
            # date_list = []
            # date_list.append(cell)
            # for modify_date_format in date_list:
            #     rowValues[1] = modify_date_format
            # print(rowValues)
            if rowValues[0] not in detail_dicts:
                detail_dicts[rowValues[0]] = [[rowValues[4]], [rowValues[7]], [rowValues[1]], [rowValues[8]],
                                              [rowValues[9]], [rowValues[5]],]
            else:
                detail_dicts[rowValues[0]][0].append(rowValues[4])
                detail_dicts[rowValues[0]][1].append(rowValues[7])
                detail_dicts[rowValues[0]][2].append(rowValues[1])
                detail_dicts[rowValues[0]][3].append(rowValues[8])
                detail_dicts[rowValues[0]][4].append(rowValues[9])
                detail_dicts[rowValues[0]][5].append(rowValues[5])
        print(detail_dicts)
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
        print(inventory_dicts)
        return inventory_dicts

    def select_commodity(self):
        detail = self.read_detail_table()
        inventory = self.read_inventory_table()
        can_be_shipped = []
        split_order = []
        # print(detail)
        for order, sku in detail.items():
            # print(order)
            # print(detail[order])
            # 判断一个订单中是否有缺货商品
            if "是" in sku[1] :
                for i, j in enumerate(sku[1]):
                    # print(sku[1][i])
                    out_of_stock = sku[0][i]
                    if sku[1][i] == "是":
                        print('订单号：{0}   SKU：{1}   马帮导出表格显示为缺货'.format(order, out_of_stock))
                        print("我马上去库存表查询")
                        # 判断缺货的sku在库存表是否有库存，有库存则把sku对应库存-1
                        if out_of_stock in inventory and inventory[out_of_stock] >= int(sku[5][i]):
                            print(int(sku[5][i]))
                            inventory[out_of_stock] = inventory[out_of_stock] - int(sku[5][i])
                            print(f"查到了，{out_of_stock} 有库存")
                            print(f"{out_of_stock} 发货后库存量还剩{inventory[out_of_stock]}件")
                            sku[1][i] = "否"
                        elif out_of_stock in inventory and inventory[out_of_stock] < int(sku[5][i]):
                            print("库存量小于配送件数")
                        else:
                            print(f"{order}  {out_of_stock}---暂时无库存")
                    else:
                        print(f"{order} SKU：{out_of_stock} 马帮导出不缺货")
                # 缺货的sku查完库存表后再次判断一个订单中是否还有缺货sku, 没有则发货
                if "是" not in sku[1]:
                    print(f'{order} 可以发货了' + '\n')
                    can_be_shipped.append(order)
                else:
                    print(f"{order} 不能发货，要去看下是否能拆分")
                    for delivery, payment_time, amount, remark in zip(detail[order][1], detail[order][2],
                                                                      detail[order][3], detail[order][4]):
                        now_time = datetime.now()
                        type_payment_time = parse(payment_time)
                        # print(type_payment_time)
                        time_difference = (now_time - type_payment_time).days
                        # print(time_difference)
                        # print(delivery, time_difference, amount)
                        # print(type(delivery), type(time_difference), type(amount))
                        if delivery == "否" and time_difference > 15 and amount >= 200 and remark != "拆分订单":
                            print('进入拆分订单操作')
                            split_order.append(order)
                            print(f"{order}可以拆分订单" + '\n')
                        else:
                            print("付款日期还没有超过15天， 金额没有大于200$，不能拆分订单" + '\n')
            else:
                print(f"订单号：{order} 订单中所有sku都不缺货可以发货" + '\n')
                can_be_shipped.append(order)
        with open(self.can_be_shipped_path, 'w', encoding='utf8') as fp:
            for orders in can_be_shipped:
                fp.write(orders + '\n')
        with open(self.split_order_path, 'w', encoding='utf8') as fp:
            for split_order_txt in split_order:
                fp.write(split_order_txt + '\n')
        # print(can_be_shipped)
        # print(split_order)
        print(inventory)

    def run(self):
        dis.date_sort()
        dis.select_commodity()


dis = Distribution()
dis.run()
