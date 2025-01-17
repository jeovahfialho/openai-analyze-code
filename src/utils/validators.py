import ast
from typing import Tuple, Optional

def validate_python_code(code: str) -> Tuple[bool, Optional[str]]:
    """
    Validates if the provided code is valid Python syntax
    
    Args:
        code (str): Python code to validate
        
    Returns:
        Tuple[bool, Optional[str]]: (is_valid, error_message)
    """
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, f"Syntax error on line {e.lineno}: {e.msg}"
    except Exception as e:
        return False, str(e)

def validate_code_size(code: str, max_size: int = 10000) -> Tuple[bool, Optional[str]]:
    """
    Validates if the code size is within acceptable limits
    
    Args:
        code (str): Code to validate
        max_size (int): Maximum allowed size in characters
        
    Returns:
        Tuple[bool, Optional[str]]: (is_valid, error_message)
    """
    if len(code) > max_size:
        return False, f"Code exceeds maximum size of {max_size} characters"
    return True, None