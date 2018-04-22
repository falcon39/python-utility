import sys
import datetime
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
    view_weather('Tokyo')
    view_news()

def view_calendar(year, month, day):
    print('')
    print('\033[1m------ CALENDAR ------\033[0m')

    cal = Calendar(year, month, day)

    line2 = cal.get_calendar_year(year)
    line3 = list(map(list, zip(*line2)))

    print('')

    for x in line3:
        print("  ".join(x[:4]))

    for x in line3:
        print("  ".join(x[4:8]))

    for x in line3:
        print("  ".join(x[8:]))

def view_weather(city_name):
    weather = Weather(city_name)
    weather.get_weather()

def view_news():
    news = News()
    news.get_headlines()

if __name__ == '__main__':
    main()
