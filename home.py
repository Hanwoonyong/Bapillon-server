#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

def image_file():

    list = []
    data = []

    for root, dirs, file in os.walk('images'):
        list = file

    for i, j in enumerate(list):
        dict = {
            'id': i,
            'title': u'Title{}'.format(i),
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'image_url': 'http://192.168.2.101:5000/image?id={}'.format(i),
            'done': False
        }
        data.append(dict)

    return data

