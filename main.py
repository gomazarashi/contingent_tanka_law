import requests
from pprint import pprint
import re
from xml.etree import ElementTree
from functools import lru_cache

#法令番号のリストを作成する関数
def make_law_number_list(category=1):
    url = f"https://elaws.e-gov.go.jp/api/1/lawlists/{category}"
    response = requests.get(url)
    root = ElementTree.fromstring(response.content.decode(encoding="utf-8"))
    numbers = [e.text for e in root.iter() if e.tag == "LawNo"]
    return numbers

#法令番号を指定して法令を取得する関数
def get_law_text(law_number):
    url=f"https://elaws.e-gov.go.jp/api/1/lawdata/{law_number}"
    response = requests.get(url)
    root = ElementTree.fromstring(response.content.decode(encoding="utf-8"))
    contents = [e.text.strip() for e in root.iter() if e.text]
    return [text.replace('\u3000', '') for text in contents if text] #全角スペースを削除


def main ():
    print(get_law_text(law_number="昭和二十二年勅令第百六十五号"))

if __name__ == '__main__':
    main()