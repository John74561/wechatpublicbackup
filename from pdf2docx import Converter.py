from pdf2docx import Converter
pdf_file = 'D:\\projects\\wechatSaveArticles\\outputtest\\【管科男排】欢庆五一，友谊排球20220504231110.pdf'#'pdf文件路径'

docx_file = 'D:\\projects\\wechatSaveArticles\\convertwordtest\\test1.docx'#'输出word文件的路径'
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()