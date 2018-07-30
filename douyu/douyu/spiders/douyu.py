
# 用来解析我们请求成功返回的json格式文件
import json
import scrapy
# 我们的Item（存放自己需要的类似一个字典）
from douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    # 这个就是蜘蛛的名字了，也就是我们scrapy list 和 scraply crwal douyu的来由
    name = 'douyu'
    # 允许的范围
    allowed_domains = ['douyucdn.cn', ]

    # 偏移量
    offset = 0
    # 手机端获取信息的json的URL，里面可以返回limit=20（20条数据）,从第offset= 开始
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    # 拼接我们的url
    start_urls = [base_url + str(offset), ]

    # 回调函数 解析数据
    def parse(self, response):
        content = response.text
        data = json.loads(content)['data']

        for i in data:
            # json格式字段里面的key对应的值
            image_url = i['vertical_src']
            # 我们先前定义的Item
            item = DouyuItem()

            # 该字段必须是可迭代对象
            item['image_urls'] = [image_url]
            yield item

        # 这里是可以设置想要获取的多少条，230可改，代表获取230张图片,可以自行设置
        # if self.offset < 230:
        #     self.offset += 20
        #     yield scrapy.Request(url=self.base_url + str(self.offset), callback=self.parse)
