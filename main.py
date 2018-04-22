import sys
import datetime
import math
from lib.common import ConfigUtil
from lib.calendar import Calendar
from lib.weather import Weather
from lib.news import News

def main():
    argv = sys.argv
    argc = len(argv)

    #引数がなかった時は日付を突っ込む
    d = datetime.datetime.today()

    if(argc < 2):
    	year = d.year
    else:
        year = argv[1]

    if(argc < 3):
    	month = d.month
    else:
        month = argv[2]

    if(argc < 4):
        day = d.day
    else:
        day = argv[3]

    view_calendar(year, month, day)
    view_weather()
    view_news()

def view_calendar(year, month, day):
    print('')
    print('\033[1m------ CALENDAR ------\033[0m')

    cal = Calendar(year, month, day)

    line2 = cal.get_calendar_year(year)
    line3 = list(map(list, zip(*line2)))

    print('')
    config = ConfigUtil()
    column_num = int(config.get('calendar', 'column_num'))
    row_num = math.floor(12 / column_num)
    #print('column_num:', column_num, 'row_num:', row_num)

    for r in range(row_num):
        for x in line3:
            print("  ".join(x[column_num*r:column_num*(r+1)]))


def view_weather():
    weather = Weather()
    weather.get_weather()

def view_news():
    news = News()
    news.get_headlines()

if __name__ == '__main__':
    main()
