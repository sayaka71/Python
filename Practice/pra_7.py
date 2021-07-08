# Python入門
# 例外情報を取り出す (p.252)

# 例外インスタンスの取得
try:
    x = 1/0
except ZeroDivisionError as instance_z:
    print(instance_z)

# トレースバックの表示
import sys
import traceback
try:
    f = open("temp.txt", "r")
except IOError:
    error_type, error_value, traceback_ = sys.exc_info()
    tb_list = traceback.format_tb(traceback_)
    print("Error Type: {}\nError Value: {}\nTraceback: {}".format(error_type, error_value, tb_list))
print()

# raise: 例外を発生させる
# 独自の例外
# Exceptionクラスを継承して例外クラスをつくる。
class RangeError(Exception):
    """
    Exceptionクラスを継承して独自の例外クラスを作成
    """
    pass

print()
def get_grade(score):
    if score < 5 or score >990:
        # 例外を発生させる
        raise RangeError(score)
    return int(score/990)
    
try:
    get_grade(1)
except RangeError:
    print("too high or too low")

print()
get_grade(1)