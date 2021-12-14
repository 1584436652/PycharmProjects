'''
@Time    : 2021/10/9 15:44
@Author  : LKT
@FileName: requests_login_paypal.py
'''
import json
import requests
import re
import time

from mail import send_mail
# from retry import retry

s = requests.session()

class PayPal_Login(object):

    def __init__(self):
        # 登录页面
        self.login_url = 'https://www.sandbox.paypal.com/signin'
        # 报告url
        self.report_url = 'https://business.sandbox.paypal.com/merchantdata/reportHome'
        # 创建交易记录报告url
        self.create_report_deal = 'https://business.sandbox.paypal.com/merchantdata/dlog'
        # 创建事件报告url
        self.create_report_cases = 'https://business.sandbox.paypal.com/merchantdata/ddr'
        # 下载文件url
        self.download_url = 'https://business.sandbox.paypal.com/merchantdata/getdlogreport?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
        }
        # self.proxies = {
        #     'https:': 'https:117.94.222.205:3256'
        # }

    # 读取config.json
    @property
    def config(self):
        with open('config.json', 'r') as fp:
            dicts = fp.read().encode(encoding='gbk').decode(encoding='utf-8')
            message = json.loads(dicts)
            return message

    # 生成登录csrf
    def get_login_csrf(self):
        print("获取登录_csrf")
        response = s.get(self.login_url, headers = self.headers).text
        csrf = re.findall(r'data-csrf-token="(.*?)"data-nonce=', response, re.S)[0]
        return csrf

    # 登录
    def login(self, csrf, login_email, login_password):
        data = {
            '_csrf': csrf,
            'login_email': login_email,
            'login_password': login_password,
            # 'partyIdHash':'4d917d90cb220ad189fdec9434d871be11167a2bb5982c87da595c529ed4b02d',
            'splitLoginContext': 'inputPassword',
            'intent':'signin',
            'isCookiedHybridEmail': 'true',
            'phoneCode': 'US +1',
            'locale.x': 'zh_XC',
            'processSignin': 'main'
        }
        s.post(self.login_url, headers=self.headers, data=data)

    # 获取创建报告的csrf
    def get_report_csrf(self):
        print("获取报告_csrf")
        response = s.get(self.report_url, headers=self.headers)
        result = response.text
        csrf = re.findall(r'data-csrf=(.*?); data-token=', result, re.S)[0]
        # {{’&#x2B;‘: '+'}, {’&#x3D‘: '='}, {’&#x2F;‘: '/'}}
        csrf_replace = csrf.replace('&#x2B;', '+').replace('&#x3D', '=').replace('&#x2F;', '/')
        print(csrf_replace)
        return csrf_replace

    # 发请求创建报告
    def create_report(self, csrf, create_start_date, create_end_date):
        # 创建交易记录报告的参数
        data_csv = {
            '_csrf': csrf,
            'name': 'DLOGTEMPLATE',
            'start_date': create_start_date,
            'end_date': create_end_date,
            'file_format': 'CSV',
            'delivery_channel': 'WEB',
            'filters': 'BALANCE_IMPACTING',
        }
        # 创建事件报告的参数
        data_Xlsx = {
            csrf: csrf,
            'name': 'ADHOCDISPUTE',
            'start_date': create_start_date,
            'end_date': create_end_date,
            'file_format': 'XLSX',
            'delivery_channel': 'WEB',
            'schedule': 'RUNONCE',
            'filters': 'DISPUTES_CHARGEBACKS',
            'case_status': 'all_cases',
        }
        # 交易记录请求
        s.post(self.create_report_deal, headers=self.headers, data=data_csv)
        time.sleep(3)
        # 事件报告请求
        s.post(self.create_report_cases, headers=self.headers, data=data_Xlsx)

    # 下载交易记录
    # @retry(tries=2)
    def download_csv(self, start_date_csv, end_date_csv):
        print('获取交易记录')
        params_csv = {
            'reportName': 'DLOGTEMPLATEB_{0}_{1}_O_01.CSV'.format(start_date_csv, end_date_csv),
            'filecount': 1,
            'file_format': 'CSV',
            'final_name': 'DLOGTEMPLATEB_{0}_{1}_O'.format(start_date_csv, end_date_csv)
        }
        res_csv = s.get(self.download_url, headers=self.headers, params=params_csv)
        print(res_csv.text)
        filename_csv = f'交易记录：{self.config["name"]}_{end_date_csv[0:9]}.CSV'
        with open(filename_csv, 'w', encoding='utf-8-sig') as fp_csv:
            fp_csv.write(res_csv.text)
        return filename_csv

    # 下载事件报告
    def download_Xlsx(self, start_date_Xlxs, end_date_Xlxs):
        print('获取事件报告')
        params_Xlxs = {
            'reportName': 'ADHOCDISPUTEB_{0}_{1}_O_01.XLSX'.format(start_date_Xlxs, end_date_Xlxs),
            'filecount': 1,
            'file_format': 'XLSX',
            'final_name': 'ADHOCDISPUTEB_{0}_{1}_O'.format(start_date_Xlxs, end_date_Xlxs)
        }
        res_Xlsx = s.get(self.download_url, headers=self.headers, params=params_Xlxs)
        result_content = res_Xlsx.content
        print(result_content)
        filename_XLSX =  f'事件：{self.config["name"]}_{end_date_Xlxs[0:9]}.XLSX'
        with open(filename_XLSX, 'wb') as fp_xlsx:
            fp_xlsx.write(result_content)
        return filename_XLSX

    def run(self):
        csrf = self.get_login_csrf()
        print(csrf)
        self.login(csrf, self.config["login_email"], self.config["login_password"])
        report_csrf = self.get_report_csrf()
        self.create_report(report_csrf, self.config["start_date"], self.config["end_date"])
        print('发送请求ing')
        time.sleep(60)
        filename_csv = self.download_csv(self.config["start_date"], self.config["end_date"])
        filename_Xlsx =self.download_Xlsx(self.config["start_date"], self.config["end_date"])
        # 用于邮件标题
        subject = self.config["name"]
        send_mail(subject, filename_csv, filename_Xlsx)


if __name__ == '__main__':
    pay = PayPal_Login()
    pay.run()
