# msg = "Hello world"

# print(msg)

# for i in range(10):
#     print(i)


num = 21
digit_sum = 0
while num:
    digit_sum += num % 10
    num //= 10
print(digit_sum)
