# 前言
这里放了一些自己练习爬虫的案例，源码中都有详细的注释。 下面是每个案例的索引，以便查阅。

# day1
核心库：`requests` `BeautifulSoup`<br>
- 从图库网上抓取一张图片，并下载下来。

# day2
核心库：`requests` `BeautifulSoup`<br>
- 从图库网上抓取一堆图片，并下载到本地某个目录下<br
- 注：注释掉的部分是常规则的抓取图片的方法， 注释外的部分是封装了代码，并且加了多进程的方法

# day3
核心库：`requests` `splinter`<br>
- 自动抢票程序，可自动登录12306并实现查询，购买功能（验证码需要人工输入）<br>
- Chromedriver下载地址：https://sites.google.com/a/chromium.org/chromedriver/downloads<br>
- 注意与Chrome浏览器的版本对应

# day4
核心库：`requests` `BeautifulSoup`<br>
- 抓取某个网站的内容，并保存到文件中<br>
- 这里抓取的网站的所有内容（包含广告）并保持网站的整体结构，即点击菜单栏会跳转到相应的页面。

# day5
核心库：`requests` `BeautifulSoup`<br>
- 抓取某个网站的内容，并保存到文件中。<br>
- 这里去掉了网站的菜单栏和广告，将整站内容保存到一个文件中。<br>
- 有些目标网站限制了单IP的访问次数，这里使用代理IP去访问，保证能抓取完整数据

# day6
核心库：`requests` `Beautiful`<br>
- 从西刺抓取代理IP（注意代理IP的类型，如果你要爬的是http网站，则使用类型为 http的代理IP；https亦然）<br>
- 访问 `http://ip.chinaz.com/getip.aspx` 去测试代理IP的可用性

# day7
核心库：`pillow`
- 生成字母+数字验证图片
- 用随机颜色填充背景，在背景上画上字母或数字，然后再对图像进行模糊，验证码图片就生成了。

# day8
核心库：`PIL` `pytesseract` `pytesseract-OCR`
- 处理验证码的步骤为：下载验证码图片-> 图片二值化-> 图片降噪 -> 验证码字符串读取
- pytesseract是Python的第三方库， 它需要调用 pytesseract-OCR 引擎来识别图片，所以在代理里要单独设置 tesseract.exe的路径
- OCR引擎需要单独下载安装，下载地址百度查找

# day9   
核心库: `requests` `itchat`
- 自动回复微信消息的机器人，调用了图灵机器人的API，可以根据接收到的消息自动回复合适的内容，有兴趣的可以玩一玩。<br>
- 图灵机器人网站：`http://www.tuling123.com/`

