# -*- coding:utf-8 -*-
from elasticsearch import Elasticsearch
from elasticsearch import helpers

esclient = Elasticsearch(hosts=['http://localhost:9200/'])

def index_obj():
    esclient.index(index='qmht-event', doc_type='product', id=1, request_timeout=2,
                   body={
                       'id': 1,
                       'eventId': '1328',
                       'title': u'【女表】浪琴(Longines)手表 军旗系列机械情侣表L4.274.4.12.6',
                       'headImage': '/attached/image/products/longines/watches/L4.274.4.12.6-1.jpg',
                       'stock': 10,
                       'price': 1783,
                       'hasSpec': 'n',
                       'color': [u'红色', u'黑色', u'白色'],
                       'size': ['XL', 'X', 'M', 'L'],
                       'tag': [u'TEST卫衣', u'衬衣', u'28寸', u'男士', u'女士', u'Coach', u'MK'],
                       'addTime': '2017-01-15 18:20:30',
                   })


def index_obj_by_bulk():
    actions = [
        {
            "_index": 'qmht-event',
            "_type": "product",
            "_id": 4,
            "_source": {
                'id': 4,
                'eventId': '1328',
                'title': u'【女表】浪琴(Longines)手表 军旗系列机械情侣表L4.274.4.12.6',
                'headImage': '/attached/image/products/longines/watches/L4.274.4.12.6-1.jpg',
                'stock': 10,
                'price': 1783,
                'hasSpec': 'n',
                'color': [u'红色', u'黑色', u'白色'],
                'size': ['XL', 'X', 'M', 'L'],
                'tag': [u'卫衣', u'衬衣', u'28寸', u'男士', u'女士', u'Coach', u'MK'],
                'addTime': '2017-01-15 18:20:30',
            }
        },
        {
            "_index": 'qmht-event',
            "_type": "product",
            "_id": 3,
            "_source": {
                'id': 3,
                'eventId': '1328',
                'title': u'【女表】浪琴(Longines)手表 军旗系列机械情侣表L4.274.4.12.6',
                'headImage': '/attached/image/products/longines/watches/L4.274.4.12.6-1.jpg',
                'stock': 10,
                'price': 1783,
                'hasSpec': 'n',
                'color': [u'红色', u'黑色', u'白色'],
                'size': ['XL', 'X', 'M', 'L'],
                'tag': [u'卫衣', u'衬衣', u'28寸', u'男士', u'女士', u'Coach', u'MK'],
                'addTime': '2017-01-15 18:20:30',
            }
        },
        {
            "_index": 'qmht-event',
            "_type": "product",
            "_id": 2,
            "_source": {
                'id': 2,
                'eventId': '1328',
                'title': u'【女表】浪琴(Longines)手表 军旗系列机械情侣表L4.274.4.12.6',
                'headImage': '/attached/image/products/longines/watches/L4.274.4.12.6-1.jpg',
                'stock': 10,
                'price': 1783,
                'hasSpec': 'n',
                'color': [u'红色', u'黑色', u'白色'],
                'size': ['XL', 'X', 'M', 'L'],
                'tag': [u'卫衣', u'衬衣', u'28寸', u'男士', u'女士', u'Coach', u'MK'],
                'addTime': '2017-01-15 18:20:30',
            }
        },

    ]
    helpers.bulk(esclient, actions=actions)


if __name__ == "__main__":
    index_obj_by_bulk()
    index_obj()
    print("Job Done")



