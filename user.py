# Импорт библиотеки requests
import requests
# Запрос GET (Отправка только URL без параметров)
response = requests.get("http://api.open-notify.org/astros.json")
# Вывод кода
print(response.status_code)
# Вывод ответа, полученного от сервера API
print(response.json())response = requests.get('https://api-server-name.com/methodname_get')
response = requests.get("https://api-server-name.com/methodname_get?param1=ford&param2=-234&param3=8267")
param_request = {'key1': 'value1', 'key2': 'value2'}  
response = requests.get('https://api-server-name.com/methodname_get', params=param_reques
url = 'https://api-server-name.com/methodname_get'  
headers = {'user-agent': 'my-app/0.0.1'}  
response = requests.get(url, headers=headers)
response = requests.post('https://api-server-name.com/methodname_post', data = {'key':'value'})
param_tuples = [('param1', 'value1'), ('param1', 'value2')]  
response = requests.post('https://api-server-name.com/methodname_post', data=param_tuples)
param_dict = {'param': ['value1', 'value2']}  
response = requests.post('https://api-server-name.com/methodname_post', data=payload_dict) 
import json  
url = 'https://api-server-name.com/methodname_post'  
param_dict = {'param': 'data'}  
response = requests.post(url, data=json.dumps(param_dict))
# Импорт библиотеки requests
import requests
# Запрос GET (Отправка только URL без параметров)
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
# Вывод ответа, через пользовательскую функцию jprint
print("response:\n{}\n\n".format(response))
print("response.url:\n{}\n\n".format(response.url))                 #Посмотреть формат URL (с параметрами)
print("response.headers:\n{}\n\n".format(response.headers))         #Header of the request
print("response.status_code:\n{}\n\n".format(response.status_code)) #Получить код ответа
print("response.text:\n{}\n\n".format(response.text))               #Text Output
print("response.encoding:\n{}\n\n".format(response.encoding))       #Узнать, какую кодировку использует Requests
print("response.content:\n{}\n\n".format(response.content))         #В бинарном виде
print("response.json():\n{}\n\n".format(response.json()))           #JSON
# Импортируем библиотеку requests 
import requests 
  
# Адрес api метода для запроса get 
url_param = "https://api-metrika.yandex.net/stat/v1/data"
# Задаем параметры для API
api_param = {
    "ids":"5251515",
    "metrics":"ym:s:users,ym:s:visits,ym:s:pageviews,ym:s:bounceRate,ym:s:pageDepth,ym:s:avgVisitDurationSeconds",
    "dimensions":"ym:s:date,ym:s:<attribution>TrafficSource,ym:s:<attribution>SourceEngine,ym:s:gender",
    "date1":"10daysAgo",
    "date2":"yesterday",
    "sort":"ym:s:date",
    "accuracy":"full",
    "limit":5
    }
header_params = {
    'GET': '/management/v1/counters HTTP/1.1',
    'Host': 'api-metrika.yandex.net',
    'Authorization': 'OAuth AgAAlkjlkjKAa976ZB-rXh-t-ookfJJcMP979ZU0',
    'Content-Type': 'application/x-yametrika+json'
    }
# Отправляем get request (запрос GET)
response = requests.get(
    url_param,
    params=api_param,
    headers=header_params
)
result = response.json()
query = result['query']
data = result['data']
print(query)
print('======================')
print(data)
# Импортируем библиотеку requests 
import requests
import pandas as pd 
import xml.etree.ElementTree as et 
v_date = '16.04.2020'
# Адрес api метода для запроса get
url = 'https://www.cbr.ru/scripts/XML_daily.asp'
params = {
    'date_req': v_date
}
# Отправляем get request (запрос GET)
response = requests.get(url, params)
tree = et.ElementTree(et.fromstring(response.text))
root = tree.getroot()
df_cols = ["date", "numcode", "charcode", "nominal", "name", "value"]
rows = []
for node in root:
    s_numcode = node.find("NumCode").text if node is not None else None
    s_charcode = node.find("CharCode").text if node is not None else None
    s_nominal = node.find("Nominal").text if node is not None else None
    s_name = node.find("Name").text if node is not None else None
    s_value = node.find("Value").text if node is not None else None
    
    rows.append({"date": v_date, "numcode": s_numcode,
                 "charcode": s_charcode, "nominal": s_nominal,
                 "name": s_name, "value": s_value})
df = pd.DataFrame(rows, columns = df_cols)
print(df.head())