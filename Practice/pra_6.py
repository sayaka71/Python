# stack スタックの練習
# 独学プログラマー
# *argsの練習にもなった。解凍演算子の使い方次第でリストをマージできたりするけど，推奨されていない。

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, *args):
        # Iterating over the Python args tuple
        for item in args:
            self.items.append(item)
        return self.items

    def pop(self):
        # 1番上をとってくる。もとのやつから削除。
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

st = Stack()
print(st.is_empty())
st.push(1,2,3)
# print(st.pop())
# >>> 3
# print(st.items)
# >>> [1,2]

# 数字リストを逆順にする。
gyaku = []
for i in range(st.size()):
    gyaku.append(st.pop())

print(gyaku)

# 文字列を逆順に
for c in "gyaku":
    st.push(c)

print(st.items)

reverse = ""

while st.size():
    reverse += st.pop()

print(reverse)
