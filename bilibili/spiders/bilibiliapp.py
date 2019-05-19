# -*- coding: utf-8 -*-
import scrapy
import json,re
from bilibili.items import BilibiliItem

class BilibiliappSpider(scrapy.Spider):
    name = 'bilibiliapp'
    # allowed_domains = ['www.bilibili.com']
    # start_urls = ['http://www.bilibili.com/']
    def start_requests(self):
            for i in range(1, 300):

                url = 'https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp&callback=__jp3'.format(i)
                url_ajax = 'https://space.bilibili.com/{}/'.format(i)
                # get的时候是这个东东, scrapy.Request(url=, callback=)
                req = scrapy.Request(url=url,callback=self.parse,meta={'id':i})
                req.headers['referer'] = url_ajax

                yield req


    def parse(self, response):
        # print(response.text)
        comm = re.compile(r'({.*})')
        text = re.findall(comm,response.text)[0]
        data = json.loads(text)
        # print(data)
        follower = data['data']['follower']
        following = data['data']['following']
        id = response.meta.get('id')
        url = 'https://space.bilibili.com/ajax/member/getSubmitVideos?mid={}&page=1&pagesize=25'.format(id)
        yield scrapy.Request(url=url,callback=self.getsubmit,meta={
            'id':id,
            'follower':follower,
            'following':following
        })

    def getsubmit(self, response):
        # print(response.text)
        data = json.loads(response.text)
        tilst = data['data']['tlist']
        tlist_list = []
        if tilst != []:
            # print(tilst)
            for tils in tilst.values():
                # print(tils['name'])
                tlist_list.append(tils['name'])
        else:
            tlist_list = ['无爱好']
        follower = response.meta.get('follower')
        following = response.meta.get('following')
        id = response.meta.get('id')
        url = 'https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'.format(id)
        yield scrapy.Request(url=url,callback=self.space,meta={
            'id':id,
            'follower':follower,
            'following':following,
            'tlist_list':tlist_list
        })

    def space(self, respinse):
        # print(respinse.text)
        data = json.loads(respinse.text)
        name = data['data']['name']
        sex = data['data']['sex']
        level = data['data']['level']
        birthday = data['data']['birthday']
        tlist_list = respinse.meta.get('tlist_list')
        animation = 0
        Life = 0
        Music = 0
        Game = 0
        Dance = 0
        Documentary = 0
        Ghost = 0
        science = 0
        Opera = 0
        entertainment = 0
        Movies = 0
        National = 0
        Digital = 0
        fashion = 0
        for tlist in tlist_list:
            if tlist == '动画':
                animation = 1
            elif tlist == '生活':
                Life = 1
            elif tlist == '音乐':
                Music = 1
            elif tlist == '游戏':
                Game = 1
            elif tlist == '舞蹈':
                Dance = 1
            elif tlist == '纪录片':
                Documentary = 1
            elif tlist == '鬼畜':
                Ghost = 1
            elif tlist == '科技':
                science = 1
            elif tlist == '番剧':
                Opera =1
            elif tlist == '娱乐':
                entertainment = 1
            elif tlist == '影视':
                Movies = 1
            elif tlist == '国创':
                National = 1
            elif tlist == '数码':
                Digital = 1
            elif tlist == '时尚':
                fashion = 1
        item = BilibiliItem()
        item['name'] = name
        item['sex'] = sex
        item['level'] = level
        item['birthday'] = birthday
        item['follower'] = respinse.meta.get('follower')
        item['following'] = respinse.meta.get('following')
        item['animation'] = animation
        item['Life'] = Life
        item['Music'] = Music
        item['Game'] = Game
        item['Dance'] = Dance
        item['Documentary'] = Documentary
        item['Ghost'] = Ghost
        item['science'] = science
        item['Opera'] = Opera
        item['entertainment'] = entertainment
        item['Movies'] = Movies
        item['National'] = National
        item['Digital'] = Digital
        item['fashion'] = fashion
        yield item



