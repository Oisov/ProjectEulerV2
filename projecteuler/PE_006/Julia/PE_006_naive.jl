function sum_of_first_n_numbers(n)
    sum(1:n)
end

function sum_of_first_n_squares(n)
    sum(i^2 for i = 1:n)
end

function PE_006_naive(n = 100)
    sum_of_first_n_numbers(n)^2 - sum_of_first_n_squares(n)
end
