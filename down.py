import urllib.request
import argparse
import wget
from read_file import read_file


filename = "img1"

parser = argparse.ArgumentParser(description='filepath')
parser.add_argument('-p', default='https://www.bikano.com/images/5969Chips-Chatak%20Masala.png')
args = parser.parse_args()

def downloadFileUrllib():
    urllib.request.urlretrieve(args.p, filename)

def bar_custom(current, total, width=80):
    print("Downloading: %d%% [%d / %d] bytes" % (current/total * 100 , current, total))

def wget_file():
    r = read_file()
    urls_list = r.read_urls_from_file()
    for url in urls_list:
        wget.download(url, bar=bar_custom)

#downloadFileUrllib()
wget_file()

