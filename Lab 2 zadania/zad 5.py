import ast

def validate_code(code):
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False

def generate_code(template, **kwargs):
    try:
        generated_code = template.format(**kwargs)

        if not validate_code(generated_code):
            raise ValueError("Generated code is not valid Python code.")

        exec(generated_code)
    except Exception as e:
        print(f"Error: {e}")

def main():
    template = """
def funkcja(x):
    return x + {add_value}
result = funkcja({input_value})
print("Result:", result)
"""

    add_value = 2
    input_value = 5
    generate_code(template, add_value=add_value, input_value=input_value)

if __name__ == "__main__":
    main()
