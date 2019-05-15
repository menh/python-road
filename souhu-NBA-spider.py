from urllib.error import URLError
from urllib.request import urlopen

import re
import pymysql
import ssl
from pymysql import Error


#

def get_matched_parts(page_html, pattern_str, pattern_ignore_case = re.I):
    print ('get_matched_parts')
    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    print (pattern_regex.findall(page_html))
    return pattern_regex.findall(page_html) if page_html else []

def get_page_html(seed_url, *, retry_times = 3, charsets = ('utf-8',)):
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
        # print (page_html)
    except URLError:
        print ('URLError')
        if retry_times > 0:
            return get_page_html(seed_url, retry_times = retry_times -1, charsets = charsets)
    return page_html

def decode_page(page_bytes, charsets = ('utf-8',)):
    print ('decode_page')
    # print (page_bytes)
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            # print (page_html)
            break
        except UnicodeDecodeError:
            print('UnicodeDecodeError')
    return page_html

def start_crawl(seed_url, match_pattern, *, max_depth = -1):
    print ('connect..1')
    conn = pymysql.connect(host = 'gz-cdb-3p7z72sk.sql.tencentcdb.com', port = 62660,
                            database = 'chibei', user = 'root',
                            password = 'mh13582342871', charset = 'utf8')

    try:
        print ('connect..')
        with conn.cursor() as cursor:
            url_list = [seed_url]
            visited_url_list = {seed_url : 0}
            while url_list:
                current_url = url_list.pop(0)
                print ('current_url :' + current_url)
                depth = visited_url_list[current_url]
                if depth != max_depth:
                    page_html = get_page_html(current_url, charsets = ('utf-8', 'gbk', 'gb2312'))
                    links_list = get_matched_parts(page_html, match_pattern)
                    print (links_list)
                    param_list = []
                    for link in links_list:
                        print ('link :' + link)
                        if link not in visited_url_list:
                            visited_url_list[link] = depth + 1
                            page_html = get_page_html(link, charset = ('utf-8', 'gbk', 'gb2312'))
                            heading = get_matched_parts(page_html, r'<h1>(.*)<span')
                            if heading:
                                param_list.apend((headings[0], link))
                    cursor.executemany('insert into tb_result values (default, %s, %s)',
                                       param_list)
                    conn.commit()
    except Error:
        print ('connect Error')
    finally:
        conn.close()

def main():
    ssl._create_default_https_context = ssl._create_unverified_context

    start_crawl('http://sports.sohu.com/nba_a.shtml', r'<a[^>]+test=a\s[^>]*href=["\'](.*?)["\']',
                max_depth = 2)



if __name__ == '__main__':
    main()
