import requests
import time
from lxml import etree

#瑞安说事：128 汽车 69 美食 136 房屋 101 人才 87 二手 172 育儿养女 85 征婚 140 家装 132 金融 554 市场 62 旅游 442 摄影 48 灌水 79

url_www=['128','69','136','101','87','172','85','140','132','554','62','442','48','79']
url_name=['瑞安说事','瑞安汽车','瑞安美食','瑞安房屋','瑞安人才','瑞安二手','瑞安教育','瑞安征婚','瑞安家装','瑞安金融','瑞安市场','瑞安旅游','瑞安摄影','瑞安灌水']
count=-1 #控制板块

def url_Reply(net_id,auth_page,title):    
    #获取多页数据
    if auth_page=='':
        auth_page=1
        print('无评论')
    else:
        auth_page=int(float(auth_page))
        print('有评论')
    #url
    url_zzm="https://bbs.ruian.com/thread-"+net_id+"-%d-1.html"
    #请求头
    headers_zzm={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }#伪装头
    
    #写入
    #fp = open('./帖子'+net_id+'.xlsx','w',encoding='gbk')  #若要分开帖子文件，可使用此语句
    fp = open('./爬虫数据/评论数据test.xlsx','a',encoding='gbk')  #追加写入模式
    authori='评论者'
    publish_time='评论时间'
    publish_address='发布地址'
    publish_text='发布内容'
    publish_id='帖子ID:'
    
    fp.write('%s\t %s\t %s\t\n'%(publish_id,net_id,title))
    fp.write('%s\t %s\t %s\t %s\t\n'%(authori,publish_time,publish_address,publish_text))
    for i_zzm in range(auth_page+1):
        s_url_zzm=url_zzm%(i_zzm+1)
        res_zzm = requests.get(s_url_zzm,headers=headers_zzm) #发起请求
        res_zzm.encoding='gbk' #设置编码格式
        text_zzm = res_zzm.text
        html_zzm = etree.HTML(text_zzm)

        items_zzm = html_zzm.xpath('//table[@id]')#选中回复
        #print(res.status_code)
        #url
        url_zzm="https://bbs.ruian.com/thread-"+net_id+"-%d-1.html"
        #请求头
        headers_zzm={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }#伪装头
        
        for item_zzm in items_zzm:
            
            authori=item_zzm.xpath('//div[@class="authi"]/a[@class="xw1"]/text()')
            publish_time=item_zzm.xpath('//div[@class="authi"]/em/text()')
            publish_address=item_zzm.xpath('//div[@class="authi"]/span[@class=""]/text()')
            publish_text=item_zzm.xpath('//td[@class="t_f"]/text()')

        try:
            i=0
            cnt_text=len(publish_text)
            while i<cnt_text:
                if(publish_text[i]=='\n' or publish_text[i]=='\r\n' or publish_text[i]=='\n\r\n'):
                    publish_text[i]='该内容被屏蔽'
                    del publish_text[i]
                    cnt_text-=1
                i+=1
        except:
            print('列表异常')
        try:
            i=0
            cnt=len(authori)
            while i<cnt:
                if(authori[i]=='用户名被屏蔽'):
                    del authori[i]
                    del publish_text[i]
                    del publish_address[i]
                    del publish_time[i]
                    cnt-=1
                i+=1
        except:
            print('列表异常')
        cnt=len(authori)
        for j in range(cnt):
            try:
                fp.write('%s\t %s\t %s\t %s\t\n'%(authori[j],publish_time[j],publish_address[j],"".join(publish_text[j].split())))
            except:
                #print(cnt2)
                print('该数据有异常，跳过爬取')
    fp.write('\n'%())
    fp.close()

def turnFormat_tuple(n):#去掉元组括号
    if n==([],):
        return n
    else:
        for i in n:
            temp="{}".format(i[0])
            return temp

def turnFormat_list(n):#去掉列表括号
    if n==[]:
        return n
    else:
        for i in n:
            temp="{}".format(i)
        return temp

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


if __name__ == '__main__':
    #url
    count+=1
    it_pages=get_model_pages(count)
    url='https://bbs.ruian.com/forum-'+url_www[count]+'-%d.html'
    #请求头
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }#伪装头
    #写入
    fp = open('./爬虫数据/帖子数据zzmtest.xlsx','a',encoding='gbk')
    auth_id='帖子id'
    
    title='帖子标题'
    publicer='帖子作者'
    commentator='最近评论者'
    fa_time='发布时间'
    type_commentatorTime='板块、最近评论的时间'
    auth_page='评论页数'
    reply='回复数'
    hot='热度'
    net_id='身份id'
    fp.write('%s\t %s\t\n'%('板块名称：',url_name[count]))
    fp.write('%s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t\n'%(auth_id,title,publicer,fa_time,commentator,type_commentatorTime,auth_page,reply,hot))
    #获取多页数据
    
    for i in range(100):
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
            auth_id=turnFormat_list(auth_id)

            title=item.xpath('.//a[@class="s xst"]/text()')#选中帖子的标题
            title=turnFormat_list(title)
            
            author=item.xpath('.//td[@class="by"]/cite/a/text()'),
            publicer=author[0][:1]
            commentator=author[0][1:2]    
            publicer=turnFormat_list(publicer)
            commentator=turnFormat_list(commentator)
            
            fa_time = item.xpath('.//em/span/text()'),
            fa_time=turnFormat_tuple(fa_time)

            type_commentatorTime = item.xpath('.//em/a/text()')
            type_commentatorTime="".join(type_commentatorTime)
            #type_tiezi=type_commentatorTime[0]
            #commentatorTime=type_commentatorTime[1]

            #type=type_commentatorTime[0][:1] 有些没有标签或type，无法切
            #type_commentatorTime=type_commentatorTime[0][1:2]
            auth_page=item.xpath('.//span[@class="tps"]/a/text()'),
            auth_page=auth_page[0][-1:]
            auth_page="".join(auth_page)
            auth_page="".join(list(filter(str.isdigit,auth_page)))

            reply=item.xpath('.//td[@class="num"]/a/text()'),
            reply=turnFormat_tuple(reply)
        
            hot=item.xpath('.//td[@class="num"]/em/text()'),
            hot=turnFormat_tuple(hot)
            if title==[]:
                print('',end="")
            else:
                fp.write('%s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t\n'%(auth_id,title,publicer,fa_time,commentator,type_commentatorTime,auth_page,reply,hot))
            if reply==([],):
                url_Reply(net_id,1,title)
                #print('无评论')
            else:
                url_Reply(net_id,auth_page,title)
                #print('有评论')
        
        fp.write('第%d页爬取成功'%(i+1))
        fp.write('\n'%())
        print('第%d页爬取成功'%(i+1))
        time.sleep(1)
    fp.close()

