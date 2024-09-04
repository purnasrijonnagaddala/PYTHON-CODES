start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print("Perfect numbers in the range {} to {}:".format(start_range, end_range))
for num in range(start_range, end_range + 1):
    sum_of_divisors = 1  # 1 is always a divisor
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    if sum_of_divisors == num:
        print(num)
