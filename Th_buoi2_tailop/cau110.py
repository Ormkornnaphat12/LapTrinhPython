def nen_vb(plaintext):
    if not plaintext:
        return ""
    encode_chars = []
    i = 0
    while i < len(plaintext):
        pre_char = plaintext[i]
        count = 1
        while i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1] and count < 9:
            count += 1
            i += 1
        if count > 1:
            encode_chars.append(f"#{count}{pre_char}")
        else:
            encode_chars.append(pre_char)
        i += 1
    return "".join(encode_chars)
def giai_vb(ciphertext):
    decoded_chars = []
    i = 0
    while i < len(ciphertext):
        if ciphertext[i] == '#' and i + 2 < len(ciphertext):
            try:
                count = int(ciphertext[i+1])
                char_repeat = ciphertext[i+2]
                decoded_chars.append(char_repeat * count)
                i += 3
            except ValueError:
                decoded_chars.append(ciphertext[i])
                i += 1
        else:
            decoded_chars.append(ciphertext[i])
            i += 1
    return "".join(decoded_chars)
original = input("Nhập văn bản gốc (Plain Text): ")
encoded = nen_vb(original)
decoded = giai_vb(encoded)

print("\n"+"="*30)
print(f"Bản gốc (Plain Text):  {original}")
print(f"Bản nén (Cipher Text):  {encoded}")
print(f"Bản khôi phục:         {decoded}")
print("="*30)
