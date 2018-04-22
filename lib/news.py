#!/usr/bin/env python
# encoding: utf-8

import sys
import requests
import json

class News(object):
    def __init__(self):
        self.api_key = 'YOUR_KEYS'
        self.api_url = 'https://newsapi.org/v2/top-headlines?sources=google-news&apiKey={key}'

    def get_headlines(self):
        url = self.api_url.format(key = self.api_key)
        #print(url)
        response = requests.get(url)
        data = json.loads(response.text)

        print('\033[1m------ NEWS ------\033[0m')

        #print(data['totalResults'])
        for i in range(data['totalResults']):
            #'\033[38;5;245;1m' + header_month[:21] + '\033[0m'
            print('\033[1;33m' + data['articles'][i - 1]['title'] + '\033[0m')
            print(data['articles'][i - 1]['description'])
            print('\033[34m' + data['articles'][i - 1]['url'] + '\033[0m')
            print('')
        #print('--------')
        #data2 = json.dumps(data, indent=4, separators=(',', ': '))
        #print(data2)
