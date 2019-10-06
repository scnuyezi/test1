import configparser

class MyConfigParser(configparser.ConfigParser):
    #configparser默认识别options不区分大小写，而caps启动需要识别大小写，所以重写optionxform
    def __init__(self):
        configparser.ConfigParser.__init__(self)

    def optionxform(self,optionstr):
        return optionstr

def applist():
    myparser = MyConfigParser()
    myparser.read('../config/apps.ini')
    applist= {}
    for item in myparser.sections():
        app = {}
        for keys in myparser.items(item):
            app[keys[0]] = keys[1]
        applist[item]=app
    return applist

def get_jdjr():
    mylist = applist()
    return mylist['jdjr']['appActivity'],mylist['jdjr']['appPackage']

if __name__ == '__main__':
    print(get_jdjr())
    print(get_jdjr()[0])