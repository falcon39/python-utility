#!/usr/bin/env python
# encoding: utf-8

import sys
import requests
import json
from lib.common import ConfigUtil

class News(object):
    def __init__(self):
        config = ConfigUtil()
        self.api_key = config.get('news', 'api_key')
        self.api_url = config.get('news', 'api_url')

    def get_headlines(self):
        url = self.api_url.format(key = self.api_key)
        #print(url)
        response = requests.get(url)
        data = json.loads(response.text)

        print('\033[1m------ NEWS ------\033[0m')

        for i in range(data['totalResults']):
            print('')
            print('\033[1;33m' + data['articles'][i - 1]['title'] + '\033[0m')
            print(data['articles'][i - 1]['description'])
            print('\033[34m' + data['articles'][i - 1]['url'] + '\033[0m')

        print('')
        #print('--------')
        #data2 = json.dumps(data, indent=4, separators=(',', ': '))
        #print(data2)
