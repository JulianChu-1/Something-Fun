import pandas as pd
import re

#def dataCleaning(num):
string1 = r"C:\Users\lenovo\Downloads\cdk ("
string2 = r").json"
json_info = ""
df = pd.DataFrame()
filename = r"C:\Users\lenovo\Downloads\cdk.json"
with open(filename,'r', encoding='utf-8') as file:
    json_info = file.read()
df_temp = pd.read_json(json_info)
df = df.append(df_temp,ignore_index = True)
for i in range(1,20):
    filename = string1 + str(i) + string2
    with open(filename,'r', encoding='utf-8') as file:
        json_info = file.read()
    df_temp = pd.read_json(json_info)
    df = df.append(df_temp,ignore_index = True)
lista = df['content'].to_list()
patterns = "：(.+)"
pattern = re.compile(patterns)
for i in range(len(lista)):
    lista[i] = pattern.findall(lista[i])
df['new'] = pd.DataFrame(lista)
del df['content']
df.to_excel("data.xlsx")