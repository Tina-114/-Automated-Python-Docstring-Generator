import argparse
import os
from insertor import insert_docstrings

def parse_args():
    """parse_args function description.


    Returns:
        None: Description of the returned value.
    """
    parser = argparse.ArgumentParser(description="CLI for automatically generating docstrings in Python files")
    parser.add_argument('path', type=str, help='File or directory path')
    parser.add_argument('--recursive', action='store_true', help='Recursively scan directories')
    parser.add_argument('--style', type=str, default='google', help='Select style for operation (google, etc.)')
    parser.add_argument('--dry-run', action='store_true', help='Run without making changes')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    return parser.parse_args()


def process_file(file_path, args):
    """process_file function description.

    Args:
        file_path (any): Description of file_path.
        args (any): Description of args.

    Returns:
        None: Description of the returned value.
    """
    if file_path.endswith('.py'):
        if args.verbose:
            print(f"Processing: {file_path}")
        insert_docstrings(file_path, dry_run=args.dry_run, verbose=args.verbose)

def main():
    """main function description.


    Returns:
        None: Description of the returned value.
    """
    args = parse_args()
    
    if os.path.isfile(args.path):
        process_file(args.path, args)
    elif os.path.isdir(args.path):
        if args.recursive:
            for root, dirs, files in os.walk(args.path):
                for file in files:
                    process_file(os.path.join(root, file), args)
        else:
            for file in os.listdir(args.path):
                process_file(os.path.join(args.path, file), args)
    else:
        print(f"Error: Path {args.path} does not exist.")

if __name__ == '__main__':
    main()