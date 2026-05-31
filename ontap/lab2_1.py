# ==================== BÀI 110: GIẢI NÉN CHUỖI KÝ TỰ ====================
"""
Quy tắc nén:
- Các ký tự liền kề và giống nhau được thay bằng: #<số lượng><ký tự>
- Ví dụ: 'YYYYY' -> '#5Y'
- '999.99' -> '#39.#29' (9 lần số 9, dấu chấm, 2 lần số 9)
- Giả sử không có trường hợp quá 9 ký tự liên tiếp giống nhau
"""

def giai_nen(cipher_text):
    """
    Hàm giải nén chuỗi cipher_text thành plain_text gốc
    Args:
        cipher_text (str): Chuỗi đã được nén
    Returns:
        str: Chuỗi gốc đã giải nén
    """
    plain_text = ""
    i = 0
    while i < len(cipher_text):
        if cipher_text[i] == '#':
            i += 1
            so_luong = int(cipher_text[i])
            i += 1
            ky_tu = cipher_text[i]
            plain_text += ky_tu * so_luong
            i += 1
        else:
            plain_text += cipher_text[i]
            i += 1
    return plain_text
if __name__ == "__main__":
    print("=== CHƯƠNG TRÌNH GIẢI NÉN CHUỖI KÝ TỰ ===\n")
    print("Quy tắc nén: #<số lượng><ký tự>")
    print("Ví dụ: '#5Y' -> 'YYYYY'")
    print("      '#39.#29' -> '999.99'\n")
    cipher_text = input("Nhập chuỗi đã được nén (cipher text): ")

    plain_text = giai_nen(cipher_text)
    print(f"\nChuỗi gốc (plain text): {plain_text}")
    if '#' in plain_text:
        print("\n Lưu ý: Ký tự '#' xuất hiện trong chuỗi gốc (không theo quy tắc)")   
    print("\n=== KẾT THÚC CHƯƠNG TRÌNH ===")