def parse_headers(headers_str):
    headers = {}
    try:
        for header in headers_str.split(','):
            key, value = header.split(':', 1)
            headers[key.strip()] = value.strip()
    except ValueError:
        print("Error: Invalid header format. Use 'Key: Value' pairs separated by commas.")
        exit(1)
    return headers

def parse_form_data(data_str):
    data = {}
    try:
        for pair in data_str.split('&'):
            key, value = pair.split('=', 1)
            data[key] = value
    except ValueError:
        print("Error: Invalid form data format. Use 'key1=value1&key2=value2'.")
        exit(1)
    return data
