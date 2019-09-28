# -*- coding: utf-8 -*-

# Scrapy settings for DoubanBookSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DoubanBookSpider'

SPIDER_MODULES = ['DoubanBookSpider.spiders']
NEWSPIDER_MODULE = 'DoubanBookSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 请求失败重试
RETRY_ENABLED = True # 是否开启retry
RETRY_TIMES = 3  # 重试次数
# RETRY_HTTP_CODECS  # 遇到什么http code时需要重试，默认是500,502,503,504,408，其他的，网络连接超时等问题也会自动retry的

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 150

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 150
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Host': 'book.douban.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'utf-8',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'DoubanBookSpider.middlewares.DoubanbookspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 200,
    'DoubanBookSpider.middlewares.ProxyMiddleware': 555,
    'DoubanBookSpider.middlewares.RandomUserAgentMiddleware': 556,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'DoubanBookSpider.pipelines.DoubanbookspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# LOG_LEVEL = 'WARNING'

# MongoDb 配置
LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'DoubanBookData'


# 设置日志
# 日志文件
import time
LOG_FILE = BOT_NAME + '_' + time.strftime("%Y%m%d", time.localtime()) + '.log'

# 日志等级
LOG_LEVEL = 'INFO'

# 是否启用日志（创建日志后，不需开启，进行配置）
LOG_ENABLED = True  # （默认为True，启用日志）

# 日志编码
LOG_ENCODING = 'utf-8'

# 如果是True ，进程当中，所有标准输出（包括错误）将会被重定向到log中;例如：在爬虫代码中的 print（）
LOG_STDOUT = False  # 默认为False