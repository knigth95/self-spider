import requests
import time
from lxml import etree

#url
url='https://bbs.ruian.com/forum-128-%d.html'
#请求头
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}#伪装头


#写入
fp = open('./爬虫数据/zzmtest.xlsx','w',encoding='gbk')
auth_id='帖子id'

title='帖子标题'
publicer='帖子作者'
commentator='最近评论者'
fa_time='发布时间'
type_commentatorTime='最近评论的时间'
auth_page='评论页数'
reply='回复数'
redu='热度'
net_id='身份id'
#fp.write('%s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t\n'%(auth_id,title,publicer,fa_time,commentator,type_commentatorTime,auth_page,reply,redu,net_id))
#获取多页数据
for i in range(1):
    s_url=url%(i+1)
    res = requests.get(s_url,headers=headers) #发起请求
    res.encoding='gbk' #设置编码格式
    text = res.text
    html = etree.HTML(text)
    items = html.xpath('//tbody')#选中帖子
    # print(res.status_code)
    for item in items:
        auth_id=item.xpath('./@id')
        #列表转字符串
        net_id="".join(auth_id)#列表不能直接提取数字
        net_id="".join(list(filter(str.isdigit,net_id)))
        print(net_id)
        title=item.xpath('.//a[@class="s xst"]/text()')#选中帖子的标题
        
        author=item.xpath('.//td[@class="by"]/cite/a/text()'),
        publicer=author[0][:1]
        commentator=author[0][1:2]    
        
        fa_time = item.xpath('.//em/span/text()'),
        #lend_author=item.xpath('.//div[@style="float:right;width:100px;line-height:16px;"]/a[1]/text()'),
        type_commentatorTime = item.xpath('.//em/a/text()')
        #type=type_commentatorTime[0][:1] 有些没有标签或type，无法切
        #type_commentatorTime=type_commentatorTime[0][1:2]
        auth_page=item.xpath('.//span[@class="tps"]/a/text()'),
        auth_page=auth_page[0][-1:]
        reply=item.xpath('.//td[@class="num"]/a/text()'),
        redu=item.xpath('.//td[@class="num"]/em/text()'),
        
 
        print(auth_id,title,auth_page,author,fa_time)
        #fp.write('%s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t\n'%(auth_id,title,publicer,fa_time,commentator,type_commentatorTime,auth_page,reply,redu,net_id))
    print('第%d页爬取成功'%(i+1))
    time.sleep(1)
fp.close()

