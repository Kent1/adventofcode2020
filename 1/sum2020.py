def find_2_numbers_sum_to_2020(numbers):
    for i1 in range(len(numbers)):
        for i2 in range(len(numbers[i1:])):
            if numbers[i1] + numbers[i2] == 2020:
                return (numbers[i1], numbers[i2])

def find_3_numbers_sum_to_2020(numbers):
    for i1 in range(len(numbers)):
        for i2 in range(len(numbers)):
            if numbers[i1] + numbers[i2] > 2020:
                continue
            for i3 in range(len(numbers)):
                print(numbers[i1] + numbers[i2] + numbers[i3])
                if numbers[i1] + numbers[i2] + numbers[i3] == 2020:
                    return (numbers[i1], numbers[i2], numbers[i3])


with open("input.txt", 'r') as f:
    lines = f.readlines()
    numbers = []
    for number in lines:
        numbers.append(int(number))
    x, y = find_2_numbers_sum_to_2020(numbers)
    print(x * y)
    x, y, z = find_3_numbers_sum_to_2020(numbers)
    print(x * y * z)


