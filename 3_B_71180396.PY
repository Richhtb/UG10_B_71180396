bil_1 = float(input("Masukkan bilangan pertama: "))
bil_2 = float(input("Masukkan bilangan kedua: "))
kalimat= input("Masukkan kalimat: ")

if kalimat.find("kali") != -1:
    print(f"hasil perkalian {bil_1} dengan {bil_2} adalah {bil_1 * bil_2}")
elif kalimat.find("bagi") != -1:
    print(f"hasil pembagian {bil_1} dengan {bil_2} adalah {bil_1 / bil_2}") 
elif kalimat.find("tambah") != -1:
    print(f"hasil penjumlahan {bil_1} dengan {bil_2} adalah {bil_1 + bil_2}")
elif kalimat.find("kurang") != -1:
    print(f"hasil pengurangan {bil_1} dengan {bil_2} adalah {bil_1 - bil_2}")
    