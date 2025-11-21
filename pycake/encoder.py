import os
import re

class PyCakeEncoder:
    def __init__(self):
        self.syntax = "dicro"
        self.secure_header = "secure = \"dire=dire\""
        self.mapping = {
            'a': '/01/', 'b': '/02/', 'c': '/03/', 'd': '/04/', 'e': '/05/',
            'f': '/06/', 'g': '/07/', 'h': '/08/', 'i': '/09/', 'j': '/10/',
            'k': '/11/', 'l': '/12/', 'm': '/13/', 'n': '/14/', 'o': '/15/',
            'p': '/16/', 'q': '/17/', 'r': '/18/', 's': '/19/', 't': '/20/',
            'u': '/21/', 'v': '/22/', 'w': '/23/', 'x': '/24/', 'y': '/25/',
            'z': '/26/', 'A': '/01v/', 'B': '/02v/', 'C': '/03v/', 'D': '/04v/',
            'E': '/05v/', 'F': '/06v/', 'G': '/07v/', 'H': '/08v/', 'I': '/09v/',
            'J': '/10v/', 'K': '/11v/', 'L': '/12v/', 'M': '/13v/', 'N': '/14v/',
            'O': '/15v/', 'P': '/16v/', 'Q': '/17v/', 'R': '/18v/', 'S': '/19v/',
            'T': '/20v/', 'U': '/21v/', 'V': '/22v/', 'W': '/23v/', 'X': '/24v/',
            'Y': '/25v/', 'Z': '/26v/', ' ': '/space/', '\n': '/newline/',
            '\t': '/tab/', '0': '/36/', '1': '/37/', '2': '/38/', '3': '/39/',
            '4': '/40/', '5': '/41/', '6': '/42/', '7': '/43/', '8': '/44/',
            '9': '/45/', '!': '/46/', '@': '/47/', '#': '/48/', '$': '/49/',
            '%': '/50/', '^': '/51/', '&': '/52/', '*': '/53/', '(': '/54/',
            ')': '/55/', '-': '/56/', '_': '/57/', '=': '/58/', '+': '/59/',
            '[': '/60/', ']': '/61/', '{': '/62/', '}': '/63/', '|': '/64/',
            '\\': '/65/', ';': '/66/', ':': '/67/', "'": '/68/', '"': '/69/',
            ',': '/70/', '.': '/71/', '<': '/72/', '>': '/73/', '/': '/74/',
            '?': '/75/'
        }
        
        self.password_mapping = {
            '0': '27', '1': '28', '2': '29', '3': '30', '4': '31',
            '5': '32', '6': '33', '7': '34', '8': '35', '9': '36'
        }

    def encode_text(self, text):
        """Encode text to pyCake format"""
        encoded_chars = []
        for char in text:
            if char in self.mapping:
                encoded_chars.append(self.mapping[char])
            else:
                encoded_chars.append(char)
        return ''.join(encoded_chars)

    def encode_password(self, password):
        """Encode password using special mapping"""
        encoded_pass = []
        for char in password:
            if char in self.password_mapping:
                encoded_pass.append(f"/{self.password_mapping[char]}/")
            else:
                encoded_pass.append(char)
        return ' '.join(encoded_pass)

    def create_encoded_file(self, original_content, password, author_name, output_path):
        """Create encoded .cake file"""
        encoded_content = self.encode_text(original_content)
        
        encoded_password = self.encode_password(password)
        
        final_content = f"{self.syntax}\n   def;\n{encoded_content}\n\npowered by [{author_name}]\n{self.secure_header}\n   def;\ndire = power&power\ndire = \"{encoded_password}\""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

def encode_file(input_file, password, author_name, output_file=None):
    """
    Encode a Python file to .cake format
    
    Args:
        input_file (str): Path to input Python file
        password (str): Password for decoding
        author_name (str): Author name for signature
        output_file (str, optional): Output file path. Defaults to None
    
    Returns:
        str: Path to encoded file
    """
    
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found")
    
    if output_file is None:
        base_name = os.path.splitext(input_file)[0]
        output_file = base_name + '.cake'
    
    encoder = PyCakeEncoder()
    
    with open(input_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    encoder.create_encoded_file(original_content, password, author_name, output_file)
    
    return output_file