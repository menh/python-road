from time import time
from threading import Thread
import requests

class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1]
        resp = requests.get(self.url)
        with open('/Users/Hao/' + filename, 'wb) as f:
            f.write(resp.content)

    def main():
        resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')

        data_model = resp.json()


    super().__init__()
    self.url = url
