class ListCalculator:
    def __init__(self, x_list, y_list):
        self.x = x_list
        self.y = y_list
    
    def lists_division(self):
              
        sum_x = sum(self.x)
        sum_y = sum(self.y)
        
        return sum_y / sum_x

# Example usage:
x_values = [5, -4, -1]
y_values = [5, 10, 15]

calculator = ListCalculator(x_values, y_values)
try:
    result = calculator.lists_division()
except ZeroDivisionError:
    print('infinite!')

print("Result:", result)
