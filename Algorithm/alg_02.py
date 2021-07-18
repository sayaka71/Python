# 圧縮のアルゴリズム

# 問題：ふたつの和を計算する関数addを作成せよ
def add(a,b):
    return a+b

print(add(30,10))

# 四則演算の結果を返す関数calcを作成せよ
def calc(a,b):
    return a+b, a-b, a/b, a*b

print(calc(4,5))

# 右と左を入れ替えるexchange
def exchange(a,b):
    tmp = a
    a = b
    b = tmp
    return a, b

print(exchange(3,4))

# リストの和を計算するadd_list
def add_list(list):
    result = 0
    for i in range(len(list)):
        result += list[i]
    return result

test_list1 = [3,5,7,10]
print(add_list(test_list1))

# リスト同士の和add_lists（可読性！）
def add_lists(list_a, list_b):
    result = []
    for (_list_a, _list_b) in zip(list_a, list_b): # Point: forで取り出す変数の前に`_`をつける。zipでそれぞれiter回す。
        result.append(_list_a + _list_b)
    return result

test_list2 = [1,2,3,4]
print(add_lists(test_list1, test_list2))

# 要素数の違うリスト同士の和になるとerrorと表示する
def add_lists(list_a, list_b):
    result = []
    try:
        for i in range(len(list_a)):
            result.append(list_a[i] + list_b[i])
        print(result)
    except IndexError:
        print("error")

test_list2 = [1,2,3,4]
test_list3 = [1,4,2]
add_lists(test_list1, test_list3)
