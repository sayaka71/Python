#　# -*- coding: utf-8 -*-
# Python 入門
# re モジュールの正規表現

"""
Script
------
正規表現とコマンドライン引数を学習するためのスクリプト。

Parameters
----------
-i, --input: words
-d, --date: date

Usage
-----
for example: 
    $ python3 pra_9.py -i "Apple"
"""

# Import re for regex (正規表現)
import re

# Import argparse for command-line options
import argparse

# Create object for parsing command-line options
parser = argparse.ArgumentParser(description="Add words that\
 you like.(ex. hiyoko)")
# Add argument which takes words as an input
parser.add_argument("-i", "--input", type=str, default = "Python",
    help="Add Words")
# Add argument which takes date as an input
parser.add_argument("-d", "--date", type=str, default = "2021/07/11",
    help="Add Date")
# Parse the command line arguments to an object
args = parser.parse_args()
print(args)

# re.compile で正規表現 object 作成 
re_word = "[pP]y"
pattern = re.compile(re_word)
print("\nPattern: " + re_word)

# search で検索
result_search = pattern.search(args.input)
print_search = "Search Result: "

if result_search is None:
    print(print_search + "NG")
else:
    print(print_search + "OK")

# sub で置換
result_sub = pattern.sub("piyo", args.input)
print_sub = "Sub Result: "

if result_sub is None:
    print(print_sub + "NG")
else:
    print(print_sub + result_sub)

# findall で部分一致したキーワードを手軽に抽出できる
html = '<a href="https://github.com/aaren/wavelets/blob/master/wavelets/transform.py">wavelet</a>'
result_findall_list = re.findall('<a href="(https://[^"]+?)">([^<]+?)</a>', html)

print_findall = "Findall Result: "

if result_findall_list is None:
    print(print_findall + "NG")
else:
    print(print_findall)
    print(result_findall_list)