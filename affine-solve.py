# FUNCTION DARI SOAL

def read_image_to_hex(image_path):
    try:
        with open(image_path, "rb") as image:
            f = image.read()
            b = bytearray(f)
            array_of_hex = [hex(byte) for byte in b]
            return array_of_hex
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except ValueError as e:
        print("Error:", e)
        return None

def array_of_hex_to_bytearray(array_of_hex):
    bytearray_data = bytearray()
    for hex_value in array_of_hex:
        if hex_value.startswith('0x'):
            hex_value = hex_value[2:]
        byte_value = int(hex_value, 16)
        bytearray_data.append(byte_value)
    return bytearray_data

def create_file_from_bytes(file_path, bytes_data):
    try:
        with open(file_path, "wb") as file:
            file.write(bytes_data)
        print("File berhasil dibuat:", file_path)
    except Exception as e:
        print("Error:", e)

# END OF FUNCTION DARI SOAL
        
def affine_cipher_decrypt(hex_values, m, b, n):
    plain_hex = []
    coef = 1

    for i in range(1, n):
        if (i * m) % n == 1:
            coef = i
            break
        
    for i in range(len(hex_values)):
        P = hex(((int(hex_values[i], 16) - b) * coef) % n)
        plain_hex.append(P)

    return plain_hex


# 0xFF -> 0x10
# 0xD8 -> 0xe1
def find_m_and_b():
    m = 1
    b = 1
    
    i = 0
    x = (256 * i) - 209

    while (x % 39) != 0:
        i += 1
        x = (256 * i) - 209

    m = x // 39

    i = 0
    b = (16 - (255 * m)) + (256 * i)

    while b < 0:
        i += 1
        b = (16 - (255 * m)) + (256 * i)

    return m, b

def main():
    image_path = "./input/chall.jpg"
    n = 256
    m, b = find_m_and_b()

    print("m:", m, "b:", b)

    hex_values = read_image_to_hex(image_path)
    if hex_values is not None:
        plain_hex = affine_cipher_decrypt(hex_values, m, b, n)
        bytearray_plain = array_of_hex_to_bytearray(plain_hex)
        create_file_from_bytes("./output/flag.jpg", bytearray_plain)

if __name__ == "__main__":
    main()