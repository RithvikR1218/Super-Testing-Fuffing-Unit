def read_wordlist(path):
    try:
        with open(path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        exit(1)
    except Exception as e:
        print(f"Error opening file '{path}': {e}")
        exit(1)
