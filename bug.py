def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list to avoid ZeroDivisionError
    average = total / count
    return average

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}") #This will work fine

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}") #This will also work fine

my_list = [10, 20, 'a']
result = calculate_average(my_list) #This will throw an error
print(f"The average is: {result}")