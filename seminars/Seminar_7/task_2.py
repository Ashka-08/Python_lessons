# a = [4, 3, -10, 1, 7, 12] превратить в a=[4, -10, 12, 3, 1, 7]

# a = [4, 3, -10, 1, 7, 12]
# a.sort(reverse=True, key=lambda x: x % 2 == 0)
# print(a)

a = [4, 3, -10, 1, 7, 12]
a.sort(key=lambda x: x%2)
print(a)


# r = [a[0], a[2], a[5], a[1], a[3], a[4]]
# print(r)

# res = []
# for i in a:
#     if i % 2 == 0:
#         res.append(i)
# for i in a:
#     if i % 2 != 0:
#         res.append(i)
# print(res)