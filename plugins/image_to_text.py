import sys
import codecs
import os
import urllib.request
import urllib.error
from datetime import datetime as dt

from PIL import Image

import pyocr
import pyocr.builders

class ImageToText:
    def __init__(self, lang='jpn'):
        self.text = ''
        self.lang = lang
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("No OCR tool found")
            sys.exit(1)
        self.tool = tools[0]
        print("Will use tool '%s'" % (self.tool.get_name()))
        self.langs = self.tool.get_available_languages()
        print("Available languages: %s" % ", ".join(self.langs))

        datadir = os.path.abspath(os.path.join(__file__, '../..'))
        datadir = os.path.join(datadir, 'text')
        tdatetime = dt.now()
        dirname = tdatetime.strftime('%Y-%m-%d')
        self.SAVE_PATH = os.path.join(datadir, dirname)

    def image_to_text(self, path):
        txt = self.tool.image_to_string(
            Image.open(path),
            lang=self.lang,
            builder=pyocr.builders.TextBuilder()
        )
        if txt:
            self.save_text(txt)

        return txt

    def save_text(self, text):
        filename = dt.now().strftime('%Y%m%d%H%M%S')
        savepath = os.path.join(self.SAVE_PATH, filename+'.txt')

        if not os.path.exists(self.SAVE_PATH):
            os.mkdir(self.SAVE_PATH)

        with codecs.open(savepath, mode='w', encoding='utf-8', errors='ignore') as f:
            f.write(text)
        print("saved: ",savepath)


            # if __name__ == '__main__':
#     img_to_text = ImageToText(lang='jpn')
#     path = '/usr/local/www/slackbot/data/2018-12-07/news.png'
#     text = img_to_text.image_to_text(path)
#     print("image to text: ")
#     print(text)