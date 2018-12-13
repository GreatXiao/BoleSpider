# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse
from BoleSpider.items import BoleItem
import datetime


class PyartSpider(scrapy.Spider):
    name = 'pyart'
    allowed_domains = ['python.jobbole.com']
    start_urls = ['http://python.jobbole.com/category/basic']

    def parse(self, response):
        """
        :param response:
        :return:
        """
        # 解析单页面所有post_url 并且作循环后调用提取函数
        post_nodes = response.xpath("//div[@id='archive']/div/div[1]/a")
        for post_node in post_nodes:
            post_url = post_node.xpath("@href").extract_first()
            image_url = post_node.xpath("img/@src").extract_first()
            if post_url:
                yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url}, callback=self.parse_detail)

        # 提取下一页的所有url
        # next_url = response.css("a[class='next page-numbers']::attr(href)").extract_first()
        # if next_url:
        #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        """
        :param response:
        :return:
        """
        # 提取字符串
        title = response.xpath("//div[@class = 'entry-header']/h1/text()").extract()[0]

        # 提取url
        post_url = response.url

        # 图片url
        front_image_url = response.meta.get("front_image_url", "")

        # 提取日期
        creat_date = response.css(".entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·", "").strip()
        # creat_date = datetime.datetime.strptime(creat_date, '%Y/%m/%d')

        # 提取数字
        fav_num = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0]
        fav_num = re.match(".*(\d+).*", fav_num)
        if fav_num:
            fav_num = fav_num.group(1)
        else:
            fav_num = 0
        bole_item = BoleItem()
        bole_item["creat_date"] = creat_date
        bole_item["fav_num"] = int(fav_num)
        bole_item["title"] = title
        bole_item["post_url"] = post_url
        bole_item["front_image_url"] = [front_image_url]

        yield bole_item


