#!usr/bin/python
#coding:utf-8


from bs4 import BeautifulSoup
import requests
import random
import urllib.request

ip_list = []
proxy = []
def get_ip_list():
    url = "https://www.kuaidaili.com/free/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
    }

    for i in range(1,30):
        i = str(i)
        link = url + 'inha/' + i +'/'
        # print(link)
        data = requests.get(link,headers=headers).text
        soup = BeautifulSoup(data,'lxml')
        ips = soup.find_all('tr')

        for x in range(1,len(ips)):
            d = ips[x].find_all('td')
            ip = d[0].text
            port = d[1].text
            type = d[2].text
            addr = d[3].text
            shijian = d[-1].text
            ip_list.append(ip + ":" + port)

            # break


    #检验ip可用性，移除不可用ip

    for ip in ip_list:
       try:
           proxy_host = "http://" + ip
           proxy_temp = {"https":proxy_host}
           res = urllib.request.urlopen(url,proxies=proxy_temp).read()

       except Exception as e:
           ip_list.remove(ip)
           # print('此ip不能用：'+ ip)
       continue

    print("能用的IP有{}个".format(len(ip_list)))
    for i in ip_list:
        c = dict.fromkeys(['HTTP'], i)
        proxy.append(c)

    print(proxy)






if __name__ == "__main__":
    get_ip_list()

