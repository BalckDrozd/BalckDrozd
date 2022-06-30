from bs4 import BeautifulSoup
import requests
import random
from fake_useragent import UserAgent
import sqlite3

db = sqlite3.connect('Triangle_Kino.db')
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Triangle_Kino (
    ID INTEGER PRIMARY KEY,
    RESURS TEXT,
    NAME TEXT,
    GOD TEXT,
    OPISANIE TEXT,
    LINK_STR TEXT,
    RAIT_KP TEXT,
    RAIT_IMD
)''')
db.commit()

'''создание рандомных User-Aget для скрытия парсера в браузере'''
user_agent_list = []
for i in range(2):
    ua = UserAgent()
    user_agent_list.append(ua.firefox)
    user_agent_list.append(ua.safari)

user_agent = random.choice((user_agent_list))
headers = {'User-Agent': user_agent}

x = 1
summ = 0
url = "https://3lord.lordfilmo.site/filmy/"

while True:
    i = 0
    page = BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

    name_list = []
    god_list = []
    link_list = []
    opisanie_list = []
    kp_raiting_list = []
    imd_raiting_list = []

    for name in page.find_all("div", class_="th-title"):
        name_text = name.text
        name_list.append(name_text)
        print(name_text)
    for god in page.find_all("div", class_="th-year"):
        god_text = god.text
        god_list.append(god_text)
        print(god_text)
    for film in page.find_all("div", class_="th-item"):
        link_str = film.find("a", class_="th-in with-mask").get("href")
        link_list.append(link_str)
        print(link_str)

    for link_f in link_list:
        page2 = BeautifulSoup(requests.get(link_f, headers=headers).text, 'lxml')
        opisanie = page2.find("div", class_="fdesc clearfix slice-this").text
        b_split_list = opisanie.split('						')
        b1 = b_split_list[-1]
        opisanie_list.append(b1)
        kp_raiting = page2.find("div", class_="frate frate-kp")
        if kp_raiting != None:
            kp_raiting1 = kp_raiting.text
        else:
            kp_raiting1 = '0'
        kp_raiting_list.append(kp_raiting1)
        imd_raiting = page2.find("div", class_="frate frate-imdb")
        if imd_raiting != None:
            imd_raiting1 = imd_raiting.text
        else:
            imd_raiting1 = '0'
        imd_raiting_list.append(imd_raiting1)

    while i < len(name_list):
        name1 = name_list[i]
        god1 = god_list[i]
        opisanie1 = opisanie_list[i]
        link2 = link_list[i]
        rait_kp1 = kp_raiting_list[i]
        rait_imd1 = imd_raiting_list[i]
        cur.execute(
            '''INSERT INTO Triangle_Kino (RESURS, NAME, GOD, OPISANIE, LINK_STR, RAIT_KP, RAIT_IMD) VALUES (?, ?, ?, ?, ?, ?, ?);''',
            (
                url, name1, god1, opisanie1, link2, rait_kp1, rait_imd1))
        db.commit()
        print('Добавлено' + str(i))
        print(name1)
        i += 1
        summ += 1
        print(f'всего добавлено------{summ}')
    print(f'сраница>>>>>>{x}')
    x += 1

    url = "https://3lord.lordfilmo.site/filmy/page/" + str(x) + "/"
    if x == 813:
        break
