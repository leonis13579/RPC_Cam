from datetime import datetime

class Trace:

    def print_info(self, info):
        print(datetime.now().strftime("%d.%m.%Y %H:%M:%S") + "\t[INFO]\t" + info)

    def print_detection(self, detection):
        print(datetime.now().strftime("%d.%m.%Y %H:%M:%S") + "\t[DETECTION]\t" + detection)

    def print_patrol(self, patrol):
        print(datetime.now().strftime("%d.%m.%Y %H:%M:%S") + "\t[PATROL]\t" + patrol)
