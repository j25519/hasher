import hashlib

def compute_sha256(text):
    try:
        # Check for empty input
        if not text.strip():
            return "Error: Input string cannot be empty."
        
        # Convert to bytes and compute SHA256 hash
        hash_object = hashlib.sha256(text.encode('utf-8'))
        return hash_object.hexdigest()
    
    except Exception as e:
        return f"Error: Something went wrong - {str(e)}"

# Prompt user for a string
user_input = input("Enter a string to hash: ")

# Compute and print the hash
result = compute_sha256(user_input)
if result.startswith("Error"):
    print(result)
else:
    print(f"SHA256 hash of {user_input}:\n{result}")
