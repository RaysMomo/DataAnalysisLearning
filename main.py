import requests
# need to hack the js
url = 'http://43.248.49.97/queryData/downloadQueryData'

headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37",
    # "Cookie": "9CKCOkIaqzqES=55v7jGO2wRaEKbgJOADk8kqBsiZiEeZLmTLWKae8uR3CS3g5oXTgaFUwB1vHNQNBZG8X.mihO_JGOAAOa7STniq; JSESSIONID=MQzLLF4lXoxy3zVMoTkzA8sZV_5aLEoXZW_An6-3cBcKy2O_cEdh!239420054; 9CKCOkIaqzqET=5FMgw.Kb5oF0xcAfaaPiLEAme5AWO._uS9v.zaVLN.RIOKCBG4J9J2tqJxib0h9.KBqIwR1Z3u_pttOlP4lcj37rUwKIPrSwzGvgia52b3XSU_NYI4338CJm2WB.BaqruWjNsCBkgfugzO2f5VhybYK3Yv95gB58wQ6cG8SFgeYF9Twq19JA5lOGHhQSU9eLi0.H.XyZz2jNrKBWxYqhaI5lLmG1yXVWPL9mcQxnD5aWakua5ktYD97lAFF8Ud_Gok2r4MySAsekxgeo99Pa8OOjuDf7T4OJkBVndjn88eiJSoX4k90I9Afs3A_9x.omoW",
    # "Referer": "http://43.248.49.97/queryData/queryDataList?pageNum=1&codeLength=8&currentStartTime=201910&currentEndTime=202104&currentDateBySource=202104&selectTableState=1&orderType=CODE%20ASC%20DEFAULT&iEType=1&currencyType=rmb&year=2021&startMonth=4&endMonth=4&monthFlag=1&outerField1=CODE_TS&outerField2=ORIGIN_COUNTRY&outerField3=TRADE_MODE&outerField4=TRADE_CO_PORT&outerValue1=30019010&outerValue2=133&outerValue3=15&outerValue4=37",
    # "Upgrade-Insecure-Requests": "1",
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Content-Length": "343",
    # "Content-Type": "application/x-www-form-urlencoded",

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "343",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "9CKCOkIaqzqES=55v7jGO2wRaEKbgJOADk8kqBsiZiEeZLmTLWKae8uR3CS3g5oXTgaFUwB1vHNQNBZG8X.mihO_JGOAAOa7STniq; JSESSIONID=MQzLLF4lXoxy3zVMoTkzA8sZV_5aLEoXZW_An6-3cBcKy2O_cEdh!239420054; 9CKCOkIaqzqET=5FMgZ2Kb5HxAxcAfaa.YCXAF1iV1doJA7d2.1OydTENTApYsR7bV03dyneHilbS21coHaunUhtaDi.V8oL03M623HxmIAGBgbb_.8iNq8Fyi2fofq7va_a4FGC7nC3OQsXkGOGt8A.d.JOwSPMGq0OmpR0nt7UaTKt.7.S5x1rgOGDdDQRHVnzldmRsgKAZC2QTXTS8wHJckryYcLv0QeL9MIT7BVi0t0pMBsmiGWACZjYoHo99rWLIPRQu4dFs1SZh3ba5wBV2Jtgq2m6KYWJwDiJbj3iE6mSgs2K0uQLwojK_8p3VP1t4BYBx_KGUetl",
    "Host": "43.248.49.97",
    "Origin": "http://43.248.49.97",
    "Referer": "http://43.248.49.97/queryData/queryDataList?pageNum=1&codeLength=8&currentStartTime=201910&currentEndTime=202104&currentDateBySource=202104&selectTableState=1&orderType=CODE%20ASC%20DEFAULT&iEType=1&currencyType=rmb&year=2021&startMonth=4&endMonth=4&monthFlag=1&outerField1=CODE_TS&outerField2=ORIGIN_COUNTRY&outerField3=TRADE_MODE&outerField4=TRADE_CO_PORT&outerValue1=30019010&outerValue2=133&outerValue3=15&outerValue4=37",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37",
}

# dict = {
#     "browserType": "chrome",
#     "browserVersion": "90.0.4430.93",
#     "deviceType": "PC",
#     "loginName": "chenlei@cstonepharma.com",
#     "pwd": "Cstone@temp82",
# }

dict = {
    "pageSize": "10",
    "iEType": "1",
    "currencyType": "rmb",
    "year": "2021",
    "startMonth": "4",
    "endMonth": "4",
    "monthFlag": "1",
    "unitFlag": "true",
    "codeLength": "8",
    "outerField1": "CODE_TS",
    "outerField2": "ORIGIN_COUNTRY",
    "outerField3": "TRADE_MODE",
    "outerField4": "TRADE_CO_PORT",
    "outerValue1": "30019010",
    "outerValue2": "133",
    "outerValue3": "15",
    "outerValue4": "37",
    "orderType": "CODE ASC DEFAULT",
    "selectTableState": "3",
    "currentStartTime": "201910"
}

# try:
#     response = requests.post(headers=headers, url=url, json=dict)
#     if response.status_code == 200:
#         # json 参数 无需指定content-type
#         print('登录成功!')
#         start = response.text.find("token") + 8
#         end = response.text.find("dataSync") - 3
#         token = response.text[start:end].replace('\\/', '/')
#         # print(response.status_code)  # 获取响应状态码
#         # print(response.text[start:end].replace('\\/','/'))  # 获取响应消息
#         for file in files:
#             get_file_url = 'https://prod-tm.crmpower.cn/rest/download/{0}?token={1}'.format(file, token)
#             r = requests.get(get_file_url, stream=True)
#             # total_size = int(int(r.headers["Content-Length"])/1024+0.5)
#             f = open(r"D:\Spider\Customs Data\{0}.csv".format(file), "wb")
#             print('开始下载文件：{}'.format(file))
#             for chunk in tqdm(r.iter_content(chunk_size=1024)):
#                 f.write(chunk)
#             print('{0}下载完成!'.format(file))
#
# except requests.RequestException as e:
#     print('登录失败！')
#     print(str(e))

try:
    # r = requests.post(url=url, json=dict, headers=headers, stream=False)
    r = requests.post(url=url, json=dict, headers=headers, stream=False)
    print(r.status_code)
    # print(r.encoding)
    # encoding='utf-8'
    print(r)
    with open(r'D:\Spider\Customs Data\test.csv', 'wb') as f:
        if r.status_code == 200:
            for chunk in r.iter_content(chunk_size=512):  # todo iter_content循环读取信息写入，chunk_size设置文件大小
                f.write(chunk)

except requests.RequestException as e:
    print('访问失败！')
    print(str(e))