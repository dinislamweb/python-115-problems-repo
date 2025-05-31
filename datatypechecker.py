#6. Data Type Checker: Write a Python function that takes a variable as input and returns 
# the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).
def data_type_checker(variable):
    """Return the data type of the variable as a string
    Args:
        variable (_type_): _description_
    """
    return type(variable).__name__
print(data_type_checker("Din Islam"))
           
