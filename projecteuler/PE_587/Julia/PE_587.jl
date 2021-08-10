
function concaveTriangleAreaN(n)
    return (2*(n^2+1)*asin((-n+1+sqrt(2)*n^(3/2))/(n^2+1))+sqrt(n)*(-2*sqrt(2)*n + 2*sqrt(2))-4)/((n^2+1)*pi -4*n^2 - 4)
end

function concaveTriangleAreaNDerivative(n)
    return (2*n^2 + 8*n + 2 + (-4*sqrt(2)*n - 4*sqrt(2))*sqrt(n))/((n^4 + 2n^2 + 1)*pi - 4*n^4 - 8*n^2 - 4)
end

function NewtonRhapson(percent_goal=0.1, steps=10^5)
    total_area = 1 - pi/4
    old_n = 2*n
    i = 1
    n = 100/percent_goal
    while i < steps && trunc(Int, old_n) != trunc(Int, n)
        old_n = n
        n = n - (concaveTriangleAreaN(n)-percent_goal/100)/(concaveTriangleAreaNDerivative(n))
        i += 1
    end
    println("steps newton: ", i)
    return Int(ceil(n))
end

function PE_587(percent_goal=0.1, min_n = 1, max_n = 10^5)

    while concaveTrianglePercentArea(min_n) < percent_goal
        min_n = div(min_n, 2)
    end
    high_val = concaveTrianglePercentArea(min_n)

    while concaveTrianglePercentArea(max_n) > percent_goal
        max_n *= 2
    end
    min_val = concaveTrianglePercentArea(max_n)

    mid_n = div(min_n + max_n, 2)
    new_mid_n = mid_n + 1

    i = 1
    while mid_n != new_mid_n

        mid_n = div(min_n + max_n, 2)
        mid_val = concaveTrianglePercentArea(mid_n)

        if mid_val > percent_goal
            min_n = mid_n
        elseif mid_val < percent_goal
            max_n = mid_n
        end
        new_mid_n = div(min_n + max_n, 2)
        i += 1
    end

    while concaveTrianglePercentArea(mid_n) > percent_goal
        i += 1
        mid_n += 1
    end
    println("bisect steps: ", i)
    return mid_n
end

function getConcaveCoordinates(n)
    x = (n^2 - sqrt(2)*n^(3/2) + n)/(1+n^2)
    y = 1 - sqrt(1-(x-1)^2) 
    return [(0,0), (x, y), (1,0)]
end

function concaveTriangleArea(x)
    return  1 - (x + sqrt(2x-x^2)+asin(1-x))/2
end

function concaveTriangleDerivative(x)
    return (x - sqrt(2x-x^2))/(2*sqrt(2x-x^2))
end

function concaveTrianglePercentArea(n)
    _, B, _ = getConcaveCoordinates(n)
    total_area = 1 - pi/4
    return 100*concaveTriangleArea(B[1])/total_area
end

# println(concaveTrianglePercentArea(15))
n = PE_587()
# percent = concaveTrianglePercentArea(n)
# println("With $n circles the concave triangle covers $percent percent of the L
# section.")
p = 20
for i =1:25
    println("percent: ", p, ". circles: ", NewtonRhapson(p))
    println("percent: ", p, ". circles: ", PE_587(p))
    p = p/2
end
