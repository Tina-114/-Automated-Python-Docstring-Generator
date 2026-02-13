import os
import re
from extractor import MetadataExtractor
from generator import generate_google_style_docstring

def get_indentation(line):
    """get_indentation function description.

    Args:
        line (any): Description of line.

    Returns:
        None: Description of the returned value.
    """
    match = re.match(r'^(\s*)', line)
    return match.group(1) if match else ''

def insert_docstrings(file_path, dry_run=False, verbose=False):
    """
    Inserts generated docstrings back into a Python file for functions missing them.
    """
    if not os.path.exists(file_path):
        if verbose:
            print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        source_code = f.read()

    extractor = MetadataExtractor(source_code)
    metadata_list = extractor.extract_function_metadata()
    
    # Sort metadata by line number descending to avoid offset issues
    metadata_list.sort(key=lambda x: x['lineno'], reverse=True)
    
    lines = source_code.splitlines()
    
    for metadata in metadata_list:
        if metadata['has_docstring']:
            if verbose:
                print(f"Function '{metadata['name']}' already has a docstring. Skipping.")
            continue
        
        # Prepare arguments for the generator, filtering out 'self' and 'cls'
        params = metadata['parameters']
        if params and params[0]['name'] in ('self', 'cls'):
            params = params[1:]
            
        func_args = {p['name']: p['type_hint'] or 'any' for p in params}
        func_return = metadata['return_type'] or 'None'
        
        raw_docstring = generate_google_style_docstring(
            metadata['name'], 
            func_args, 
            func_return
        )
        
        # Get indentation of the function definition
        # metadata['lineno'] is 1-indexed
        def_line = lines[metadata['lineno'] - 1]
        base_indent = get_indentation(def_line)
        inner_indent = base_indent + '    '
        
        # Apply indentation to the docstring
        indented_docstring_lines = [inner_indent + line if line.strip() else line for line in raw_docstring.splitlines()]
        indented_docstring = '\n'.join(indented_docstring_lines)
        
        if verbose:
            print(f"Inserting docstring for '{metadata['name']}' at line {metadata['lineno'] + 1}")
            
        lines.insert(metadata['lineno'], indented_docstring)

    new_content = '\n'.join(lines)
    
    if dry_run:
        print(f"--- Dry Run: Changes for {file_path} ---")
        print(new_content)
        print("--- End Dry Run ---")
    else:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        if verbose:
            print(f"Successfully updated {file_path}")

# Example usage:
# insert_docstring('your_script.py')