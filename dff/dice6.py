nums = input('Введите числа через пробел: ').split()
nums = [int(i) for i in nums]
target = 9
print(nums)

for i in nums:
    k = target - i
    if k in nums:
        print(nums.index(k), nums.index(i))
