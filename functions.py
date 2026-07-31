def greet():
    print("Hello Benguela!!")
    print("Hello Again!!")
    
def check_weather():
    temperature = 30
    if temperature > 18:
        print("It's hot!")
    else:
        print("It's nice weather!")
        
# params
def greet2 (name, last_name="Kataleko"):
    print(f"Hello {name} {last_name}")
    
discount = 20

# Local and Global variable
def calculate_total (price):
    tax_rate = 0.08
    # discount = 10
    
    # Calculation
    tax = price * tax_rate
    final_price = price + tax - discount
    
    # Print the final price
    print(f"Total: ${final_price}")
    
def add_print(a, b):
    print(a + b)
    
def add_return (a, b):
    return a + b
    
def calculate_area (width, height):
    area = width * height
    return area

def double(number):
    return number * 2

# Store in a variable
result = double(5)

# Use in an expression
total = double(5) + double(3)

# Pass to other functions
# print(double(10))

def simple_function () :
    numbers = [1,2,3,4,5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number

f,l = simple_function()
print(f,l)