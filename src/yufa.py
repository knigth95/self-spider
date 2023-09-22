from zmq import NULL


a=[1,2,3,4,5]
b=(1,2,3,4,5)
c=[6,7,8,9,0]
d=(a,c)
zzm='865655'
zzm1="".join(list(filter(str.isdigit,zzm)))
zzm5= ['连花清瘟瑞安哪里还能买到？早上跑了几家药店，全部没货了']

tuple_test =  (['aisjij'],)
tuple_test2=('2022-12-7 12:04')

list_test = ['11']

def turnForman_tuple(n):#去掉元组括号
    if n==([],):
        return n
    else:
        for i in n:
            temp="{}".format(i[0])
            return temp

def turnForman_list(n):#去掉列表括号
    if n==[]:
        print('无')
        return n
    else:
        for i in n:
            temp="{}".format(i)
        return temp
print(tuple_test)
tuple_test = turnForman_tuple(tuple_test)
print('////')
print(tuple_test)
print('////')

dict_test = {}
assert not dict_test

list = [("fred's", 13), ("jack's", 19), ("mark's", 16), ("amy's", 12), ("finlay's", 17)]

for i in zzm5:
    temp0="{}".format(i)
    print(temp0)
tuple_test=str(tuple_test)
print(tuple_test)

def turngeshi(n):
    n="".join(n)
    #n="".join(list(filter(str.isdigit,n)))
    print(n)
    return n

if(zzm5!=''):
    print(zzm5)
    zzm6 = turngeshi(zzm5)
    zzm7="".join(zzm5)
    
else:
    print("no")
def get_url(net_id,auth_page):
    for i in range(auth_page):
        url=url="https://bbs.ruian.com/thread-"+net_id+"-%d-1.html"
        s_url=url%(i+1)
        print(s_url)

url="https://bbs.ruian.com/thread-"+zzm+"-%d-1.html"
net_id=['normalthread_8654360']
for i in range(1):
    auth_page=str(i)
    net_id="".join(net_id)#列表不能直接提取数字
    #net_id="".join(list(filter(str.isdigit,net_id)))
    auth_page='5'
    auth_page=int(auth_page)
    print(auth_page)
    get_url(net_id,2)
    s_url=url%(i+1)
    print(s_url)

