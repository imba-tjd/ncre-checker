import urllib.request
import time
from datetime import date
from threading import Thread
from pathlib import Path
import logging
import sys


check_content = '2024年9月全国计算机等级考试成绩、证书查询开通'
# check_content = 2024年9月全国计算机等级考试报名工作启动

sendkey = '<SENDKEY>'


def fetch():
    checked_date = None

    while True:
        if checked_date == date.today():
            time.sleep(1*60*60)
            continue
        checked_date = date.today()

        try:
            req = urllib.request.Request('https://ncre.neea.edu.cn/html1/category/1507/872-1.htm', headers={'User-Agent': ''})
            with urllib.request.urlopen(req) as resp:
                html = resp.read().decode()
            if check_content in html:
                if sendkey != '<SENDKEY>':
                    urllib.request.urlopen(f'https://sctapi.ftqq.com/{sendkey}.send?title=ncre').close()
                logging.warning('%s yes', time.ctime())
            else:
                logging.info('%s ok', time.ctime())
        except:
            logging.exception('%s', time.ctime())


async def app(scope, receive, send):
    await send({
        'type': 'http.response.start',
        'status': 200,
    })
    await send({
        'type': 'http.response.body',
        'body': b'NCRE ' + started + b' started<br>' + Path('log.txt').read_bytes().replace(b'\n', b'<br>'),
    })


started = str(date.today()).encode()
print('NCRE', started, 'started')

if __name__ != '__main__' or sys.executable.endswith('pythonw.exe'):
    logging.basicConfig(level=logging.INFO, filename='log.txt')

if __name__ == '__main__':
    fetch()
else:
    Thread(target=fetch, daemon=True).start()
