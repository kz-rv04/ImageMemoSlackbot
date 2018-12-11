import os
import codecs
import glob
import random


def read_text():
    datadir = os.path.abspath(os.path.join(__file__, '../..'))
    datadir = os.path.join(datadir, 'text')

    files = glob.glob(datadir+'/*/*')
    file = files[random.randint(0, len(files) - 1)]

    text = ''
    with codecs.open(file, mode='r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    return text

def delete_text(path):
    if os.path.exists(path):
        os.remove(path)

# if __name__ == '__main__':
#     print(read_text())