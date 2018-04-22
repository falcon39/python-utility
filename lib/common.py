import configparser

class Common(object):
    def __init__(self):
        self.month_name = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
        self.weekday_name = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
        self.month_num = 12

class ConfigUtil(object):
    def __init__(self):
        self.config_file = r'./settings.ini'
        self.cp = configparser.ConfigParser()
        self.cp.read([self.config_file])

    def get(self, section, key):
        config = configparser.ConfigParser()
        config.read(self.config_file)

        data = config.get(section, key)
        return data
