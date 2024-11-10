def read_wordlist(path):
    try:
        with open(path, 'r') as file:
            # Read each line as a separate word, stripping any extra whitespace
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        exit(1)
    except Exception as e:
        print(f"Error opening file '{path}': {e}")
        exit(1)
