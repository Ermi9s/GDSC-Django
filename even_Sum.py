count = 0
sum = 0
evens = []

for num in range(1,51):
    if num % 2 == 0:
        sum += num
        if num % 3 == 0 and num % 5 != 0:
            evens.append("Three")
            count += 1
        elif num % 5 == 0 and num % 3 != 0:
            evens.append("Five")
            count += 1
        elif num % 3 == 0 and num % 5 == 0:
            evens.append("Five/Three")
            count += 1
        else:
            evens.append(num)

print("The total sum is:",end=" ")
print(sum)
print("number of replaced by Three and Five is:",end=" ")
print(count)
print("The list:")
for item in evens:
    print(item)



