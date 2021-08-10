using Primes


function number_2_palindrome(number)
    str_num = string(number)
    parse(Int, str_num * reverse(str_num))
end


function is_palindrome(number)
    number_str = string(number)
    return number_str == reverse(number_str)
end


function temp_even_factors(length)
    length = div(length, 2)
    factor_1 = parse(BigInt, ("9"^length) * ("0"^(length-1)) * "1")
    factor_2 = parse(BigInt, "9"^(2*length))
    return (factor_1, factor_2)
end


function equal_number_of_digits(number_1, number_2)
    return floor(log(10, number_1)) == floor(log(10, number_2))
end


function PE_004(palindrome_length = 3)

    if palindrome_length % 2 == 0
        temp_factor_1, temp_factor_2 = temp_even_factors(palindrome_length)
        temp_palindrome = temp_factor_1 * temp_factor_2
        if is_palindrome(temp_palindrome)
            return temp_palindrome
        end
    end

    max_num , min_num = 10^(palindrome_length)-1, 10^(palindrome_length-1)
    max_num_11, min_num_11 = div(max_num, 11), div(min_num, 11)

    for number = max_num:-1:min_num

        palindrome = number_2_palindrome(number)
        smaller_palindrome = div(palindrome, 11)

        if isprime(smaller_palindrome)
            continue
        end

        smallest_possible_factor = max(div(smaller_palindrome, max_num),
                                       min_num_11)
        for number = max_num_11:-1:smallest_possible_factor+1
            if smaller_palindrome % number == 0
                return palindrome
            end
        end
    end
end
