def generate_google_style_docstring(func_name, func_args, func_return):
    """
    Generates a Google-style docstring for a function.

    Args:
        func_name (str): The name of the function.
        func_args (dict): A dictionary of the function's arguments where keys are argument names and values are their types.
        func_return (str): The return type of the function.

    Returns:
        str: A Google-style formatted docstring.
    """
    docstring = f"\"\"\"{func_name} function description.\n\n"
    if func_args:
        docstring += "Args:\n"
        for arg, arg_type in func_args.items():
            docstring += f"    {arg} ({arg_type}): Description of {arg}.\n"
    
    if func_return:
        docstring += f"\nReturns:\n    {func_return}: Description of the returned value.\n"
    
    docstring += "\"\"\""
    return docstring

# Example usage
if __name__ == '__main__':
    print(generate_google_style_docstring('example_function', {'arg1': 'int', 'arg2': 'str'}, 'bool'))