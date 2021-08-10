ALPHABET_INDEX = Dict(letter => index for (index, letter) in enumerate('A':'Z'))


function namescore(name)
    sum(ALPHABET_INDEX[letter] for letter in name)
end


function sort_file(filename)
    file = open(filename)
    sort(split(readstring(filename),","))
end


function PE_022(filename="../p022_names.txt")
    total = 0
    for (index, name) in enumerate(sort_file(filename))
        total += index*namescore(name[2:end-1])
    end
    total
end

println(PE_022())
