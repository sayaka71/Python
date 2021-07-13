# Intoroduction

"""
bitとbyte:
    0 or 1 しかコンピュータは扱えない。
    1 bit = 2^1
    8 bit = 2^8 = 256 パターン
    8 bit = 1 byte
"""

a = 3 # 整数(integer)
print(type(a))

b = 1.5 # 実数(float)
print(type(b))

name1 = "あい"
name2 = "うえお"
name3 = name1 + name2
age = 22

print(type(name3))
print(name3)

# 練習問題
# name1, name2, ageを使って
# '私はあいうえおです。22歳です。'
# と表示するプログラムを作成。
print('私は{}です。{}です。'.format(name3, age))
print('私は' + name3 + 'です。' + str(age) + 'です。') #ageを文字列に直して型を整える
