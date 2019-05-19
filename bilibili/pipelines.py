# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class BilibiliPipeline(object):
    def open_spider(self,spider):
        # self.f = open('1.txt','w')
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client.bili
        self.collection = db.bilibili
    def process_item(self, item, spider):
        data = {
            'name':item['name'],
            'sex':item['sex'],
            'level':item['level'],
            'birthday':item['birthday'],
            'follower':item['follower'],
            'following':item['following'],
            'animation':item['animation'],
        'Life':item['Life'],
        'Music':item['Music'],
        'Game':item['Game'],
        'Dance':item['Dance'],
        'Documentary':item['Documentary'],
        'Ghost':item['Ghost'],
        'science':item['science'],
        'Opera':item['Opera'],
        'entertainment':item['entertainment'],
        'Movies':item['Movies'],
        'National':item['National'],
        'Digital':item['Digital'],
        'fashion':item['fashion']
        }
        result = self.collection.insert(data)
        print(result)



        return item
    def close_spider(self,spider):
        # self.f.close()
        pass
