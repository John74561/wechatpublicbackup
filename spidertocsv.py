

import json
from mimetypes import init
import requests
import time
import random
import yaml
import os
# with open("wechat.yaml", "rb") as fp:
#     config = yaml.load(fp,Loader=yaml.SafeLoader)
# cookie="pgv_pvid=9346132276; ua_id=aOf9WHAlcOvdWMt7AAAAAFOnimQqOC15INBS-X2ZwRk=; xid=3cfea1e528304d8de0a36a7314192c84; mm_lang=zh_CN; iip=0; tvfe_boss_uuid=4002b0aed5f4de98; RK=s4DpUv8vTX; ptcz=0dde81c5860da07846f9a522ef189766577cb84ae2b45e0e9bcf648077ea675c; o_cookie=1317648217; pac_uid=1_1317648217; fqm_pvqid=5bf7456e-fdce-4a60-981d-25d2eb65065c; rewardsn=; wxtokenkey=777; _qpsvr_localtk=0.953891846691262; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; pgv_info=ssid=s8019024690; uuid=28d3e544dd6d8d6f535465b75e98e275; wxuin=60831741041882; cert=BAaUxfWvtxQB6sUaBuofrDPQDqg4URI9; sig=h01532e32efaff0ce9d7fb94bdf8874735c2be3805188f81da3d01302ef6c42560b87f7c2eb60972d76; data_bizuin=3874843653; data_ticket=j2PXeYq/qyj/LEW7fEXeqLhsyeq21HCUL02qu+RrXxK16LMlva3SFcS5EmgtL7n7; master_key=uh/AmJ9dnCO5d7LqNLoDEP2ZWThrn4DB6hykhKrRonA=; master_user=gh_4a0145504686; master_sid=VkV4MTFwbHZzVF9RYXdOdVNfeUtBeUhDSGRUNEVlSXlucU1ONzBST2s5UU9haVVpM19VUnlVdFNtUWVBQkZ0NU1JV0JLMUdPcGI5Y3dJWG9aaFFUUXVxYmNnZTZCUkhrNWh4NjVWYndlSG9GTW5vRTZDSTFrTUhVUFA2dlJENHFrN0JaWTRPQnRIUUZrQWlR; master_ticket=3d6c1034d897a4223eff43738c8405fc; bizuin=3874843653; slave_user=gh_4a0145504686; slave_sid=QW9HZzhsNGJzTUlzVnBpeUVFaEZNRmYzVGllbG9ibEdHUU5kU3o1N1Z5TUpxRDB0c3NTNHFJNFBDZTgyaUNzRjJiOGhDWURoVFpvUksyazhNcFpxcjcxc3FVRl9yNWhNOVh3djhETkptT3lEdG94R1hoZE5MenhpbnpYTWpsZWFIWVAyN1ptcjh5STBvQVJI",
# useragent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
fakeid='MzA5MzM1MTQzNA==' 
token='886287982'
headers = {
    "Cookie": "pgv_pvid=9346132276; ua_id=aOf9WHAlcOvdWMt7AAAAAFOnimQqOC15INBS-X2ZwRk=; xid=3cfea1e528304d8de0a36a7314192c84; mm_lang=zh_CN; iip=0; tvfe_boss_uuid=4002b0aed5f4de98; RK=s4DpUv8vTX; ptcz=0dde81c5860da07846f9a522ef189766577cb84ae2b45e0e9bcf648077ea675c; o_cookie=1317648217; pac_uid=1_1317648217; fqm_pvqid=5bf7456e-fdce-4a60-981d-25d2eb65065c; rewardsn=; wxtokenkey=777; _qpsvr_localtk=0.953891846691262; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; pgv_info=ssid=s8019024690; uuid=28d3e544dd6d8d6f535465b75e98e275; wxuin=60831741041882; cert=BAaUxfWvtxQB6sUaBuofrDPQDqg4URI9; sig=h01532e32efaff0ce9d7fb94bdf8874735c2be3805188f81da3d01302ef6c42560b87f7c2eb60972d76; data_bizuin=3874843653; data_ticket=j2PXeYq/qyj/LEW7fEXeqLhsyeq21HCUL02qu+RrXxK16LMlva3SFcS5EmgtL7n7; master_key=uh/AmJ9dnCO5d7LqNLoDEP2ZWThrn4DB6hykhKrRonA=; master_user=gh_4a0145504686; master_sid=VkV4MTFwbHZzVF9RYXdOdVNfeUtBeUhDSGRUNEVlSXlucU1ONzBST2s5UU9haVVpM19VUnlVdFNtUWVBQkZ0NU1JV0JLMUdPcGI5Y3dJWG9aaFFUUXVxYmNnZTZCUkhrNWh4NjVWYndlSG9GTW5vRTZDSTFrTUhVUFA2dlJENHFrN0JaWTRPQnRIUUZrQWlR; master_ticket=3d6c1034d897a4223eff43738c8405fc; bizuin=3874843653; slave_user=gh_4a0145504686; slave_sid=QW9HZzhsNGJzTUlzVnBpeUVFaEZNRmYzVGllbG9ibEdHUU5kU3o1N1Z5TUpxRDB0c3NTNHFJNFBDZTgyaUNzRjJiOGhDWURoVFpvUksyazhNcFpxcjcxc3FVRl9yNWhNOVh3djhETkptT3lEdG94R1hoZE5MenhpbnpYTWpsZWFIWVAyN1ptcjh5STBvQVJI",
    "User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
}

# 请求参数
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
begin = "0"
count='5'
params = {
    "action": "list_ex",
    "begin": begin,
    "count": "5",
    "fakeid": fakeid,
    "type": "9",
    "token": token,
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1"
}
#result file
wechat_spider_json_file='wechat_spider_data.json'

# 获取当前json文件内容，计算已爬取的页数
if os.path.exists(wechat_spider_json_file):
    with open(wechat_spider_json_file, "r",encoding='utf-8') as file:
        wechat_app_msg_list = json.load(file)
        #print("之前已抓取{}页文章,将从下一页开始抓取".format(1+len(wechat_app_msg_list))
else:
    wechat_app_msg_list = []
i = len(wechat_app_msg_list)
print("之前已抓取{}页文章,将从下一页开始抓取".format(i))
max=1
# 使用while循环获取, 直至抓取完成
# while i<max:
while True:
    init=i*int(count)
    params['begin']=str(init)
    # 随机暂停几秒，避免过快的请求导致过快的被查到
    num=random.randint(1,10)
    print("等待{0}秒，准备抓取第{1}页，每页{2}篇".format(num, (i+1), count))
    time.sleep(num)
    # 执行抓取接口
    resp = requests.get(url, headers=headers, params = params)
    # 微信流量控制, 退出
    if resp.json()['base_resp']['ret'] == 200013:
        print("frequencey control, stop at {}".format(str(begin)))
        time.sleep(3600)
        continue
    print(resp.json()['app_msg_list'])
    # 如果返回的内容中为空则结束
    if len(resp.json()['app_msg_list']) == 0:
        print("all ariticle parsed")
        break

    # 抓取成功，json格式保存返回的接口信息
    wechat_app_msg_list.append(resp.json())     
    print("抓取第{0}页成功，每页{1}篇, 共抓取了{2}篇".format((i+1), count, (i+1)*int(count)))
    

    # 翻页
    i += 1    
# json格式保存结果至文件
with open(wechat_spider_json_file, "w",encoding='utf-8') as file:
    file.write(json.dumps(wechat_app_msg_list, indent=2, ensure_ascii=False))
# 文章的id，标题，创建时间，链接写入csv文件
for item in resp.json()['app_msg_list']:    
 
    arti_create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item['create_time']))
    arti_info = '"{}","{}","{}","{}"'.format(str(item["aid"]), str(arti_create_time), item['link'], item['title'])
    with open("app_msg_list.csv", "a", encoding='utf-8-sig') as f:
        f.write(arti_info+'\n')         
print("第{0}页文章的id，标题，创建时间，链接写入csv文件app_msg_list.csv成功".format(i+1))

