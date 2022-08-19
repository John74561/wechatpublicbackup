# wechatpublicbackup
尝试备份一下自己公众号的内容

# 目的：用来保存某公众号下所有文章到word



## 参考
https://zhuanlan.zhihu.com/p/379062852
https://blog.csdn.net/qq_29789133/article/details/116136714
https://blog.csdn.net/weixin_30267691/article/details/98638295
首要参考
https://www.cnblogs.com/leslie12956/p/16282238.html
yaml
https://zhuanlan.zhihu.com/p/145173920



error:
https://blog.csdn.net/weixin_44807854/article/details/110729478#:~:text=%E6%8A%A5%E9%94%99%E4%BF%A1%E6%81%AF%EF%BC%9AModuleNotFoundError%3A%20No%20module,named%20%E2%80%98werkzeug.contrib%E2%80%99%20%E5%8E%9F%E5%9B%A0%EF%BC%9Acontrib%E6%A8%A1%E5%9D%97%E5%B7%B2%E5%BC%83%E7%94%A8%EF%BC%8C%E5%B0%86werkzeug%E5%9C%A81.0%E7%89%88%E4%B8%AD%E7%A7%BB%E5%85%A5%20%E6%A0%B8%E5%BF%83%E6%88%96%E5%AE%8C%E5%85%A8%E5%88%A0%E9%99%A4%E3%80%82


pdfkit
https://zhuanlan.zhihu.com/p/94608155#:~:text=pdfkit%20%7C%20%E5%88%A9%E7%94%A8python%E5%AE%9E%E7%8E%B0html%E6%96%87%E4%BB%B6%E8%BD%ACpdf%201%20%E4%B8%89%E6%AD%A5%E5%AE%9E%E7%8E%B0%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90pdf%E6%96%87%E6%A1%A3%EF%BC%9A%202%201.%E4%BD%BF%E7%94%A8%20pip,wkhtmltopdf.exe%20%E6%96%87%E4%BB%B6%204%203.%E4%BD%BF%E7%94%A8%20pdfkit%20%E5%BA%93%E7%94%9F%E6%88%90pdf%E6%96%87%E4%BB%B6%205%204.%E7%BB%93%E8%AE%BA

去除特殊字符比如“
https://www.coder.work/article/1248983

string到dataframe
https://www.coder.work/article/3181620


json
https://zhuanlan.zhihu.com/p/398105018
https://zhuanlan.zhihu.com/p/447820510#:~:text=%E4%BD%BF%E7%94%A8Python%E5%A4%84%E7%90%86JSON%E6%96%87%E4%BB%B6%201%203.1.%20%E5%B0%86JSON%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E4%B8%BA%E5%AD%97%E5%85%B8%E7%B1%BB%E5%9E%8B%20%E9%A6%96%E5%85%88%E6%88%91%E4%BB%AC%E9%9C%80%E8%A6%81%E5%AF%BC%E5%85%A5%20json%E5%BA%93%2C%20%E6%8E%A5%E7%9D%80%E6%88%91%E4%BB%AC%E4%BD%BF%E7%94%A8open%E5%87%BD%E6%95%B0%E6%9D%A5%E8%AF%BB%E5%8F%96JSON%E6%96%87%E4%BB%B6%2C%E6%9C%80%E5%90%8E%E5%88%A9%E7%94%A8json.load%20%28%29%E5%87%BD%E6%95%B0%E5%B0%86JSON%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%BD%AC%E5%8C%96%E4%B8%BAPython%E5%AD%97%E5%85%B8%E5%BD%A2%E5%BC%8F.,6%203.6.%20%E6%A0%BC%E5%BC%8F%E5%8C%96%E8%BE%93%E5%87%BA%20...%207%203.7.%20%E8%BE%93%E5%87%BA%E5%AD%97%E6%AE%B5%E6%8E%92%E5%BA%8F%20

try except
http://c.biancheng.net/view/4599.html

## 另一种没尝试的方法fiddle抓包：
https://zhuanlan.zhihu.com/p/77438394
## 结果：
92转换失败
900+成功，部分无图
## 可能的原因：
有的是因为|
有的可能是css样式？
html写法不规范
或者什么原因
## 环境 
anaconda：web
## 目录说明
backup：备份的json
spidertocsv.py:主爬虫程序
readcsv.py:csv转pdf
jsontoCsv.ipynb:实验，json转csv
其余文件，已弃用
output：输出结果
convertwordtest：转换为word的测试
outputtest：输出测试
test：测试的爬虫结果

20220820 
