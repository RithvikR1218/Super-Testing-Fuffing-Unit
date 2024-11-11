import random
import struct

# Mutation Techniques
def mutate_flip_bits(data, num_flips=3):
    data = bytearray(data)
    for _ in range(num_flips):
        byte_index = random.randint(0, len(data) - 1)
        bit_index = random.randint(0, 7)
        data[byte_index] ^= (1 << bit_index)
    return bytes(data)

def mutate_insert_bytes(data, num_inserts=2):
    data = bytearray(data)
    for _ in range(num_inserts):
        index = random.randint(0, len(data))
        data.insert(index, random.randint(0, 255))
    return bytes(data)

def mutate_delete_bytes(data, num_deletes=2):
    data = bytearray(data)
    for _ in range(num_deletes):
        if len(data) > 0:
            index = random.randint(0, len(data) - 1)
            del data[index]
    return bytes(data)

def mutate_duplicate_bytes(data, num_duplicates=3):
    data = bytearray(data)
    for _ in range(num_duplicates):
        index = random.randint(0, len(data) - 1)
        data.insert(index, data[index])
    return bytes(data)

def mutate_boundary_values(data):
    boundary_values = [0, 255, 127, -1, 1, 2, 1024, 65535]
    data = bytearray(data)
    for _ in range(random.randint(1, 3)):
        value = random.choice([v for v in boundary_values if 0 <= v <= 65535])
        index = random.randint(0, len(data) - 2)
        packed_value = struct.pack('>H', value)
        data[index:index+2] = packed_value
    return bytes(data)

def mutate_magic_numbers(data):
    magic_numbers = [
        b'\x89PNG\r\n\x1a\n',  # PNG header
        b'\xFF\xD8\xFF\xE0',   # JPEG header
        b'GIF89a',             # GIF header
        b'%PDF-',              # PDF header
    ]
    data = bytearray(data)
    magic = random.choice(magic_numbers)
    index = random.randint(0, len(data) - len(magic))
    data[index:index + len(magic)] = magic
    return bytes(data)

def mutate_insert_ascii(data):
    ascii_chars = b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    data = bytearray(data)
    insert_str = bytes([random.choice(ascii_chars) for _ in range(random.randint(3, 10))])
    index = random.randint(0, len(data))
    data[index:index] = insert_str
    return bytes(data)

def mutate_swap_bytes(data, num_swaps=2):
    data = bytearray(data)
    for _ in range(num_swaps):
        if len(data) < 2:
            break
        idx1, idx2 = random.sample(range(len(data)), 2)
        data[idx1], data[idx2] = data[idx2], data[idx1]
    return bytes(data)

def mutate_shuffle_sections(data, num_sections=3):
    if len(data) < num_sections:
        return data
    section_length = len(data) // num_sections
    sections = [data[i*section_length:(i+1)*section_length] for i in range(num_sections)]
    random.shuffle(sections)
    return b''.join(sections)

def mutate_reorder_bytes(data, chunk_size=3):
    if len(data) < chunk_size:
        return data
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    random.shuffle(chunks)
    return b''.join(chunks)

def mutate_truncate_or_pad(data):
    if random.choice([True, False]):  # Truncate
        new_length = random.randint(1, len(data))
        return data[:new_length]
    else:  # Pad
        padding = bytes([random.randint(0, 255) for _ in range(random.randint(1, 10))])
        return data + padding

def mutate_duplicate_chunk(data, num_chunks=2):
    data = bytearray(data)
    for _ in range(num_chunks):
        start = random.randint(0, len(data) - 1)
        end = start + random.randint(1, min(10, len(data) - start))
        data[start:start] = data[start:end]
    return bytes(data)

def mutate_remove_chunk(data, num_chunks=2):
    data = bytearray(data)
    for _ in range(num_chunks):
        if len(data) < 2:
            break
        start = random.randint(0, len(data) - 2)
        end = start + random.randint(1, min(10, len(data) - start))
        del data[start:end]
    return bytes(data)

def mutate_numeric_values(data):
    data = bytearray(data)
    for i in range(len(data) - 2):
        if data[i:i+2].isdigit():
            num = int(data[i:i+2])
            data[i:i+2] = str((num + random.randint(-5, 5)) % 100).zfill(2).encode()
    return bytes(data)

def mutate_repeat_pattern(data):
    data = bytearray(data)
    pattern = bytes([random.choice(b'0123456789ABCDEF')]) * random.randint(5, 15)
    index = random.randint(0, len(data))
    data[index:index] = pattern
    return bytes(data)

def mutate_hex_substitution(data):
    data = bytearray(data)
    index = random.randint(0, len(data) - 1)
    hex_str = hex(data[index])[2:].encode()
    data[index:index+1] = hex_str
    return bytes(data)

def mutate_unicode_substitution(data):
    substitutions = {
        ord('a'): b'\xce\xb1',  # Greek alpha
        ord('A'): b'\xce\x91',  # Greek Alpha
        ord('o'): b'\xce\xbf',  # Greek omicron
        ord('O'): b'\xce\x9f',  # Greek Omicron
        ord('e'): b'\xce\xb5',  # Greek epsilon
        ord('E'): b'\xce\x95',  # Greek Epsilon
        ord('i'): b'\xce\xb9',  # Greek iota
        ord('I'): b'\xce\x99'   # Greek Iota
    }
    data = bytearray(data)
    for _ in range(random.randint(1, 5)):
        index = random.randint(0, len(data) - 1)
        byte = data[index]
        if byte in substitutions:
            substitution = substitutions[byte]
            data[index:index+1] = substitution
    return bytes(data)

def mutate_xor_bytes(data):
    data = bytearray(data)
    for _ in range(random.randint(1, 5)):
        index = random.randint(0, len(data) - 1)
        xor_value = random.randint(0, 255)
        data[index] ^= xor_value
    return bytes(data)


# Applying Random Mutations
def dynamic_fuzzer(data, num_mutations=20, num_outputs=1):
    mutation_functions = [
        mutate_flip_bits,
        mutate_insert_bytes,
        mutate_delete_bytes,
        mutate_duplicate_bytes,
        mutate_boundary_values,
        mutate_magic_numbers,
        mutate_insert_ascii,
        mutate_swap_bytes,
        mutate_shuffle_sections,
        mutate_reorder_bytes,
        mutate_truncate_or_pad,
        mutate_duplicate_chunk,
        mutate_remove_chunk,
        mutate_numeric_values,
        mutate_repeat_pattern,
        mutate_hex_substitution,
        mutate_unicode_substitution,
        mutate_xor_bytes
    ]

    output_datalist = []
    
    for i in range(num_outputs):
        for _ in range(num_mutations):
            mutation = random.choice(mutation_functions)
            data = mutation(data)
        output_datalist.append(data.decode('utf-8', 'ignore'))
    return output_datalist

# Example Test Case and Output Display
if __name__ == "__main__":
    input_data = "Testing123"
    input_data = input_data.encode()
    print("Original Input:")
    print(input_data)

    while True:
        try:
            fuzzed_data = dynamic_fuzzer(input_data, num_mutations=20, num_outputs=5)
            break
        except:
            pass
    
    print("\nFuzzed Output:")
    for _ in fuzzed_data:
        print(_)