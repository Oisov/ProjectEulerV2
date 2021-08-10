def is_palindrome(number):
    string = str(number)
    return string == string[::-1]


def palindrome_product_3(n=3):
    max_palindrome = 0
    for i in xrange(10**n - 1, 0, -1):
        # Since all palindromes of length 2n are divisible by 11, either j or i has to be as well"
        if i % 11 == 0:
            j_max = i
            j_range = xrange(j_max + 1, min(max_palindrome / i, j_max), -1)
        else:
            j_max = 11 * int(i / 11)
            j_range = xrange(j_max, min(max_palindrome / i, j_max), -11)

        for j in j_range:
            product = i * j
            if is_palindrome(product):
                if product > max_palindrome:
                    max_palindrome = product
                    break
    return max_palindrome
