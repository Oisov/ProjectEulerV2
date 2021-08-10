
def digit_sum(number):
    return sum(map(int, str(number)))

def PE_119(n):
    index = 0
    total = 0
    digit_power_sums = []
    for k in range(2, 101):
        for j in range(2, 101):
            number = k**j
            if digit_sum(number) == k:
                digit_power_sums.append(number)
    return sorted(digit_power_sums)[n-1]
print(PE_119(30))
# isDigitPowerSum([1, 0, 0, 1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 9, 9])
