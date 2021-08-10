TWENTY = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "ninteen"
]

HUNDRED = [
    "ten",
    "twenty",
    "thirty",
    "fourty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]


function large_number_suffix(block)
    if block == 0
        ""
    elseif block == 1
        "thousand"
    elseif block == 2
        "million"
    elseif block == 3
        "billion"
    end
end


function small_number_2_name(digit_lst, is_first_chunk)
    """
    Converts a three digit number into a string

        [3, 4, 1] > Three-hundred and fourty one

    """
    number_string = ""
    hundred_place = digit_lst[1]
    tens_place = 10*digit_lst[2] + digit_lst[3]

    if hundred_place != 0
        number_string *= TWENTY[hundred_place] * "-hundred"
    end

    if tens_place != 0
        # Insert and only if it is not the start of the word
        if !(is_first_chunk && hundred_place == 0)
            number_string *= " and "
        end
        if tens_place < 20
            number_string *= TWENTY[tens_place]
        else
            if digit_lst[2] != 0
                number_string *= HUNDRED[digit_lst[2]] * " "
            end
            if digit_lst[3] != 0
                number_string *= TWENTY[digit_lst[3]]
                end
        end
    end

    number_string *= " "
    number_string
end


function number_2_name(number)
    digitz = reverse(digits(number))
    pad = 3-length(digitz)%3
    #Pads number in front with zeroes such that number is divisible by 3
    padded_digits = append!(zeros(Int, pad==3?:0:pad), digitz)

    number_name = ""
    chunks = trunc(Int, length(padded_digits)/3-1)

    is_first_chunk = true
    for index = 0:chunks

        next_three_digits = padded_digits[1+3*index:3+3*index]
        number_name *= small_number_2_name(next_three_digits, is_first_chunk)

        if next_three_digits != [0,0,0]
            number_name *= large_number_suffix(chunks-index) * " "
        end
        is_first_chunk = false
    end
    number_name
end


function PE_017(stop=1000,start=1)
    total = 0
    for number = start:stop
        string_number = replace(filter(x -> !isspace(x),
                               number_2_name(number)),"-","")
        total += length(string_number)
    end
    total
end

println(PE_017())
