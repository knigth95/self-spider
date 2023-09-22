编译器环境：
    python环境：python3.10.8
    依赖的python库：
        requests
        lxml
        time
        相关安装命令：1）pip install requests  2)pip install lxml 3)pip install time

功能函数：
    main():主要执行函数，爬取瑞安论坛上帖子各种内容，生成帖子数据zzmtest.xlsx文件并跳转至url_Reply()函数
    url_Reply(net_id,auth_page,title)：爬取帖子对应评论的内容，三个参数（分别为帖子id、对应评论的页数、帖子标题）生成评论数据test.xlsx
    turnFormat_tuple(n):数据处理，去掉元组括号,参数为要处理的对应元素
    turnFormat_list(n):数据处理，去掉列表括号，参数为要处理的对应元素
    get_model_pages(count)：获取对应板块的页数，参数为对应板块下标
    新增抛出异常功能，避免长时间工作遇到某些数据无法爬取（暂定图形化评论内容无法爬取）
执行方法及生成结果：
    配置好上述编译器环境后在code-spider文件夹下编译运行main.py文件，也可以在code-spider文件夹的终端中输入命令：python ./main.py。
    编译并运行该文件后会在'爬虫数据'这个文件夹里生成“评论数据test.xlsx”、“帖子数据zzmtest.xlsx”两个文件，其中有需要爬取的信息。
    可以打开这两个文件查看测试数据浏览文件信息的排版。
