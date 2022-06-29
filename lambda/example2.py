from functools import reduce

monday = [32, 543, 7456, 23, 65, 675, 32, 14, 65, 10]
tuesday = [3, 2, 43, 65, 76, 532, 4, 1, 65, 90]
wednesday = [32, 32532, 543, 67, 123, 534, 765324, 56, 9067, 4235]
thursday = [31, 423, 6345, 123, 654876, 854, 432, 654, 8768, 312]
friday = [321, 235, 76, 876, 432, 547, 876, 312, 453, 2893]

days = [monday, tuesday, wednesday, thursday, friday]
a = map(lambda x: sum(x) , days)
print(sum(list(a)) * 20)
a1 = reduce(lambda total, x: total + sum(x),days, 0)
print(a1 * 20)


print(sum(wednesday))

soma = 0
for i in range(0, len(days)):
    for i2 in range(0, len(days[i])):
        soma += days[i][i2]
print(soma * 20)
