import hashlib
import argparse

def compute_hash(text, algorithm):
    try:
        # Check for empty input
        if not text.strip():
            return "Error: Input string cannot be empty."

        # Map algos to hashlib
        algo_map = {
            'sha256': hashlib.sha256,
            'sha384': hashlib.sha384,
            'sha512': hashlib.sha512,
            'sha3_256': hashlib.sha3_256,
            'blake2b': hashlib.blake2b,
            'blake2s': hashlib.blake2s
        }

        # Check algorithm is supported
        if algorithm.lower() not in algo_map:
            return f"Error: Unsupported algorithm '{algorithm}'. Supported: {', '.join(algo_map.keys())}"

        # Convert to bytes and compute hash
        hash_object = algo_map[algorithm.lower()](text.encode('utf-8'))
        return hash_object.hexdigest()

    except Exception as e:
        return f"Error: Something went wrong - {str(e)}"

def main():
    # Make it a command line application
    parser = argparse.ArgumentParser(
        description="Hasher v0.0.2: Quickly get cryptographic hashes from strings.",
        epilog="Supported algorithms: sha256 (default), sha384, sha512, sha3_256, blake2b, blake2s."
    )
    parser.add_argument(
        '-a', '--algorithm',
        default='sha256',
        help="Hashing algorithm to use (default: sha256)"
    )
    parser.add_argument(
        'text',
        nargs='?',
        help="String to hash (will prompt for a string if not specified)"
    )

    # Parse arguments
    args = parser.parse_args()

    # Prompt user for a string
    if args.text is None:
        print("Welcome to Hasher v0.0.2!")
        user_input = input("Enter a string to hash: ")
    else:
        user_input = args.text

    # Compute and print the hash
    result = compute_hash(user_input, args.algorithm)
    if result.startswith("Error"):
        print(result)
    else:
        print(f"{args.algorithm} hash of {user_input}:\n{result}")

if __name__ == "__main__":
    main()