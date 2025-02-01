def calculate_average(numbers):
    total = 0
    count = 0
    for number in numbers:
        try:
            total += float(number)
            count += 1
        except (ValueError, TypeError):
            print(f"Skipping non-numeric value: {number}")
    if count == 0:
        return 0
    average = total / count
    return average

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [10, 20, 'a']
result = calculate_average(my_list)
print(f"The average is: {result}") #This will handle the error gracefully