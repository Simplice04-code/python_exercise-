def is_perfect(num):
    divisors_sum = sum(i for i in range(1, num // 2 + 1) if num % i == 0)
    return divisors_sum == num

perfect_numbers = []

for n in range(2, 1000000):
    if is_perfect(n):
        perfect_numbers.append(n)

print("Perfect numbers less than 1,000,000:", perfect_numbers)