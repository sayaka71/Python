# 文法の復習
# ラムダ関数
# lambda x: x%2 == 0
# lambda name: print('Hi!' + name)
is_even = lambda x: x%2 == 0
print(is_even(2))
print(is_even(3))

# 関数みたいに使う(defで定義するのとあんまり変わらん)
say_hi = lambda name: print('Hi!' + name)
say_hi('Sayaka')

# 使い捨て関数(本来の使い方)
print(list(map(lambda x: x*2, [1,2,3])))

# filterで，配列の奇数飲みをフィルタリング
odd_list = list(filter(lambda x: x%2==1, [1,2,3,4,5,6,7]))
print(odd_list)

# sortedの並び替え基準の設定
sort_list = list(sorted(['pig', 'piggy', 'pi'], key=lambda x: len(x)))
print(sort_list)