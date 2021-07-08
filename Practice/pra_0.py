# practice for decorater
# 2021.06.03
# @sayaka

"""
POINT: 関数もオブジェクトです！
        → 関数の引数，関数の戻り値に"関数を変数として"使える。
"""

# デコレーター関数を定義
def multiple(x):
    def _multiple(f):
        def new_f(*args, **kwds):
            result = f(*args, **kwds)
            return result * x
        return new_f
    return _multiple

# decoraterを指定
@multiple(3)
# 修飾される関数
def kobuta(y):
    return y


