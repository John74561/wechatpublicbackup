# -*- coding: utf-8 -*-
from venv import create
import requests
import time
import random
headers = {
    "cookie": "pgv_pvid=9346132276; ua_id=aOf9WHAlcOvdWMt7AAAAAFOnimQqOC15INBS-X2ZwRk=; xid=3cfea1e528304d8de0a36a7314192c84; mm_lang=zh_CN; iip=0; tvfe_boss_uuid=4002b0aed5f4de98; RK=s4DpUv8vTX; ptcz=0dde81c5860da07846f9a522ef189766577cb84ae2b45e0e9bcf648077ea675c; o_cookie=1317648217; pac_uid=1_1317648217; fqm_pvqid=5bf7456e-fdce-4a60-981d-25d2eb65065c; rewardsn=; wxtokenkey=777; _qpsvr_localtk=0.953891846691262; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; pgv_info=ssid=s8019024690; uuid=28d3e544dd6d8d6f535465b75e98e275; wxuin=60831741041882; cert=BAaUxfWvtxQB6sUaBuofrDPQDqg4URI9; sig=h01532e32efaff0ce9d7fb94bdf8874735c2be3805188f81da3d01302ef6c42560b87f7c2eb60972d76; data_bizuin=3874843653; data_ticket=j2PXeYq/qyj/LEW7fEXeqLhsyeq21HCUL02qu+RrXxK16LMlva3SFcS5EmgtL7n7; master_key=uh/AmJ9dnCO5d7LqNLoDEP2ZWThrn4DB6hykhKrRonA=; master_user=gh_4a0145504686; master_sid=VkV4MTFwbHZzVF9RYXdOdVNfeUtBeUhDSGRUNEVlSXlucU1ONzBST2s5UU9haVVpM19VUnlVdFNtUWVBQkZ0NU1JV0JLMUdPcGI5Y3dJWG9aaFFUUXVxYmNnZTZCUkhrNWh4NjVWYndlSG9GTW5vRTZDSTFrTUhVUFA2dlJENHFrN0JaWTRPQnRIUUZrQWlR; master_ticket=3d6c1034d897a4223eff43738c8405fc; bizuin=3874843653; slave_user=gh_4a0145504686; slave_sid=QW9HZzhsNGJzTUlzVnBpeUVFaEZNRmYzVGllbG9ibEdHUU5kU3o1N1Z5TUpxRDB0c3NTNHFJNFBDZTgyaUNzRjJiOGhDWURoVFpvUksyazhNcFpxcjcxc3FVRl9yNWhNOVh3djhETkptT3lEdG94R1hoZE5MenhpbnpYTWpsZWFIWVAyN1ptcjh5STBvQVJI",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
}
url = 'https://mp.weixin.qq.com/cgi-bin/appmsg'
fad = 'MzA5MzM1MTQzNA=='                     #爬不同公众号只需要更改 fakeid

def page(num=1):                             #要请求的文章页数
    aid=[]
    title = []
    link = []
    create_time=[]
    for i in range(num):
        # 随机暂停几秒，避免过快的请求导致过快的被查到
        time.sleep(random.randint(1,10))
        data = {
            'action': 'list_ex',
            'begin': i*5,       #页数
            'count': '5',
            'fakeid': fad,
            'type': '9',
            'query':'' ,
            'token': '886287982',
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
        }
        r = requests.get(url,headers = headers,params=data)
        dic = r.json()            
        for i in dic['app_msg_list']:     #遍历dic['app_msg_list']中所有内容
            aid.append(i['aid'])
            title.append(i['title'])      #取 key键 为‘title’的 value值
            link.append(i['link'])        #去 key键 为‘link’的 value值
            create_time.append(i['create_time'])
        print(f"第{i}页爬取成功\n")
    return aid,title,link,create_time

if __name__ == '__main__':
    num=1
    with open("app_msg_list.csv", "w",encoding='utf-8') as file:
            file.write("文章标识符aid,标题title,链接url,时间time\n")
    (ad,tle,lik,create_ti) = page(num)
    for a,x,y,b in zip(ad,tle,lik,create_ti):
        print(a,x,y,b)
        info=a+x+y+b
        with open("app_msg_list.csv", "a",encoding='utf-8') as f:
                f.write(info+'\n')
        
        

