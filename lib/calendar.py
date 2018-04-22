import math
import datetime
from lib.common import Common

class Calendar(object):
    def __init__(self, year, month, day):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        '''
        self.month_name = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
        self.weekday_name = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
        self.month_num = 12
        '''
        self.all_days = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]]

    '''
    当月日付をリスト形式で取得
    '''
    def get_day_list(self, year, month):
        month = int(month)
        year = int(year)
        days = self.all_days[month - 1]

        # うるう年の場合、要素の末尾("29")を削る
        if not self.check_leapyear(year):
            #print(str(year) + "年はうるう年じゃないよ")
            if(month == 2):
                #print("うるう年じゃない2月です〜")
                days.pop()

        weekday = self.get_weekday(year, month, 1)
        for w in range(weekday):
            days.insert(0, '')

        for w in range(14):
            days.append('')

        _out = days[:42]

        out = [days[i:i+7] for i in range(0, len(_out), 7)]

        return out

    '''
    うるう年判定
    '''
    def check_leapyear(self, year):
        if year % 400 == 0: return True
        if year % 4 == 0 and year % 100 == 0: return False
        if year % 4 == 0: return True

        return False

    '''
    曜日判定

    戻り値:
        0 = 日曜日
        1 = 月曜日
        2 = 火曜日
        3 = 水曜日
        4 = 木曜日
        5 = 金曜日
        6 = 土曜日
    '''
    def get_weekday(self, year, month, day):
        year = int(year)
        month = int(month)
        day = int(day)
        if(month == 1 or month == 2):
            month += 12; year -= 1
        y = year % 100
        c = int(math.floor(year/100))
        m = month
        d = day
        w = int (y+ math.floor(y/4) + math.floor(c/4) -2*c+ math.floor(26*(m+1)/10) +d-1)
        w = w % 7
        if (w < 0):
            w += 7
        return w

    def get_calendar_month(self, year, month):
        line = ['', '', '', '', '', '', '', '', '']
        cnt = 0

        common = Common()

        header_month = common.month_name[month - 1] + "                          "
        line[cnt] += '\033[38;5;245;1m' + header_month[:21] + '\033[0m'
        cnt += 1

        line[cnt] += ' '.join(map(str, common.weekday_name)) + " "
        cnt += 1

        d = datetime.datetime.today()

        for s1 in self.get_day_list(year, month):
            s5 = ''
            for s2 in s1:
                s3 = '{: >2}'.format(s2)

                if s2 != '':
                    if year == d.year and month == d.month and s2 == d.day:
                        #s4 = '\033[31m' + s3 + '\033[0m'
                        s4 = '\033[38;5;226m' + s3 + '\033[0m'
                    elif self.get_weekday(year, month, s2) == 0:
                        s4 = '\033[31m' + s3 + '\033[0m'
                    elif self.get_weekday(year, month, s2) == 6:
                        s4 = '\033[36m' + s3 + '\033[0m'
                    else:
                        s4 = s3
                else:
                    s4 = s3
                s5 += s4 + " "
            line[cnt] += s5
            #line[cnt] += "  "
            cnt += 1
        return line

    def get_calendar_year(self, year):
        column_num = 3
        row_num = math.floor(12 / column_num)
        target_month = 1
        flg_exit = False
        list_month = ['', '', '', '', '', '', '', '', '', '', '', '']

        common = Common()

        for i in range(row_num):
            for j in range(column_num):
                if target_month > common.month_num:
                    flg_exit = True
                    break
                else:
                    list_month[target_month - 1] = self.get_calendar_month(year, target_month)
                    target_month += 1
            if flg_exit:
                break
        return list_month
