"""
pyCake - A Python package for encoding and decoding Python files with secure encryption
"""

__version__ = "1.0.0"
__author__ = "LORD NEXIRU"

from .encoder import encode_file
from .decoder import decode_file

__all__ = ['encode_file', 'decode_file']