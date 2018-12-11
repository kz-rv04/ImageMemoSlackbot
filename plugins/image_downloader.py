import codecs
import os
import urllib.request
import urllib.error
from datetime import datetime as dt

class ImageDownloader:
    def __init__(self, slack_token):
        self.SLACK_TOKEN = slack_token
        self.headers = {
            'User-Agent' : 'Mozilla/5.0 SlackBot',
            'Authorization': 'Bearer %s' % self.SLACK_TOKEN
        }
        datadir = os.path.abspath(os.path.join(__file__, '../..'))
        datadir = os.path.join(datadir, 'data')
        tdatetime = dt.now()
        dirname = tdatetime.strftime('%Y-%m-%d')
        self.SAVE_PATH = os.path.join(datadir, dirname)

    def download_image(self, url, filename, token):
        path = ''
        try:
            req = urllib.request.Request(url, headers=self.headers)
            data = urllib.request.urlopen(req).read()

            if not os.path.exists(self.SAVE_PATH):
                os.mkdir(self.SAVE_PATH)
            path = os.path.join(self.SAVE_PATH, filename)
            with codecs.open(path, mode="wb") as f:
                f.write(data)
            print("saved:", path)
        except urllib.error.URLError as e:
            print(e)

        return path

