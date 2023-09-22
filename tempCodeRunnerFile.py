def main():  # 主函数
    resLs = []  # 初始化列表
    for i in range(10):
        collect(i * 25, resLs)  # 抓取数据
        print(f'第{i + 1}页采集完成!')
        sleep(0.2)
    df = pd.DataFrame(resLs)  # 转列表为dataframe
    path = pd.ExcelWriter('豆瓣TOP250.xlsx')
    df.to_excel(path, index=False)
    path.save()  # 保存数据