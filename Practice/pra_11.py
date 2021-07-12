# -*- coding: utf-8 -*-

"""
イテレータ
---------
    イテレータは，__next__メソッドを実装するオブジェクトのこと。
    一般にデータを操作するポインタ的な役割を担う。
    大きなデータをロードしてfor文を回すより，イテレータを用いて逐次的にデータを処理した方が効率的になる。
"""

# イテレータ作成
users = iter(['piyo', 'yado', 'usa'])

# イテレータを進める：users.__next__()

try:
    while True:
        print(users.__next__())
except StopIteration:
    print("End")
