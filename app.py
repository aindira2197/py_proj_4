# Foydalanuvchidan sonlar ro‘yxatini olish
sonlar = input("Sonlarni probel bilan kiriting: ")

# Stringni listga aylantiramiz
royxat = list(map(int, sonlar.split()))

# Eng katta sonni boshlang‘ich qilib olamiz
max_son = royxat[0]

# Ro‘yxatni tekshiramiz
for son in royxat:
    if son > max_son:
        max_son = son

# Natijani chiqaramiz
print("Eng katta son:", max_son)
