import chardet

print(chardet.detect(b'it is chardet'))

data = '黄河之水天上来'.encode('gbk')
print(chardet.detect(data))

data1 = '黄河之水天上来'.encode('utf-8')
print(chardet.detect(data1))

data2 = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data2))