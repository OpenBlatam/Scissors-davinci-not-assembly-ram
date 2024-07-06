# Unix libraries
import ast

# Simple Python code
code = """
def hello_world():
    print("Hello, world!")
"""

# Parse code to AST
tree = ast.parse(code)

# Print the result. It should represent the structure of your Python code.
print(ast.dump(tree, indent=4))

