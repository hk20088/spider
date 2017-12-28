#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='Leon Hu'

import requests
from bs4 import BeautifulSoup

# proxy_url ='http://www.xicidaili.com/wt/{0}' # 国内http代理
proxy_url ='http://www.xicidaili.com/wn/{0}' # 国内https代理
testip_url = 'http://ip.chinaz.com/getip.aspx'  # 测试IP网站

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}

def getips():
    # 从西刺获取免费代理IP，每页100个，这里取3页
    for i in range(1, 4):
        res = requests.get(proxy_url.format(i), headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        ips = soup.find_all('tr')

        for i in range(1, len(ips)):
            tr = ips[i]
            tds = tr.find_all('td')
            ip = tds[1].text + '\t' + tds[2].text + '\n'
            with open('f:/ipss.txt', 'a') as f:
                f.write(ip)


# 将获取到的IP封装成代理IP
def fillips(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    proxys = []
    for i in range(0, len(lines)):
        ip = lines[i].strip('\n').split('\t')
        proxy_host_http = 'http://' + ip[0] + ':' + ip[1]
        proxy_host_https = 'https://' + ip[0] + ':' + ip[1]
        proxy_temp = {'http':proxy_host_http,'https':proxy_host_https}
        proxys.append(proxy_temp)
    return proxys;




# 测试获取到的代理IP是否可用，将可用的IP写到新文件中
def testips(proxys):
    for i in range(0,len(proxys)):
        try:

            # proxies在访问http网站时用http设置，访问https网站时用https设置。否则代理不会生效
            res = requests.get(testip_url, proxies=proxys[i], timeout =10)
            if res.status_code == requests.codes.ok:
                print(res.text)
                with open('f:/availableIps.txt', 'a') as f:
                    f.write(str(proxys[i])+'\n')

        except Exception:
            print(i ,'代理不可用')
            continue



if __name__ == '__main__':
    getips()
    testips(fillips('f:/ips.txt'))


