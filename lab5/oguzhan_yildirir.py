def find_mean(*numbers, **values):
    max = 0
    total = 0
    for number in numbers:
        total += number
        if (number > max):
            max = number

    mean = float(total / len(numbers))

    normalized = []
    filtered = []

    filtered_total = 0

    for number in numbers:
        number /= max
        normalized.append(round(number, 2))
        
        if (number >= values['value1'] and number <= values['value2']):
            filtered.append(round(number, 2))
            filtered_total += number

    filtered_mean = filtered_total / len(filtered)

    print("-------------------")
    print("Average: ", '%.2f' % mean)
    print("Input list: ", numbers)
    print("Normalized list: ", normalized)
    print("Treshold: low:", values["value1"], ", high: ", values["value2"])
    print("Filtered list: ", filtered)
    print("Avg of normalized and filtered values: ", '%.2f' % filtered_mean)
    print("-------------------")

find_mean(1,2,3, value1=0.5, value2=1)