using Primes

function isGeneralizedHammingNumber(number, primeList, primeDict)
    for prime in primeList
        while number % prime == 0
            number = div(number, 2)
        end
    end
end


limit = 10^9
total = 0
for two = 0:log(2, limit)
    num1 = 2^two
    for three = 0:log(3, div(limit,num1))
        num2 = num1 * 3^three
        for five = 0:log(5, div(limit, num2))
            num3 = num2 * 5^five
            for seven = 0:log(7, div(limit, num3))
                num4 = num3 * 7^seven
                for eleven = 0:log(11, div(limit, num4))
                    num5 = num4 * 11^eleven
                    for thirteen = 0:log(13, div(limit, num5))
                        num6 = num5 * 13^thirteen
                        for seventeen = 0:log(17, div(limit, num6))
                            num7 = num6 * 17^seventeen
                            for nineteen = 0:log(19, div(limit, num7))
                                num8 = num7 * 19^nineteen
                                for twentythree = 0:log(23, div(limit, num8))
                                    num9 = num8 * 23^twentythree
                                    for twentynine = 0:log(29, div(limit, num9))
                                        num10 = num9 * 29^twentynine
                                        for thirtyone = 0:log(31, div(limit, num10))
                                            num11 = num10 * 31^thirtyone
                                            for thirtyseven = 0:log(37, div(limit, num11))
                                                num12 = num11 * 37^thirtyseven
                                                for fortyone = 0:log(41, div(limit, num12))
                                                    num13 = num12 * 41^fortyone
                                                    for fortythree = 0:log(43, div(limit, num13))
                                                        num14 = num13 * 43^fortythree
                                                        for fortyseven = 0:log(47, div(limit, num14))
                                                            num15 = num14 * 47^fortyseven
                                                            for fiftythree = 0:log(53, div(limit, num15))
                                                                num16 = num15 * 53^fiftythree
                                                                for fiftynine = 0:log(59, div(limit, num16))
                                                                    num17 = num16 * 59^fiftynine
                                                                    for sixtyone = 0:log(61, div(limit, num17))
                                                                        num18 = num17 * 61^sixtyone
                                                                        for sixtyseven = 0:log(67, div(limit, num18))
                                                                            num19 = num18 * 67^sixtyseven
                                                                            for seventyone = 0:log(71, div(limit, num19))
                                                                                num20 = num19 * 71^seventyone
                                                                                for seventythree = 0:log(73, div(limit, num20))
                                                                                    num21 = num20 * 73^seventythree
                                                                                    for seventynine = 0:log(79, div(limit, num21))
                                                                                        num22 = num21 * 79^seventynine
                                                                                        for eightythree = 0:log(83, div(limit, num22))
                                                                                            num23 = num22 * 83^eightythree
                                                                                            for eightynine = 0:log(89, div(limit, num23))
                                                                                                num24 = num23 * 89^eightynine
                                                                                                for nintyseven = 0:log(97, div(limit, num24))
                                                                                                    num25 = num24 * 97^nintyseven
                                                                                                    total += 1
                                                                                                end
                                                                                            end
                                                                                        end
                                                                                    end
                                                                                end
                                                                            end
                                                                        end
                                                                    end
                                                                end
                                                            end
                                                        end
                                                    end
                                                end
                                            end
                                        end
                                    end
                                end
                            end
                        end
                    end
                end
            end
        end
    end
end
println(total)






