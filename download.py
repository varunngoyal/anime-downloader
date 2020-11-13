import urllib.request
import argparse
import wget
from read_file import read_file
import requests
import shutil
import time
import sys

filename = "img1"

parser = argparse.ArgumentParser(description='filepath')
parser.add_argument(
    '-p', default='https://www.bikano.com/images/5969Chips-Chatak%20Masala.png')
args = parser.parse_args()


def downloadFileUrllib():
    urllib.request.urlretrieve(args.p, filename)


def bar_custom(current, total, width=80):
    print("Downloading: %d%% [%d / %d] bytes" %
          (current/total * 100, current, total))


def wget_file():
    r = read_file()
    urls_list = r.read_urls_from_file()
    for url in urls_list:
        wget.download(url)


def requests_file():
    r = read_file()
    urls_list = r.read_urls_from_file()
    i = 1
    for url in urls_list:
        r = requests.get(url, allow_redirects=True, stream=True,
                         headers={'User-agent': 'Mozilla/5.0'})

        filename = str(r.headers['Content-Disposition'][22:-1])

        if r.status_code == 200:
            print('downloading ', filename, '...')

            with open(filename, "wb") as f:
                dl = 0
                total_length = int(r.headers.get('content-length'))
                for data in r.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(100*dl / total_length)
                    sys.stdout.write("\r[%s%s] %.2f/%.2f MB" %
                                     ('='*done, ' '*(100-done),
                                      dl/(1024*1024), total_length/(1024*1024)))
                    sys.stdout.flush()

            print('\nfile', filename, 'saved successfully!')

            print('waiting for 1 second....')
            time.sleep(10)
            i = i+1


if __name__ == '__main__':
    # downloadFileUrllib()
    # wget_file()
    requests_file()
