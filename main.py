

import json
import requests
import time
import random
import yaml
import os
with open("wechat.yaml", "r") as file:
    file_data = file.read()
config = yaml.safe_load(file_data) 

headers = {
    "Cookie": config['cookie'],
    "User-Agent": config['user-agent'] 
}

# 请求参数
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
begin = "0"
params = {
    "action": "list_ex",
    "begin": begin,
    "count": "5",
    "fakeid": config['fakeid'],
    "type": "9",
    "token": config['token'],
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1"
}

# 存放结果
app_msg_list = []
# 在不知道公众号有多少文章的情况下，使用while语句
# 也方便重新运行时设置页数
with open("app_msg_list.csv", "w",encoding='utf-8') as file:
    file.write("文章标识符aid,标题title,链接url,时间time\n")
i = 0
while True:
    begin = i * 5
    params["begin"] = str(begin)
    # 随机暂停几秒，避免过快的请求导致过快的被查到
    time.sleep(random.randint(1,10))
    resp = requests.get(url, headers=headers, params = params, verify=False)
    # 微信流量控制, 退出
    if resp.json()['base_resp']['ret'] == 200013:
        print("frequencey control, stop at {}".format(str(begin)))
        time.sleep(3600)
        continue
    
    # 如果返回的内容中为空则结束
    if len(resp.json()['app_msg_list']) == 0:
        print("all ariticle parsed")
        break
        
    msg = resp.json()
    if "app_msg_list" in msg:
        for item in msg["app_msg_list"]:
            info = '"{}","{}","{}","{}"'.format(str(item["aid"]), item['title'], item['link'], str(item['create_time']))
            with open("app_msg_list.csv", "a",encoding='utf-8') as f:
                f.write(info+'\n')
        print(f"第{i}页爬取成功\n")
        print("\n".join(info.split(",")))
        print("\n\n---------------------------------------------------------------------------------\n")

    # 翻页
    i += 1    