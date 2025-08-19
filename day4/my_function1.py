def my_function(num1, num2):
    return num1 + num2

print(f'Sum = {my_function(10, 20)}')
print(f'Sum = {my_function(*(40, 90))}')
print(f'Sum = {my_function((40, 90))}') # TypeError. No value is passed to num2
