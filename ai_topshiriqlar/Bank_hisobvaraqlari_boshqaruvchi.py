# Bank hisobvaraqlari boshqaruvchi
# Kurs: Dasturlash / IT
# Mavzu: O'rnatish va muhit — Python, interpreter, IDE sozlash
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())

for _ in range(n):
    hisob_raqami, foiz, muddat = input().split()
    hisob_raqami = int(hisob_raqami)
    foiz = float(foiz)
    muddat = float(muddat)
    
    natija = foiz * muddat / 9
    
    print(f"Hisob raqami {hisob_raqami} uchun to'lanadigan foiz: {natija:.2f}")