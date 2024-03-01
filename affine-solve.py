# FUNCTION DARI SOAL

# def affine_cipher(hex_values, m, b, n):
#     cipher_hex = []
#     for i in range(len(hex_values)):
#         C = hex((m * int(hex_values[i], 16) + b) % n)
#         cipher_hex.append(C)
#     return cipher_hex

# def affine_decrypt
#     self.sanitize

#     if @key_a == '' || @key_b == ''
#       @plaintext = 'Invalid key'
#       return
#     end

#     coef = 1
#     for i in 1..25
#       if (i * @key_a) % 26 == 1
#         coef = i
#         break
#       end
#     end


#     @plaintext = ''
#     for i in 0..@ciphertext.length-1
#       @plaintext += (((@ciphertext[i].ord - 65 - @key_b) * coef) % 26 + 65).chr
#     end
#   end

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

def main():
    image_path = "./output/chall-test.jpg"
    n = 256
    b = 237
    m = 241

    # b = random.randint(1, n)
    # m = random.randint(1, n)

    # while math.gcd(m, n) != 1:
    #     m = random.randint(1, n)

    hex_values = read_image_to_hex(image_path)
    if hex_values is not None:
        plain_hex = affine_cipher_decrypt(hex_values, m, b, n)
        bytearray_plain = array_of_hex_to_bytearray(plain_hex)
        create_file_from_bytes("./output/chall-test-decrypt.jpg", bytearray_plain)

if __name__ == "__main__":
    main()