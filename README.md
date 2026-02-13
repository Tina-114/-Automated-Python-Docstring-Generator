# Docstring Generator

A lightweight CLI tool to automatically generate and insert Google-style docstrings into Python projects. It uses Python's built-in `ast` module to parse the code and identify functions missing documentation.

## Features

- **Automatic Metadata Extraction**: Detects function names, parameters (including type hints and default values), and return types.
- **Google Style Support**: Generates docstrings following the Google Python Style Guide.
- **Smart Insertion**: Automatically identifies the correct line and indentation to insert the docstring.
- **Recursive Scanning**: Process a single file or an entire directory tree.
- **Dry Run Mode**: Preview changes in the terminal without modifying your files.
- **Skips Existing**: Intelligent enough to skip functions that already have docstrings.

## Installation

You can install the tool localy by cloning the repository and running:

```bash
pip install .
```

## Usage

Run the tool using the `cli.py` script:

### Process a single file
```bash
python cli.py your_script.py --verbose
```

### Process a directory recursively
```bash
python cli.py ./src --recursive --verbose
```

### Preview changes (Dry Run)
```bash
python cli.py your_script.py --dry-run
```

## Example

### Input:
```python
def add(a: int, b: int) -> int:
    return a + b
```

### Output:
```python
def add(a: int, b: int) -> int:
    """add function description.

    Args:
        a (int): Description of a.
        b (int): Description of b.

    Returns:
        int: Description of the returned value.
    """
    return a + b
```

## Project Structure

- `cli.py`: The entry point for the command-line interface.
- `extractor.py`: Handles parsing Python source code and extracting function metadata.
- `generator.py`: Generates formatted Google-style docstrings.
- `insertor.py`: Manages the safe insertion of docstrings into the source files.
- `parser.py`: A utility script for identifying missing docstrings in a file.
