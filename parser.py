import ast

class DocStringAnalyzer(ast.NodeVisitor):
    def __init__(self):
        """__init__ function description.


        Returns:
            None: Description of the returned value.
        """
        self.missing_docstrings = []

    def visit_FunctionDef(self, node):
        """visit_FunctionDef function description.

        Args:
            node (any): Description of node.

        Returns:
            None: Description of the returned value.
        """
        if ast.get_docstring(node) is None:
            self.missing_docstrings.append((node.name, 'function'))
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        """visit_ClassDef function description.

        Args:
            node (any): Description of node.

        Returns:
            None: Description of the returned value.
        """
        if ast.get_docstring(node) is None:
            self.missing_docstrings.append((node.name, 'class'))
        self.generic_visit(node)

    def report(self):
        """report function description.


        Returns:
            None: Description of the returned value.
        """
        if not self.missing_docstrings:
            print("All functions and classes have docstrings.")
        else:
            print("Missing docstrings:")
            for name, type_ in self.missing_docstrings:
                print(f'- {type_.capitalize()}: {name}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python parser.py <python_file>')
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        node = ast.parse(file.read())
        analyzer = DocStringAnalyzer()
        analyzer.visit(node)
        analyzer.report()