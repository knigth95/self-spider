import requests
import time
from lxml import etree

#url
url_zzm="https://bbs.ruian.com/thread-8654360-%d-1.html"
#请求头
headers_zzm={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}#伪装头

#写入
fp = open('./extest.xlsx','w',encoding='gbk')
authori='评论者'
publish_time='评论时间'
publish_address='发布地址'
publish_text='发布内容'

#fp.write('%s\t %s\t %s\t %s\t\n'%(authori,publish_time,publish_address,publish_text))
#获取多页数据
#auth_page=int(float(auth_page))
for i in range(2):
    s_url_zzm=url_zzm%(i+1)
    res_zzm = requests.get(s_url_zzm,headers=headers_zzm) #发起请求
    res_zzm.encoding='gbk' #设置编码格式
    text_zzm = res_zzm.text
    html_zzm = etree.HTML(text_zzm)
    j=0
    items_zzm = html_zzm.xpath('//table[@id]')#选中回复
    #print(res.status_code)
    for item_zzm in items_zzm:
        
        authori=item_zzm.xpath('//div[@class="authi"]/a[@class="xw1"]/text()')
        cnt=len(authori)
        publish_time=item_zzm.xpath('//div[@class="authi"]/em/text()')
        publish_address=item_zzm.xpath('//div[@class="authi"]/span[@class=""]/text()')
        
        publish_text=item_zzm.xpath('//td[@class="t_f"]/text()')
        cnt1=len(publish_text)
        print(publish_text)
        print(cnt1)
        print('////')
        print(authori)
        print(cnt)
        while j<cnt:
            fp.write('%s\t %s\t %s\t %s\t\n'%(authori[j],publish_time[j],publish_address[j],"".join(publish_text[j+1].split())))
            j+=1
        #fp.write("%s\t %s\t %s\t %s\t \n"%(authori,public_time,public_address,author_text))
    print('第%d页爬取成功'%(i+1))
    #time.sleep(1)
fp.close()