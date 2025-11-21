import os
import re

class PyCakeDecoder:
    def __init__(self):
        self.reverse_mapping = {
            '/01/': 'a', '/02/': 'b', '/03/': 'c', '/04/': 'd', '/05/': 'e',
            '/06/': 'f', '/07/': 'g', '/08/': 'h', '/09/': 'i', '/10/': 'j',
            '/11/': 'k', '/12/': 'l', '/13/': 'm', '/14/': 'n', '/15/': 'o',
            '/16/': 'p', '/17/': 'q', '/18/': 'r', '/19/': 's', '/20/': 't',
            '/21/': 'u', '/22/': 'v', '/23/': 'w', '/24/': 'x', '/25/': 'y',
            '/26/': 'z', '/01v/': 'A', '/02v/': 'B', '/03v/': 'C', '/04v/': 'D',
            '/05v/': 'E', '/06v/': 'F', '/07v/': 'G', '/08v/': 'H', '/09v/': 'I',
            '/10v/': 'J', '/11v/': 'K', '/12v/': 'L', '/13v/': 'M', '/14v/': 'N',
            '/15v/': 'O', '/16v/': 'P', '/17v/': 'Q', '/18v/': 'R', '/19v/': 'S',
            '/20v/': 'T', '/21v/': 'U', '/22v/': 'V', '/23v/': 'W', '/24v/': 'X',
            '/25v/': 'Y', '/26v/': 'Z', '/space/': ' ', '/newline/': '\n',
            '/tab/': '\t', '/36/': '0', '/37/': '1', '/38/': '2', '/39/': '3',
            '/40/': '4', '/41/': '5', '/42/': '6', '/43/': '7', '/44/': '8',
            '/45/': '9', '/46/': '!', '/47/': '@', '/48/': '#', '/49/': '$',
            '/50/': '%', '/51/': '^', '/52/': '&', '/53/': '*', '/54/': '(',
            '/55/': ')', '/56/': '-', '/57/': '_', '/58/': '=', '/59/': '+',
            '/60/': '[', '/61/': ']', '/62/': '{', '/63/': '}', '/64/': '|',
            '/65/': '\\', '/66/': ';', '/67/': ':', '/68/': "'", '/69/': '"',
            '/70/': ',', '/71/': '.', '/72/': '<', '/73/': '>', '/74/': '/',
            '/75/': '?'
        }
        
        self.password_reverse_mapping = {
            '27': '0', '28': '1', '29': '2', '30': '3', '31': '4',
            '32': '5', '33': '6', '34': '7', '35': '8', '36': '9'
        }

    def extract_password(self, content):
        """Extract and decode password from .cake file"""
        password_match = re.search(r'dire = \"(.*?)\"', content)
        if password_match:
            encoded_password = password_match.group(1)
            password_parts = re.find(r'/(\d+)/', encoded_password)
            decoded_password = ''
            for part in password_parts:
                if part in self.password_reverse_mapping:
                    decoded_password += self.password_reverse_mapping[part]
                else:
                    decoded_password += part
            return decoded_password
        return None

    def decode_text(self, encoded_text):
        """Decode pyCake format to original text"""
        decoded_text = encoded_text
        
        for code, char in sorted(self.reverse_mapping.items(), key=lambda x: len(x[0]), reverse=True):
            decoded_text = decoded_text.replace(code, char)
        
        return decoded_text

    def extract_encoded_content(self, content):
        """Extract the main encoded content from .cake file"""
        lines = content.split('\n')
        encoded_lines = []
        in_content = False
        
        for line in lines:
            if line.strip() == 'def;':
                in_content = not in_content
                continue
            if in_content and not line.strip().startswith('powered by') and not line.strip().startswith('secure'):
                encoded_lines.append(line)
        
        return '\n'.join(encoded_lines)

def decode_file(input_file, password=None, output_file=None):
    """
    Decode a .cake file back to Python format
    
    Args:
        input_file (str): Path to input .cake file
        password (str, optional): Password for decoding. If None, will be prompted
        output_file (str, optional): Output file path. Defaults to None
    
    Returns:
        str: Path to decoded file
    """
    
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found")
    
    decoder = PyCakeDecoder()
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    stored_password = decoder.extract_password(content)
    
    if password is None:
        password = input("Enter password to decode: ")
    
    if password != stored_password:
        raise ValueError("Incorrect password!")
    
    encoded_content = decoder.extract_encoded_content(content)
    decoded_content = decoder.decode_text(encoded_content)
    
    if output_file is None:
        base_name = os.path.splitext(input_file)[0]
        output_file = base_name + '2cake.py'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decoded_content)
    
    return output_file