"""
Create by yy on 2019-07-24
"""

# get a md5 str
import hashlib
import time


def md5(s1):
    """
    This function can turn a str into a str which has been encrypted by md5

    :param s1: It's a str.
    :return: str
    """
    s = str(s1)
    h1 = hashlib.md5()
    h1.update(s.encode(encoding='utf-8'))
    s = h1.hexdigest()
    return s


def get_now_time_stamp():
    return int(time.time())


def get_date_time(time_stamp, date_format):
    """
    get a date which type is str
    :param time_stamp:
    :param date_format:
    :return:
    """
    time_arr = time.localtime(time_stamp)
    return time.strftime(date_format, time_arr)
