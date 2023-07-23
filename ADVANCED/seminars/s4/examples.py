# про распаковку

# example 1
nums = list('1234567890')
print(nums) #['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def to_int(num):
    return int(num)


list_nums = map(to_int, nums)

print(*list_nums) #1 2 3 4 5 6 7 8 9 0


# example 2
tpl = (1, 2, 3, 4, 5, 6)

a, b, c, d, e, f = tpl

print(a, b, c, d, e, f) # 1 2 3 4 5 6


# example 3
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

a, b, c, d, e, *f = tpl

print(a, b, c, d, e, f) #1 2 3 4 5 [6, 7, 8, 9, 0]

# example 4
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

*a, b, c, d, e, f = tpl

print(a, b, c, d, e, f) #[1, 2, 3, 4, 5] 6 7 8 9 0


# example 5
tpl = list('1234567890')
print(list(zip(*tpl))) #[('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')]