# 导包（无需另外安装，Python自带）
import webbrowser as web
import os

# try后面有大用
try:
    # 定义一个函数为s()，执行s()时等于执行下面的代码
    def s():
        print("必应（Bing）：1")
        print("百度（Baidu）：2")
        print("360导航：3")
        print("搜狗（Sogou）：4")
        print("中国搜索（ChinaSo）：5")
        engine = input("请输入你要使用的搜索引擎（退出请按Ctrl+C）：") # 询问需要的搜索引擎
        if engine == "1": #判断用户选择的搜索引擎（下面以此类推）
            while True:
                search = input("你要搜索的内容（切换搜索引擎输入engines）：")
                if search == "engines": # 判断是否切换搜索引擎（下面以此类推）
                    s()
                else:
                    web.open(f"https://cn.bing.com/search?q={search}&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQg1MTE1ajBqOagCCLACAQ&FORM=ANAB01&adppc=EdgeStart&PC=CNNDDB") # 打开搜索网页（下面以此类推）
        elif engine == "2":
            while True:
                search = input("你要搜索的内容（切换搜索引擎输入engines）：")
                if search == "engines":
                    s()
                else:
                    web.open(f"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={search}&rsv_pq=cb8b75730005cfa8&rsv_t=914eS7mMLyB4V%2BuuF8qNIBbQMnTTRyts1NGohFPa9dgo%2BDqhLDOSD5CS5YE&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_btype=t&inputT=1546&rsv_sug3=23&rsv_sug1=17&rsv_sug7=100&rsv_sug2=0&rsv_sug4=2098")
        elif engine == "3":
            while True:
                search = input("你要搜索的内容（切换搜索引擎输入engines）：")
                if search == "engines":
                    s()
                else:
                    web.open(f"https://www.so.com/s?ie=utf-8&src=hao_360so_a1004_per&shb=1&hsid=f8b2c9f78df61d5c&ssid=&q={search}&cp=1120000024")
        elif engine == "4":
            while True:
                search = input("你要搜索的内容（切换搜索引擎输入engines）：")
                if search == "engines":
                    s()
                else:
                    web.open(f"https://www.sogou.com/web?query={search}&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&ie=utf8&from=index-nologin&s_from=index&sourceid=9_01_03&sessiontime=1731670348285")
        elif engine == "5":
            while True:
                search = input("你要搜索的内容（切换搜索引擎输入engines）：")
                if search == "engines":
                    s()
                else:
                    web.open(f"https://www.chinaso.com/newssearch/all/allResults?q={search}")

    # 循环执行函数s()
    while True:
        s()

# 捕捉由于用户按下Ctrl+C导致的结束（try立大功）
except KeyboardInterrupt:
    print("\n已退出，再见")
finally:
    print("GoodBye")
    os.system("pause") # 防止应用自动退出，导致用户看不到“再见”的字样