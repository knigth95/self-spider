from lxml import etree
import requests

url_www=['128','69','136','101','87','172','85','140','132','554','62','442','48','79']


def get_model_pages(count):
    url_pages='https://bbs.ruian.com/forum-'+url_www[count]+'-1.html'
    headers_pages={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }#伪装头
    res_pages = requests.get(url_pages,headers=headers_pages) #发起请求
    res_pages.encoding='gbk' #设置编码格式
    text_pages = res_pages.text
    html_pages = etree.HTML(text_pages)
    it_pages=html_pages.xpath('//*[@id="fd_page_top"]/div/a[10]/text()')
    it_pages="".join(it_pages)
    it_pages="".join(list(filter(str.isdigit,it_pages)))
    it_pages=int(float(it_pages))
    return it_pages


n=get_model_pages(2)

print(n)

zzm=['1','2','3','4','5']
cnt=len(zzm)
i=0
while i<cnt:
    print(len(zzm))
    if(zzm[i]=='3'):
        del zzm[i]
        cnt-=1
    i+=1
    print(i)
print(len(zzm))

def turnFormat_list(n):#去掉列表括号
    if n==[]:
        return n
    else:
        for i in n:
            temp="{}".format(i)
        return temp
type_time= ['新闻', '2022-12-13 14:05']
type1=type_time[0]
time1=type_time[1]
type_time="".join(type_time)
print(turnFormat_list(type_time))
#print(type_time)
print(type1)
print(time1)