import requests
from bs4 import BeautifulSoup

def  get_html():
    """"获取html信息"""
    r = requests.get("https://www.runoob.com")
    text = r.content.decode('utf-8')
    soup = BeautifulSoup(text, 'lxml')
    index_nav = soup.find(id="index-nav")
    li_list = index_nav.find_all('li')
    for li in li_list:
        print(li.text)
    # index = soup.find(class_='xxx')
    # print(index_nav)

if __name__ == '__main__':
    get_html()
