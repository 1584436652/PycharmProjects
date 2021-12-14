import pandas as pd


# data = pd.read_excel(r'C:\Users\Administrator\Desktop\20核单.xlsx')
# df = pd.DataFrame(data)
# print(df.to_string())
# print(df.info())
# for x in df.index:
#     print(x)

persons = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]
}

df = pd.DataFrame(persons)

df.drop_duplicates(inplace = True)
print(df)