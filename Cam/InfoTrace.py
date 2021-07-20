from datetime import datetime


def print_info(info):
    print(datetime.now().strftime("%d.%m.%Y %H:%M:%S") + "\t[INFO]\t" + info)

def print_detection(detection):
    print(datetime.now().strftime("%d.%m.%Y %H:%M:%S") + "\t[DETECTION]\t" + detection)
