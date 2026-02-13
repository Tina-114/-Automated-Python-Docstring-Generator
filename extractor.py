import ast

class MetadataExtractor:
    def __init__(self, source_code: str):
        """__init__ function description.

        Args:
            source_code (str): Description of source_code.

        Returns:
            None: Description of the returned value.
        """
        self.source_code = source_code
        self.tree = ast.parse(source_code)

    def extract_function_metadata(self):
        """extract_function_metadata function description.


        Returns:
            None: Description of the returned value.
        """
        functions_metadata = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                metadata = {
                    'name': node.name,
                    'lineno': node.lineno,
                    'has_docstring': ast.get_docstring(node) is not None,
                    'parameters': [
                        self._extract_parameter_info(param)
                        for param in node.args.args
                    ],
                    'return_type': self._extract_return_type(node.returns),
                    'default_values': self._extract_default_values(node.args)
                }
                functions_metadata.append(metadata)
        return functions_metadata

    def _extract_parameter_info(self, param):
        """_extract_parameter_info function description.

        Args:
            param (any): Description of param.

        Returns:
            None: Description of the returned value.
        """
        return {
            'name': param.arg,
            'type_hint': self._extract_type_hint(param.annotation)
        }

    def _extract_type_hint(self, annotation):
        """_extract_type_hint function description.

        Args:
            annotation (any): Description of annotation.

        Returns:
            None: Description of the returned value.
        """
        return ast.get_source_segment(self.source_code, annotation) if annotation else None

    def _extract_return_type(self, returns):
        """_extract_return_type function description.

        Args:
            returns (any): Description of returns.

        Returns:
            None: Description of the returned value.
        """
        return self._extract_type_hint(returns)

    def _extract_default_values(self, args):
        """_extract_default_values function description.

        Args:
            args (any): Description of args.

        Returns:
            None: Description of the returned value.
        """
        default_values = []
        for default in args.defaults:
            default_values.append(ast.get_source_segment(self.source_code, default))
        return default_values
    
# Example usage:
# source_code = "def example_function(param1: int, param2: str = 'default') -> bool:\n#     pass"
# extractor = MetadataExtractor(source_code)
# print(extractor.extract_function_metadata())