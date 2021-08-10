function remainingValues(values, index, valuesLength = -1)
    if index == 1
        return values[2:end]
    elseif valuesLength == -1
        valuesLength = length(values)
    end

    notIndex = values[1:index-1]
    if index <  valuesLength
        append!(notIndex, values[index+1:valuesLength])
    end

    return notIndex
end

function isSubsetsIncreasing(values)
    return (values[1] + values[2]) >= values[end]
end

function isSubsetSumsDifferent(values)
    lengthValues = length(values)

    for i = 1:lengthValues

        sumOne = values[i]
        tempI = remainingValues(values, i, lengthValues)

        for j = (i+1):lengthValues

            sumTwo = values[j]
            println(" ")
            print("[")
            for (indexx, val) in enumerate(values)
                if indexx == j || indexx == i
                    print([val])
                else
                    print(val)
                end
                if indexx < lengthValues
                    print(" ,")
                end
            end
            print("]")
            println(",")
            for value in reverse(remainingValues(tempI, j-1, lengthValues-1))
                println(value, ", ", sumOne, ", ", sumTwo)
                if sumOne < sumTwo
                    sumOne += value
                elseif sumOne > sumTwo
                    sumTwo += value
                else
                    return false
                end
            end
            println(" ")

        end
    end
    return true
end

arrayOne = sort([81, 88, 75, 42, 87, 84, 86, 65])
arrayTwo= sort([157, 150, 164, 119, 79, 159, 161, 139, 158])

println(isSubsetSumsDifferent(arrayOne))
