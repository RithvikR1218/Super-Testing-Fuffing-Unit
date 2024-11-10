import argparse
import threading
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
    parser.add_argument("-t", "--threads", type=int, default=4, help="Number of threads (default is 4)")
    return parser.parse_args()

def thread_worker(word, method, url, headers, data):
    send_request(method, url, word, headers, data)

def main():
    # Parse arguments
    args = parse_args()

    # Check if 'FUZZ' is in URL or data
    if "FUZZ" not in args.url and (not args.data or "FUZZ" not in args.data):
        print("Error: 'FUZZ' keyword is not present in the URL or form data.")
        exit(1)

    # Read wordlist from file
    words = read_wordlist(args.wordlist)

    # Parse headers and form data if provided
    headers = parse_headers(args.headers) if args.headers else {}
    data = parse_form_data(args.data) if args.data else {}

    # List to hold threads
    threads = []

    # Start threads for each word in the wordlist
    for word in words:
        thread = threading.Thread(target=thread_worker, args=(word, args.method, args.url, headers, data))
        threads.append(thread)
        thread.start()

        # Limit the number of threads running simultaneously (to avoid overwhelming the system)
        if len(threads) >= args.threads:
            for t in threads:
                t.join()
            threads = []

    # Join remaining threads
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
