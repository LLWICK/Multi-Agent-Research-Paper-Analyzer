import json
import re

def clean_json(markdown_json_str):
    """
    Cleans a JSON string that may have markdown code block syntax and returns a Python dictionary.
    
    Args:
        markdown_json_str (str): JSON string possibly wrapped in triple backticks.
        
    Returns:
        dict: Parsed JSON as a Python dictionary.
    """
    # Remove markdown code block backticks and optional language tag (like ```json)
    cleaned_str = re.sub(r'^```[a-z]*\n|```$', '', markdown_json_str.strip(), flags=re.IGNORECASE)
    
    # Parse the JSON string into a Python dictionary
    try:
        data = json.loads(cleaned_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")
    
    return data