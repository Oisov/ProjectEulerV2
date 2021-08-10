function file_2_matrix(path="../Data/PE_011_data.txt")
    convert(Array{Int64}, readdlm(path))
end

function direction_product(matrix, y, x, delta_y, delta_x, elements)
    product = 1
    for i = (1:elements)-1

        next_x = x + i*delta_x
        next_y = y + i*delta_y

        value = matrix[next_x, next_y]
        if value == 0
            return 0
        end
        product *= value
    end
    product
end

function PE_011(product_length=4, matrix=file_2_matrix())
    rows, columns = size(matrix)
    max_product = -Inf
    directions = [(0, 1), (1, 0), (1, -1), (1, 1)]

    for i = 1:rows
        for j = 1:columns

            legal_left = (j - product_length) >= 1
            legal_right = (j + product_length) <= columns
            legal_down = (i + product_length) <= rows

            legal_direction = [legal_right,
                                legal_down,
                                legal_left && legal_down,
                                legal_right && legal_down]

            for index in find(legal_direction)
                delta_x, delta_y = directions[index]
                product = direction_product(matrix,
                                         i, j,
                                         delta_x, delta_y,
                                         product_length)
                if product > max_product
                    max_product = product
                end
            end

        end
    end
    max_product
end
