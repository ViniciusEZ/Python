# add, update, clear, discard
# union |
# intersection &
# difference -
# symmetric difference ^

# s1 = {1,2,3,4,5}
# print(s1)
# s1 = set()
# s1.update([1,2,3,4,5], {5,6,7,8,9})
# print(s1)
# l1 = [1,2,3,4,5,5,5,5,2,4,5,'Vinicius', 'Vinicius']
# l1 = set(l1)
# l1 = list(l1)
# print(l1)
#
# s1 = {1,2,3,4,5,11,12,13}
# s2 = {1,2,3,4,5,6,7,8,9,10}
# s3 = s1 ^ s2
# print(s3)

l1 = ['Beatriz', 'João', 'Magno']
l2 = ['Magno', 'João','João','João','João','João','João',
      'João','João','Beatriz', 'Beatriz']

l1 = list(set(l1))
l2 = list(set(l2))
print(l1, l2)