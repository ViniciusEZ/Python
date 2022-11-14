"""
Create a function that converts a given ASCII string to its hexadecimal SHA-256 hash.
"""
from hashlib import sha256

def to_sha256(s):
    return sha256(s.encode()).hexdigest()


print(to_sha256("Hello World!"))