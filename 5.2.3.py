from itertools import combinations

# 20, 20 , 20
# 10, 10, 10, 10, 10
# 5, 5
# 1, 1, 1, 1, 1,

wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
comb15 = combinations(wallet, 15)
comb14 = combinations(wallet, 14)
comb13 = combinations(wallet, 13)
comb12 = combinations(wallet, 12)
comb11 = combinations(wallet, 11)
comb10 = combinations(wallet, 10)
comb9 = combinations(wallet, 9)
comb8 = combinations(wallet, 8)
comb7 = combinations(wallet, 7)
comb6 = combinations(wallet, 6)
comb5 = combinations(wallet, 5)
comb4 = combinations(wallet, 4)
comb3 = combinations(wallet, 3)

listC = list(comb15) + list(comb14) + list(comb13) + list(comb12) + list(comb11) + list(comb10) + \
        list(comb9) + list(comb8) + list(comb7) + list(comb6) + list(comb5) + list(comb4) + list(comb3)

listF = []
for x in listC:
    if x not in listF:
        if sum(x) == 100:
            listF.append(x)

# list = [0]
# listW = []
#
#     for i in wallet:
#         for x in list:
#             if x < 100:
#                 list[list.index(x)] = x+i
#                 listW.append(i)


print(dir(listF))
# for x in perm:
#     for y in perm:
#         if x == y:
#             permList.remove(x)
