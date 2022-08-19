
import pdfkit
import datetime
import wechatsogou
import re
import time

import pandas as pd
ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3) 

def url2pdf(url, title,create_time):
    '''
    使用pdfkit生成pdf文件
    :param url: 文章url
    :param title: 文章标题
    :param targetPath: 存储pdf文件的路径
    '''
    
    try:
        content_info = ws_api.get_article_content(url)
        path_wkthmltopdf = r'D:\\plugin\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'    
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf) 
        
    except:
        return False
        
    # 处理后的html
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
    </head>
    <body>
    <h2 style="text-align: center;font-weight: 400;">{title}</h2>
    {content_info['content_html']}
    </body>
    </html>
    '''
    





    # s = "123,abc .?/&？》^_^dddA。"
    # 把所有编码非\u0030-\u0039(数字)、\u0041-\u007a(英文字母)的字符替换为空字符串
    # rs = re.sub("([^\u0030-\u0039\u0041-\u007a])", '', s)
    # print(rs) # "123abcdddA"

    create_time1=re.sub("([^\u0030-\u0039\u0041-\u007a])", '', create_time)
    titleAll=title+create_time1+'.pdf'
    pdfkit.from_string(html, 'D:/projects/wechatSaveArticles/output/'+titleAll, configuration=config)


# url2pdf("http://mp.weixin.qq.com/s?__biz=MzA5MzM1MTQzNA==&mid=2649599673&idx=1&sn=a400e16463302504c307e41d452efbda&chksm=884635dcbf31bcca190a66ffbdb822cf78a219e6b4b834d4d7b6e6c867d9d9e65f7721ef15e5#rd",
# "如日方升，锦绣前程")


# with open('D:\\projects\\wechatSaveArticles\\end.csv', 'r',encoding='utf-8') as f:
#     reader = csv.reader(f)
result=pd.read_csv('D:\\projects\\wechatSaveArticles\\end.csv',encoding='utf-8')
df0=result['string'].str.split(',',expand=True)
df0.columns=['aid','time','url','title','none']
df0['url']=df0['url'].str.replace('"',' ')
df0['title']=df0['title'].str.replace('"',' ')
df0['time']=df0['time'].str.replace('"',' ')
# print(result[1])

lenth=len(df0)
print(lenth)
# i=0
for i in range(lenth):
    # print(i)
    try:
        url2pdf(df0['url'][i],df0['title'][i],df0['time'][i])
    except:
        print('errorname',df0['title'][i]+df0['time'][i],i)

