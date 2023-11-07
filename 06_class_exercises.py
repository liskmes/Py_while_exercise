
# i = 0
# num = 0

# while i < 100:
#     num = num + 1
#     print(num)

#     i += 1

"""
演示while循环基础练习题：求1-100的和
"""
sum = 0
i = 1
while i <=100:
    # sum = sum + i
    sum += i
    print(sum)
    print(f"i值为：{i}")

    i += 1
    print(f"此时i值为：{i}")

print(f"1-100累加的和是：{sum}")