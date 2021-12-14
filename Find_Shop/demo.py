import PySimpleGUI as sg
import re

def me():
   print('我是test_first')

def shou():
   menu_def = [['&Help', '&没有去进行逻辑判断，全部填完再“开始”']]
   layout = [
      [sg.Menu(menu_def)],
      [sg.Text('安能一部', size=(30,1), justification='center', font=("Helvetica", 18), text_color="#dc7487")],
      [sg.Button('选择下载的源文件')],
      [sg.Button('选择库存表')],
      [sg.Button('选择处理完后文件保存地址')],
      [sg.Text('金额($)'), sg.InputText(key="money",size=(5, 20))],
      [sg.Button('开始'), sg.Cancel('退出')],

            ]
   window = sg.Window('Everything bagel', layout,
                      no_titlebar=True,
                      font=("Helvetica", 14),
                      default_element_size=(60, 1),
                      grab_anywhere=True
                      )
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
         detail_file_address = sg.popup_get_file('请选择你要读取的表格：')
      elif event == '选择库存表':
         stock_file_address = sg.popup_get_file('请选择你要读取的表格：')
      elif event == '选择处理完后文件保存地址':
         save_file_address = sg.popup_get_folder('请选择你的文件：')
      elif event == '开始':
         while True:
            if is_number(values["money"]):
               me()
               break
            else:
               sg.popup('InputError：请输入正整数', text_color='#01a19d', font=("楷体", 12), background_color='#ffffff')
               break
   window.close()

shou()