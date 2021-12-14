import xlrd
import pandas as pd
import os
import re
import PySimpleGUI as sg

from datetime import datetime
from xlrd import xldate_as_tuple
from dateutil.parser import parse


class Distribution():

    def __init__(self):
        self.date_sort_table_path = "/排序后的表.xlsx"
        self.can_be_shipped_path = "/可发货订单.txt"
        self.split_order_path = "/拆分订单.txt"

    # 用PySimpleGpUI简单界面画
    def pySimpleGpUI_show(self):
        menu_def = [['&Help', [
                               '&1.数据和库存表按模板下载(马帮的数据不要合并下载,按test模板下载)'
                               ]]]
        layout = [
            [sg.Menu(menu_def)],
            [sg.Button('选择下载的源文件'), sg.Text(size=(40, 1), key='key_first', font=("Helvetica", 12))],
            [sg.Button('选择库存表'), sg.Text(size=(40, 1), key='key_second', font=("Helvetica", 12))],
            [sg.Button('选择处理完后文件保存地址'), sg.Text(size=(40, 1), key='key_third', font=("Helvetica", 12))],
            [sg.Text('金额($)'), sg.InputText(key="money", size=(5, 20)), sg.Text('时间天数'),
             sg.InputText(key="date_input_text", size=(5, 20))],
            [sg.Button('开始'), sg.Cancel('退出')],
        ]
        window = sg.Window('My_Work', layout,
                           no_titlebar=True,
                           font=("Helvetica", 14),
                           default_element_size=(60, 1),
                           grab_anywhere=True
                           )

        # 判断输入金额是否为正整数
        def is_number(num):
            pattern = re.compile(r'^[1-9]\d*$')
            result = pattern.match(num)
            if result:
                return True
            else:
                return False

        while True:
            event, values = window.read()
            if event in (None, '退出'):
                break
            elif event == '选择下载的源文件':
                self.detail_file_address = sg.popup_get_file('读取的表格：')
                window['key_first'].update(self.detail_file_address)
            elif event == '选择库存表':
                self.stock_file_address = sg.popup_get_file('选取库存表：')
                window['key_second'].update(self.stock_file_address)
            elif event == '选择处理完后文件保存地址':
                self.save_file_address = sg.popup_get_folder('请选择你的文件夹：')
                window['key_third'].update(self.save_file_address)
            elif event == '开始':
                while True:
                    try:
                        if  self.detail_file_address != None and self.stock_file_address != None \
                                and self.save_file_address != None and is_number(values["money"]) \
                                and is_number(values["date_input_text"]):
                            self.order_money = int(values["money"])
                            self.order_date = int(values["date_input_text"])
                            self.run()
                            sg.popup(f'已处理完毕,保存至{self.save_file_address}', text_color='#01a19d', font=("楷体", 11),
                                     background_color='#ffffff')
                            break
                        else:
                            sg.popup('InputError：金额输入正整数', text_color='#01a19d', font=("楷体", 12),
                                     background_color='#ffffff')
                            break
                    except AttributeError:
                        sg.popup('FileError：检查地址是否全部输入', text_color='#01a19d', font=("楷体", 12),
                                 background_color='#ffffff')
                        break
        window.close()

    # 判断文件是否存在
    def file_address(self):
        if os.path.exists(f'{self.save_file_address}{self.date_sort_table_path}'):
            os.remove(f'{self.save_file_address}{self.date_sort_table_path}')

    # 读取原表进行时间排序，筛选正常销售订单
    def date_sort(self):
        detail_table_path = self.detail_file_address
        df = pd.read_excel(detail_table_path, index_col=0)
        data_save = df.sort_values('付款时间', ascending=True)
        select = data_save.loc[data_save['商品状态'] == "正常销售"]
        self.file_address()
        select.to_excel(f'{self.save_file_address}{self.date_sort_table_path}')

    # 读取转换后的表格，把需要的字段存入字典
    def read_detail_table(self):
        detail_dicts = {}
        read_xls = xlrd.open_workbook(f'{self.save_file_address}{self.date_sort_table_path}')
        xls_sheet = read_xls.sheets()[0]
        row_len = xls_sheet.nrows
        for detail_row in range(1, row_len):
            rowValues = xls_sheet.row_values(detail_row)  # 某一行数据
            if rowValues[0] not in detail_dicts:
                detail_dicts[rowValues[0]] = [[rowValues[4]], [rowValues[7]], [rowValues[1]], [rowValues[8]],
                                              [rowValues[9]], [rowValues[5]],]
            else:
                detail_dicts[rowValues[0]][0].append(rowValues[4])   # sku
                detail_dicts[rowValues[0]][1].append(rowValues[7])   # 商品是否缺货
                detail_dicts[rowValues[0]][2].append(rowValues[1])   # 付款时间
                detail_dicts[rowValues[0]][3].append(rowValues[8])   # 金额
                detail_dicts[rowValues[0]][4].append(rowValues[9])   # 备注
                detail_dicts[rowValues[0]][5].append(rowValues[5])   # 商品状态
        return detail_dicts

    # 读取库存表，把需要的字段存入字典
    def read_inventory_table(self):
        inventory_dicts = {}
        read_xls = xlrd.open_workbook(self.stock_file_address)
        xls_sheet = read_xls.sheets()[0]
        row_len = xls_sheet.nrows
        for inventory_row in range(1, row_len):
            rowValues = xls_sheet.row_values(inventory_row)  # 某一行数据
            inventory_dicts[rowValues[0]] = int(rowValues[5])
        return inventory_dicts

    def select_commodity(self):
        detail = self.read_detail_table()
        inventory = self.read_inventory_table()
        can_be_shipped = []
        split_order = []
        append_dicts = {}
        for order, sku in detail.items():
            # 判断一个订单中是否有缺货商品
            if "是" in sku[1] :
                count = 0
                for i, j in enumerate(sku[1]):
                    # print(sku[1][i])
                    out_of_stock = sku[0][i]
                    if sku[1][i] == "是":
                        print('{0} {1}  马帮导出表格显示为缺货'.format(order, out_of_stock))
                        print("我马上去库存表查询")
                        # 判断缺货的sku在库存表是否有库存
                        if out_of_stock in inventory and inventory[out_of_stock] >= int(sku[5][i]):
                            print(f"查到了，{out_of_stock} 有库存")
                            if order not in append_dicts:
                                append_dicts[order] = [[out_of_stock], [sku[1][i]], [sku[5][i]]]
                            else:
                                append_dicts[order][0].append(out_of_stock)
                                append_dicts[order][1].append(sku[1][i])
                                append_dicts[order][2].append(int(sku[5][i]))
                            append_dicts[order][1][count] = "否"
                            count += 1
                        elif out_of_stock in inventory and inventory[out_of_stock] < int(sku[5][i]):
                            print("库存不足以配送当前sku")
                            if order not in append_dicts:
                                append_dicts[order] = [[out_of_stock], [sku[1][i]], [sku[5][i]]]
                            else:
                                append_dicts[order][0].append(out_of_stock)
                                append_dicts[order][1].append(sku[1][i])
                                append_dicts[order][2].append(int(sku[5][i]))
                            count += 1
                        else:
                            print("无库存")
                            if order not in append_dicts:
                                append_dicts[order] = [[out_of_stock], [sku[1][i]], [sku[5][i]]]
                            else:
                                append_dicts[order][0].append(out_of_stock)
                                append_dicts[order][1].append(sku[1][i])
                                append_dicts[order][2].append(int(sku[5][i]))
                            count += 1
                    else:
                        print(f"{order} {out_of_stock} 马帮导出不缺货")
                # 缺货的sku查完库存表后再次判断一个订单中是否还有缺货sku, 没有则发货
                if "是" not in append_dicts[order][1]:
                    print(f'{order} 可以发货了')
                    for counts in range(0, count):
                        # 符合发货需要减掉对应库存
                        inventory[append_dicts[order][0][counts]] = inventory[append_dicts[order][0][counts]] \
                                                                    - int(append_dicts[order][2][counts])
                        print(f"{append_dicts[order][0][counts]}"
                              f" 发货后库存量还剩{inventory[append_dicts[order][0][counts]]}件")
                    can_be_shipped.append(order)
                else:
                    print(f"{order} 不能发货，要去看下是否能拆分")
                    for delivery, payment_time, amount, remark in zip(detail[order][1], detail[order][2],
                                                                      detail[order][3], detail[order][4]):
                        now_time = datetime.now()
                        # 需要捕获一个TypeError异常，防止原表日期格式被改动出错
                        try:
                            type_payment_time = parse(payment_time)
                        except TypeError:
                            date = datetime(*xldate_as_tuple(payment_time, 0))
                            cell = date.strftime('%Y/%m/%d %H:%M:%S')   # 转成时间str
                            type_payment_time = parse(cell)
                        time_difference = (now_time - type_payment_time).days
                        # 这里有break，continue因为只要订单中任意sku满足条件就能拆分订单，后期可能会改动
                        if delivery == "否" and time_difference >= self.order_date \
                                and amount >= self.order_money and remark != "拆分订单":
                            print('有订单+sku满足条件已进入拆分订单操作ing')
                            split_order.append(order)
                            print(f"{order} 可以拆分订单" + '\n')
                            break
                        else:
                            print(f"付款日期还没有超过{self.order_date}天， 金额没有大于{self.order_money}$，不能拆分订单"
                                  + '\n')
                            continue
            else:
                print(f"订单号：{order} 订单中所有sku都不缺货可以发货" + '\n')
                can_be_shipped.append(order)

        with open(f'{self.save_file_address}{self.can_be_shipped_path}', 'w', encoding='utf8') as fp1:
            for orders in can_be_shipped:
                fp1.write(orders + '\n')
        with open(f'{self.save_file_address}{self.split_order_path}', 'w', encoding='utf8') as fp2:
            for split_order_txt in split_order:
                fp2.write(split_order_txt + '\n')

    def run(self):
        dis.date_sort()
        dis.select_commodity()


dis = Distribution()
dis.pySimpleGpUI_show()
