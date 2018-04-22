#!/usr/bin/env python
# encoding: utf-8

import sys
import requests
import json

class Weather(object):
    def __init__(self, city_name):
        self.city_name = city_name
        self.units = 'metric'
        self.api_key = 'YOUR_KEYS'
        self.api_url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&APPID={key}'
        self.icons = {
            'unknown': [
                "            ",
                "\033[38;5;250m    .--.    \033[0m",
                "\033[38;5;250m   (   _)   \033[0m",
                "\033[38;5;250m      (     \033[0m",
                "\033[38;5;250m      *     \033[0m",
                "             ",
            ],
            'clear sky': [
                "            ",
                "\033[38;5;226m    \\   /    \033[0m",
                "\033[38;5;226m     .-.     \033[0m",
                "\033[38;5;226m  ‒ (   ) ‒  \033[0m",
                "\033[38;5;226m     `-᾿     \033[0m",
                "\033[38;5;226m    /   \\    \033[0m",
                "            ",
            ],
            'few clouds': [
                "            ",
                "\033[38;5;226m   \\  /\033[0m      ",
                "\033[38;5;226m _ /\"\"\033[38;5;250m.-.    \033[0m",
                "\033[38;5;226m   \\_\033[38;5;250m(   ).  \033[0m",
                "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
                "             ",
            ],
            'scattered clouds': [
                "             ",
                "\033[38;5;250m     .--.    \033[0m",
                "\033[38;5;250m  .-(    ).  \033[0m",
                "\033[38;5;250m (___.__)__) \033[0m",
                "             ",
            ],
            'broken clouds': [
                "             ",
                "\033[38;5;240;1m     .--.    \033[0m",
                "\033[38;5;240;1m  .-(    ).  \033[0m",
                "\033[38;5;240;1m (___.__)__) \033[0m",
                "             ",
            ],
            'shower rain': [
                "            ",
                "\033[38;5;250m     .-.     \033[0m",
                "\033[38;5;250m    (   ).   \033[0m",
                "\033[38;5;250m   (___(__)  \033[0m",
                "\033[38;5;111m    ʻ ʻ ʻ ʻ  \033[0m",
                "\033[38;5;111m   ʻ ʻ ʻ ʻ   \033[0m",
                "             ",
            ],
            'rain': [
                "            ",
                "\033[38;5;240;1m     .-.     \033[0m",
                "\033[38;5;240;1m    (   ).   \033[0m",
                "\033[38;5;240;1m   (___(__)  \033[0m",
                "\033[38;5;21;1m  ‚ʻ‚ʻ‚ʻ‚ʻ   \033[0m",
                "\033[38;5;21;1m  ‚ʻ‚ʻ‚ʻ‚ʻ   \033[0m",
                "             ",
            ],
            'thunderstorm': [
                "            ",
                "\033[38;5;240;1m     .-.     \033[0m",
                "\033[38;5;240;1m    (   ).   \033[0m",
                "\033[38;5;240;1m   (___(__)  \033[0m",
                "\033[38;5;228;5m    ⚡   ⚡    \033[0m",
                "\033[38;5;228;5m       ⚡     \033[0m",
                "             ",
            ],
            'snow': [
                "            ",
                "\033[38;5;250m     .-.     \033[0m",
                "\033[38;5;250m    (   ).   \033[0m",
                "\033[38;5;250m   (___(__)  \033[0m",
                "\033[38;5;255m    *  *  *  \033[0m",
                "\033[38;5;255m   *  *  *   \033[0m",
                "             ",
            ],
            'mist': [
                "             ",
                "\033[38;5;251m _ - _ - _ - \033[0m",
                "\033[38;5;251m  _ - _ - _  \033[0m",
                "\033[38;5;251m _ - _ - _ - \033[0m",
                "             ",
            ],
        }

    def get_weather(self):
        url = self.api_url.format(city = self.city_name, unit = self.units, key = self.api_key)
        #print(url)
        response = requests.get(url)
        data = json.loads(response.text)

        print('\033[1m------ WEATHER (' + data['name'] + ') ------\033[0m')
        for icon in self.icons[data['weather'][0]['description']]:
            print(icon)
        '''
        for key in self.icons.keys():
            print('***', key, '***')
            for icon in self.icons[key]:
                print(icon)
            print('')
        '''
        print(data['weather'][0]['description'])
        print('')
        print(data['main']['temp'], '°C')
        print('  min:', data['main']['temp_min'], '°C')
        print('  max:', data['main']['temp_max'], '°C')
        print('')
        #print('--------')
        #data2 = json.dumps(data, indent=4, separators=(',', ': '))
        #print(data2)
