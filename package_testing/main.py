# import my_calculator.addition as addition
# import my_calculator.subtraction as subtraction

# from my_calculator import addition, subtraction

# from my_calculator.addition import add
# from my_calculator.subtraction import subtract

# __init__ file in my_calculator package will handle imports
from my_calculator import add, subtract

result_add = add(10, 4)
result_subtract = subtract(10, 4)

print(f"The addition result is: {result_add}")
print(f"The subtraction result is: {result_subtract}")
 