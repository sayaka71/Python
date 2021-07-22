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

# 圧縮のアルゴリズム
with open("input.txt") as f:
    text = f.read()

# originalのファイルを情報が劣化しないように圧縮する
# 圧縮を行う関数：text_encode
# 復元を行う関数：text_decode

raw_text = text[:300]
print(f'raw text: {raw_text}\n')

# 圧縮を行う関数：text_encode
def text_encode(text):
    """
    10001 = 1[01] 0[03] 1[01]という法則でエンコードする
    myfile.txtに書き込んで圧縮ファイル作成
    """
    f = open('encode.txt', 'w')
    # first
    first_text = text[0]
    f.write(first_text)
    cnt = 1

    for _text in text[1:]:
        if _text == first_text:
            num = _text
            cnt += 1

        elif _text != first_text:
            if cnt < 10:
                cnt = '0' + str(cnt)
            f.write(str(cnt))
            first_text = _text
            cnt = 1
            f.write(first_text)

    if cnt < 10:
        cnt = '0' + str(cnt)
    f.write(str(cnt))
    f.close()

text_encode(raw_text)

with open("encode.txt") as f:
    encode_text = f.read()
print(f'encode text: {encode_text}')

# 復元を行う関数：text_decode
def text_decode(encode_text):
    f = open('decode.txt', 'w')
    idx_list = []
    for i in range(len(encode_text)):
        if i % 3 == 0:
            idx_list.append(int(encode_text[i]))
        elif i % 3 == 1:
            idx_list.append(int(encode_text[i:i+2]))

    for j in range(len(idx_list)):
        if j % 2 == 0:
            f.write(str(idx_list[j])*idx_list[j+1])

    f.close()

text_decode(encode_text)

with open("decode.txt") as f:
    decode_text = f.read()
print(f'decode text: {decode_text}')

print(raw_text == decode_text)
