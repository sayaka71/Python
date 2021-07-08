# 2021.06.28
# 線形探索（番兵）

def banpei(l,t):
    l.append(t)
    i = 0
    while l[i]!=t:
        i += 1
    print("i:{}, num:{}".format(i, t))

l = [2,3,4,1,6,7,8,10,9,2,3]
t = 10
banpei(l,t)