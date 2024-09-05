num = 153  # Change this number to check different numbers

# Convert the number to a string to find its length
num_str = str(num)
order = len(num_str)

# Calculate the sum of each digit raised to the power of the number of digits
sum_of_powers = sum(int(digit) ** order for digit in num_str)

# Check if the number is equal to the sum of its digits raised to the power of the number of digits
if num == sum_of_powers:
    print(num, "is an Amstrong number")
else:
    print(num, "is not an Amstrong number")
