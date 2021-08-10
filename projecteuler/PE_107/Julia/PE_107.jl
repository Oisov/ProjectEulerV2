function file2matrix(path = "../Data/PE_107_data_02.txt", isMinimal = true)
    lines = readlines(open(path))
    rows, columns = length(lines), length(split(lines[1],","))
    matrix = Matrix(rows, columns)

    open(path) do f
        for (row, line) in enumerate(eachline(f))
            for (column, char) in enumerate(split(line, ","))
                try
                    matrix[row, column] = parse(Int, char)
                catch
                    if isMinimal
                        matrix[row, column] = Inf
                    else
                        matrix[row, column] = -Inf
                    end
                end
            end
        end
    end
    matrix
end

matrix = file2matrix()


function prims(matrix, isMinimal = true)
    nodes = [1]
    edges = []
    pathSum = []

    if isMinimal
        for k = 1:size(matrix)[1]-1
            minVal = Inf
            minRow, minColumn = 1, 1
            # Loop through the nodes, find minimal edge
            for node in nodes
                tempMin, column = findmin(matrix[node, :])
                if tempMin < minVal
                    minVal = tempMin
                    minRow, minColumn = node, column
                end
            end

            push!(pathSum, matrix[minRow, minColumn])

            # Makes sure that the new node can not path back
            for node in nodes
                matrix[minColumn, node] = Inf
                matrix[node, minColumn] = Inf
            end

            # Push the minimal edge onto the list of visited notes
            push!(nodes, minColumn)
        end
    else
        minVal = -Inf
        for node in nodes
            tempMax = findmax(matrix[node, :])
        end
    end
    sum(pathSum)
end

function networkWeight(matrix)
    total = 0
    for value in matrix
        if abs(value) < Inf
            total += value
        end
    end
    div(total, 2)
end

function PE_107(matrix = file2matrix())
    totalWeight = networkWeight(matrix)
    minimalWeight = prims(matrix)
    return totalWeight - minimalWeight
end

println(PE_107())
