function file_2_number(file="../Data/PE_008_data.txt")
    s = readstring(open(file))
    replace(s, "\n", "")
end


function string_2_product(string)
    prod(digits(parse(Int, string)))
end


function max_substring_sum(string, product_length)
    max_product = string_2_product(string[1:product_length])
    next_product = max_product

    first_value = parse(Int, string[1])

    for index = 2:(length(string)-product_length+1)
        next_value = parse(Int, string[index+product_length-1])

        next_product *= (next_value/first_value)
        if next_product > max_product
            max_product = next_product
        end

        first_value = parse(Int, string[index])
    end
    max_product
end


function PE_008(product_length = 13, number_string = file_2_number())
    max_product = -Inf
    for substring_number in split(number_string, "0")
        if length(substring_number) < product_length
            continue
        end

        max_substring_product = max_substring_sum(substring_number,
                                                  product_length)

        if max_substring_product > max_product
            max_product = max_substring_product
        end
    end
    BigInt(max_product)
end
