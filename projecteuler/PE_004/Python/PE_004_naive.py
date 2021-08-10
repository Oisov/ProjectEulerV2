def is_palindrome(number):
    string = str(number)
    return string == string[::-1]


def PE_004_naive(length=3):
    palindrome_max = 0
    lower = 10**(length - 1) + 1
    higher = 10**length
    for i in range(lower, higher):
        for j in range(lower, higher):
            if is_palindrome(str(i * j)):
                palindrome = i * j
                if palindrome > palindrome_max:
                    palindrome_max = palindrome
    return palindrome_max
