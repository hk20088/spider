# 前言
这里放了一些自己练习爬虫的案例，源码中都有详细的注释。 下面是每个案例的索引，以便查阅。

# day1
核心库：`requests` `BeautifulSoup`<br>
从图库网上抓取一张图片，并下载下来。

# day2
核心库：`requests` `BeautifulSoup`<br>
从图库网上抓取一堆图片，并下载到本地某个目录下<br
注：注释掉的部分是常规则的抓取图片的方法， 注释外的部分是封装了代码，并且加了多线程的方法

# day3
核心库：`requests` `splinter`<br>
自动抢票程序，可自动登录12306并实现查询，购买功能（验证码需要人工输入）<br>
Chromedriver下载地址：https://sites.google.com/a/chromium.org/chromedriver/downloads<br>
注意与Chrome浏览器的版本对应

# day4
核心库：`requests` `BeautifulSoup`<br>
抓取某个网站的内容，并保存到文件中<br>
这里抓取的网站的所有内容（包含广告）并保持网站的整体结构，即点击菜单栏会跳转到相应的页面。

# day5
核心库：`requests` `BeautifulSoup`<br>
抓取某个网站的内容，并保存到文件中。<br>
这里去掉了网站的菜单栏和广告，将整站内容保存到一个文件中。


