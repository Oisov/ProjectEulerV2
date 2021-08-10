function sum_of_first_n_numbers(n)
    div(n*(n+1), 2)
end

function sum_of_first_n_squares(n)
    div(n*(n+1)*(2n+1), 6)
end

function PE_006(n = 100)
    sum_of_first_n_numbers(n)^2 - sum_of_first_n_squares(n)
end
