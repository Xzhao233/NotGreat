import requests, bs4, jieba, pandas,os
import pyecharts.charts as chart

os.chdir(os.getcwd())
url_old = input('请输入解析b站视频的cid：')
url = 'https://comment.bilibili.com/' + url_old + '.xml'
print(url)
response = requests.get(url)
response.encoding = 'utf-8'
soup = bs4.BeautifulSoup(response.text,features="xml")
data = soup.find_all('d')
res = ''
for i in data:
    res = res + i.text
# 将字符串res拆分为词语
word = jieba.lcut(res)
new = []
for i in word:
    if len(i) > 1:
        new.append(i)
df = pandas.DataFrame({'弹幕': new})
count = df['弹幕'].value_counts()
#print(new)
# 获取count的索引列，并转化为列表
lis1 = list(count.keys())
lis2 = list(count.values)
# 使用Bar()功能，创建一个图
l = chart.Bar()
l.add_xaxis(lis1[0:10])
# 获取列表lis2的前10个元素，添加到y轴，并设置序列名为'数量'
l.add_yaxis('数量',lis2[0:10])
l.render('弹幕信息.html')
print('输出文件地址： ',os.getcwd())
