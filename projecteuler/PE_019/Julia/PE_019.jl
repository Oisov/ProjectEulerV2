function PE_019(day="Sunday", startDate=Date(1901,1,1),endDate=Date(2000,12,31))
    total_days = 0

    date = startDate
    while date < endDate
        if Dates.dayname(date) == day
            total_days += 1
        end
        date += Dates.Month(1)
    end

    total_days
end
