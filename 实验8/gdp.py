import urllib.request
import re
import pandas as pd
import time

def getdata(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent',' Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
    data=urllib.request.urlopen(req).read().decode('utf-8')
    str1=str(data)
    pat='''<tr>
                                    <td>(.*?)</td>
                                    <td>(.*?)</td>
                                    <td>(.*?)</td>
                                    <td>(.*?)\(.*?</td>
                                        <td>.*?</td>
                                </tr>'''
    result=re.compile(pat).findall(str1)
    return result

if __name__ == '__main__':
    for i in range(1968,2021):
        print('正在收集第%d年数据'%i)
        years = []
        rank=[]
        country=[]
        zhou=[]
        total=[]
        url='https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/'+str(i)+'.html'
        data=getdata(url)
        for j in range(0,len(data)):
            years.append(i)
            rank.append(data[j][0])
            country.append(data[j][1])
            zhou.append(data[j][2])
            total.append(data[j][3])
        dataframe = pd.DataFrame({'年数': years, '排名': rank, '国家/地区': country, '所在洲': zhou, 'GDP(美元计)': total})
        dataframe.to_csv(str(i)+"年世界GDP排名.csv", index=False, sep=',', encoding="utf_8_sig", mode="a+")
        print(i,'年数据收集完成')
        time.sleep(2)
