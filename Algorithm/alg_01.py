# Intoroduction

"""
bitとbyte:
    0 or 1 しかコンピュータは扱えない。
    1 bit = 2^1
    8 bit = 2^8 = 256 パターン
    8 bit = 1 byte

複数の変数:
    - リスト (a = [1,2,3], a[1]で抽出, a[0:2] => 1,2)
    - タプル (書き換えのできないリスト、(1,2,3)でかく)
    - 辞書 (d = {'りか': 23, 'ぴよ': 21}, d['ぴよ'])

アクセス:
    - []: 要素へのアクセス
    - (): 関数へのアクセス
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

# List
p = [1,3,10,17]
print(p[2:] + p[-2:])

# タプル
t = (1,2,3)
print(t[2])
# t[2] = 10は不可能

# for文
names = ['井上', '小林', '佐藤', '山田']
for name in names:
    print('{}さん，こんにちは。'.format(name))

# if文
num = 4
def hantei(num):
    if num%2==0:
        print('偶数です。')
    elif num%2==1:
        print('奇数です。')
hantei(num)


# 演習課題
"""
問題：
    1万までの素数を表示するプログラムを書いてください
発展：
    スピードアップを図ってください
"""

def sosu(max):
    """
    素数：1とその数しか公約数を持たない数（1,2,3,5,7,11...）
    アルゴリズム：地道に公約数を探して判定する
    - num: 判定される数
    - i: 割ってみるのに使うための数
    - k: 公約数の個数
    """
    for num in range(1,max+1):
        i = num
        k = 0
        while i>0 or k<2:
            i -= 1

            if i==0:
                break

            elif num%i==0:
                k += 1

        
        if k==1:
            print(num, k, i)

# 時間
import time

# 処理前の時刻
t1 = time.time()

# 処理
sosu(100)

# 処理後の時刻
t2 = time.time()
 
# 経過時間を表示
elapsed_time = t2-t1
print(f"経過時間：{elapsed_time}")

# 経過時間：0.0006620883941650391

# 解答1
def gem_prime1(max):
    numbers = []
    for i in range(1,max+1):
        flag = True # 判定フラグ
        for j in range(2,i):
            if i%j==0:
                flag = False
        if flag:
            numbers.append(i)
    print(numbers)

# 処理前の時刻
t1 = time.time()

# 処理
gem_prime1(1000)

# 処理後の時刻
t2 = time.time()
 
# 経過時間を表示
elapsed_time = t2-t1
print(f"gem_prime1 経過時間：{elapsed_time}")


# 高速化する
# 一つでも割り切れていたらループから抜ける(break)
# 解答2
def gem_prime2(max):
    numbers = []
    for i in range(1,max+1):
        flag = True # 判定フラグ
        for j in range(2,i):
            if i%j==0:
                flag = False
                break
        if flag:
            numbers.append(i)
    print(numbers)

# 処理前の時刻
t1 = time.time()

# 処理
gem_prime2(1000)

# 処理後の時刻
t2 = time.time()
 
# 経過時間を表示
elapsed_time = t2-t1
print(f"gem_prime2 経過時間：{elapsed_time}")

# さらに高速化する
# 2,3,4,5,6,7で順に割っていくのではなく，すでに持っている素数(numbers)で割っていく
# 自分で考えれたので多分天才かも
def gem_prime3(max):
    numbers = [1]
    for i in range(2,max+1):
        flag = True # 判定フラグ
        for j in numbers[1:len(numbers)+1]: 
            if i%j==0:
                flag = False
                break
        if flag:
            numbers.append(i)

    print(numbers)

# 処理前の時刻
t1 = time.time()

# 処理
gem_prime3(1000)

# 処理後の時刻
t2 = time.time()
 
# 経過時間を表示
elapsed_time = t2-t1
print(f"gem_prime3 経過時間：{elapsed_time}")