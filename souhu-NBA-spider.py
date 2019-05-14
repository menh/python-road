from urllib.error import URLError
from urllib.request import urlopen

import re
import pymysql
import ssl
from pymysql import Error

#
def start_crawl(seed_url, match_pattern, *, max_depth = -1):
    conn = pymysql.connect(host = 'localhost', port = 3306,
                            database = 'chibei', user = 'root',
                            password = '123456', chatset = 'utf-8')

    try:
        with conn.cursor() as cursor:
            usr_list = [seed_url]
            visited_url_list = {seed_url : 0}
            while url_list:
                current_url = url_list.pop(0)
                depth = visited_url_list[current_url]
