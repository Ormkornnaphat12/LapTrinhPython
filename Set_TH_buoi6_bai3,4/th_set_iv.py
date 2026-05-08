# cho nhap 1 chuoi(s) . Tim tu dau tien lap lai trong S
# S = "ab ca bc ab" in ra "ab"
# S = "ab ca bc ca ab bc" in ra "ca"
# S = "ab ca bc " in ra "None"
def tu_lap_lai(s):
    Words = s.split() #tach chuoi thanh danh sach
    seen = set()
    for word in Words:
        if word in seen:
            return word
        seen.add(word)
    return "None"
S = input("Nhap chuoi: ")
print("Tu lap lai dau tien:",tu_lap_lai(S))
