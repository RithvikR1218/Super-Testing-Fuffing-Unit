import argparse
from src.request_handler import send_request
from src.wordlist_handler import read_wordlist
from src.utils import parse_headers, parse_form_data

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file path and (optional) keyword separated by colon. eg. '/path/to/wordlist'")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-X", "--method", help="Request method (GET/POST)", default="GET")
    parser.add_argument("-d", "--data", help="Form data for POST request (e.g. key1=value1&key2=value2)")
    parser.add_argument("-H", "--headers", help="Custom headers for request (e.g. 'User-Agent: Mozilla/5.0')")
    return parser.parse_args()

def main():
    # Parse arguments
    args = parse_args()

    # Check if 'FUZZ' is in URL
    if "FUZZ" not in args.url and args.data is not None and "FUZZ" not in args.data:
        print("Error: 'FUZZ' keyword is not present in the URL or form data.")
        exit(1)

    # Read wordlist from file
    words = read_wordlist(args.wordlist)

    # Parse headers and form data if provided
    headers = parse_headers(args.headers) if args.headers else {}
    data = parse_form_data(args.data) if args.data else {}

    # Handle requests
    send_request(args.method, args.url, words, headers, data)

if __name__ == "__main__":
    main()
