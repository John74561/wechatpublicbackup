import pdfkit
import datetime
import wechatsogou

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
    
    pdfkit.from_string(html, title+create_time+'.pdf', configuration=config)


url2pdf("http://mp.weixin.qq.com/s?__biz=MzA5MzM1MTQzNA==&mid=2649599673&idx=1&sn=a400e16463302504c307e41d452efbda&chksm=884635dcbf31bcca190a66ffbdb822cf78a219e6b4b834d4d7b6e6c867d9d9e65f7721ef15e5#rd",
"如日方升，锦绣前程")