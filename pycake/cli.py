import argparse
import sys
from .encoder import encode_file
from .decoder import decode_file

def main():
    parser = argparse.ArgumentParser(description='pyCake - Python File Encoder/Decoder')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Encode command
    encode_parser = subparsers.add_parser('encode', help='Encode a Python file to .cake format')
    encode_parser.add_argument('input_file', help='Input Python file')
    encode_parser.add_argument('-p', '--password', required=True, help='Password for encoding')
    encode_parser.add_argument('-a', '--author', required=True, help='Author name')
    encode_parser.add_argument('-o', '--output', help='Output .cake file')
    
    # Decode command
    decode_parser = subparsers.add_parser('decode', help='Decode a .cake file to Python format')
    decode_parser.add_argument('input_file', help='Input .cake file')
    decode_parser.add_argument('-p', '--password', help='Password for decoding')
    decode_parser.add_argument('-o', '--output', help='Output Python file')
    
    args = parser.parse_args()
    
    try:
        if args.command == 'encode':
            output_path = encode_file(
                args.input_file, 
                args.password, 
                args.author, 
                args.output
            )
            print(f"File encoded successfully: {output_path}")
            
        elif args.command == 'decode':
            output_path = decode_file(
                args.input_file,
                args.password,
                args.output
            )
            print(f"File decoded successfully: {output_path}")
            
        else:
            parser.print_help()
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
