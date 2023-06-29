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


def main ():
    print(make_law_number_list())
    print("--------------------")
    print(len(make_law_number_list()))

if __name__ == '__main__':
    main()